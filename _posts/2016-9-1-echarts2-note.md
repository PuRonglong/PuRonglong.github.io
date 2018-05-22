---
layout: post
title: echarts2迁移图
description: "echarts2迁移图"
tags: [技术]
image:
  background: triangular.png
comments: true
share: true
---

最近又在使用echarts2.0了（虽然已经出了3），工具这种东西呀，日新月异，变化太快，这里把echart2使用中遇到的一些点总结一下，免得其他同学遇到同样问题又去查文档，查资料了。

<!-- more -->

echarts里面迁移图是比较常用的一个实例了，比如这样：

![img]({{site.url}}images/article/2016-9-1/1.png)

从一个地方迁移到多个其他地方，我们姑且叫做迁出吧。但实际中常常还有另一个场景，叫迁入，也就是多个目标迁入到一个地点。

结果成了这样:

![img]({{site.url}}images/article/2016-9-1/2.png)

每条线的数据量都聚集到一起了，无法看清。这时候应该让数据显示在出发地而不是目的地。

查了文档似乎echarts的迁移图不支持迁入这样的场景，或者说没有适配。

有一个方法来解决这个问题。迁移图表里面有两个配置，markline和markpoint，控制markline的label不显示，让markpoint的数据显示，听起来好像是可以，实际操作的话，发现还有就是有一个effect的配置，它是用来标注图形炫光特效的，如果要让markpoint的数据能显示出来，这个effect的配置就要为false，关掉特效。

附上一个配置如下：

```json
{
        "name": "渝中",
        "type": "map",
        "mapType": "市工商局",
        "data": [],
        "markLine": {
            "smooth": true,
            "effect": {
                "show": true,
                "scaleSize": 1,
                "period": 30,
                "color": "#fff",
                "shadowBlur": 10
            },
            "itemStyle": {
                "normal": {
                    "label":{
                        "show":false
                    },
                    "borderWidth": 1,
                    "lineStyle": {
                        "type": "solid",
                        "shadowBlur": 10
                    }
                }
            },
            "tooltip": {
                "show": true
            },
            "data": []
        },
        "markPoint": {
            "symbol": "emptyCircle",
            "effect": {
                "show": false,
                "shadowBlur": 0
            },
            "symbolSize": 30,
            "itemStyle": {
                "normal": {
                    "label": {
                        "position": "top",
                        "show": true,
                        "textStyle": {
                            "fontSize": 14
                        }
                    }
                },
                "emphasis": {
                    "label": {
                        "show": false,
                        "position": "top",
                        "textStyle": {
                            "fontSize": 30
                        }
                    }
                }
            },
            "data": []
        }
    }
```

