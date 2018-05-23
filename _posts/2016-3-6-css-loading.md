---
layout: post
title: css3制作loading
description: "css制作loading"
tags: [技术]
image:

comments: true
share: true
---

> 讨论最近看到的一个loading动效

先来看一看效果图吧~

![img]({{site.url}}images/article/2016-3-6/1.gif)

<!-- more -->

让我们一步一步来制作：

首先呢，定义一个整个的大背景（也就是我们的黑色背景）div，然后在这个div里面是我们的小div，这个小的div里要放的就是我们需要显示的loading动效。代码如下：

HTML:

```html
	<div class = "preloader">
		<div class = "loader">&nbsp</div>
	</div>
```

CSS:

```css
	body, html{
	  width: 100%;
	  height: 100%;
	}

	.preloader{
	  width: 100%;
	  height: 100%;
	  background: #000;
	}

	.loader{
	  width: 2em;
	  height: 2em;
	  position: absolute;
	  top: calc(50% - 1em);
	  left: calc(50% - 1em);
	  transform: translate(165deg);
	}
```

以上，就做好了我们的容器，那么图中的点和线是怎么做的呢？这就要结合伪元素和box-shadow啦~

给loader容器设置伪元素：

```css
	.loader:before{
	  position: absolute;
	  width: 0.3em;
	  height: 0.3em;
	  content: ' ';
	  border-radius: 0.15em;
	  left: 50%;
	  top: 50%;
	  transform: translate(-50%, -50%);
	  box-shadow: 0.85em -0.55em rgba(225, 20, 98, 0.75), -0.85em 0.55em rgba(111, 202, 220, 0.75);
	}
```

如下：

![img]({{site.url}}images/article/2016-3-6/5.png)

width和height两个属性决定两点大小，box-shadow决定两点位置和颜色，总共这两个点有三个位置四种状态，分别是这三个位置，

![img]({{site.url}}images/article/2016-3-6/2.png)

![img]({{site.url}}images/article/2016-3-6/3.png)

![img]({{site.url}}images/article/2016-3-6/4.png)

三个位置是左中右，四种状态是点线点点，拿上面那个点作为例子，当这个点到达中的位置的时候，对应这时的状态要把点的width加长，变为线，过了这个状态到达左边位置的时候状态又变为点，最后的状态时，把位置又定位到初始的时候，这样，一个点的一个动画就算完成了，其他四个点主要就是位置和颜色的不同了

看看动画部分代码：

```css
	@keyframes before {
	    0% {
	        width: 0.3em;
	        box-shadow: 0.85em -0.55em rgba(225, 20, 98, 0.75), -0.85em 0.55em rgba(111, 202, 220, 0.75);
	    }

	    35% {
	        width: 2em;
	        box-shadow: 0 -0.55em rgba(225, 20, 98, 0.75), 0 0.55em rgba(111, 202, 220, 0.75);
	    }

	    70% {
	        width: 0.3em;
	        box-shadow: -0.85em -0.55em rgba(225, 20, 98, 0.75), 0.85em 0.55em rgba(111, 202, 220, 0.75);
	    }

	    100% {
	        box-shadow: 0.85em -0.55em rgba(225, 20, 98, 0.75), -0.85em 0.55em rgba(111, 202, 220, 0.75);
	    }
	}
```

完整代码：

```css
	*{
	    list-style: none;
	    margin: 0;
	    padding: 0;
	    text-decoration:none;
	}
	body{
	    margin: 0;
	    padding: 0;
	    overflow-x: hidden;
	    -webkit-text-size-adjust: none;
	    -webkit-tap-highlight-color: rgba(0,0,0,0);
	    font: 12px "Open Sans", "Helvetica Neue","微软雅黑",Helvetica, Arial, sans-serif;
	    letter-spacing: -0.05em;
	    position: absolute;
	    top: 0;
	    left: 0;
	    max-width:100%;
	    min-width: 100%;
	    -webkit-appearance: none;
	}
	body, html{
	  width: 100%;
	  height: 100%;
	}

	.preloader{
	  width: 100%;
	  height: 100%;
	  background: #000;
	}

	.loader{
	  width: 2em;
	  height: 2em;
	  position: absolute;
	  top: calc(50% - 1em);
	  left: calc(50% - 1em);
	  transform: rotate(165deg);
	}

	.loader:before, .loader:after{
	  position: absolute;
	  width: 0.3em;
	  height: 0.3em;
	  content: ' ';
	  border-radius: 0.15em;
	  left: 50%;
	  top: 50%;
	  transform: translate(-50%, -50%);
	}

	.loader:before{
	  animation: before 2s infinite;
	}

	.loader:after{
	  animation: after 2s infinite;
	}

	@keyframes before {
	    0% {
	        width: 0.3em;
	        box-shadow: 0.85em -0.55em rgba(225, 20, 98, 0.75), -0.85em 0.55em rgba(111, 202, 220, 0.75);
	    }

	    35% {
	        width: 2em;
	        box-shadow: 0 -0.55em rgba(225, 20, 98, 0.75), 0 0.55em rgba(111, 202, 220, 0.75);
	    }

	    70% {
	        width: 0.3em;
	        box-shadow: -0.85em -0.55em rgba(225, 20, 98, 0.75), 0.85em 0.55em rgba(111, 202, 220, 0.75);
	    }

	    100% {
	        box-shadow: 0.85em -0.55em rgba(225, 20, 98, 0.75), -0.85em 0.55em rgba(111, 202, 220, 0.75);
	    }
	}

	@keyframes after {
	    0% {
	        height: 0.3em;
	        box-shadow: 0.55em 0.85em rgba(61, 184, 143, 0.75), -0.55em -0.85em rgba(233, 169, 32, 0.75);
	    }

	    35% {
	        height: 2em;
	        box-shadow: 0.55em 0 rgba(61, 184, 143, 0.75), -0.55em 0 rgba(233, 169, 32, 0.75);
	    }

	    70% {
	        height: 0.3em;
	        box-shadow: 0.55em -0.85em rgba(61, 184, 143, 0.75), -0.55em 0.85em rgba(233, 169, 32, 0.75);
	    }

	    100% {
	        box-shadow: 0.55em 0.85em rgba(61, 184, 143, 0.75), -0.55em -0.85em rgba(233, 169, 32, 0.75);
	    }
	}
```

这是此次demo的codepen地址
[CSS3-loader-1](http://codepen.io/puronglong/pen/EKVJeO)