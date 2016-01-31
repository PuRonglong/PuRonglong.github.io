layout: post
title: My codewars(1)
description: "codewars"
tags: [技术,codewars]
image:
  background: triangular.png
comments: true
share: true
---

>这是我的codewars系列，用于收集codewars上遇到的一些题目,先从第8层开始咯~

编程codewars是个很好的东西，现在做的题目虽然简单，还没有涉及到深层次的数据结构和算法等问题，但是对知识点是一个很好的复习和熟悉，类似的网站还有比如fightcode，光是听这个名字就知道了是干什么的啦，通过和两个人的code的一个fight来相互竞争着解决一个问题，看谁更快解决问题，如果把语言看做一把剑的话，它就是用js这把剑去和持有c，java的剑的人去fight咯

<figure>
    <a href="http://7vznhl.com1.z0.glb.clouddn.com/2015-5-7-mycodewarscodewars.jpg">
        <img src="http://7vznhl.com1.z0.glb.clouddn.com/2015-5-7-mycodewarscodewars.jpg" alt="cover of the book" />
    </a>
    <figcaption>codewars</figcaption>
</figure>

1.
Write a function that flattens an Array of Array objects into a flat Array. Your function must only do one level of flattening.

Examples

```flatten([1,2,3]) // => [1,2,3]```
```flatten([[1,2,3],["a","b","c"],[1,2,3]])  // => [1,2,3,"a","b","c",1,2,3]```
```flatten([[[1,2,3]]]) // => [[1,2,3]]```

<!--more-->

从这道题的例子就可以看出这是一道对数组合并的考察，这就涉及到JS中的关于数组的一些操作如reduce,comcat等，那么让我们来好好捋一捋哒：

在JavaScript高级程序设计第三版的P97页的*5.2.9 归并方法*讲到的reduce()和ruduceRight()。这两个方法都会迭代数组的所有项，然后构建一个最终返回的值。这两个方法接受四个参数：前一个值，当前值，项的索引值，数组对象

reduce()方法可对数组中的所有元素调用指定的回调函数。 该回调函数的返回值为累积结果，并且此返回值在下一次调用该回调函数时作为参数提供。

使用reduce()方法可以执行求数组中所有值之和的操作，比如：

{% highlight JavaScript %}
var values = [1,2,3,4,5];
var sum = values,reduce(function(prev,cur,index,array){
return prev + cur;
});
alert(sum);//15
{% endhighlight %}

而w3cschool对concat()方法的解释是此法用于连接两个或两个数组。该方法不会改变现有的数组，而仅仅返回被连接数组的一个副本。

我们还是来看一个例子：
{% highlight JavaScript %}
var a = [1,2,3];
document.write(a.concat(4,5));//1,2,3,4,5
{% endhighlight %}

如果要连接多个数组，可以在concat参数中添加多个数组。但是呢，concat（）方法这种方式占用了两倍内存，因为构成新数组的原来成员并没有销毁，将其置空就可以被垃圾回收了，但这样只是对较小的数组能解决问题，遇到大型数据时还需要优化了。

讨论完这两个方法，那我们来看看如何解决这个问题，博客园上看到一个方法是这样的：

{% highlight JavaScript %}
var flatten = function (array){
   return array.reduce(function(a,b){
       return a.concat(b);
   },[])
}
{% endhighlight %}

在stackoverflow上的另一种解法：

{% highlight JavaScript %}
var flatten = function (array) {
    var newArray = [];
    var arrayLength = array.length;
    for (i = 0; i < arrayLength; i++) {
        newArray = newArray.concat(array[i]);
    }
    return newArray;
}
{% endhighlight %}

这两种方法显然第一种更clever一些，他想到了使用reduce()与concat()方法的组合，第二种没有用到reduce，便想到了定义一个空的数组，让这个数组和传的参数进行concat

2.
Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.

Can you help her?

dear Jenny~let me help you~拿到这道题容易比较想到的是if-else的情况：

{% highlight JavaScript %}
function greet(name){
  if(name === "Johnny"){
    return "Hello, my love!";
  }else{
  return "Hello, "+name+"!"}
}
{% endhighlight %}

不过用三元法一行就能搞定啦

{% highlight JavaScript %}
function greet(name){
  return "Hello, " + (name == "Johnny" ? "my love" : name) + "!";
}
{% endhighlight %}

话说感觉get到一项新技能...

