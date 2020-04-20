---
layout: post
title: 让按钮变得有趣
description: "让按钮变得有趣"
tags: [技术]
comments: true
share: true
cover: https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420162244.png
---

最近在zealer网站上看到一个有趣的动画效果，分析并实现了下，讲讲过程。

<!-- more -->

来，我们先看看效果(鼠标移动到按钮上)：

<p data-height="265" data-theme-id="dark" data-slug-hash="akqqWx" data-default-tab="result" data-user="puronglong" data-embed-version="2" class="codepen">See the Pen <a href="http://codepen.io/puronglong/pen/akqqWx/">js-button-hover-follow-mouse</a> by puronglong (<a href="http://codepen.io/puronglong">@puronglong</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>

通过鼠标左右移动改变背景颜色，挺有意思的，这是怎实现的呢？

通过拆解这组动画会发现，其实原本是像下面这样的：

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420162208.png)

原来这个按钮的前面有一个一样大小的span，鼠标移动到按钮上的时候改变span的right属性，让它往右移动，在按钮的background和文字之间加了一个span，从而形成我们看到的效果。

了解了原理之后我们发现，重点在于获取到鼠标的位置，这个值与span的位置是息息相关的。

首先是骨架html：

```html
<div class="wrap">
    <div class="wrap_go">
        <span style="right: 160px;"></span>
        <a href="javascript:;">加载更多</a>
    </div>
</div>
```

接着是我们的样式css：

```css
.wrap_go{
    width: 160px;
    height: 40px;
    position: relative;
    margin: 1px auto 30px;
    background: #111;
}
.wrap_go a{
    color: #ffffff;
    text-decoration: none;
    width: 160px;
    height: 40px;
    line-height: 40px;
    display: inline-block;
    text-align: center;
    z-index: 1;
    position: relative;
}
.wrap_go span{
    width: 160px;
    height: 40px;
    background: #414141;
    position: absolute;
    z-index: 0
}
```

可以看到现在的效果是这样的：

![img]({{site.url}}images/article/2016-7-18/1.png)

那么后面就是重要的一步，添加行为，我们使用jQuery实现：

首先，获取到wrap_go和span:

```js
var wrap_go = $('.wrap').find('.wrap_go');
var span = wrap_go.find('span').eq(0);
```

在wrap_go上绑定事件，当我们mouseenter的时候，获取到当前的鼠标坐标，这里我们定义一个完成此功能的getMousePos函数，函数最终返回的值应该是鼠标在wrap_go里面的坐标，选取这个坐标的x轴值，用wrap_go的width长度的值减去获取的x轴值，就是span的right属性的值。

jquery里，pageX和pageY用来获取鼠标在整个页面中的坐标，用这个pageX减去wrap_go的偏移就是鼠标在wrap_go当中的位置了。

下面就是定义的getMousePos函数：

```js
function getMousePos(e, n){
    var left = 0, top = 0;
    if (!e){
        var event = window.event;
    }
    if (e.pageX || e.pageY) {
        left = e.pageX;
        top = e.pageY;
        // 获得wrap_go元素当前的偏移，这是固定的
        var a = n.offset();

        // 当前鼠标在wrap_go的div里的坐标为鼠标在页面的坐标-wrap_go坐标
        left -= a.left;
        top -= a.top;
    }

    return{
        left: left,
        top: top
    };
}
```

所以这个时候我们的js文件是这样的：

```js
$(document).ready(function($) {

    bindEvent();

    function bindEvent() {
        var i = this;
        var wrap_go = $('.wrap').find('.wrap_go');
        var span = wrap_go.find('span').eq(0);

        wrap_go.on('mouseenter', function(i){

            // mouseenter的时候获取enter时的坐标，这个$(this)就是wrap_go
            var t = getMousePos(i, $(this));
            console.log(t.left);

            function getMousePos(e, n){
                var left = 0, top = 0;
                if (!e){
                    var event = window.event;
                }
                if (e.pageX || e.pageY) {
                    left = e.pageX;
                    top = e.pageY;
                    // 获得wrap_go元素当前的偏移，这是固定的
                    var a = n.offset();

                    // 当前鼠标在wrap_go的div里的坐标：鼠标坐标-wrap_go坐标
                    left -= a.left;
                    top -= a.top;
                }

                return{
                    left: left,
                    top: top
                };
            }
        });
    }
});
```

这样鼠标移入的时候就能看到效果了，但是还需要在鼠标mousemove的时候也改变它的样式，所以还需要添加一个mousemove事件：

把mousemove时获取的数据处理后赋值给span的css属性

```js
wrap_go.on('mousemove', function(i) {
    // mousemove的时候实时获取坐标
    t = getMousePos(i, $(this));
    span.css({
        right: parseInt($(this).width() - t.left)
    });
});
```

当mouseleave的时候恢复原来的样式：

```js
wrap_go.on('mouseleave', function() {
    // mouseleave的时候恢复样式
    span.animate({
        right: '160px'
    });
});
```

从这里可以看到当鼠标mouseleave的时候，是有一个动画的，因此一进来mouseenter的时候，需要先阻止先前的动画，记得加上span.stop()。

以上，基本的效果就出来啦。

但是测试的时候发现一个问题，当鼠标多次移入移出的时候，该效果就不灵了，没有反应了。通过查看span的right属性分析可以看到，当我们enter的时候，是能获取到当前的一个坐标值的，但是很快这个right属性的值就又变为160px，也就是恢复原值了。照理这个恢复原值的操作应该在mouseleave的时候才发生啊，我这儿还没有leave呢。

知道是

```js
span.animate({
    right: '160px'
});
```

造成的问题以后，可以考虑再加一个span.stop()来阻止掉这个right改为160px的行为，加在哪里呢？加在mousemove的时候。

再来测试一遍，可以啦！

完整js如下：

```js
$(document).ready(function($) {

    bindEvent();

    function bindEvent() {
        var i = this;
        var wrap_go = $('.wrap').find('.wrap_go');
        var span = wrap_go.find('span').eq(0);

        wrap_go.on('mouseenter', function(i){
            span.stop();

            // mouseenter的时候获取enter时的坐标
            var t = getMousePos(i, $(this));
            console.log(t.left);

            wrap_go.on('mousemove', function(i) {
                // mousemove的时候实时获取坐标
                t = getMousePos(i, $(this));
                span.css({
                    right: parseInt($(this).width() - t.left)
                });
                span.stop();
            });

            wrap_go.on('mouseleave', function() {
                // mouseleave的时候恢复样式
                span.animate({
                    right: '160px'
                });
            });

            function getMousePos(e, n){
                var left = 0, top = 0;
                if (!e){
                    var event = window.event;
                }
                if (e.pageX || e.pageY) {
                    left = e.pageX;
                    top = e.pageY;
                    // 获得wrap_go元素当前的偏移，这是固定的
                    var a = n.offset();

                    // 当前鼠标在wrap_go的div里的坐标：鼠标坐标-wrap_go坐标
                    left -= a.left;
                    top -= a.top;
                }

                return{
                    left: left,
                    top: top
                };
            }
        });
    }
});
```