---
layout: post
title: My codewars(2)
description: "codewars"
tags: [技术]
image:

comments: true
share: true
---

7.

Description:
Consider an array of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,

<!-- more -->

```[true,  true,  true,  false,```<br  />
	```true,  true,  true,  true ,```<br  />
	```true,  false, true,  false,```<br  />
	```true,  false, false, true ,```<br  />
	```true,  true,  true,  true ,```<br  />
	```false, false, true,  true]```

The correct answer would be 17.

翻译过来就是如果一个数组中有true，就让num的值增加一个

常规想到的是一个循环，在这个循环中遍历，如果找到一个true，就+1，如下:

```js
function countSheeps(arrayOfSheeps){
	var num=0;
	for (var i = 0; i < arrayOfSheeps.length; i++) {
			if (arrayOfSheeps[i]==true) {
					num++;
			};
	};
	return num;
}
```

但是更clever的方法如下：

```js
function countSheeps(arrayOfSheeps) {
	return arrayOfSheeps.filter(Boolean).length;
}
```

这个more clever的方法用到了filter,那我们来看看JS中的filter:

```js
array1.filter(callbackfn[, thisArg])
```

这个方法的返回值为一个包含回调函数为其返回 true 的所有值的新数组。 如果回调函数为 array1 的所有元素返回 false，则新数组的长度为 0。

8.

Create an any? (JS: any) function that accepts an array and a block (JS: function), and returns true if the block (/function) returns true for any item in the array. If the array is empty, the function should return false.

就是对一个数组进行一个方法，如果能够满足，那么就返回true，否则返回false

```js
function any(arr, fun){
	for(var i = 0; i < arr.length; i++) {
		var v = arr[i];
		if(fun(v, i) === true) {
			return true;
		}
	}  
	return false;
}
```

不过原来还有更简单的方法：

```js
function any(arr, fun){
	return arr.some(fun)
}
```

some()意指某些，指是否某些项合乎条件，而与之相对的是every()，表示每一项都要满足

当时没有反应过来的是这个fun是它已经给好了的，不用再自己写的了

9.

Create a method all? (JS: all) which takes an array, and a block (JS: function), and returns true if the block (/function) returns true for every element in the array. Otherwise, it should return false. If the array is empty, it should return true, since technically nothing failed the block (/function) test.
要求数组中的每个元素都满足方法，由上题可想到使用every()

```js
function all( arr, fun ){
	return arr.every(fun)
}
```

或者常见的循环：

```js
function all( arr, fun ){
	for (i = 0; i < arr.length; i++) {
		 if(!fun(arr[i], i))
			 return false;
	}
	return true;
}

all([1,2,3,4,5], function(v){return v>9});//false
```

10.

We want to create a constructor function 'NameMe', which takes first name and last name as parameters. The function combines the first and last names and saves the value in "name" property.

We already implemented that function, but when we actually run the code, the "name" property is accessible, but the "firstName" and "lastName" is not accessible. All the properties should be accessible. Can you find what's wrong with it? A test fixture is also available

```js
function NameMe(first, last) {
	this.firstName = first;
	this.lastName = last;
	return {name: this.firstName + ' ' + this.lastName};
}
```

for example:

```var n = new NameMe('John', 'Doe');```
```n.firstName //Expected: John```
```n.lastName //Expected: Doe```
```n.name //Expected: John Doe```

这里对不同的输入如firstName和lastName要有不同结果，怎么能用一个return呢，所以去掉这个return，然后再加上同前面一样加上一个this

```js
function NameMe(first, last) {
		this.firstName = first;
		this.lastName = last;
		this.name=first + ' ' + last};
}
```

11.

Description

We need a function that can transform a string into a number. What ways of achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

Examples

```stringToNumber("1234") == 1234```<br  />
```stringToNumber("605" ) == 605```<br  />
```stringToNumber("1405") == 1405```<br  />
```stringToNumber("-7"  ) == -7```

通过描述即可知道是将一个字符串转变为数字，所以solution如下：

```js
var stringToNumber = function(str){
	return parseInt(str);
}
```

以为就这样就完了吗？不，让我们从这道题延伸出什么吧——看看js字符串转换成数字都有哪些方法呢？

1.转换函数

js提供了parseInt()和parseFloat()两个转换函数。前者把值转换成整数，后者把值转换成浮点数。只有对String类型调用这些方法，这两个函数才能正确运行；对其他类型返回的都是NaN(Not a Number)。

2.强制类型转换

还可使用强制类型转换（type casting）处理转换值的类型。使用强制类型转换可以访问特定的值，即使它是另一种类型的。
ECMAScript中可用的3种强制类型转换如下：
Boolean(value)——把给定的值转换成Boolean型；
Number(value)——把给定的值转换成数字（可以是整数或浮点数）；
String(value)——把给定的值转换成字符串。
用这三个函数之一转换值，将创建一个新值，存放由原始值直接转换成的值。

3.利用js变量弱类型转换

你是不是想到了什么，哈哈，一起来看看例子吧~

```js
var str= '056.789 ';
var x = str-0;
```

没错，就是运用了JS的语言特性——弱类型，通过一个算术运算将字符串类型的值转换为数字类型的值，不过一般不推荐这种写法的。

12.

Who likes keywords? Nobody likes keywords, so why use them?

