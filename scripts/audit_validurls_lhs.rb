#!/usr/bin/env ruby
# frozen_string_literal: true

# Audit validurls LHS in assets/js/broken_redirect_list.js against a Jekyll URL map
# JSON from jekyll_url_map_dump.rb (baseline commit). Optionally rewrite the JS file.
#
# Usage:
#   bundle exec ruby scripts/audit_validurls_lhs.rb --baseline-json scripts/temp/baseline_jekyll_urls.json [--apply]
#
# Build baseline JSON:
#   git worktree add --detach scripts/temp/wt-baseline <BASE_SHA>
#   cd scripts/temp/wt-baseline && bundle install
#   bundle exec ruby ../../../scripts/jekyll_url_map_dump.rb /path/to/baseline_jekyll_urls.json

require "json"
require "open3"
require "optparse"
require "set"

REPO_ROOT = File.expand_path("..", __dir__)
JS_PATH = File.join(REPO_ROOT, "assets", "js", "broken_redirect_list.js")
RX_VALIDURL = /\Avalidurls\['([^']+)'\]\s*=\s*'([^']*)'(?:;)?\s*\z/

def normalize_url_for_compare(url)
  u = url.to_s.strip.gsub(%r{(?<!:)//+}, "/")
  parts = u.split("#", 2)
  path = parts[0] || ""
  frag = parts[1] ? "##{parts[1]}" : nil
  q = nil
  if path.include?("?")
    pq = path.split("?", 2)
    path = pq[0] || ""
    q = pq[1] ? "?#{pq[1]}" : nil
  end
  path = path.chomp("/")
  file_segment = File.basename(path)
  has_extension = !file_segment.empty? && file_segment.match?(/\.[A-Za-z0-9]{2,}$/)
  path += "/" unless path.empty? || has_extension
  "#{path}#{q}#{frag}"
end

def path_query_norm(url)
  normalize_url_for_compare(url).split("#", 2).first
end

def lhs_has_locale_segment?(lhs)
  lhs.match?(%r{\A/docs/[a-z]{2}(?:-[a-z]{2})?/}i)
end

def user_guide_path(lhs)
  m = lhs.match(%r{\A/docs/user_guide/(.+)})
  return nil unless m

  m[1].split("#", 2).first
end

def new_ia_user_guide_lhs?(lhs)
  return false unless lhs.start_with?("/docs/user_guide/")

  p = user_guide_path(lhs).to_s
  seg = p.split("/").first
  return false if seg.nil? || seg.empty?

  # Only top-level IA folders after /user_guide/ — avoid matching legacy .../get_started/... paths.
  %w[channels messaging audience administer analytics get_started brazeai].include?(seg)
end

def legacy_user_guide_lhs?(lhs)
  return false unless lhs.start_with?("/docs/user_guide/")

  p = user_guide_path(lhs).to_s
  return true if p.start_with?("message_building_by_channel/")
  return true if p.start_with?("engagement_tools/")
  return true if p.start_with?("administrative")
  return true if p.start_with?("data_and_analytics/")
  return true if p.start_with?("data/report") || p.start_with?("data/unification") || p.start_with?("data/analysis")
  return true if p.start_with?("personalization_and_dynamic_content/")
  return true if p.start_with?("message_building_and_personalization/")
  return true if p.start_with?("outbound_messaging/")
  return true if p.start_with?("email/") && !p.start_with?("channels/")

  false
end

def legacy_top_level_lhs?(lhs)
  %w[
    /docs/best_practices
    /docs/dashboard_features
    /docs/deep_dives
    /docs/quick_wins
    /docs/message_building_and_personalization
    /docs/whatsapp_response_messaging
  ].any? { |pre| lhs == pre || lhs.start_with?("#{pre}/") || lhs.start_with?("#{pre}#") }
end

def compute_terminal_targets(from_to_norm)
  terminal = {}
  from_to_norm.each_key do |from|
    cur = from_to_norm[from]
    seen = {}
    64.times do
      break if cur.nil? || cur.empty?
      break unless cur.start_with?("/docs/")

      cn = normalize_url_for_compare(cur)
      break if seen[cn]

      seen[cn] = true
      nxt = from_to_norm[cn] || from_to_norm[path_query_norm(cn)]
      break if nxt.nil? || nxt.empty?
      break if nxt == cur

      cur = nxt
    end
    terminal[from] = cur
  end
  terminal
end

def preferred_lhs_literal(a, b)
  path_a = a.split(/(?=[#?])/, 2).first
  path_b = b.split(/(?=[#?])/, 2).first
  a_slash = path_a.match?(%r{/\z}) && path_a.length > "/docs/x".length
  b_slash = path_b.match?(%r{/\z}) && path_b.length > "/docs/x".length
  return b if a_slash && !b_slash
  return a if b_slash && !a_slash

  [a, b].min_by(&:length)
end

def load_baseline_path_queries(json_path)
  data = JSON.parse(File.read(json_path))
  data.values.map { |u| path_query_norm(u) }.to_set
end

def rg_mentions_lhs?(lhs)
  return false if lhs.nil? || lhs.length < 12

  needle = lhs.sub(%r{\A/docs/?}, "")
  return false if needle.length < 8

  dirs = %w[_docs _lang _includes].map { |d| File.join(REPO_ROOT, d) }.select { |d| File.directory?(d) }
  return false if dirs.empty?

  out, st = Open3.capture2("rg", "-l", "--glob", "*.md", needle, *dirs)
  st.success? && !out.to_s.strip.empty?
rescue StandardError
  false
end

def collapse_norm_map(map)
  map.keys.each do |k|
    v = map[k]
    seen = {}
    while v.is_a?(String) && v.start_with?("/docs/")
      vn = normalize_url_for_compare(v)
      nxt = map[vn] || map[path_query_norm(vn)]
      break if nxt.nil? || nxt.empty?
      break if seen[vn]

      seen[vn] = true
      v = nxt
    end
    map[k] = v
  end
  map
end

options = { apply: false, baseline_json: nil }
OptionParser.new do |o|
  o.banner = "usage: audit_validurls_lhs.rb --baseline-json PATH [--apply]"
  o.on("--baseline-json PATH", "jekyll_url_map_dump JSON at baseline commit") { |v| options[:baseline_json] = v }
  o.on("--apply", "Rewrite broken_redirect_list.js") { options[:apply] = true }
end.parse!

abort "usage: audit_validurls_lhs.rb --baseline-json PATH [--apply]" unless options[:baseline_json] && File.file?(options[:baseline_json])
abort "missing #{JS_PATH}" unless File.file?(JS_PATH)

baseline = load_baseline_path_queries(options[:baseline_json])

lines = File.readlines(JS_PATH, chomp: true)
first_v = lines.index { |l| l.start_with?("validurls[") }
last_v = lines.rindex { |l| l.start_with?("validurls[") }
abort "no validurls" unless first_v && last_v

preamble = lines[0...first_v]
tail = lines[(last_v + 1)..] || []

entries = []
lines[first_v..last_v].each do |line|
  next if line.strip.empty? || line.strip.start_with?("//")

  m = RX_VALIDURL.match(line.strip)
  entries << { lhs: m[1], rhs: m[2] } if m
end

from_to_norm = {}
entries.each do |e|
  k = normalize_url_for_compare(e[:lhs])
  to = e[:rhs].to_s.strip
  next if to.empty?

  from_to_norm[k] = normalize_url_for_compare(to)
end

terminals = compute_terminal_targets(from_to_norm)

groups = Hash.new { |h, k| h[k] = [] }
entries.each_with_index do |e, i|
  fk = normalize_url_for_compare(e[:lhs])
  groups[terminals[fk]] << i
end

removal = Set.new
reason = {}

entries.each_with_index do |e, i|
  lhs = e[:lhs]
  fk = normalize_url_for_compare(lhs)

  if lhs_has_locale_segment?(lhs)
    removal << i
    reason[i] = "locale_segment"
    next
  end

  g = groups[terminals[fk]]
  next if g.size < 2

  new_ia = new_ia_user_guide_lhs?(lhs)

  has_legacy_or_baseline_other = g.any? do |j|
    next false if j == i

    o = entries[j][:lhs]
    legacy_user_guide_lhs?(o) || legacy_top_level_lhs?(o) || baseline.include?(path_query_norm(o))
  end

  # Primary prune: new-IA-shaped LHS when a legacy or baseline-published LHS maps to the same terminal.
  if new_ia && has_legacy_or_baseline_other
    removal << i
    reason[i] = "redundant_new_ia_same_rhs"
  end
  # Intentionally omit broad "same terminal as baseline" removal: many real legacy /docs/... shortcuts
  # share a destination with current Jekyll URLs; removing those would drop valid bookmarks.
end

entries.each_with_index do |e, i|
  next if removal.include?(i)

  lhs = e[:lhs]
  pq = path_query_norm(lhs)
  next if baseline.include?(pq)
  next unless new_ia_user_guide_lhs?(lhs)

  fk = normalize_url_for_compare(lhs)
  next if groups[terminals[fk]].size > 1

  next if rg_mentions_lhs?(lhs)

  removal << i
  reason[i] = "new_ia_not_baseline_no_md_refs"
end

kept = entries.each_with_index.reject { |(_e, i)| removal.include?(i) }.map(&:first)

deduped = {}
kept.each do |e|
  k = normalize_url_for_compare(e[:lhs])
  if deduped[k]
    other = deduped[k]
    win_lhs = preferred_lhs_literal(other[:lhs], e[:lhs])
    winner = (win_lhs == e[:lhs] ? e : other)
    rhs = winner[:rhs]
    deduped[k] = { lhs: win_lhs, rhs: rhs }
  else
    deduped[k] = { lhs: e[:lhs], rhs: e[:rhs] }
  end
end

final_map = {}
deduped.each_value do |e|
  final_map[normalize_url_for_compare(e[:lhs])] = e[:rhs].to_s.strip
end

collapsed = final_map.dup
collapse_norm_map(collapsed)

order = []
seen_k = Set.new
entries.each_with_index do |e, i|
  next if removal.include?(i)

  k = normalize_url_for_compare(e[:lhs])
  next if seen_k.include?(k)

  seen_k << k
  order << k
end

new_lines_by_key = {}
deduped.each_value do |e|
  k = normalize_url_for_compare(e[:lhs])
  rhs = collapsed[k] || e[:rhs]
  lhs = e[:lhs]
  lhs_esc = lhs.gsub("\\", "\\\\").gsub("'", "\\\\'")
  rhs_esc = rhs.to_s.gsub("\\", "\\\\").gsub("'", "\\\\'")
  new_lines_by_key[k] = "validurls['#{lhs_esc}'] = '#{rhs_esc}';"
end

ordered_lines = order.filter_map { |k| new_lines_by_key[k] }

out = []
out.concat(preamble)
out.concat(ordered_lines)
out.concat(tail)

puts "Baseline JSON: #{options[:baseline_json]}"
puts "Removed #{removal.size} validurl rows (of #{entries.size})"
reason_tally = Hash.new(0)
removal.each { |i| reason_tally[reason[i]] += 1 }
puts "Removal reasons: #{reason_tally.inspect}"

if options[:apply]
  File.write(JS_PATH, "#{out.join("\n")}\n")
  puts "Wrote #{JS_PATH}"
else
  puts "Dry run (no --apply). Removed LHS sample (first 40):"
  removal.first(40).each { |i| puts "  #{reason[i]}: #{entries[i][:lhs]}" }
  puts "  …" if removal.size > 40
end
