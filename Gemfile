source "https://rubygems.org"

gem 'bootstrap', '~> 5.3.3'
gem "github-pages", group: :jekyll_plugins
group :jekyll_plugins do
  gem "jekyll-github-metadata"
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-hostname"
  gem "webrick"
end



# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem
# do not have a Java counterpart.
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
