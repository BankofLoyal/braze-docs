#!/usr/bin/env ruby
# frozen_string_literal: true

# Verifies redirect destinations for mappings required by validate_doc_redirects.rb
# exist in the Jekyll URL map for HEAD (proves targets resolve after build).
#
# Usage (after ./bdocs check_redirects --json scripts/temp/redirect-report.json):
#   bundle exec ruby scripts/jekyll_url_map_dump.rb /tmp/jekyll-url-map-head.json
#   bundle exec ruby scripts/verify_redirect_targets_in_jekyll.rb scripts/temp/redirect-report.json /tmp/jekyll-url-map-head.json
#
# Optional: audit legacy validurls rows whose RHS is not a published Jekyll URL:
#   bundle exec ruby scripts/verify_redirect_targets_in_jekyll.rb --audit-stale /tmp/jekyll-url-map-head.json

require "json"
require "set"

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

RX = /validurls\['([^']+)'\]\s*=\s*'([^']*)'/

def load_published_urls(map_path)
  JSON.parse(File.read(map_path)).values.map { |u| normalize_url_for_compare(u) }.to_set
end

def published_include?(published, raw_target)
  n = normalize_url_for_compare(raw_target)
  base = n.split("#", 2).first
  return true if published.include?(n)
  return true if published.include?(base)

  # Path only: Jekyll map has no ?tab= / ?sdktab= (client-side on the same doc URL)
  path_only = base.split("?", 2).first
  path_norm = normalize_url_for_compare(path_only)
  published.include?(path_norm)
end

def audit_stale_redirect_targets(map_path)
  published = load_published_urls(map_path)
  redirect_file = File.join(__dir__, "..", "assets", "js", "broken_redirect_list.js")
  stale = []
  File.foreach(redirect_file, chomp: true) do |line|
    next if line.strip.start_with?("//")
    m = RX.match(line)
    next unless m

    _from, to = m[1], m[2]
    next if to.strip.empty?

    stale << to unless published_include?(published, to)
  end
  puts "Stale redirect target audit (RHS not matching any Jekyll doc URL on HEAD)"
  puts "  Jekyll map: #{map_path}"
  puts "  Stale count: #{stale.size}"
  stale.first(25).each { |u| puts "  #{u}" }
  puts "  …" if stale.size > 25
  puts "  Note: Legacy rows often predate IA; fix high-traffic keys as time allows."
end

if ARGV[0] == "--audit-stale"
  map_path = ARGV[1] || "/tmp/jekyll-url-map-head.json"
  unless File.file?(map_path)
    warn "Missing #{map_path}"
    exit 2
  end

  audit_stale_redirect_targets(map_path)
  exit 0
end

report_path = ARGV[0] || "scripts/temp/redirect-report.json"
map_path = ARGV[1] || "/tmp/jekyll-url-map-head.json"

unless File.file?(report_path)
  warn "Missing #{report_path} — run: ./bdocs check_redirects --base origin/develop --json #{report_path}"
  exit 2
end
unless File.file?(map_path)
  warn "Missing #{map_path} — run: bundle exec ruby scripts/jekyll_url_map_dump.rb #{map_path}"
  exit 2
end

report = JSON.parse(File.read(report_path))
pairs = report["required_mappings"] || []
if pairs.empty?
  warn "No required_mappings in #{report_path} — re-run check_redirects with an updated validate_doc_redirects.rb"
  exit 2
end

published = load_published_urls(map_path)
missing = []
pairs.each do |row|
  to = row["to"]
  next if to.nil? || to.to_s.strip.empty?

  missing << row unless published_include?(published, to)
end

puts "Required redirect target check (#{pairs.size} mappings from #{report_path})"
puts "  Jekyll map: #{map_path}"
if missing.empty?
  puts "OK — every required redirect destination matches a Jekyll doc URL on HEAD."
  exit 0
end

puts "FAILED — #{missing.size} required destination(s) missing from Jekyll map:"
missing.first(20).each { |row| puts "  #{row['from']} → #{row['to']}" }
puts "  …" if missing.size > 20
exit 1
