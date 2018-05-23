---
layout: post
title: 聊聊CSS(4):CSS3中的transition
description: "CSS3:transition"
tags: [技术]
image:

comments: true
share: true
---

> 聊聊CSS3中的transition

先让我们来看看一个实际例子吧：

举一个网上看到的例子，火箭起飞，通过下面的gif图片我们能看到当鼠标移入太空的时候，火箭升空并倾斜，鼠标移除恢复原样
![img](http://7vznhl.com1.z0.glb.clouddn.com/2015-9-1-02)

<!-- more -->

W3C标准中对CSS3的transition是这样描述的：

CSS的transition允许CSS的属性值在一定的时间区间内平滑地过渡。这种效果可以在鼠标单击，获得焦点，被点击或对元素任何改变中触发，并圆滑地以动画效果改变CSS的属性值。简洁点说就是当元素从一种样式变换为另一种样式时为元素添加效果。

transition主要有***四个属性***，那这四个属性怎么记呢？变换的话总得有变换的属性名吧，知道是要哪个属性变，还得有变换的持续时间吧，持续时间里还得有变换速率吧，是先快后慢呢还是先慢后快呢；最后呢，一般动画都会有个延迟选项吧；所以就是**属性**，**时间**，**速率**，**延迟**

这四个属性中又分别有各自的属性值。

来看第一个，属性，它有三个属性值:<br  />
分别是none(没有属 性改 变)；all（所有属性改变）这个是默认值；indent（元素属性名）；当其值为none时，transition停止执行，当指定为all 时，则元素产生all属性值在变化时都将执行transition效果，ident是可以指定元素的某一个属性值。这里ident指定的属性值有一点需要注意的是，不是所有的属性改变都会触发transition动作效果，具体有哪些CSS属性类型可以实现transition这样的持续在某一段时间内进行动画变换，W3C官方给出有列表，[这里](http://www.w3.org/TR/css3-transitions/#properties-from-css-)。

第二个时间就很好理解了，表示转换过程持续的一段时间。

第三个速率是最有意思的一个属性值了:<br  />它表示在这段时间内随着时间推进属性值改变时的的变换速率。而这个属性呢有7个属性，分别是ease(逐渐变慢);linear(匀速)；ease-in(加速);ease-out(减速);ease-in-out(加速然后减速);cubic-bezier(自定义时间曲线);前面6个值其实就是选取的自定义时间曲线的某一个点。CSS3中这条曲线是按照[贝塞尔曲线](http://baike.baidu.com/link?url=TPrH0xPK4dERFnDo6vGUJ9Rj2zW_yHyUoXvXb50maxU0-sb7nugcFnqUq3LKYPze7HxoHtPgvIsbW_eO69cStK)进行计算的，从百科中我们可以看到关于这条曲线的各种计算公式啊，以及通过它牵扯出来的一门学科，叫计算机矢量图形学。但在这里我们更关心的是它的意义：无论是直线或曲线都能在**数学**上予以描述。也就是我们只需要知道cubic-bezier这个属性有(x1,y1,x2,y2)这四个点，通过这四个点可以画出一条曲线，这条曲线呢，表现的就是属性值的一个变化速率，至于这条曲线背后的数学知识就不要纠结啦。说到这里，就不得不提一下chrome浏览器的在调试CSS动画时的方便了，如下图：我们可以通过上方的那个小球就能即时看到动画效果，并且拖动中间两个点来自定义速率：

![img](http://7vznhl.com1.z0.glb.clouddn.com/2015-9-1-01transition.gif)

最后一个延迟也很好理解，就是指延迟多少时间后再进行属性值改变

当我们想要同时改变几个属性值的时候，我们可以用all，比如

```transition: all 0.6s ease-in-out;```

可是这样的话，所有属性值的改变时间，速率，延迟都是一样的，如果想要这几个不同的属性改变时的时间，速率，延迟不一样，也可以分别指定，如：
```transition: width 0.6s ease-in-out 1s,height 0.6s ease-in-out;```

那么更关键的在于实际应用中能有什么新的体验呢？

就是我们看到的第一个火箭的例子了，主要代码在这里

```html
<style type="text/css"> 
/* 这是初始状态 */ 
#outerspace { 
	position: relative; 
	height: 400px; 
	background: #0c0440 url(/images/outerspace.jpg);
} 

div.rocket { 
	position: absolute; 
	bottom: 10px;
	left: 20px;
	-webkit-transition: all 3s ease-in;
	transition: all 3s ease-in;
} 
div.rocket img { 
	-webkit-transition: all 2s ease-in-out;
	transition: all 2s ease-in-out;
}
/* 最后状态 */ 
#outerspace:hover{
	backgrouond-position: -50% bottom;
}
#outerspace:hover div.rocket { 
	-webkit-transform: translate(540px,-200px);
	transform: translate(540px,-200px);
}
#outerspace:hover div.rocket img {
	-webkit-transform: rotate(70deg);
	transform: rotate(70deg);
}
</style>
```

通过代码能看的比较清楚的描述transition的作用：过渡。通过定义初始值和最终值，如果有transition属性那么就会在到最终状态的过程中有过渡动画。这里通过定义hover时太空往左走和火箭往右走产生“飞”的感觉。

而这里transform只是定义状态而已，过渡动画是靠transition完成的，不过貌似现在animation用的比较多些。

这里```background-position:50% 50%;```可以用来定义背景图片居中，左上角是0,0;右下角是100,100;想要说的是这里的百分比定位的点是容器和容器内元素的百分比的点重合的位置，不是左上角。可看官网上的解释[background-position](http://www.w3.org/TR/css3-background/#the-background-position)

在某篇文章中看到这样的效果：

![img](http://7vznhl.com1.z0.glb.clouddn.com/2015-9-2-01demo.gif)

这里其实是两张图片，通过```background-position```将两张图定位重合，对背景色的图片开始height:0,当:hover的时候再给height一个值，中间用transition,这样当height变化时,因为定位重合，看起来就好像是从底部“长”出来一样。

这些是transition部分，以后再聊聊transform,animation等~