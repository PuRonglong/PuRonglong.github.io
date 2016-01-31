layout: post
title: jQuery中的Ajax学习笔记
description: "主要讲jQuery中的Ajax的一些相关用法"
tags: [读书笔记]
image:
  background: triangular.png
comments: true
share: true
---


>前段时间学习了《锋利的jQuery第六章》jQuery与Ajax应用，现做如下笔记：

<figure>
	<a href="http://img11.360buyimg.com/n0/g6/M04/06/1C/rBEGDFD2UYIIAAAAAAGrx67MlCIAABWBAKB-WkAAavf388.jpg">
		<img src="http://img11.360buyimg.com/n0/g6/M04/06/1C/rBEGDFD2UYIIAAAAAAGrx67MlCIAABWBAKB-WkAAavf388.jpg" alt="cover of the book" />
	</a>
	<figcaption>《锋利的jQuery(第二版)》</figcaption>
</figure>

<!--more-->

## 什么是Ajax呢？

我们先来了解一下，什么是Ajax呢？Ajax全称为`“Asynchronous JavaScript and XML”(异步JavaScript和XML)`，它并不是指一种单一的技术，而是有机地利用了一系列交互式网页应用相关的技术所形成的结合体。简短地说，在不重载整个页面的情况下，Ajax通过后台加载数据，并在网页上进行显示。

我们来简要回顾一下Ajax。早在1998年，微软就引入了一个ActiveX控件，从而能够在脚本控制下执行异步请求。在2005年，`Adaptive Pathde Jesse James Garrett`创造了术语Ajax(Asynchronous JavaScript and XML，异步的JavaScript与XML)

**Ajax请求的生命周期**，是从客户端向服务器端发送请求，然后再从服务器端返回。在向服务器发出请求之前，需要执行如下的设置步骤：

* 指定HTTP方法，比如(POST或者GET)；

* 提供要接触的服务器端资源的URL；

* 告诉XHR实例如何通报进度；

* 为POST请求提供任何主体内容。

## 6.1 Ajax的优势和不足

它的优势有：
1.不需要插件支持：Ajax不需要任何浏览器插件，就可以被绝大多数主流浏览器所支持，用户只需要允许js在浏览器上执行即可。

2.优秀的用户体验：这也是Ajax技术的**最大优点**，能在不刷新整个页面的前提下更新数据，使得Web应用程序能更为迅速地回应用户的操作。

3.提高Web程序的性能：Ajax模式和传统模式相比在性能上的最大区别就在于`传输数据的方式`，在传统模式中，数据提交是通过表单（Form）来实现的，而数据获取是靠全页面刷新来重新获取整页的内容。即Ajax是以异步方式提交数据给一个服务器，而不再采用旧式的“提交——处理——重新加载页面”(post-process-reload)技术，Ajax模式只是通过XMLHttpRequest对象来向服务器端提交希望提交的数据，即按需发送。

4.减轻服务器和带宽的负担：Ajax的工作原理相当于在用户和服务器之间加了一个中间层，使用户操作与服务器响应`异步化`。它在客户端创建Ajax引擎，把传统方式下的一些服务器负担的工作转移到客户端，便于客户端资源来处理，减轻服务器和带宽的负担。

Ajax主要有以下几点**不足之处**：

1.浏览器对XMLHttpRequest对象的支持度不足。Ajax的不足之一首先来自于浏览器。

2.破坏浏览器前进，“后退”按钮的正常功能。在Ajax中“前进”和“后退”按钮的功能都会失效，虽然可以通过一定的方法（添加锚点）来使得用户可以使用“前进”和“后退”按钮，但相对于传统的方式却麻烦了很多。

3.对搜索引擎的支持不足

4.开发和调试工具的缺乏

5、另外，像其他方面的一些问题，比如说违背了url和资源定位的初衷。例如，我给你一个url地址，如果采用了ajax技术，也许你在该url地址下面看到的和我在这个url地址下看到的内容是不同的。这个和资源定位的初衷是相背离的。

## 6.2Ajax的XMLHttpRequest对象

Ajax的核心是XMLHttpRequest对象，它是Ajax实现的关键——发送异步请求，接收相应及执行回调都是通过它来完成的。

## 6.3安装Web环境——AppServ

文中安装的是AppServ，我自己电脑上用的是nginx

## 6.4编写第一个Ajax例子

主要讲解了一个用传统JavaScript实现的Ajax例子。

## 6.5jQuery中的Ajax

jQuery中，jQuery对Ajax操作进行了**封装**，提供了多个与AJAX有关的方法。通过这些方法，能够使用HTTP Get和HTTP Post从远程服务器上请求文本，HTML,XML或JSON-同时我们能把这些外部数据直接载入网页的被选元素中。

