---
layout: post
title: jekyll和github pages的一些问题
description: "some note"
tags: [技术]
image:
background: triangular.png
comments: true
share: true
---

> 在部署jekyll和github pages的时候遇到的一些问题

因为以前用过jekyll，所以以为jekyll和github pages搭配很简单，结果自己使用的过程中遇到了一些问题，使用google和stackoverflow解决了问题，有必要记录一下。

<!-- more -->

![img](/images/article/2016-6-3/1.png)

使用jekyll+github pages初步搭建好博客以后，需要实现标签的功能，点击标签页面跳转到相应的页面。标签的实现我使用了插件，新建一个_plugins文件夹，在里面新建一个ruby文件build-tag.rb，这个ruby文件里的代码实现了标签功能，原理就是生成对应标签的文件，比如整个首页是一个index，插件就是为每一个标签生成一个index，这样就能现实标签页了。

然后启动jekyll服务，jekyll serve，查看localhost://4000并没有什么问题，愉快地上传到github，却发现本地实现一切正常，放到github上标签功能却失效了。查找到问题在这里，github help里这样说的：

```
You can further customize your GitHub Pages site by adding Jekyll plugins.

GitHub Pages officially supports the Jekyll plugins found in the GitHub Pages gem. For the exact versions of the Jekyll plugins that GitHub Pages supports, see this list of GitHub Pages dependencies. Other plugins are not supported, so the only way to incorporate them in your site is to generate your site locally and then push your site's static files to your GitHub Pages site.
```

意思是，通过添加插件，你可以自定义你的github pages网页，但是github pages官方只支持一些指定的插件，然后给出了支持的插件列表。其它的插件不支持，也就是说我们自己写的放在_plugins里的插件github pages是不支持的。最后告诉我们唯一的办法是在本地生成文件然后push到github pages站点上。我们知道当我们使用markdown写了博文以后，jekyll会生成整个项目的静态文件（也就是我们网页上常见的html，css这些）在```_site```文件夹里，因为这个目录下的文件是被build出来的，不是源码，通常git repo（乃至所有源码管理系统）不应包含非源码的内容，所以github官方才说不要把site文件夹push上去，如果使用了github pages服务，正确配置以后github pages会帮你build。

至于为什么不支持，则是因为安全问题。

但这时候就遇到我们上面说的情况了，它在build的时候并不会识别我们自己的插件，所以点击标签链接的时候报404错误。

知道了问题以后，唯一的方法就是把我们编译过后的文件传上去，但不是说我们就传site里的文件就好了，因为代码管理的原则就是放源代码而不是编译后的文件，通过源码和每一次的commit信息才能看到项目一步一步是怎么建立起来的。于是我将.gitignore文件里的忽略site文件夹的配置去掉了，将其push上去，私以为github pages会自动查找site文件夹里的内容，结果当然是不行的了。

正确的做法是把源码和编译后的文件分开。

这个时候就要用到git强大的分支系统啦，一个分支放源码，一个分支放编译后的文件。可是又有一个问题，如果我们的站点是托管在以username.github.io命名的项目上的话：

```
then GitHub Pages will always serve content from the master branch
```

username.github.io是github一个特殊的命名，凡是以这个名字命名的项目，github pages会强制使用master分支，即使这个项目下新建有其它分支。

对于既想要使用此项目管理博客源码又想要发布文章的人来说，有个小方法就是把site里的内容放到master分支上，然后新建一个分支，比如命名为source，这个分支上放的就是博客源码。

```
git checkout -b source master
```

上面git指令表示从这个master分支上新建一个source分支。新建了一个分支以后记得在github里的setting选项里把这个库的没人分支改为source。

通过github的分支系统，这样我们就能在一个库里分别管理我们的源码和编译文件了。我们push了源码（source分支）之后还要push编译文件（master分支），每次手动操作，切换分支这些很繁琐，可以使用代码简化流程，新建一个rakefile.rb文件，内容如下：

```ruby
require "rubygems"
require "tmpdir"

require "bundler/setup"
require "jekyll"


desc "Generate blog files"
task :generate do
  Jekyll::Site.new(Jekyll.configuration({
    "source"      => ".",
    "destination" => "_site"
  })).process
end


desc "Generate and publish blog to gh-pages"
task :publish => [:generate] do
  Dir.mktmpdir do |tmp|
    cp_r "_site/.", tmp

    pwd = Dir.pwd
    Dir.chdir tmp

    system "git init"
    system "git add ."
    message = "Site updated at #{Time.now}"
    system "git commit -m #{message.inspect}"
    system "git remote add origin 项目的git地址"
    system "git push origin master --force"

    Dir.chdir pwd
  end
end
```

现在就可以使用```rake publish```这个命令同时compile和push我们的站点到github pages。

但运行的时候提示报错：

```
cannot load such file -- bundler/setup
```

没有bundler，看来的安装，执行：

```
sudo gem install bundler
```

提示：

```
ERROR:  While executing gem ... (Errno::EPERM)
    Operation not permitted - /usr/bin/bundle
```

查找资料找到问题所在：

```
No, you'll need to either change your GEM_HOME or do something like sudo gem install bundler -n /usr/local/bin because of El Cap's introduction of SIP (System Integrity Protection).
```

上面这个bundler里issue说得很清楚，这是Mac OS El Capitan这个版本的mac系统的缘故。

于是执行：

```
sudo gem install bundler -n /usr/local/bin
```

成功安装。

参考资料：

[Using Jekyll plugins on GitHub Pages](http://ixti.net/software/2013/01/28/using-jekyll-plugins-on-github-pages.html)

[Unable to run gem install bundler in OS X El Capitan #4065](https://github.com/bundler/bundler/issues/4065)