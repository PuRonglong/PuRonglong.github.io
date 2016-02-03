layout: post
title: 用browsersync提高效率
description: "工具"
tags: [技术,工具]
image:
background: triangular.png
comments: true
share: true
---

>一个高效的用于“实时刷新”的工具

一般来说，当我们进行项目开发时，文件保存以后，需要通过刷新浏览器来查看修改后的效果。而且，由于习惯，一般开发者都会多刷几遍。那么在强调高效开发的今天，有没有什么工具提高这种重复的工作的低效率呢？

这就是我们今天要介绍的***browersync***

![img](http://7vznhl.com1.z0.glb.clouddn.com/2015-10-1-02QQ20151005-1@2x.png)

首先是安装：

先确保安装了node环境。进入终端后，输入以下进行全局安装。

    npm install -g browser-sync

使用：

在终端中进入项目目录，当我们本地没有起服务的时候，执行以下代码：

    browser-sync start --server --files "css/*.css"

这里的start和server其实就是browser起了一个服务，默认端口可以在终端中看到，后面的files表示监听文件的改变，```css/*.css```指监听哪些文件的改变，如果只是想项目做出改变就有所监听的话可以使用```--files "**"```

如果本地通过php,node,nginx等起了服务，对于这些动态站点使用代理模式：

    browser-sync start --proxy "localhost:4000" --files "**"

BrowserSync会提供一个新地址用于访问。运行结果如下：

![img](http://7vznhl.com1.z0.glb.clouddn.com/2015-10-1-01QQ20151005-0@2x.png)

可以看到，browsersync起的本地服务地址端口是3000，3001端口是它的一个UI界面控制的端口。

目前我的使用是[jekyll](http://www.puronglong.com/jekyll/)起个本地服务搭配browsersync来使用，结合OSX-EI-Capitan最新的分屏功能(如果本身是用双屏的人就更好了)，还是挺舒服的。

当然了，为了适应自动化的开发流程，browser-sync也是支持grunt和gulp的，以[gulp](http://www.puronglong.com/gulp/)为例，在gulp的配置文件中再新添一个gulp任务

    var gulp        = require('gulp');
    var browserSync = require('browser-sync');

    // Static server
    gulp.task('browser-sync', function() {
        browserSync.init({
            server: {
                baseDir: "./"
            }
        });
    });

    // or...

    gulp.task('browser-sync', function() {
        browserSync.init({
            proxy: "yourlocal.dev"
        });
    });

然后执行这个gulp任务。

更多详情请看[这里](http://www.browsersync.io/docs/)