在jQuery中$.ajax()方法属于最底层的方法，第2层是load(),$.get()和$.post()方法，第三层是$.getScript()和$.getJSON()方法。

### 6.5.1
**jQuery $.load() 方法**

结构：load(url[,data][,callback])

<figure>
	<a href="/images/article/2014-12/load.png">
		<img src="/images/article/2014-12/load.png" alt="load" />
	</a>
	<figcaption>load()方法参数解释</figcaption>
</figure>

下面是一个load()方法的例子的jQuery代码：

{% highlight JavaScript %}
$(function(){
				$("#btn1").click(function(){
					$("#test").load("here.html");
				})
			})
{% endhighlight %}		

**注意**：load()方法中，无论Ajax请求是否成功，只要当请求完成(complete)后，回调函数(callback)就被触发。

**jQuery $.get() 方法**

$.get() 方法通过 HTTP GET 方法来进行异步请求

结构：$.get(url[,data][,callback][,type])

<figure>
	<a href="/images/article/2014-12/get.png">
		<img src="/images/article/2014-12/get.png" alt="get" />
	</a>
	<figcaption>load()方法参数解释</figcaption>
</figure>

下面的例子使用$.get()方法从服务器上的一个文件中取回数据：

{% highlight JavaScript %}
$(function(){
					$.get('test.txt', function(data,status) {
						alert("数据："+data+"\n状态："+status);
					}); //$.get() 的第一个参数是我们希望请求的 URL。
						// 第二个参数是回调函数。第一个回调参数存有被请求页面的内容，第二个回调参数存有请求的状态。
						//而且回调函数只有在数据成功返回(success)后才被调用，这点与load()方法不一样。
				})
{% endhighlight %}

### $.post()方法

它与$.get()方法的结构和使用方式都相同，不过它们之间仍然有以下区别：

<figure>
	<a href="/images/article/2014-12/post-vs-get.png">
		<img src="/images/article/2014-12/post-vs-get.png" alt="get" />
	</a>
	<figcaption>load()方法参数解释</figcaption>
</figure>

### jQuery $.post() 方法

$.post() 方法通过 HTTP POST 请求从服务器上请求数据

语法：

$.post(URL,data,callback);

由于POST和GET方式提交的所有数据都可以通过$_REQUEST[]来获取，因此只需要改变jQuery函数，就可以将程序在GET请求和POST请求之间切换。

另外，当load()方法带有参数传递时，会使用POST方式发送请求。因此也可以使用load()方法来完成同样的功能。

