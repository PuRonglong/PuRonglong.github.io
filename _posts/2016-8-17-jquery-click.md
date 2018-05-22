---
layout: post
title: jquery,echarts,postal的一些知识点
description: "jquery,echarts,postal的一些知识点"
tags: [技术]
image:
  background: triangular.png
comments: true
share: true
---

最近使用jquery，echarts和postal的时候遇到一些问题，其中的一些点解决后总结记录一下：

<!-- more -->

### jquery中click多次触发问题：

在使用jquery的click事件的时候遇到一个问题，点击第一次的时候触发一次click事件，当从别的页面回到此页再次点击就会触发两次click事件，第二次触发是因为在原来绑定的事件上再次绑定了一次，通常的做法是在绑定之前先解绑以确保事件不会绑定多次，如下：

```js
$('#inMoney').unbind("click").click(function() {
	......
});
```

### 重绘echarts报错问题：

我使用的2.0版本。首先重现一下场景：

要绘制两张echarts图表，进入页面绘制第一张图，点击详情绘制第二张echarts，不报错，切换到别的页面切换回来，第一张图存在，第二张图隐藏，点击详情显示第二张图，功能正确，但是在浏览器里能看到提示报错：

```
Echarts Cannot read property 'modLayer' of null
```

在github的地址的issue里可以看到有人讨论此问题：[https://github.com/ecomfe/echarts/issues/1885](https://github.com/ecomfe/echarts/issues/1885)

分析原因应该是再次进入时第二个echarts图表所对应的echart对象已经不存在了，所以在第二次绘制时重新初始化一下应该可以解决此问题：

```js
myChartmap = echarts.init(document.getElementById('moveMap'));
```

问题解决。

重新初始化解决重绘echarts报错。

宝宝开心。

### 使用postal.js在angualr中发布事件

主要是一个事件的发布和接受问题。在发布和接受中定义相同的频道和主题，就能在同一个频道里接受相应主题的信息。

```js
$scope.$bus.publish({
    channel: 'chart',
    topic: 'chart.onStatistics',
    data:{}
});

$scope.$bus.subscribe({
    channel: 'chart',
    topic: 'chart.onStatistics',
    callback: function(data) {
        var name = data.name;
        $scope.vm.visible = false;
        $scope.vm.minimizedBarVisible = false;
        $scope.$bus.publish({
            channel: "statisticsEntity",
            topic: "statisticsEntity.close",
            data: {}
        });
        }
    }
});
```

从中可以看到发布的时候可以传data数据，接受到信息以后在callback里进行接受到信息以后的回调函数。

而且从上面的一个例子可以看到postal的一个弊端，就是这儿发布一个事件一那儿发布一个事件，这样有些乱，有时候都不知道有没有在别的地方发布或接受某些事件。

确实这是以前的做法，发布事件来处理后续操作，其实主流来说应该使用路由来控制不同状态。