You know what keyword I use too much? if! We should make a function called _if, with its arguments as a logical test and two functions/lambdas where the first function is executed if the boolean is true, and the second if it's false, like an if/else statement, so that we don't have to mess around with those nasty keywords! Even so, It should support truthy/falsy types just like the keyword.

Examples:

_if(true, function(){console.log("True")}, function(){console.log("false")})
// Logs 'True' to the console.

solution:

```js
function _if(bool, func1, func2) {
	return bool ? func1() : func2();
}
```

13.

The code gives an error!

a = 123.toString

solution:

```js
var a = String(123);
var a = 123..toString();
var a = 123 .toString();
var a = (123).toString();
var a = 123 + '';
```

方法有好几种，通过这道题来总结下toString()和String()吧：toString() 方法可把一个逻辑值转换为字符串，并返回结果。如果调用该方法的对象不是 Boolean，则抛出异常 TypeError。几乎每个值都有toString()方法，除了null和undefined。但任何值都可以使用String()方法。String() 函数把对象的值转换为字符串。

14.

Example:

```last( [1,2,3,4] ) // => 4```<br  />
```last( "xyz" )     // => z```<br  />
```last( 1,2,3,4 )   // => 4```

In javascript and CoffeeScript a list will be an array, a string or the list of arguments.

solution:

```js
function last(list) {
	if (arguments.length > 1) {
		return arguments[arguments.length - 1];
	}
	if (Array.isArray(list)) {
		return list.pop();
	} else if (typeof list == 'string') {
		return list.charAt(list.length - 1)
	} else {
		return list;//通过多次if的判断如果都不满足，直接返回list
	}
}
```

或者:

```js
function last(list){
	var last = arguments[arguments.length - 1];
	return last[last.length - 1] || last;
}
```

15.

Create a function which answers the question "Are you playing Banjo?". If your name starts with the letter "R" or lower case "r", you are playing Banjo!

The function takes a name as its only argument, and returns one of the following strings:

"[name] plays banjo"<br  />
"[name] does not play banjo"<br  />
Names given are always valid strings.

solution:

```js
function areYouPlayingBanjo(name) {
	return name.charAt(0)=="r"||"R"?name +" plays banjo":name + " does not play banjo";
}
```

乍一看好像对啊没什么问题，可是问题就出在了```||```运算符上，来总结一下逻辑或运算符```||```： 

当运算符```||```的两个运算数都是布尔值，它对这两个运算数执行布尔OR操作。 

它先计算第一个运算数，如果这个表达式的值可以被转换成true，那么它就返回左边这个表达式的值。否则计算第二个运算数 

即使```||```运算符的运算数不是布尔值，任然可以将它看作布尔OR运算，因为无论它返回的值是什么类型，都可以被转换为布尔值。 

而且另一方面，对非布尔型的运算数使用了```||```，这是利用了它对非布尔型的值会将其返回的特性。该运算符的这一用法通常是选取一组备选值中的第一个定义了的并且非空的值（也就是说第一个不会转换为false的值）

如果像上面这样的话，按照JS语法中的运算优先级，会先进行==运算然后是```||```运算，而```name.charAt(0)=="r"||"R"```中"R"始终为true，这就导致无论是什么运算符进去返回的结果都是true

所以将以上改为如下:

```js
function areYouPlayingBanjo(name) {
	return name.charAt(0)=="r"||name.charAt(0)=="R"?name +" plays banjo":name + " does not play banjo";
}
```

那如果像这样的代码的话，and和or又分别返回多少呢？

```js
var a = 2;
var b = 3;
var and = a && b ;
var or = a || b;
console.log(and);
console.log(or);
```

也许起初会认为： andflag 和orflag 的值都为 true; 毕竟 ```&&``` 和 ```||``` 都是求Boolean ，但实际打出来结果却是and=3,or=2;

那么如果a,b的值为false呢？让我们打出来看看吧：

```js
var a = false;
var b = 0;
var and = a && b ;
var or = a || b;
console.log(and);//false
console.log(or);//0

var a = false;
var b = null;
var and = a && b ;
var or = a || b;
console.log(and);//false
console.log(or);//null

var a = 0;
var b = null;
var and = a && b ;
var or = a || b;
console.log(and);//0
console.log(or);//null

var a = 0;
var b = false;
var and = a && b ;
var or = a || b;
console.log(and);//0
console.log(or);//false
```

简单概括起来就两句话：

```a && b``` :如果执行a后返回true，则执行b并返回b的值；如果执行a后返回false，则整个表达式返回a的值，b不执行；<br  />
```a || b```:如果执行a后返回true，则整个表达式返回a的值，b不执行；如果执行a后返回false，则执行b并返回b的值；<br  />
```&&``` 优先级高于 ```||```;

该逻辑运算符支持短路原则。什么是短路原则呢？
如```&&```中第一个表达式为假就不会去处理第二个表达式，而||正好相反。<br  />
js也遵循上述原则。<br  />
当||时，找到为true的分项就停止处理，并返回该分项的值，否则执行完，并返回最后分项的值。<br  />
当&&时，找到为false的分项就停止处理，并返回该分项的值。

分析一下语境。或，```||```，只有前面的不能通过，后面的语句才能执行。与，```&&```， 只有前面的能通过，后面的语句才能执行。

根据短路原理还能这样改写：

```js
if(a >=5){ 
alert("你好"); 
} 
//可以简成： 
a >= 5 && alert("你好"); 
```