但在此期间报错了，后来找到原因：Apache、IIS、Nginx等绝大多数web服务器，都不允许静态文件响应POST请求，网上找到的资料：[http://blog.csdn.net/haitun312366/article/details/8241350](http://blog.csdn.net/haitun312366/article/details/8241350)，貌似需要修改nginx的相关配置。

## 6.5.3$.getScript()方法和$.getJson()方法

### 1.$.getScript()方法

有时候，在页面初次加载时就取得所需的全部JavaScript文件是完全没有必要的。虽然可以再需要哪个JavaScript文件时，动态地创建`<script>`标签，如：

{% highlight JavaScript %}
$(document.createElement("script")).attr("src","test.js").appendTo("head");
{% endhighlight %}

或者：

{% highlight JavaScript %}
$("<script type='text/javascript' src='test.js'/>").appendTo("head">;
{% endhighlight %}

但这种方式并不理想。为此，jQuery提供了`$.getSctipt()`方法来直接加载.js文件，与加载一个HTML片段一样简单方便，并且不需要对JavaScript文件进行处理，JavaScript文件会自动执行。jQuery代码如下：

{% highlight JavaScript %}
$(function(){
				$("#send").click(function(){
					$.getScript('test.js');
				})
			})
{% endhighlight %}

这个方法也有回调函数

### 2.$.getJSON() 方法

$.getJSON()方法用于加载JSON文件，与$.getScript()方法的用法相同:

{% highlight JavaScript %}
$(function(){
				$('#send').click(function(event) {
					$.getJSON('test.json',function(data){
						//data:返回的数据
					})
				});
			})
{% endhighlight %}

### 6.5.4 $.ajax()方法
$.ajax()方法是最底层的Ajax实现

结构为:$.ajax(options)

该方法只有一个参数，但在这个对象里包含了$.ajax()方法所需要的请求设置以及回调函数等信息，参数以key/value的形式存在，所有参数都是可选的.

前面用到的$.load(),$.get(),$.post().$.getScript和$.getJSON()这些方法，都是基于$.ajax()方法构建的，$.ajax()方法是jQuery最底层的Ajax实现，因此可以用它来代替前面的所有方法。

下面是一个简单的Ajax请求的例子：

{% highlight JavaScript %}
$(function(){
				$.ajax({
					url:"here.html",
					dataType:"html",
					success:function(r){
						console.log("make it");
					},
					error : function(r){
						console.log("something didn't work");
					}
				})
			})
{% endhighlight %}

如果想使某个Ajax请求不受全局方法的影响，那么可以在使用$.ajax(options)方法时，将参数中的global设置为false

设置请求默认值

当我们计划发起大量请求时，如果能为页面上的这些选项设置默认值会很方便。jQuery就为我们提供了一种方式来定义一组默认的AJAX属性值，如果没有覆盖这些属性的值，则会使用这些默认值。如果要发起很多相似的Ajax请求，这可以简化页面。

$.ajaxSetup(options)

把传去的一组选项属性创建为随后调用$.ajax()的默认值。参数options:（对象)对象实例，其属性定义了一组默认的Ajax选项。

注意：通过这个函数设置的默认值不会应用到load()方法。对于诸如$.get()和$.post的实用函数，这些默认值也不会覆盖HTTP方法。例如，设置默认type为GET不会导致$.post()使用HTTP的GET方法。

假设要创建一个保安大多数Ajax请求的页面(使用实用函数来创建，而不是load()方法)，我们希望设置一些默认值，以免每次调用时都指定它们。我们可以在页面头部的<script>元素的第一行编写这样的代码

{% highlight JavaScript %}
$.ajaxSetup({
				type:'POST',
				timeout:5000,
				dataType:'html'
			});
{% endhighlight %}

这将会确保随后的每个Ajax调用(除了前面提到的load()方法)都会使用这些默认值。除非使用传入Ajax使用函数的属性来显示地覆盖它们

## 6.7 jQuery中的Ajax全局事件

下面来看一下jQuery中的Ajax全局事件。jQuery简化Ajax操作不仅体现在调用Ajax方法和处理响应方面，而且还体现在对调用Ajax方法的过程中的HTTP请求的控制。通过jQuery提供的一些自定义全局函数，能够为各种与Ajax相关的事件注册回调函数。例如当Ajax请求开始时，会触发ajaxStart()方法的回调函数；当Ajax请求结束时，会触发ajaxStop()方法的回调函数。这些方法都是全局的方法，因此无论创建它们的代码位于何处，只要有Ajax()请求发生，就会触发它们。

{% highlight JavaScript %}
$(function(){
				$("#loading").ajaxStart(function(){
					$(this).show();
				});
				$("#loading").ajaxStop(function(){
					$(this).hide();
				});
				$.get('test.txt', function(data,status) {
						alert("数据："+data+"\n状态："+status);
						// console.log(123);
					}); 
				})
{% endhighlight %}

除了ajaxStart()和ajaxStop()，还有另外几个方法：

<figure>
	<a href="/images/article/2014-12/ajax-all-event.png">
		<img src="/images/article/2014-12/ajax-all-event.png" alt="get" />
	</a>
	<figcaption>load()方法参数解释</figcaption>
</figure>

期间关于ajaxSend()遇到些问题，记录下来：

{% highlight JavaScript %}
$(document).ready(function(){
                $("#div1").ajaxSend(function(){
                alert(123);
              });
                  $("button").click(function(){
                    $("#div1").load("here.html");
              });
            });//上面定义$("#div1").ajaxSend(function(){});事件不在任何一下onClick事件中。
			//如果发生了全局事件的重复定义，在本例中也就是每一个onClick事件中都定义一次全局事件$("#div1").ajaxSend(function(){});的话，那么，该全局事件会增加执行次数，而不是覆盖前面的定义
{% endhighlight %}

是在这里找到的相关资料：[http://zhina123.blog.163.com/blog/static/41789578201211931319529/](http://zhina123.blog.163.com/blog/static/41789578201211931319529/)

jquery中各个事件执行顺序如下：

* 1.ajaxStart(全局事件)

* 2.beforeSend

* 3.ajaxSend(全局事件)

* 4.success

* 5.ajaxSuccess(全局事件)

* 6.error

* 7.ajaxError (全局事件)

* 8.complete

* 9.ajaxComplete(全局事件)

* 10.ajaxStop(全局事件)


## 序列化问题 
项目过程中，经常会有传输数据的时候，在传输数据的过程中，发送方需要把这个对象转换为字节序列，才能在网络上传送；接收方则需要把字节序列再恢复为对象。 而序列化 (Serialization)就是将对象的状态信息转换为可以存储或传输的形式的过程

jQuery中提供了serialize()方法，作用于一个jQuery对象，将DOM元素内容序列化为字符串，用于Ajax请求。

格式：var data = $("form").serialize();

功能：将表单内容序列化成一个字符串。

这样在ajax提交表单数据时，就不用一一列举出每一个参数。只需将data参数设置为 $("form").serialize() 即可。

{% highlight JavaScript %}
$(document).ready(function(){
            $("button").click(function(){
                $("div").text($("form").serialize());
              });
            });
{% endhighlight %}

因为serialize()方法作用于jQuery对象，所以不光只有表单能使用它，其他选择器选取的元素也都能使用它，如：

{% highlight JavaScript %}
$(“:checkbox,:radio”).serialize();
{% endhighlight %}

### serializeArray()方法

　　格式：var jsonData = $("form").serializeArray();

　　功能：将页面表单序列化成一个JSON结构的对象。注意该方法不是返回字符串，而是将DOM元素序列化后，返回JSON格式的数据。也因为是一个对象，所以可以使用$.each()函数对数据进行迭代输出。

　　比如，[{"name":"lihui", "age":"20"},{...}] 获取数据为 jsonData[0].name

{% highlight JavaScript %}
$(function(){
       $("#send").click(function(){
            var $data =  $(":checkbox,:radio").serializeArray();
            alert( $data );
       })
    })
{% endhighlight %}

### $.param()方法

它是serialize()方法的核心，用来对一个数组或对象按照key/value进行序列化

{% highlight JavaScript %}
$(function(){
				var obj = {a:1,b:2,c:3};
				var k = $.param(obj);
				alert(k);
			})//输出a=1&b=2&c=3
{% endhighlight %}

## 避免缓冲
对于AJAX请求，GET请求中的数据缓冲存在根本性的问题。遗憾的是，即使有必要，服务器也很少在AJAX请求中重新请求数据。浏览器简单地从本地缓存汇中读取数据`（要知道，浏览器在历史上就从不是为异步数据请求设计的）`。这个问题首先影响到Internet Explorer。在手工编程中，在查询字符串后附加由JavaScript生成的随机数或者时间戳(不管在服务器还是在客户端，这个数值基本上都没有进一步的用途)是一个好的变通方法。这种方法知识为了告诉浏览器必须重新加载数据。事实上，这种技巧是目前避免缓冲行为(在传统的Web数据请求中确实很有用的一种行为)的**唯一简单而可靠的方法**。明确提供这类机制的框架(例如YUI)在后台所做的也就是这些。在jQuery中，目前必须为大部分方法手工创建一个额外的参数，并将这个参数附加到URL中。只有ajax()方法通过特殊参数提供了对应的避免缓冲选项。

## $.ajax()的扩展技术
在jQuery1.5中，引入了$.ajax()的3个扩展功能：

### 前置过滤器：
前置过滤器(prefilter)指的是任何AJAX请求被发送之前和$.ajax()处理任何选项之前执行的回调函数

{% highlight JavaScript %}
$.ajaxPrefilter(
				function(requestOptions,originalOptions,jqXHR){
					//Modify options,control the original options,store jqXHR object etc
				});
{% endhighlight %}

### 转换器：
转换器指的也是新型的回调函数。转换器在服务器以预期之外的数据类型发送响应数据时调用。可以在回调函数中采取相应的措施，转换数据类型或者引入自己的数据类型。转换器保存在ajaxSetting中，可以全局添加。

{% highlight JavaScript %}
({
				converters:{
					"text mydatatype":function(textValue){
						if (valid(textValue)) {
							if (valid(textValue)) {
								//some logic
								return mydatatypeValue;
							}
							else{
								//indicate parse-error
								throw exceptionObject;
							}
						};
					}
				}
			})
{% endhighlight %}

可以用转换器创建自定义数据类型(数据类型必须采用小写字母)。    如果观察前一个程序清单中的典型转换器，就可以请求类型为mydatatype的数据，如:

{% highlight JavaScript %}
$.ajax(url,{
				dataType:"mydatatype"
			});
{% endhighlight %}

### 分发器：
jQuery中的分发器(transport)是提供一下两个方法的一个对象：send()abort()上述两个方法都由$.ajax()在内部使用，可以用于扩展$.ajax()。但是，jQuery文档还指出，分发器应该只作为最后手段，在前置过滤器和转换器都不足以影响AJAX请求时使用。因为每个请求需要自己的分发器对象实例，这些对象不能被直接注册。作为替代，应该提供一个函数来返回这样的对象。这种生成对象的函数被称为工厂(Factory)。分发器工厂的注册如下：

{% highlight JavaScript %}
$.ajaxTransport(function(requestOptions,originalOptions,jqXHR){
				if (/*conditions for transport*/) {
					return {
						send:function(header fields as map,callback){
							/*code for sending*/
						},
						abort:function(){
							/*code in case of abort*/
						}
					}
				};
			})
{% endhighlight %}

本次笔记以《锋利的jQuery》(第二版)为主，参考资料有《jQuery实战》(第二版),《jQuery应用开发实践指南》。有任何建议，还望大家不吝赐教[抱拳]


**文章来自 [https://github.com/PuRonglong/PuRonglong.github.io]({https://github.com/PuRonglong/PuRonglong.github.io})**