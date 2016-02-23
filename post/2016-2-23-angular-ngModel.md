layout: post
title: angular养成记(二)ngModel
description: "angular养成记(二)ngModel"
tags: [代码]
image:
background: triangular.png
comments: true
share: true
---

>聊聊angular中的ngModel

先来看看angular权威指南中对```ng-model```的定义：

```ng-model```指令用来将```input,select,text area```或自定义表单控件同包含他们的作用域中的属性进行绑定。它可以提供并处理表单验证功能，在元素上设置相关的CSS类(ng-valid,ng-invalid等)，并负责在父表单中注册控件。

它将当前作用域中运算表达式的值同给定的元素进行绑定。如果属性并不存在，它会隐式创建并将其添加到当前作用域中。

我们应该始终用ngModel来绑定$scope上一个数据模型内的属性，而不是$scope上的属性，这可以避免在作用域或后代作用域中发生属性覆盖。

```ng-model```比较常见的就是用于input标签的双向数据绑定

demo1:

HTML:

	<body >
		<div ng-controller="HelloController">
		    <p>双向绑定</p>
		    <input ng-model="greeting">
		    <p>Hello {{greeting || "World"}}</p>
		    <button ng-click="init()">重置</button>
		    <hr>
		</div>

		<script>
		    function HelloController($scope) {
		        $scope.init = function() {
		            $scope.greeting = "Hello";
		        }
		    }
		</script>
	</body>

```ng-model```为```greeting```的这个input中输入的值就是下面p标签中```greeting```的对应值。

结合上次的```ng-switch```，若```ng-model```的值和```ng-switch```的值相等，则可以通过```ng-model```控制```ng-switch```内容的显示

demo2:

HTML:

	<input ng-model = "selection" />
	<code>selection={{selection}}</code>

	<div class="animate-switch-container"
	ng-switch ="selection">
		<div class="animate-switch" ng-switch-when="settings">Settings Div</div>
		<div class="animate-switch" ng-switch-when="home">Home Span</div>
		<div class="animate-switch" ng-switch-default>default</div>
	</div>

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

用```ng-pattern```匹配一个正则表达式，当input输入框为empty的时候，输入框的背景是绿色，输入非纯数字时样式为```.myinput.ng-invalid```，


























