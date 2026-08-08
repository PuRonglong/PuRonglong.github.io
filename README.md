# 蒲荣龙的博客

> 基于 [jekyll-theme-H2O](https://github.com/kaeyleo/jekyll-theme-H2O) 修改的个人博客。

一个简洁、响应式、支持夜间模式与技术写作的 Jekyll 静态博客。文章用 Markdown 编写，由 GitHub Pages 自动构建并托管。

## 特性

- **响应式设计**：适配桌面与移动端。
- **文章分页**：基于 `jekyll-paginate`，每页 15 篇，分页路径 `page:num`（如 `/page2`）。
- **代码高亮**：Rouge 语法高亮；代码块相关样式/脚本按正文是否含 `<pre>` **按需加载**。
- **数学公式**：MathJax 按需加载（文章 front matter 设 `mathjax: true`，或正文含 `$$` 自动启用）。
- **站内搜索**：基于 `search.json` 的客户端全文检索（标题 + 标签 + 摘要匹配，配置 `search: true`）。
- **夜间模式**：右下角一键切换（localStorage 记忆），状态记录在 `body.night-mode`；未手动设置时按 `nightMode` 配置自动（23 点至 6 点）。
- **回到顶部**：右下角悬浮按钮，滚动超过 400px 出现，点击平滑滚动至顶部（原生 JS，无第三方依赖）。
- **标签 / 标签云**：侧栏推荐标签 + 独立 `/tags.html` 页面。
- **社交链接**：微博、Instagram、豆瓣（见 `_config.yml` 的 `sns`）。
- **PWA 离线缓存**：`sw.js` 对静态资源缓存优先、页面网络优先，支持离线访问。
- **性能优化（相对原版 H2O 的改动）**：
  - 移除 **jQuery**，交互脚本（导航/搜索/分页/夜间模式/版权保护）全部改为**原生 JS** 重写，零第三方依赖，消除首屏渲染阻塞；
  - 第三方库 CDN 统一为**国内双源**（staticfile → bootcdn 两级回退），不使用 jsdelivr 等国外源；
  - 移除 Font Awesome，改用内联 SVG 图标（`currentColor` 跟随主题色）；
  - 移除第三方访客统计（不蒜子 / busuanzi），不再加载外部统计脚本；
  - CSS 合并压缩为单一 `bundle.min.css`（normalize + `github-markdown.css` + `app.min.css` 合并，并剥离 `github-markdown.css` 内嵌的 octicons base64 字体；`prism.css` 仍独立、按正文是否含代码块条件加载）；
  - 新增 `sitemap.xml` / `feed.xml`（jekyll-sitemap / jekyll-feed）与 `robots.txt`，SEO 与订阅能力开箱即用；
  - favicon 多分辨率优化（16/32/48，约 5KB）；
  - 清理无用旧资源（social-share、util.js、hero.jpg、profile.png 等）。

## 快速开始

### 本地预览

需要 Ruby 与 Jekyll。GitHub Pages 线上锁定 **Jekyll 3.9**，本地建议保持一致：

```bash
gem install jekyll jekyll-paginate
jekyll serve
# 或（项目含 Gemfile 时）bundle exec jekyll serve
```

打开 <http://127.0.0.1:4000> 预览。

> ⚠️ 版本注意：本仓库使用 `jekyll-paginate` 1.1.0（其依赖 Jekyll `< 3.0`）。若本地用 **Jekyll 4** 运行，分页会**静默失效**——首页文章列表为空、且不报任何错误。要本地完整预览分页，请使用 Jekyll 3.9 环境；推送到 GitHub Pages 则由其锁定的 3.9 正常生成分页。

### 部署

直接推送到 `master` 分支，GitHub Pages 自动构建发布：

- 仓库地址：<https://github.com/PuRonglong/PuRonglong.github.io>
- 访问地址：<https://puronglong.github.io>（自定义域名 `puronglong.com`，见 `_config.yml` 的 `url`）

```bash
git add -A
git commit -m "update"
git push origin master
```

## 目录结构

```
.
├── _config.yml          # 站点配置
├── _layouts/            # 页面布局（default / post / page）
├── _includes/           # 复用片段（head、header、footer、author-card、back-to-top、anchor、mathjax …）
├── _posts/              # 博客文章（Markdown）
├── assets/              # 样式 assets/css、脚本 assets/js、字体 assets/fonts、图片
├── index.html           # 首页（分页文章列表）
├── tags.html            # 标签页
├── 404.html             # 404 页面
├── sw.js                # Service Worker（PWA 离线缓存）
├── search.json          # 站内搜索索引（构建时生成）
├── favicon.ico          # 站点图标
```

> 搜索脚本可读源位于 `dev/js/index.js`；项目已无 gulp 构建链，编辑该源文件不会自动更新 `assets/js/index.min.js`（需手动同步）。`dev/` 已在 `_config.yml` 的 `exclude` 中，不会被 Jekyll 发布。
>
> 隐私说明：6 个分析报告页（`shs/ jjs/ jls/ gjjjs/ zxs/ sjs/`）与 `kindlenotes/` 为私人内容，已通过 `robots.txt` Disallow + 页面 `<meta name="robots" content="noindex">` 双重手段阻止搜索引擎收录。

## 配置

主要配置集中在 `_config.yml`：

| 配置项 | 说明 |
| --- | --- |
| `title` / `description` | 站点标题与简介 |
| `url` / `baseurl` | 站点域名；GitHub Pages 用户页 `baseurl` 留空 |
| `author` / `nickname` / `bio` / `avatar` | 博主信息（显示在侧栏） |
| `nav` | 导航链接定义于 `_data/nav.yml`（`home` / `tags`） |
| `paginate` / `paginate_path` | 分页数量与路径（默认 15，`page:num`） |
| `search` | 是否开启站内搜索 |
| `nightMode` | 默认是否启用夜间模式 |
| `showNightToggle` | 是否显示右下角夜间模式切换按钮（默认 true） |
| `theme-color` | 主题色 `default` / `pink` |
| `postPatterns` | 文章头图图案（circuitBoard / seaOfClouds / food …） |
| `sns` | 社交账号（weibo / instagram / douban …） |
| `recommend-tags` | 侧栏是否展示推荐标签 |
| `highlighter` | 代码高亮器（rouge） |
| `markdown` / `kramdown.input` | kramdown + GFM |
| `excerpt_separator` | 摘要分隔符，默认 `<!-- more -->` |

## 写文章

在 `_posts/` 下新建文件，命名 `YYYY-MM-DD-title.md`，头部填 front matter：

```yaml
---
layout: post
title: "文章标题"
date: 2026-07-26
tags: [Jekyll, 前端]
mathjax: true        # 文章含 LaTeX 公式时开启
# prism: true        # 代码块多数情况自动判定，一般无需手动设置
---
```

- 正文用 Markdown（GFM）编写。
- 文中插入 `<!-- more -->` 控制首页摘要截断位置。
- 代码块用三个反引号 ` ``` ` 包裹，可指定语言（如 ` ```ruby `）。
- 数学公式用 `$$ ... $$`（行内公式视 MathJax 配置）。

## 许可证

本仓库基于 [jekyll-theme-H2O](https://github.com/kaeyleo/jekyll-theme-H2O)，原主题采用 [MIT](https://github.com/kaeyleo/jekyll-theme-H2O/blob/master/LICENSE) 许可证。
