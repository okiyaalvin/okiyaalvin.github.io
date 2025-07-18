# frozen_string_literal: true
source "https://rubygems.org"

gem "jekyll", "~> 4.4"
gem "jekyll-theme-chirpy", "~> 7.3"

# Local serve helper (needed because WEBrick was removed from stdlib in Ruby 3+)
group :jekyll_plugins do
  gem "webrick"
end

# Optional testing
group :test do
  gem "html-proofer", "~> 5.0"
end

# Windows helpers (safe to leave; Bundler will ignore on Linux)
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

gem "wdm", "~> 0.2.0", platforms: [:mingw, :x64_mingw, :mswin]
