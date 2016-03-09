layout: post
title: HTML+CSS九宫格
description: "HTML+CSS九宫格"
tags: [代码]
image:
background: triangular.png
comments: true
share: true
---

>使用 HTML+CSS 实现如图布局，border-widht 5px，一个格子大小是 50*50，hover时候边框变为红色

先来看一看效果图吧~

![img](./images/article/2016-3-8/8.gif)

让我们一步一步来制作：

定义一个大的div容器，里面包裹的是ul，对ul下的li进行浮动排列，通过控制width的宽度形成九宫格的形式。

具体点就是每一个li的宽度都是55px，然后li里面有一个a标签，a标签的宽度是50px，然后给a加上一个5px的蓝色border，大致显示出原图了，听起来很美好，可是这时会发现，每一个li因为内部都有一个有5px边框的a标签，所以相邻的border会导致实际上border有10px了，显然不符合预期，怎么办捏？

这时候就要用到神奇的margin负值啦，对每一个li的上和左加一个border宽度的margin负值，如下：

	li{
		margin-top: -5px;
		margin-left: -5px;
	}

看起来很美好，如下：

![img](./images/article/2016-3-8/1.png)

可是当我们hover一个li的时候才发现，实际上是这样的：

![img](./images/article/2016-3-8/2.png)

想到为什么了吗？

因为我们对每个li赋予了margin的负值，然后每个li都会往相应的方向移动5px，解决了border的问题，但是添加hover样式：

	li a:hover{
		border-color: red;
	}

hover的时候让border变为红色，这一步没有错，以九宫格所示的8号格为例，实际上它的右边框是变为红色了的，只是我们的margin-left: -5px让右边方格9往左移动了5px，刚好盖住了8的右边框，看起来这里像是8的右边框的这个未变色边框，实际上是9的左边框，我们hover的是8，所以9的边框当然不会变色了。

知道是位置造成的视觉差，那么我们在位置上下工夫咯~

w3c中position列出了下面几个属性值：

![img](./images/article/2016-3-8/3.png)

absolute是脱离文档流的，用在这里肯定会出问题，而relative是没有脱离文档流的。代码如下：

	li a:hover{
        border-color: red;
        position:relative;
    }

来来来，试试。

![img](./images/article/2016-3-8/4.png)

O(∩_∩)O哈哈~，加上一个left更能看的清楚一些：

![img](./images/article/2016-3-8/5.png)

可以在这里看实际例子：

[关于这个css九宫格的demo地址](http://codepen.io/puronglong/pen/eZZgVN?editors=1100)

上面的例子中我们用到了margin的负值。

margin的负值还是挺有用的，常用的比如还可以用来实现多列等高的布局需求，所称的padding补偿法。

首先把列的padding-bottom设为一个足够大的值，再把列的margin-bottom设一个与前面的padding-bottom的正值相抵消的负值，父容器设置超出隐藏

原图如下：

![img](./images/article/2016-3-8/6.png)

我们可以看到，左右不等高的时候左列会有空窗。使用margin-bottom负值如下：

	.left{
	  float:left; width:150px; background:#B0B0B0;
	  padding-bottom: 2000px;
	  margin-bottom: -2000px;
	}
	.right{ float:left; width:450px; background:#6CC;
	  padding-bottom: 2000px;
	  margin-bottom: -2000px;
	}

显示效果：

![img](./images/article/2016-3-8/7.png)

可以在这里看实际例子：

[css-margin负值-多列等高](http://codepen.io/puronglong/pen/MyyJad?editors=1100)

并且给原本没有width的元素使用margin负值的时候，其实它的宽度是会增加的。通常的使用场景是图文混排时，每行最后一个元素的margin值如何处理？使用margin负值。