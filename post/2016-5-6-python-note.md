layout: post
title: python笔记
description: "python笔记"
tags: [代码]
image:
background: triangular.png
comments: true
share: true
---

> 记录python的一些笔记

URI是统一资源标识符，用于标识某一互联网资源，而URL是统一资源定位符，表示资源的地点（互联网上所处的位置）。所以URL是URI的子集。

	urllib2 - An extensible library for opening URLs using a variety of protocols

除了"http:"，URL同样可以使用"ftp:"，"file:"等等来替代。HTTP是基于请求和应答机制的：客户端提出请求，服务端提供应答。

re.sub()：

sub是substitute的简写，表示替换，作用：

对于输入的一个字符串，利用正则表达式（的强大的字符串处理功能），去实现（相对复杂的）字符串替换处理，然后返回被替换后的字符串。

比如这个字符串：
	
	inputStr = "hello 123 world 456"

想要把数字都替换，则这样使用：

	replacedStr = re.sub("\d+", "222", inputStr)

re.sub替换所有的匹配项，并不只是第一个匹配项

	re.sub('[abc]', 'o', 'caps')   
	'oops' 

re.findall()：

匹配所有符合规律的内容，返回包含结果的列表

re.search()：

匹配并提取第一个符合规律的内容，返回一个正则表达式对象

str.split()：

split()：拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）

编码：把一个Python对象编码转换成Json字符串

	json.dumps()

解码：把Json格式字符串解码转换成Python对象

	json.loads()

urllib模块提供urlretrieve()函数。urlretrieve()方法直接将远程数据下载到本地。

xrange()接受三个参数分别是start,stop和step（其中start和step是可选的，stop是必需的）

抓包利器Fiddler-fidder介绍：

电脑与互联网之间的通信是通过不同的数据包收发来实现的。Fiddler可以从中间对数据进行拦截。拷贝一份数据后再将数据发送给目的端。同类的还有WireShark。
