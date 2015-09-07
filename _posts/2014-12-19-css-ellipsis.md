---
layout: post
title: 聊聊CSS(1):<br  />关于用css实现的文字超出部分显示省略号
description: "CSS"
tags: [技术,CSS]
image:
  background: triangular.png
comments: true
share: true
---

>文字超出部分显示省略号还是比较常用的一个效果,最近看到网上的一些方法亲自实践了一下,发现有些以前一些浏览器不能用的属性现在可以用了，于是总结一下：

我们先来看下HTML代码：

{% highlight JavaScript %}
<div>
    <p><span>用css来实现当文字超出宽度时显示省略号的效果</span></p>
</div>
{% endhighlight %}

CSS代码：

{% highlight JavaScript %}
div{
	width:200px;
}
span{
	display:block;
	width:200px;
	overflow:hidden;
	white-space:nowrap;//段落中的文本不进行换行
	text-overflow:ellipsis;
}
{% endhighlight %}

我们可以看到其中用到了`text-overflow:ellipsis;`网上说这是一个IE特有的属性，别的浏览器不支持，经过实践，现在chrome和火狐都已经支持了，效果和版本号如下：

<!--more-->

在chrome下的效果：

<figure>
	<a href="/images/article/2014-12-19/1.png">
		<img src="/images/article/2014-12-19/1.png" alt="效果" />
	</a>
</figure>

我的chrome版本号：

<figure>
	<a href="/images/article/2014-12-19/2.png">
		<img src="/images/article/2014-12-19/2.png" alt="38.0.2125.111m" />
	</a>
</figure>

在火狐下的效果：

<figure>
	<a href="/images/article/2014-12-19/3.png">
		<img src="/images/article/2014-12-19/3.png" alt="效果" />
	</a>
</figure>

我的火狐版本号：

<figure>
	<a href="/images/article/2014-12-19/4.png">
		<img src="/images/article/2014-12-19/4.png" alt="33.1.1" />
	</a>
</figure>

查到的资料还说opera不支持`text-overflow`，针对Opera的话得使用`-o-text-overflow:ellipsis;`欧朋浏览器还没有装所以无法实践，但通过网上查找已经找到答案，有博主说自己新版的欧朋已经支持这个属性了，看博客时间是2012年，看来也是早就支持了的。

而且CSS中的这些属性都不能少，否则不能显示省略号。可以顺着这样的思路来记，要把文本限制在一行`(white-space:nowrap;`（`white-space`属性声明建立布局过程中如何处理元素中空白符）),这一行有宽度(width)，有宽度就有超出的部分，将超出的部分隐藏起来(`overflow:hidden;`)，然后后面跟上省略号(`text-overflow:ellipsis;`)。

还有一种**非常规**的方法补省略号，要用到伪对象after,思路是一个标签作内容，再加一个标签作填补省略号用，并且加起来的宽度不能超过它们容器的宽度，否则就换行。

来看下CSS代码：

{% highlight JavaScript %}
span{
	display:block;
	width:200px;
	overflow:hidden;
	white-space:nowrap;
}
p{
	clear:both;
}
p span{
	float:left;
	max-width:175px;
}
p:afer{
	content:"...";
}
{% endhighlight %}

这样能有省略号的效果，但会有小小的**问题**，我们一起来看下效果：

<figure>
	<a href="/images/article/2014-12-19/5.png">
		<img src="/images/article/2014-12-19/5.png" alt="效果" />
	</a>
</figure>

在chrome下和火狐下都是这样的效果，可见这样的方法并不完美。

并且使用text-overflow:ellipsis来显示省略号也有好处，可以不用限定字数，对SEO也比较友好，比如我们的标题使用这个属性，标题看起来被截取了，但搜索引擎搜索的时候还是按完整的标题搜索，因为标题实际上并没有被截取，只是没有显示完全而已。

当然这样控制的方法都有一个最大的不足就是只能控制一行，js可以控制多行，并且也不复杂，我们这里只是就事论事罢了。


本次学习不仅学到知识，也再一次验证了那句话：**实践出真知**。不仅要多看，还要多写，多练，实践才是检验真理的唯一标准，因为IT技术发展迅速，不知道什么时候以前不能用的现在就可以用了，以前能用的现在就不能用了，让代码真正的在自己手上过一遍，这是作为程序员基本的一个节操。

