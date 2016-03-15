layout: post
title: 数据统计系统
description: "总结数据统计系统开发"
tags: [技术]
image:
  background: triangular.png
comments: true
share: true
---

>和凯明大大一起做完一个数据统计系统，总结一下~

最开始的时候，模板里用的是jquery.flot.js这样一个jquery的图表插件：

![img](./images/article/2016-3-15/1.png)

但是在使用的过程中常常发现一些问题，比如一般会出现这样的图表展示：

![img](./images/article/2016-3-15/2.png)

一般来说，图表展示横纵坐标都会有标签名的，用于告诉用户这个坐标是干什么用的，可是在jquery.flot里没有发现这一项配置，照理来说这样的功能应该是图表都应该有的吧，查找了一遍发现居然没有这项配置，无奈只得找找有没有解决办法了，google出来一个这个[flot-axislabels](https://github.com/markrcote/flot-axislabels)。

这是一个```Axis Labels Plugin for Flot```，

还有当底部X横坐标刻度上的介绍比较长的时候，这时就不能横向展示了，否则会太拥挤，我们可以考虑将其竖着显示出来，可是呢，考虑到竖着的显示效果有点别扭，还是斜着放置比较合适，可是jquery.flot在这方面的处理又不太好，自定义程度不够。

就在找解决办法的时候，发现了别人在使用```eCharts```这个百度开源的一项图表展示工具。了解了一下发现一方面自定义程度高，一方面图表的动画效果不错，并且界面整洁，体验大大提高，于是决定采用这个图表库了。

![img](./images/article/2016-3-15/3.png)

下一步的问题就是如何把eCharts集成到项目中去。项目是使用的angular框架，那么问题就是如何在angular项目的适当位置使用我们的echarts呢？大概的想法应该是从angular的directive入手，以属性的方式自定义一个指令，在需要使用echarts的地方调用这个指令。

首先在项目中引入echarts文件：

	js/libs/echarts-all.js

创建并引入一个ui-echarts文件：

	js/angualr/ui-echarts.js

上面这个文件就是我们需要写的指令所在处。

我们的HTML文件是这样的：

	<div class = "col-xs-12">
		<div e-chart ui-option = "{

		}"</div>
	</div>

这个e-chart指令就是我们要调用的指令，ui-option里面是我们的echarts配置，多次调试后配了一个好看点的：

	{
        color: ['#23B7E5'],//系列颜色
        title:{//图表标题
            text:'视频投票数',
            subtext:'数据来自——美甲大咖',
            x : 'center',
        },
        tooltip: {//提示框
            show: true,
            trigger: 'axis',//触发类型,默认是数据触发
            enterable: true,//鼠标是否可进入气泡
        },
        toolbox:{//右上角工具栏
            show : true,
            feature : {
                mark : {show: true},
                dataView : {show: true, readOnly: true},
                magicType : {show: true, type: ['line', 'bar']},
                restore : {show: true},
                saveAsImage : {show: true}
            }
        },
        dataZoom:{//底部拖拽栏
            show:true,
            realtime:true,//缩放变化实时显示
            start: 10,//拖动条起始百分比位置
            end: 90,
            handleColor:'#008acd',
            dataBackgroundColor:'#efefff',
        },
        legend: {//图例
            data:['投票数'],
            x : 'left',
        },
        grid: {//控制图表边线与绘制的canvans边界距离
            y: 80,
            y2: 160,
            },
        xAxis : [
            {
                name : '视频期数',
                type : 'category',
                data : vote_result_x,
                nameTextStyle : {fontSize:15},
            }
        ],
        yAxis : [
            {
                name : '投票数',
                type : 'value',
                nameTextStyle : {fontSize:15},
            }
        ],
        series : [//数据图表
            {
                name:'投票数',
                type:'line',
                data:vote_result_Y,//Y轴数据
                itemStyle:{
                    normal: {
                        lineStyle: {
                            width: 2,
                            color: '#23B7E5',
                            shadowColor : 'rgba(0,0,0,0.5)',
                            shadowBlur: 10,
                            shadowOffsetX: 8,
                            shadowOffsetY: 8,
                        },
                        barBorderRadius: 4,
                        label: {show: true},
                        areaStyle: {type: 'default'},//是否显示区域面积
                    },
                    emphasis:{
                        label: {show: true},
                    },
                },
                markPoint:{//图表最大最小点
                    data:[
                        {type:'max',name:'最大值'},
                        {type:'min',name:'最小值'},
                    ],
                },
                markLine:{//图表平均线
                    data:[
                        {type:'average',name:'平均值'}
                    ],
                },
            },
        ],
    };

