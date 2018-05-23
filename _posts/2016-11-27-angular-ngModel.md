---
layout: post
title: angularJS tips(2)：ng-model过滤
description: "angularJS tips(2)： ng-model过滤"
tags: [技术]
image:
  
comments: true
share: true
---

angular tips。

遇到一个需求，需要对ng-model的值进行过滤，记录下解决方案并扩展一下。

<!-- more -->

场景是这样的，如下，有两个input:

```html
经度：
<input class="form-control" style="display: inline-block;width: 120px;" ng-model="position.fLongitude"/> 
纬度：
<input class="form-control" style="display: inline-block;width: 120px;" ng-model="position.fLatitude"/>
```

如上所示，我们的input标签绑定了ng-model，position.fLongitude的值是获取的数据，返回的经纬度数据精确到了小数点后六位，但现在要显示到小数点后两位，并且不改变实际的坐标值。在angular中容易想到用过滤器，类似`|number:2`这样的形式，但是这样使用过滤器是要花括号中，在ng-model中尝试使用了下，如：

```js
ng-model="position.fLongitude | number:2"
```

效果的确是显示了两位小数，但是浏览器中会报一个angular的错误：

```
AngularJs Error: [ngModel:nonassign]
```

官网对这个错误是这么解释的：

![img]({{site.url}}images/article/2016-11-27/1.png)

This error occurs when expression the ngModel directive is bound to is a non-assignable expression.

这个方法并不完美，那如何在ng-model中进行过滤呢？网上找到的解决方法是写一个指令。

html如下，添加了一个指令和readonly属性。

```html
经度：
<input class="form-control" style="display: inline-block;width: 120px;" ng-model="position.fLongitude" display-address readonly/> 
纬度：
<input class="form-control" style="display: inline-block;width: 120px;" ng-model="position.fLatitude" display-address readonly/>
```

在一个``xxxBootstrap.js``文件中启用该指令，如下：

```js
(function () {
    'use strict';

    define([
        'angular',
        'directives/positionPicker/displayAddressDirective',
        'directives/positionPicker/mapDialogController'
    ], function (angular ,displayAddressDirective,mapDialogController) {
        var app = angular.module('app');
        displayAddressDirective.start(app);
        mapDialogController.start(app);
    });
}).call(this);
```

displayAddressDirective.js指令文件的内容：

```js
(function() {
    'use strict';
    define([
        'angular',
    ], function(angular) {
        var app = angular.module('app');
        function displayAddressDirective() {
            return {
                require: 'ngModel',
                link: function(scope, elm, attrs, ctrl) {                        
                    ctrl.$formatters.push(function formatter(value) {
                        return parseFloat(value).toFixed(2);
                    });
                    ctrl.$parsers.unshift(function parser() {
                        return ctrl.$modelValue;
                    });
                }
            };
        }

        function init(app) {
            app.directive('displayAddress', displayAddressDirective);
            return displayAddressDirective;
        }

        return {
            start: init
        };
    });

}).call(this);
```

link中的function就是让我们的数据显示两位的方法，并且查看所传参数还是六位小数，没有被改变。

以上就是对ng-model使用过滤的方法。

看angular权威指南指令一节，把link里的东西讲清楚。

在查找资料的时候看到一个关于ng-model和ng-bind的探讨，有必要提一下：

```
What's the difference between ng-model and ng-bind?
```

ng-bind has one-way data binding ($scope --> view). It has a shortcut {{ val }} which displays the scope value $scope.val inserted into html where val is a variable name.

ng-model is intended to be put inside of form elements and has two-way data binding ($scope --> view and view --> $scope).

上面这个最高票答案把两者的区别解释的很清楚了，但是下面的一个回答也很精彩：

tosh's answer gets to the heart of the question nicely. Here's some additional information....

Filters & Formatters

ng-bind and ng-model both have the concept of transforming data before outputting it for the user. To that end, ng-bind uses filters, while ng-model uses formatters.

filter (ng-bind)

With ng-bind, you can use a filter to transform your data.

formatter (ng-model)

To create an ng-model formatter, you create a directive that does require: 'ngModel', which allows that directive to gain access to ngModel's controller.

看到这里，不禁联想到我们上面的那个ng-model过滤器的问题不也可以用ng-bind来解决吗？因为我们的input后来使用了readonly属性呀，这样可以直接用ng-bind来显示了，之前需求是输入框可修改所以用的input和ng-model。

并且ng-bind可以使用过滤器，用一个demo来更直观说明：

![img]({{site.url}}images/article/2016-11-27/2.png)

上面的问答说明了ng-bind和ng-model两者的内在区别，但两者在应用中的区别还得提一下。

我们知道这两种方法都可以在AngularJS中显示模型中的数据，如：

```html
<p>[[text]]</p>//这里的括号应该是花括号，但是jekyll中也是解析花括号的方式，所以这里换了一下
```
和基于属性的ng-bind指令：

```html
<p ng-bind="text"></p>
```

项目初始化的时候，花括号写法未被渲染的模板会被用户看到，第二种方法在数据加载完成之前用户就不会看到任何内容，所以在初始化页，通常是index页要显示模型数据时可使用ng-bind。

以上。

参考资料：
[whats-the-difference-between-ng-model-and-ng-bind](http://stackoverflow.com/questions/12419619/whats-the-difference-between-ng-model-and-ng-bind)
