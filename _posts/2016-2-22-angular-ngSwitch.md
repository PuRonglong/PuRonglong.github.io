---
layout: post
title: angular养成记(一)ngSwitch
description: "angular养成记(一)ngSwitch"
tags: [技术]
comments: true
share: true
cover: https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420163837.png
---

> 来聊聊angular中的ngSwitch

angular官网的文档太不错了，比手中的angularjs权威指南好太多，后者讲的不细，总是有种一笔带过的感觉。

ngSwitch选择一组元素中的一个，当这个元素和表达式的值匹配的时候显示。换句话说，你定义了一个放有指令的容器，```on="..."```属性等于一个表达式或者是```ng-switch```。

<!-- more -->

在容器内定义含有这个属性的其他元素，当属性的值和表达式的值匹配时则显示。如果没有找到匹配的表达式则使用默认值。

要注意的是属性的value不能是表达式。因为会被视为为字符串来匹配。例如```ng-switch-when="someVal"```会匹配```"someVal"```而不是表达式```$scope.someVal```的值。

这个指令创建了新的域。

比如：

```html
	<ANY ng-switch="expression">
	  	<ANY ng-switch-when="matchValue1">...</ANY>
	  	<ANY ng-switch-when="matchValue2">...</ANY>
	  	<ANY ng-switch-default>...</ANY>
	</ANY>
```

动画：

* enter:ngSwitch的内容改变并且子元素进入的容器中的时候
* leave:ngSwitch的内容改变并且在前一个内容被从DOM中移除之前

demo1，通过ng-switch-when进行视图切换：

HTML:

```html
    <div class="view-container" ng-controller="viewController as view" ng-switch="view.current">
        <div class="view-page view-1" ng-switch-when="1">
            <input type="button" value="1" ng-click="view.current = '1'" />
            <input type="button" value="2" ng-click="view.current = '2'" />
        </div>
        <div class="view-page view-2" ng-switch-when="2">
            <input type="button" value="1" ng-click="view.current = '1'" />
            <input type="button" value="2" ng-click="view.current = '2'" />
        </div>
    </div>
```

CSS:

```css
.view-page{
    position: absolute;
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
}
body{
    overflow: hidden;
}
.view-1{
    background: #b3c589;
}
.view-2 {
    background: #8fc241;
}

.view-page.ng-enter{
    animation: moveFromRight .5s both;
}
.view-page.ng-leave{
    animation: moveToLeft .5s both;
}
@keyframes moveFromRight{
    from { transform: translateX(100%); }
}
@keyframes moveToLeft{
    to { transform: translateX(-100%); }
}
```

JS:

```js
var myApp = angular.module('myApp', ['ui.router', 'ngAnimate']);

myApp.controller('viewController', function(){
    this.current = '1';
});
```

demo2，如果输入框的值和ng-switch-when匹配则显示：

HTML:

```html
    <div ng-controller="SomeController" ng-switch on="person">
        <input type="text" ng-model="person" />
        <h1 ng-switch-default>请输入</h1>
        <h1 ng-switch-when="puronglong">{{ person}}</h1>
    </div>
```

JS:

```js
    var myApp = angular.module('myApp', []);

    myApp.controller('SomeController', function() {
      person = {};
    });
```

上面看了基本用法以后，那么如果当两个```ng-switch-when```要显示的是同样的内容，这两个```ng-switch-when```可以合并吗？

可以按照下面的demo3：

HTML：

```html
	<select ng-model="status" ng-options="status for status in statusList"></select>
    <p ng-switch ="(status == 'wrong') || (status == 'incorrect')">
        <span ng-switch-when="true">
            Wrong
        </span>
        <span ng-switch-default>
           Correct
        </span>
    </p>
```

JS：

```js
	function ctrl($scope){
    	$scope.statusList=["incorrect","wrong","stuff"];
	}
```

通过在```ng-switch```中控制不同的状态而不是通过```ng-switch-when```来控制，就可以解决这个问题了