我们引入了echarts文件，而在ui-echarts文件中要写的代码作用就是表明这里要调用echarts了。

指令的名字按照angular的规则来：

	angular.modul('ui.echarts', []).directive('eChart', [function(){
		return {
			restrict: 'A',
			link: link
		};
	}]);

restrict: 'A'告诉angular这个指令在DOM中以属性的形式被声明。

link：用来创建可以操作DOM的指令，这里是我们定义的一个link的函数。

完整是这样：

	angular.module('ui.echarts', []).directive('eChart', [function () {

	    function link($scope, element, attrs) {

	        // 基于准备好的dom，初始化echarts图表
	        var myChart = echarts.init(element[0]);//实例化一个eCharts对象

	        //监听options变化
	        if (attrs.uiOptions) {
	            attrs.$observe('uiOptions', function () {//监控uiOptions属性
	                var options = $scope.$eval(attrs.uiOptions);//执行当前作用域下的表达式
	                if (angular.isObject(options)) {
	                    myChart.setOption(options, true);
	                }
	            }, true);
	        }
	    }

	    return {
	        restrict: 'A',
	        link: link
	    };
	}]);

一步一步说明一下：

	var myChart = echarts.init(element[0]);

这是echarts文档给出的图表实例化方法，在这里我们实例化了这么一个echarts对象，但是在我们的表格中，我们提供了功能按钮用于不同类型的数据的选择，就是说我们的数据是会改变的，所以一开始获取到数据以后展现出图表，但是在数据变化的时候我们需要图表跟着变化，而我们的数据就是我们HTML文件里ui-option="{}"下X和Y轴的数据：

	xAxis : [
        {
            name : '最近视频期数',
            type : 'category',
            data : {{photo_result_x}},
            nameTextStyle : {fontSize:15},
        }
    ],
    yAxis : [
        {
            name : '上传图片数',
            type : 'value',
            nameTextStyle : {fontSize:15},
        }
    ],
    series : [
        {
            name:'上传图片数',
            smooth: true,
            type:'line',
            data:{{photo_result_y}}
        }

XAxis里的data就是x轴的数据，这里要注意的而是Y轴的数据并不是在yAxis里面定义，而是在series下的data里，这是容易犯错的一个地方。

我们知道是```ui-option```里的这些数据在变化了，那么我们就要监听```ui-option```的变化。

	function link($scope, element, attrs) {

        // 基于准备好的dom，初始化echarts图表
        var myChart = echarts.init(element[0]);//实例化一个eCharts对象

        //监听options变化
        if (attrs.uiOptions) {
            attrs.$observe('uiOptions', function () {//监控uiOptions属性
                var options = $scope.$eval(attrs.uiOptions);//执行当前作用域下的表达式
                if (angular.isObject(options)) {
                    myChart.setOption(options, true);
                }
            }, true);
        }
    }

上面attrs参数代表实例属性，是一个由定义在元素上的属性组成的标准化列表，

	if (attrs.uiOptions)//如果我们定义的ui-option这个属性存在的话，执行下步

```$observe```是属性对象上的方法，它是用来监控DOM属性上的值的变化，它仅用在指令内部，当你需要在指令内部监控包含有插值表达式的DOM属性的时候，就要用到这个方法。

```$eval``` 即```scope.$eval```，是执行当前作用域下的表达式，如：```scope.$eval('a+b'); ```而这个里的```a,b```是来自 ```scope = {a: 2, b:3};```

```angular.isObject```判断给定的对象是否为object类型。

以上，就能生成我们的echarts图表了，并能实时监控图表变化。

![img](./images/article/2016-3-15/4.png)
![img](./images/article/2016-3-15/5.png)
![img](./images/article/2016-3-15/6.png)
![img](./images/article/2016-3-15/7.png)
![img](./images/article/2016-3-15/8.png)