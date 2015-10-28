---
layout: post
title: 在table中使用border-radius
description: "在table中使用border-radius"
tags: [技术]
image:
background: triangular.png
comments: true
share: true
---

先来看看设计图吧：

<figure>
    <a href="http://7vznhl.com1.z0.glb.clouddn.com/2015-10-8-01Snip20151028_2.png">
        <img src="http://7vznhl.com1.z0.glb.clouddn.com/2015-10-8-01Snip20151028_2.png" alt="result" />
    </a>
</figure>

<!--more-->

拿到图，先想到还是表格，table标签，可是，table表格是矩形的，没关系，我们有border-radius呀，结果如下：

<p data-height="268" data-theme-id="20434" data-slug-hash="LVGvoX" data-default-tab="result" data-user="puronglong" class='codepen'>See the Pen <a href='http://codepen.io/puronglong/pen/LVGvoX/'>table&&border-radius</a> by puronglong (<a href='http://codepen.io/puronglong'>@puronglong</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>

咦，给table加没有效果

但可以给每个单元格加圆角啊，嗯，好像很有道理的样子，试试：

<p data-height="268" data-theme-id="20434" data-slug-hash="RWyPzP" data-default-tab="result" data-user="puronglong" class='codepen'>See the Pen <a href='http://codepen.io/puronglong/pen/RWyPzP/'>table&&border-radius-2</a> by puronglong (<a href='http://codepen.io/puronglong'>@puronglong</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>

嗯？怎么和想象的不一样捏，左右上角的直线角还在呢，而底部的圆角并没有效果

后来找到问题是：```CSS3's border-radius property and border-collapse:collapse don't mix.```

如此看来collapse是用不了了，那使用border-collapse: separate呢，如下:

<p data-height="268" data-theme-id="20434" data-slug-hash="GpdWjQ" data-default-tab="result" data-user="puronglong" class='codepen'>See the Pen <a href='http://codepen.io/puronglong/pen/GpdWjQ/'>table&&border-radius3</a> by puronglong (<a href='http://codepen.io/puronglong'>@puronglong</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>

这里声明下border-collapse属性的区别了，w3school是这样说的：

<figure>
    <a href="http://7vznhl.com1.z0.glb.clouddn.com/2015-10-8-03Snip20151028_4.png">
        <img src="http://7vznhl.com1.z0.glb.clouddn.com/2015-10-8-03Snip20151028_4.png" alt="result" />
    </a>
</figure>

于是我们看到separate的问题就在于表格边框并不合并，这样会使得边框看起来很粗，实在太丑，难保不会被设计狮打死，

所以问题在于，用border-radius形成圆角，可以，但是在table表单中border-collapse:collapse和border-radius不相容，使用border-collapse:separate可以实现圆角，但单元格边框不会合并

后来解决办法在[这里](http://stackoverflow.com/questions/628301/css3s-border-radius-property-and-border-collapsecollapse-dont-mix-how-can-i)找到，原题最高票答案不适合此需求，因为给出的解决方案是单元格没有边框的，并且是给table加上背景色，会导致单元格加上border后颜色也会同table一样，倒是看看第二票答案，demo：

<p data-height="268" data-theme-id="20434" data-slug-hash="XmqMxN" data-default-tab="result" data-user="puronglong" class='codepen'>See the Pen <a href='http://codepen.io/puronglong/pen/XmqMxN/'>table&&border-radius-4</a> by puronglong (<a href='http://codepen.io/puronglong'>@puronglong</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>

关键在于table标签内不要写border=‘1’，这个border是给单元格加上边框，这里我们单元格是需要边框，但在html里的table标签里直接写就会让每个单元格有边框，合起来就变粗了，于是通过table tr th,table tr td这样来给单元格加上想要的边框，如下：

{% highlight JavaScript %}
table tr th,table tr td {
    border-right: 1px solid #d4d8da;
    border-bottom: 1px solid #d4d8da;
    padding: 5px;
}
{% endhighlight %}

控制单边的边框生成。

哦啦，问题解决了：

<p data-height="268" data-theme-id="20434" data-slug-hash="PPeEML" data-default-tab="result" data-user="puronglong" class='codepen'>See the Pen <a href='http://codepen.io/puronglong/pen/PPeEML/'>table&&border-radius-5</a> by puronglong (<a href='http://codepen.io/puronglong'>@puronglong</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>

以上就是关于在table中使用border-radius碰到的一些问题哒