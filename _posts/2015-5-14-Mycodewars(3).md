---
layout: post
title: My codewars(3)
description: "codewars"
tags: [技术]
comments: true
share: true
cover: https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420174406.png
---

16.

Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

<!-- more -->

solution:

```js
function lovefunc(flower1,flower2){
    if (flower1%2==0&&flower2%2!==0) {
        return true;
    }else if(flower1%2!==0&&flower2%2==0){
        return true;
    }else return false;
}
```

Best Practice:

```js
function lovefunc(flower1, flower2){
  return flower1 % 2 !== flower2 % 2;
}
```

17.

Description:<br  />
Color Ghost

Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of white" or "yellow" or "purple" or "red" when instantiated

```ghost = new Ghost();```<br  />
```ghost.color //=> "white" or "yellow" or "purple" or "red"```

solution:

```js
var Ghost = function() {
    var array = ['white','yellow','purple','red'];
    var index = Math.floor(Math.random()*array.length);
    this.color = array[index];
}
```

Best Practices:

```js
var Ghost = function() {
	this.color = ["white","yellow","purple","red"][Math.floor(Math.random() * 4)];
};
```

18.

What ?

None of zese codevarriors seemz to remember hiz own name !

Kould you help ?

```var albert = new Warrior("Al")```<br  />
```var boris  = new Warrior("Boris")```

```albert.toString() // "Hi! my name's Boris" ```

example:

```js
    function Warrior(n){
      name = n;  
      this.name = function(n){
        if( n ) name=n;
        return name;
      }
    }
      
    Warrior.prototype.toString = function(){
        return "Hi! my name's "+this.name();
    }
```

solution1:

```js
    function Warrior(n){
      var name = n;
      this.name = function(n){
        if( n ) name=n;
        return name;
      }  
    }

    Warrior.prototype.toString = function(){
        return "Hi! my name's "+this.name();
    }
```

solution2:

```js
    function Warrior(n){
      this.n = n;  
      this.name = function(n){
        if (n) { this.n=n; }
        return this.n;
      }
    }
```

solution3:

```js
function Warrior(n){
  name = n;  //去掉也可通过
  this.name = function(name){
    if( name ) n=name;
    return n;
  }
}
```

其实通过这几个答案就能发现，原题bug在于name属性的问题，此题的tag也的确是在bug下

19.

Description:

Write the definition of the function "say" such that calling this:

```say("Hello")("World")```<br  />
```returns "Hello World"```

solution:

```js
var say = function(string1) {
	return function(string2) {
		return string1 + ' ' + string2;
	}
}
```

20.

Description:

Given an input n, write a function always that returns a function which returns n. Ruby should return a lambda or a proc.

```var three = always(3);```<br  />
```three(); // return 3```

solution:

```js
function always(n) {
 	return function () { return n };
 
}
```

21.

Write a function that can return the smallest value of an array or the index of that value. The function's 2nd parameter will tell whether it should return the value or the index.

Assume the first parameter will always be an array filled with at least 1 number and no duplicates. Assume the second parameter will be a string holding one of two values: 'value' and 'index'.

```min([1,2,3,4,5], 'value') // => 1```<br  />
```min([1,2,3,4,5], 'index') // => 0```

solution:

```js
function min(arr, toReturn) {
    var minNumber = Math.min.apply(Math,arr);
    var num = arr.indexOf(minNumber);
    if (toReturn == 'value') {
        return minNumber;
    }else if (toReturn == 'index') {
        return num;
    };
}
```

Best Practices:

```js
function min(arr, toReturn) {
  var val = Math.min.apply(null, arr)
  return toReturn == 'value' ? val : arr.indexOf(val)
}
```

这道题用到了求数组中最小值，简要总结一下JS中获取数组中最大(最小)值的方法。除了上面用到的```Math.min.apply()```方法,还可以使用sort()方法，如：

```js
    var arr = [7,3,4,6,10]; 
    var b = arr.sort(function(a,b){ 
        return (a-b);
    });
    console.log(b[0]);
```

先通过sort()方法对数组进行排序，注意，sort里的比较函数是一定要传入的。

上面是对一维数组的求法，那么遇到多维数组怎么取得最小值呢？如下：

```js
    var a=[1,2,3,[5,6],[1,4,8]];
    var ta=a.join(",").split(",");//转化为一维数组
    alert(Math.max.apply(null,ta));//最大值
    alert(Math.min.apply(null,ta));//最小值
```

结合join和split

22.

Description:

Shouldn't the two functions getMax1 and getMax2 be equivalent? Can you spot a problem and fix it? Can you learn something about JavaScript style in this kata?

example:

```js
    function getMax1()
    {
      var max = 
      {
       name: 'Max Headroom'
      }
      return max;
    }

    function getMax2()
    {
      return
      {
        name: 'Max Headroom'
      }
    }
```

solution:

```js
    function getMax1()
    {
      var max = 
      {
       name: 'Max Headroom'
      }
      return max;
    }

    function getMax2()
    {
      return{
        name: 'Max Headroom'
      }
    }
```

开始的时候没有弄明白，但是这两句就说的很清楚了：

```
    note Javascript does not require the semicolon but can assume it meaning nothing is returned
    instead move the brace up
```

JavaScript可以不用分号这个是在书上就看到过的，但是知道这个知识点为什么当时没有反应过来呢？所以看和做还是有所不同的，需要结合应用才能更加有效哒~

23.

Description:

Sum Array

Write a method sum (sum_array in python) that takes an array of numbers and returns the sum of the numbers. These may be integers or decimals for Ruby and any instance of Num for Haskell. The numbers can also be negative. If the array does not contain any numbers then you should return 0.

Examples

Assumptions

You can assume that you are only given numbers.<br  />
You cannot assume the size of the array.<br  />
You can assume that you do get an array and if the array is empty, return 0.<br  />
What We're Testing<br  />

We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.

Disclaimer

This is for beginners so we want to test basic loops and math operations. Advanced users may find this extremely easy and can easily write this in one line.

solution:

```js
function sum (numbers) {
    var sum = 0;
    for (var i = 0; i < numbers.length; i++) {
        sum+=numbers[i]
    };
    return sum;
};
```

best practice:

```js
sum = function (numbers) {
	"use strict";
	return numbers.reduce(function(t, n){
		return t + n;
	}, 0);
};
```

考察reduce()