3.
It's to hot, and they can't even…

One hot summer day Pete and his friend Billy decided to buy watermelons. They chose the biggest crate. They rushed home, dying of thirst, and decided to divide their loot, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the number of watermelons in such a way that each of the two parts consists of an even number of watermelons. However, it is not obligatory that the parts are equal.

Example: the boys can divide a stack of 8 watermelons into 2+6 melons, or 4+4 melons.

The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, whether they can divide the fruits in the way they want. For sure, each of them should get a part of positive weight.

Task

Given an integral number of watermelons w (1 ≤ w ≤ 100; 1 ≤ w in Haskell), check whether Pete and Billy can divide the melons so that each of them gets an even amount.

Examples

```divide(2) === false // 2 = 1 + 1```
```divide(3) === false // 3 = 1 + 2```
```divide(4) === true  // 4 = 2 + 2```
```divide(5) === false // 5 = 2 + 3```
```divide(6) === true  // 6 = 2 + 4```

刚开始看的时候会被这道题目的长度给吓到，但实际分析不难发现，问题就是求这个西瓜能不能分成两个人手上的都是偶数，而知只有偶数才能分成两个加数都是偶数，显而易见每人分一份这样是不行的，排除掉偶数2，所以问题就转变成了求分成的数是不是偶数并且这个数不能是2

{% highlight JavaScript %}
function divide(weight){
  return (weight>2)&&(weight%2==0)?true:false;
}
{% endhighlight %}

或者

{% highlight JavaScript %}
function divide(weight){
  return weight > 2 && !(weight % 2);
}
{% endhighlight %}

4.
Teach snoopy and scooby doo how to bark using object methods. Currently only snoopy can bark and not scooby doo.

Use method prototypes to enable all Dogs to bark.

史努比~~

solution:

{% highlight JavaScript %}
function Dog (breed) {
  this.breed = breed;
}

var snoopy = new Dog("Beagle");

Dog.prototype.bark = function() {
  return "Woof";
};

var scoobydoo = new Dog("Great Dane");
{% endhighlight %}

通过在Dog这个函数的原型上声明一个变量，从而让后来new的对象都能继承它的bark方法了

5.
Create a function with two arguments that will return a list of length (n) with multiples of (x).

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array (or list in Python or Haskell.)

Examples:

```countBy(1,10) === [1,2,3,4,5,6,7,8,9,10]```
```countBy(2,5) === [2,4,6,8,10]```

可以得知，题目要求这个函数有两个参数，第一个参数是起始值，后面的值是个数，然后输出是要求每个数都是前一个数加上一个起始值，便想到了用一个循环执行这样一个相加的过程，然后返回一个数组

{% highlight JavaScript %}
function countBy(x,n){
                var z = [];
                z.push(x);
                for (var i = 1; i < n; i++) {
                    z[i] = z[i-1] + x;
                };
                return z;
}
{% endhighlight %}

相比之下还有更简洁的方法：

{% highlight JavaScript %}
function countBy(x, n) {
    var z = [];
    for (i = 1; i <= n; i++) {
        z.push(x * i);
    }
    return z;
}
{% endhighlight %}

6.
Ahoy matey!

You are a leader of a small pirate crew. And you have a plan. With the help of OOP you wish to make a pretty eficient system to identify ships with a heavy booty on board.

Unfortunattely for you, people weigh a lot this days, so how do you know if a ship if full of gold and not people?

You begin with writing a generic Ship class:

function Ship(draft,crew) {
 this.draft = draft;
 this.crew = crew;
}
Every time your spies see a new ship enter the dock, they will create a new ship object:

var titanic = new Ship(15,10);
Now comes the tricky part: An average man will sink the ship by exactly 1.5 units. (Ship's draft goes up) That means the draft can show the estimated weight of the presumable booty aboard.

if it weighs more than 20 without people, it is worthy to board. Your system should have a method

isWorthIt
to decide that:

titanic.isWorthIt() //return false

题意是说海盗有个船，船上有人和货物，要尽可能放多的货物，如果货物比全体船员的1.5倍还多20，那么这艘船就值得board，准备出发了。

{% highlight JavaScript %}
function Ship(draft,crew) {
 this.draft = draft;
 this.crew = crew;
}

Ship.prototype.isWorthIt = function(){
return this.draft-(this.crew*1.5) > 20;
}
{% endhighlight %}
