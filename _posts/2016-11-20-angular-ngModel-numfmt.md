---
layout: post
title: angularJS tips(1) ：报错[ngModel:numfmt]
description: "angularJS tips(1) ：报错 [ngModel:numfmt]"
tags: [技术]
image:
  background: triangular.png
comments: true
share: true
---

使用angular 1.x版本遇到报错[ngModel:numfmt]问题。

<!-- more -->

如图：

![img]({{site.url}}images/article/2016-11-20/1.png)

浏览器里报了这个错，什么原因导致的呢？又如何解决？先来复现一下当时的场景吧，如图所示，有上下两个div，

![img]({{site.url}}images/article/2016-11-20/2.png)

下面的div刚开始ng-show的值是false的，点击上面的编辑按钮让下面的div显示，并将上面的值赋给下面div中的空格里，错误就是在点击的时候报的，那么这个编辑按钮都进行了哪些操作呢？如下：

```js
$scope.messageTellServiceEdit = function(){
    $scope.messageTellSettingVisible = true;
    $scope.settingSms_url = $scope.messageServiceDataUrl;
    $scope.settingPre_day = $scope.messageServiceDataPreDay;
    $scope.settingSend_hour = $scope.getHour;
    $scope.settingSend_min = $scope.getMinute;
    $scope.settingSend_second = $scope.getSecond;
    $scope.settingSend_content = $scope.messageServiceDataTellContent;
    $("#inputDay").val($scope.settingPre_day);
    $("#inputHour").val($scope.getHour);
    $("#inputMin").val($scope.getMinute);
    $("#inputSecond").val($scope.getSecond);
};
```

HTML里面是这样的：

```html
<input id="inputHour" type="number" min="0" max="23" class="fontftw" ng-model="settingSend_hour" style="margin-right:5px;width:39px;height:35px;border:1px solid #a3caf4;font-size:15px;"><span>时</span>
```

查找了下这个问题，有一篇说是指令（驼峰书写）与HTML中调用的指令名称（小写）不相同导致的。改用-的形式可以解决。检查自己的指令是用的-形式，应该不是这个问题，查到另一个帖子说：

AngularJS 前台报错 ngModel:numfmt

Error: ngModel:numfmt Model is not of type `number`

错误：ngModel：numfmt模型的类型是`number`

就是说你input中model的参数可能是text，然后你在input的type中的参数是number。这样就会造成model和你Type的参数类型不匹配，然后angularJS就会报错，并且你的参数会在浏览器中显现不出来。

可是我的浏览器里除了ngModel:numfmt并没有说Model is not of type `number`啊。但应该是类型的原因，试一下吧，既然是number的缘故，先把number改为text果然就没有报错误了，然后在浏览器打断点调试，比如这一句$scope.settingSend_hour = $scope.getHour;后者的值是一个'3'，注意这是一个字符串，

这个settingSend_hour的model值我们在html里面是这样写的：

```html
<input id="inputHour" type="number" min="0" max="23" class="fontftw" ng-model="settingSend_hour" style="margin-right:5px;width:39px;height:35px;border:1px solid #a3caf4;font-size:15px;"><span>时</span>
```

打出来它的值的数据类型是number，因为其中定义了type="number"，可能是这两者数据类型的不同导致我们在执行：

```js
$scope.settingSend_hour = $scope.getHour;
```
的时候导致错误了，试着在这里给数据类型做个处理如：$scope.settingSend_hour = parseInt($scope.getHour);果然不再报错。问题解决啦。

在查资料过程中看到一个点这里也提一下：

```
"ng-show" just hide and show the element and the element is still render,
when using "ng-if" the element would be removed or don't exist in the DOM when false.
```

这段说明了ng-show和ng-if的区别。

以后再看到这个报错就知道是数据类型的缘故了。

这个问题解决了，但是让我们从中延伸一下。

我们知道js里面有5种基本数据类型，number,string,null,undefined,boolean，上面遇到的报错问题中我们用到了parseInt方法，把string的数据类型变为number数据类型，那么还有哪些其他方法来进行这种数据类型改变呢？

第一种是parseInt()方法，w3c定义parseInt() 函数可解析一个字符串，并返回一个整数。它的几种特殊情况：

```js
parseInt('a') //NaN
parseInt('10.1') //10
```

第二种方法是使用parseFloat函数，道理和parseInt()一样的，区别在于parseFloat() 函数可解析一个字符串，并返回一个浮点数。比如：

```js
parseFloat("34.66") //34.66
```

第三种方法使用js的Number()方法进行类型转换，可转换为整数或浮点数。js权威指南50页指出，当不通过new运算符调用这些函数时，它们会作为类型转换函数进行类型转换。

它的用法结果如：

```js
Number('1') //1
Number('1.0') //1
Number('1.1') //1.1
Number(null) //0
Number(undefined) //NaN
Number(false) //0
Number(true) //1
Number( "5.6.7 ") //NaN
Number('a') //NaN
```

这里要注意的是Number(null)可以转化为数字0，但是Number(undefined)却不可以。

而类似的类型转换方法还有：

Boolean(value)——把给定的值转换成Boolean型。

String(value)——把给定的值转换成字符串。

Boolean(value)方法能把给定的值转换成布尔类型，我们知道一般用1来表示true，0表示false，所以有

```js
Boolean(1) //true
Boolean(0) //false
Boolean(-1) //true
Boolean(undefined) //false
Boolean(null) //false

String(null); //'null'
```

第四种方法是使用js弱类型的特性，就像通过'1'+2可以输出'12'，将字符串转换为数字类型可以如下：

```js
'2'*1   //2
'2'-0   //2
```

以上。