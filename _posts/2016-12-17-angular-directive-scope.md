---
layout: post
title: angular tips(3):directive之scope
description: "angular tips(3):directive之scope"
tags: [技术]
image:
  
comments: true
share: true
---

指令是angular的强大功能之一，指令作用域则是指令中一个重要的点。

<!-- more -->

angular中一个指令被创建以后，它的作用域有两种情况，继承父作用域或创建自己的作用域，而在我们的指令中，可以通过配置scope参数更改相应的作用域范围。

> scope参数是可选的，可以被设置为true或一个对象。默认值是false。
> 当scope设置为true时，会从父作用域继承并创建一个新的作用域对象。

从上可知scope值有布尔，对象两类三种：

当scope参数被设置为false时,在指令模板中可以直接使用父作用域中的变量，函数，更改子作用域变量会影响父作用域。

当scope参数被设置为true时,在指令模板中可以继承父作用域中的变量，函数，更改子作用域变量不会影响父作用域。

当scope参数是一个对象的时候，表明这是一个隔离作用域。通过几种符号可以将指令内部的隔离作用域，同指令外部的作用域进行数据绑定。下面主要来说说第三种情况：

来看网上@finley的一个示例：

<p data-height="330" data-theme-id="20434" data-slug-hash="EyraKX" data-default-tab="result" data-user="mafeifan" data-embed-version="2" data-pen-title="scope = {}" class="codepen">See the Pen <a href="http://codepen.io/mafeifan/pen/EyraKX/">scope = {}</a> by finley (<a href="http://codepen.io/mafeifan">@mafeifan</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="https://production-assets.codepen.io/assets/embed/ei.js"></script>

HTML内容:

```html
<div class="container" ng-controller="MyController">
    <div class="my-info">
    名字：{\{name}}<span ng-bind="name"></span><br/>
    年龄：<span ng-bind="age"></span><br />
    </div>
    <div class="my-directive" my-directive my-name="{\{name}}" age="age" change-my-age="changeAge()"></div>
</div>
```

js内容：

```js
angular.module("MyApp", [])
  .controller("MyController", function($scope) {
    $scope.name = "dreamapple";
    $scope.age = 20;
    $scope.changeAge = function() {
      $scope.age = 0;
    }
  })
  .directive("myDirective", function() {
    return {
      restrict: "AE",
      scope: {
        name: '@myName',
        age: '=',
        changeAge: '&changeMyAge'
      },
      replace: true,
      template: "<div class='my-directive'>" +
        "<h3>下面部分是我们创建的指令生成的</h3>" +
        "我的名字是：<span ng-bind='name'></span><br/>" +
        "我的年龄是：<span ng-bind='age'></span><br/>" +
        "在这里修改名字：<input type='text' ng-model='name'><br/>" +
        "<button ng-click='changeAge()'>修改年龄</button>" +
        " </div>"
    }
  });
```

scope对象参数里有3类符号：

> @符号将本地作用域同DOM属性的值进行绑定。指令内部作用域可以使用外部作用域的变量。

初始化的时候指令中的name变量是和父级作用域中一样的，当修改指令中的name变量的时候，没有改变父级作用域中的name值。

> =符号可以将本地作用域上的属性同父级作用域上的属性进行双向的数据绑定。就像普通的数据绑定一样。

调用函数修改age的值时，=符号双向数据绑定的原则让父级作用域中age和子级作用域中age值都改变了。写法上注意一个是属性的值，一个是属性，所以在一个有方括号一个没有。

上面的例子如果只想子级age的值变化而父级age值不变，调用函数改变age值时就应该只改变子级作用域中的age，可以这样修改：

```html
<div class="container" ng-controller="MyController">
    <div class="my-info">
    名字：{\{name}}<span ng-bind="name"></span><br/>
    年龄：<span ng-bind="age"></span><br />
    </div>
    <div class="my-directive" my-directive my-name="{\{name}}" age="{\{age}}" change-my-age="changeAge()"></div>
</div>
```

js文件：

```js
angular.module("MyApp", [])
  .controller("MyController", function($scope) {
    $scope.name = "dreamapple";
    $scope.age = 20;
  })
  .directive("myDirective", function() {
    return {
      restrict: "AE",
      scope: {
        name: '@myName',
        age: '@'
      }, 
      link:function(scope){
        scope.changeAgeChild=function(){
          this.age=666;
        }
      },
      replace: true,
      template: "<div class='my-directive'>" +
        "<h3>下面部分是我们创建的指令生成的</h3>" +
        "我的名字是：<span ng-bind='name'></span><br/>" +
        "我的年龄是：<span ng-bind='age'></span><br/>" +
        "在这里修改名字：<input type='text' ng-model='name'><br/>" +
        "<button ng-click='changeAgeChild()'>修改年龄</button>" +
        " </div>"
    }
  });
```

这样子作用域中的age被改变，而父级不变。

参考资料：

《angular权威教程》