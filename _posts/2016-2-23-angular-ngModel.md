---
layout: post
title: angular养成记(二)ngModel
description: "angular养成记(二)ngModel"
tags: [技术]
image:

comments: true
share: true
---

> 聊聊angular中的ngModel

先来看看angular权威指南中对```ng-model```的定义：

```ng-model```指令用来将```input,select,text area```或自定义表单控件同包含他们的作用域中的属性进行绑定。它可以提供并处理表单验证功能，在元素上设置相关的CSS类(ng-valid,ng-invalid等)，并负责在父表单中注册控件。

<!-- more -->

它将当前作用域中运算表达式的值同给定的元素进行绑定。如果属性并不存在，它会隐式创建并将其添加到当前作用域中。

我们应该始终用ngModel来绑定$scope上一个数据模型内的属性，而不是$scope上的属性，这可以避免在作用域或后代作用域中发生属性覆盖。

```ng-model```比较常见的就是用于input标签的双向数据绑定

demo1:

HTML:

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420151521.png)

```ng-model```为```greeting```的这个input中输入的值就是下面p标签中```greeting```的对应值。

结合上次的```ng-switch```，若```ng-model```的值和```ng-switch```的值相等，则可以通过```ng-model```控制```ng-switch```内容的显示

demo2:

HTML:

```html
	<input ng-model = "selection" />
	<code>selection={{selection}}</code>

	<div class="animate-switch-container"
	ng-switch ="selection">
		<div class="animate-switch" ng-switch-when="settings">Settings Div</div>
		<div class="animate-switch" ng-switch-when="home">Home Span</div>
		<div class="animate-switch" ng-switch-default>default</div>
	</div>
```

当关联ng-model的select/input/textarea元素在改变时涉及以下的css类：

ng-valid: the model is valid

ng-invalid: the model is invalid

ng-valid-[key]: for each valid key added by $setValidity

ng-invalid-[key]: for each invalid key added by $setValidity

ng-pristine: the control hasn't been interacted with yet

ng-dirty: the control has been interacted with

ng-touched: the control has been blurred

ng-untouched: the control hasn't been blurred

ng-pending: any $asyncValidators are unfulfilled

ng-empty: the view does not contain a value or the value is deemed "empty", as defined by the ngModel.NgModelController method

ng-not-empty: the view contains a non-empty value

demo3:

HTML:

```html
	<script>
	 angular.module('inputExample', [])
	   .controller('ExampleController', ['$scope', function($scope) {
	     $scope.val = '1';
	   }]);
	</script>
	<style>
	  .my-input {
	    transition:all linear 0.5s;
	    background: transparent;
	  }
	  .my-input.ng-invalid {
	    color:white;
	    background: red;
	  }
	  .my-input.ng-empty{
		background: green;
	}
	</style>
	<p id="inputDescription">
		Update input to see transitions when valid/invalid.
		Integer is a valid value.
	</p>
	<form name="testForm" ng-controller="ExampleController">
		<input ng-model="val" ng-pattern="/^\d+$/" name="anim" class="my-input"
	         aria-describedby="inputDescription" />
	</form>
```

用```ng-pattern```匹配一个正则表达式，当input输入框为empty的时候，输入框的背景是绿色，输入非纯数字时样式为```.myinput.ng-invalid```，

demo4:

联系上次说到的```ng-switch```，```stackoverflow上```有个问题说，当在ng-switch里有一个ng-model，可是在console.log这个ng-model的值的时候打不出来，这个问题还是有价值的，这里说一下，他的代码如下：

HTML：

```html
	<div ng-controller="Ctrl">
		<select ng-model="selection" ng-options="item.type for item in items">
		</select>
		<tt>selection={{selection}}</tt>
		<hr/>
		<div>
			<ul>
			  <li ng-repeat="op in options"><a style="line-height: 13px;" title="{{op.title}}" tabindex="-1" href ng-click="selectSearchType(op)">{{op.title}}</a></li>
			</ul>
		</div>

		<span class="pew"  ng-switch on="searchType.type" >
			<div class="pew" ng-switch-when="title1">Settings Div</div>
			<span class="pew"  ng-switch-when="title2"><input ng-model="test" placeholder="pre" type="text" />{{test}}</span>
			<span class="pew"  ng-switch-default>default</span>
		</span>
		<button ng-click="actionme()">click</button>
	</div>
```

JS：

```js
	function Ctrl($scope) {
	  $scope.items = [{'type' : 'settings'}, {'type':'home'}, {'type':'other'}];
	  $scope.selection = $scope.items[0];

	  $scope.options = [
	    {'title' : 'Title1', 'label' : 'Zip code', 'type' : 'xxx' },
	    {'title' : 'Title2', 'label' : 'MD', 'type' : 'title1'},
	    {'title' : 'Title3', 'label' : 'DMS', 'type' : 'title2'}
	];

	  $scope.test = '';
	  $scope.searchType = $scope.options[0];

	  $scope.selectSearchType = function(op){
	    $scope.searchType = op;
	  };

	  $scope.actionme = function(){
	    console.log('value is:' + $scope.test);
	    // alert($scope.test);
	  };
	}
```

原来是ng-switch创建了他自己的作用域。所以事实上是在ng-switch里创建了一个子作用域。在ngSwitch指令下的作用域中存在另一个test原型。当input中输入value然后点击按钮想要打印父作用域的原型时，实际上子作用域上的改变不能change父作用域上的原型。

ng-model里的是子作用域的原型，而想要打印的是父作用域的原型，所以会出现```noting is binded for the scope attribute $scope.test```

解决方法：

方法一：

```html
	<input ng-model="test.value" placeholder="pre" type="text" />
	$scope.test={value:''}
```

方法二：

```html
	<input ng-model="$parent.test" placeholder="pre" type="text" />
```