---
layout: post
title: css 中的 inline-bock
description: "css 中的 inline-bock"
tags: [技术]
cover: https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/2020-12-19-074215.jpg
comments: true
share: true
---

关于一次 display: inline-block 遇到的问题。

<!-- more -->

事情是这样的，想要实现并排的两个div，但是却如下显示：

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/2020-12-19-073702.jpg)

经过检查是设置的display:inline-block这个css属性导致的，但是同样的样式，改变以上文字数量就可以并列显示呢？如下：

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/2020-12-19-073745.jpg)

先来看看display:inline-block属性的定义：

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/2020-12-19-073811.jpg)

实际上是定义了一个行内块元素，行内元素有个vertical-align属性：

```css
The vertical-align CSS property specifies the vertical alignment 
of an inline or table-cell box. -- MDN
```

该属性定义行内元素的基线相对于该元素所在行的基线的垂直对齐方式。如果没有给该属性赋值会使用默认值baseline，也就是基线。

那么什么又是基线呢？

网上看到一句话：inline-block的基线是正常流中最后一个line box的基线，除非，这个line box里面既没有line boxes ，或者其本身overflow属性的计算值不是visible，则它的基线是margin底边缘。

以上得知，如果两个div里是空的，这两个div应该也能正常对齐：

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/2020-12-19-074118.jpg)

或者给overflow设置一个值也是可以的：

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/2020-12-19-074136.jpg)

而且我们回头看第一张图，第一个div的第二行字和第二个div的第一行字的确是在同一个基准线上的。如果第一个div有三行，那后面的就会以第三行为基准对齐。

所以正是基准线导致两个div没有对齐，只要给class名为box的样式设置一个基线的对准值就行了，无论值是top，middle，还是bottom都可以。而这个基准线，两个div都是以父级元素作为参考，父级是同一个div，所以两者就对齐了。

另外使用行内元素进行排列还要注意的是标签之间换行会导致显示有间隙，解决方法有很多，如代码里去掉换行。

为什么代码里的换行会在浏览器里显示成有间隙呢？这个间隙实际是字符问题，我们可以通过改变父级font-size值的大小间隙随之改变可以看出，那么去掉字符大小应该就没有间隙了，所以可以对父级div使用font-size:0px效果如图：

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/2020-12-19-074157.jpg)

最后附上一张基线图：

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/2020-12-19-074215.jpg)

以上。
