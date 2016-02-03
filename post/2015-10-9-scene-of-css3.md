layout: post
title: 一个css3实现的简单场景
description: "一个css3实现的简单场景"
tags: [技术,CSS]
image:
background: triangular.png
comments: true
share: true
---

>看到的一个demo，实现一遍：

一个简单的demo，表现了日出而作，日落而息的场景，让我们来看看是怎么实现的：

![img](http://7vznhl.com1.z0.glb.clouddn.com/2015-10-9-01scene-sun.gif)

首先我们要知道一个关键帧的概念，其实就类似于给每一个动画照相，照出来的照片就是这个动画里的某一帧，而css3的animation就是通过分别定义某一张照片的样式，再定义一个持续时间，然后它自己会把这几帧连起来形成动画。

首先对这个场景进行分离，分别是我们需要给其加上动画的几个元素，有最基础的，天空，大地，然后是太阳，云朵，月亮。

还要定义animation每个属性的属性值：

	animation-name: sky;/*动画名称*/
    animation-duration: 10s;/*周期时长*/
    animation-timing-function: ease;/*规定动画速度曲线*/
    animation-iteration-count: 1;/*规定动画播放次数*/
    animation-direction: normal;/*动画方向*/
    animation-play-state: running;/*是否暂停*/
    animation-fill-mode: forwards;/*设置对象状态为动画开始时的状态*/

每一帧就是一个状态，天空和大地比较简单，都分别有两种，天黑天亮，如下：

<p data-height="500" data-theme-id="20434" data-slug-hash="dYKmro" data-default-tab="result" data-user="puronglong" class='codepen'>See the Pen <a href='http://codepen.io/puronglong/pen/dYKmro/'>scene1-sun-1</a> by puronglong (<a href='http://codepen.io/puronglong'>@puronglong</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>

然后是太阳，太阳初升和日落时是红色的，正午呈黄色，升起和降落的位置有所变化，并且它的层级应该在大地后面，天空前面，如下所示：

<p data-height="500" data-theme-id="20434" data-slug-hash="yYExyR" data-default-tab="result" data-user="puronglong" class='codepen'>See the Pen <a href='http://codepen.io/puronglong/pen/yYExyR/'>scene1-sun-2</a> by puronglong (<a href='http://codepen.io/puronglong'>@puronglong</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>

云朵从左边过来，慢慢往右边行走，注意这里的云朵其实是由三个div做成的，这里通过border-radius分别设置垂直半径和水平半径形成一个椭圆，三个叠加在一起就形成一个抽象的云朵啦，而云朵的层级还要在太阳之上，要盖住太阳，如下：

<p data-height="500" data-theme-id="20434" data-slug-hash="vNrzNy" data-default-tab="result" data-user="puronglong" class='codepen'>See the Pen <a href='http://codepen.io/puronglong/pen/vNrzNy/'>scene1-sun -3</a> by puronglong (<a href='http://codepen.io/puronglong'>@puronglong</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>

最后需要添上的就是我们的月亮姐姐啦，要等天黑以后再出来，月牙形的是由两个圆形制作的，不过其中一个圆形的颜色和天黑的颜色一样所以看不出来罢了，月亮出来后云朵为什么要那么快躲起来呢，有云，月黑风高夜，杀人放火时，😂

<p data-height="500" data-theme-id="20434" data-slug-hash="ZbRMLZ" data-default-tab="result" data-user="puronglong" class='codepen'>See the Pen <a href='http://codepen.io/puronglong/pen/ZbRMLZ/'>scene1-sun-4</a> by puronglong (<a href='http://codepen.io/puronglong'>@puronglong</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>

以上就是一个简单场景中对css3中animation属性的运用。