---
layout: post
title: chrome下click与extent-change的问题
description: "chrome下click与extent-change的问题"
tags: [技术]
image:
  background: triangular.png
comments: true
share: true
---

在chrome下click与extent-change有些问题，记录一下解决方法。

<!-- more -->

比如说，有一张地图map，在chrome中打开，图中有几个座标被标识出来，是我们查询出来的结果，当我们拖动地图查看的时候，当拖拽完毕的时候，需要自动再去查询当前视窗下是否有我们查询的结果，这类触发事件使用的是extent-change，然后每一个座标点击的时候会显示该点的信息窗口，当两者结合起来的时候发现出问题了，当我们点击该点的时候，在chrome中实际上有时会触发拖拽事件，在IE浏览器下没有这个问题。

这样会有什么问题呢？比如我们要点击显示该座标点的详情，但是点击却发现没有效果，因为触发的实际上是拖拽事件。

后来使用的解决方案是，在一开始生成map的时候，把map.extent赋值给一个叫做oldExtent的变量，这就是每次我们移动时之前的map，当我们进行extent-change的时候，进行判断当前的视图有无变化，如果没有变化，说明当前视图并没有移动，此刻click事件不应该出发查询操作，直接return掉，代码如下：

```js
if (oldExtent && event.extent && event.extent.xmin == oldExtent.xmin && event.extent.ymin == oldExtent.ymin && event.extent.xmax == oldExtent.xmax && event.extent.ymax && oldExtent.ymax) {
        return;
    }

    oldExtent = event.extent;
```

return以后，更新oldExtent。