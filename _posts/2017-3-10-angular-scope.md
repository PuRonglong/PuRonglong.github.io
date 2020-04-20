---
layout: post
title: angular(4):指令中的隔离作用域
description: "angular(4):指令中的隔离作用域"
tags: [技术]
comments: true
share: true
cover: https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420163837.png
---

书上看到angular隔离作用域的一个例子，敲了下遇到一个困惑问题。

<!-- more -->

如图对比：

示例一：

![]https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420164457.png)

示例二：

![](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420164508.png)

上图中的例子只是引用了两种版本angular，rc(release candidate)表示候选发行版，数字表示候选版号，一般来说候选版和正式版没有多大区别的，但是在这个截图里，我想要试试angular中的隔离作用域的时候，却发现两者的结果不一样，

先来说说这两种结果的问题，因为想要达到的效果是隔离作用域，那么隔离作用域里应该是获取不到外部作用域中的变量的值，所以按照隔离作用域的说法正常的结果应该是候选版那个截图的结果，但是第二张图的结果表明，隔离作用域中的值却获取到了外部作用域中的值。而这个版本的angular是正式版。

试了下后续的版本，无论是正式版还是候选版，得到的结果都是第二种，于是疑惑了，是在后续的angular版本中指令不能使用scope:{}的写法来进行隔离作用域了吗？不应该呀。查找了一阵资料，在版本的发布日志中也没有看到有这个问题提出来，那想要不使用scope的三种符号进行隔离作用域有别办法吗？

找到问题了，如图，示例三：

![](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420164518.png)

把示例三进行如下修改：

![](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420164526.png)

因为平时都是用的template链接模板这种方式，可能没遇到这个问题，所以被一开始示例一二的两种结果给困惑到了，但现在问题解决了。
