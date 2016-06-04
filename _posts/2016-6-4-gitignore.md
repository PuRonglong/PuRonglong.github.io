---
layout: post
title: git忽略已经被提交的文件
description: "git忽略已经被提交的文件"
tags: [技术]
image:
  background: triangular.png
comments: true
share: true
---

> git忽略已经被提交的文件

上次在github pages项目里修改了gitignore配置文件，提交了site文件夹，后来不准备把这个文件push上去，于是在gitignore里又添加了site，结果发现，这时候配置gitignore没有用了。

原因在于.gitignore文件只能作用于git没有跟踪过的文件，如果文件被git记录过，那么.gitignore对它们就没有效果了。正确的做法应该是使用正确的git指令```git rm```。

<!-- more -->

正确指令如下：

```
git rm --cached _site
```

rm是git的一个指令：

git-rm - Remove files from the working tree and from the index

--cached是该指令的一个options选项配置：

```
--cached
   Use this option to unstage and remove paths only from the index.
   Working tree files, whether modified or not, will be left alone.
```

_site是我们需要从git里取消的文件。


