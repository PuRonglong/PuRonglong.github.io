source "https://rubygems.org"

# 锁定构建依赖，保证本地与 CI 构建可复现。
# 注意：GitHub Pages 默认部署使用其自带的 Jekyll 3.9 工具链（会忽略本 Gemfile）。
# 如需在本地用与 Pages 完全一致的版本做分页等测试，可改用 `gem "github-pages"`。
gem "jekyll", "4.4.1"
# 与系统 Ruby 3.3 默认的 bigdecimal 保持一致，避免 Bundler 在 default gem 上版本冲突。
gem "bigdecimal", "~> 3.1.0"
gem "webrick"
# timezone 需要 tzinfo；Windows 平台还需 tzinfo-data 才能解析 Asia/Shanghai 等时区。
gem "tzinfo", "~> 2.0"
gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw, :jruby]
# Windows 下启用 native 文件监听，避免 Jekyll 轮询文件变化。
gem "wdm", "~> 0.1", platforms: [:mingw, :mswin, :x64_mingw, :jruby]
gem "jekyll-paginate", "1.1.0"
gem "jekyll-sitemap"
gem "jekyll-seo-tag"
gem "jekyll-feed"
