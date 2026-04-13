#!/usr/bin/env ruby
# frozen_string_literal: true

# Verifies every path key in _data/sitemap_<locale>.json maps to an existing file under _docs/.
#
# Usage (repo root):
#   bundle exec ruby scripts/verify_sitemap_json_paths.rb
#   bundle exec ruby scripts/verify_sitemap_json_paths.rb _data/sitemap_en.json

require "json"

sitemap_path = ARGV[0] || "_data/sitemap_en.json"
unless File.file?(sitemap_path)
  warn "Missing #{sitemap_path}"
  exit 2
end

map = JSON.parse(File.read(sitemap_path))
missing = []
map.each_key do |key|
  # Keys look like "_api/foo.md" — repo file is _docs/_api/foo.md
  rel = key.start_with?("_") ? key : "_#{key}"
  path = File.join("_docs", rel)
  missing << key unless File.file?(path)
end

puts "Sitemap path check: #{sitemap_path}"
puts "  Entries: #{map.size}, missing files: #{missing.size}"
if missing.any?
  missing.first(30).each { |k| puts "  #{k}" }
  puts "  …" if missing.size > 30
  exit 1
end

puts "OK — every sitemap key resolves to a file under _docs/."
exit 0
