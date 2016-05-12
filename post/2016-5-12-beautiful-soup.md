layout: post
title: eautiful Soup笔记
description: "some note"
tags: [代码]
image:
background: triangular.png
comments: true
share: true
---

> python中的Beautiful Soup

我们前面提到过一个xpath，今天要讲的Beautiful Soup作用类似，它是一个可以从HTML或XML文件中提取数据的Python库。

下面的一段HTML代码将作为例子被多次用到.这是爱丽丝梦游仙境的的一段内容(以后内容中简称为爱丽丝的文档):

	html_doc = """
	<html><head><title>The Dormouse's story</title></head>
	<body>
	<p class="title"><b>The Dormouse's story</b></p>

	<p class="story">Once upon a time there were three little sisters; and their names were
	<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
	<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
	<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
	and they lived at the bottom of a well.</p>

	<p class="story">...</p>
	"""

我们要想使用BeautifulSoup解析这段代码，首先要得到一个BeautifulSoup的对象，然后对这个对象进行BeautifulSoup的相关操作。

	from bs4 import BeautifulSoup
	soup = BeautifulSoup(html_doc)

首先是引入BeautifulSoup，当然在这之前我们要先进行安装：

	pip install beautifulsoup4

然后实例化一个BeautifulSoup对象，打印出这个对象我们可以看到是这样的：

	print(soup.prettify())
	# <html>
	#  <head>
	#   <title>
	#    The Dormouse's story
	#   </title>
	#  </head>
	#  <body>
	#   <p class="title">
	#    <b>
	#     The Dormouse's story
	#    </b>
	#   </p>
	#   <p class="story">
	#    Once upon a time there were three little sisters; and their names were
	#    <a class="sister" href="http://example.com/elsie" id="link1">
	#     Elsie
	#    </a>
	#    ,
	#    <a class="sister" href="http://example.com/lacie" id="link2">
	#     Lacie
	#    </a>
	#    and
	#    <a class="sister" href="http://example.com/tillie" id="link2">
	#     Tillie
	#    </a>
	#    ; and they lived at the bottom of a well.
	#   </p>
	#   <p class="story">
	#    ...
	#   </p>
	#  </body>
	# </html>

获取到BeautifulSoup对象后，那么有哪些方法可以操作呢？

（1）获取标签内容：

我们可以利用soup加标签名轻松地获取这些标签的内容，如下：

	soup.title
	# <title>The Dormouse's story</title>

	soup.title.name
	# u'title'

	soup.title.string
	# u'The Dormouse's story'

	soup.title.parent.name
	# u'head'

	soup.p
	# <p class="title"><b>The Dormouse's story</b></p>

	soup.p['class']
	# u'title'

	soup.a
	# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

	soup.find_all('a')
	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
	#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
	#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

	soup.find(id="link3")
	# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

对于标签，它有两个重要的属性，分别是name和attrs，前者是标签名，后者是属性：

	print soup.p.attrs
	#{'class': ['title'], 'name': 'dromouse'}

获取属性：

	css_soup = BeautifulSoup('<p class="body strikeout"></p>')
	css_soup.p['class']
	# ["body", "strikeout"]

	css_soup = BeautifulSoup('<p class="body"></p>')
	css_soup.p['class']
	# ["body"]

还可以对这些属性和内容等等进行修改：

	soup.p['class']="newClass"
	print soup.p
	#<p class="newClass" name="dromouse"><b>The Dormouse's story</b></p>

tag的属性操作方法与字典一样。

（2）获取到标签内容后，想要获取标签里面的文本该怎么办呢？

	print soup.p.string
	#The Dormouse's story

现在来了解一下搜索方法的细节:

	find_all( name , attrs , recursive , text , **kwargs )

find_all()方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件。这里有几个例子:

	soup.find_all("title")
	# [<title>The Dormouse's story</title>]

	soup.find_all("p", "title")
	# [<p class="title"><b>The Dormouse's story</b></p>]

	soup.find_all("a")
	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
	#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
	#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

	soup.find_all(id="link2")
	# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

	import re
	soup.find(text=re.compile("sisters"))
	# u'Once upon a time there were three little sisters; and their names were\n'

find():

```find_all()```方法将返回文档中符合条件的所有tag,尽管有时候我们只想得到一个结果.比如文档中只有一个<body>标签,那么使用 ```find_all()```方法来查找<body>标签就不太合适,使用find_all方法并设置limit=1参数不如直接使用find()方法.下面两行代码是等价的:

	soup.find_all('title', limit=1)
	# [<title>The Dormouse's story</title>]

	soup.find('title')
	# <title>The Dormouse's story</title>

唯一的区别是find_all()方法的返回结果是值包含一个元素的列表,而find()方法直接返回结果。

soup.head.title是tag的名字方法的简写.这个简写的原理就是多次调用当前tag的find()方法:

	soup.head.title
	# <title>The Dormouse's story</title>

	soup.find("head").find("title")
	# <title>The Dormouse's story</title>

按CSS搜索。

按照CSS类名搜索tag的功能非常实用,但标识CSS类名的关键字class在Python中是保留字,使用class做参数会导致语法错误.从BeautifulSoup的4.1.1版本开始,可以通过class_参数搜索有指定CSS类名的tag。

	soup.find_all("a", class_="sister")
	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
	#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
	#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

get_text():

如果只想得到tag中包含的文本内容,那么可以嗲用get_text()方法,这个方法获取到tag中包含的所有文版内容包括子孙tag中的内容,并将结果作为Unicode字符串返回:

	markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
	soup = BeautifulSoup(markup)

	soup.get_text()
	u'\nI linked to example.com\n'
	soup.i.get_text()
	u'example.com'

可以通过参数指定tag的文本内容的分隔符:

	# soup.get_text("|")
	u'\nI linked to |example.com|\n'

还可以去除获得文本内容的前后空白:

	# soup.get_text("|", strip=True)
	u'I linked to|example.com'

编码：

还可以调用 BeautifulSoup 对象或任意节点的 encode() 方法,就像Python的字符串调用 encode() 方法一样:

	soup.p.encode("latin-1")
	# '<p>Sacr\xe9 bleu!</p>'

	soup.p.encode("utf-8")
	# '<p>Sacr\xc3\xa9 bleu!</p>'

CSS选择器：

Beautiful Soup支持大部分的CSS选择器,在Tag或BeautifulSoup对象的.select()方法中传入字符串参数,即可使用CSS选择器的语法找到tag:

	soup.select("title")
	# [<title>The Dormouse's story</title>]

	soup.select("p nth-of-type(3)")
	# [<p class="story">...</p>]

通过tag标签逐层查找:

	soup.select("body a")
	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
	#  <a class="sister" href="http://example.com/lacie"  id="link2">Lacie</a>,
	#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

	soup.select("html head title")
	# [<title>The Dormouse's story</title>]

找到某个tag标签下的直接子标签:

	soup.select("head > title")
	# [<title>The Dormouse's story</title>]

	soup.select("p > a")
	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
	#  <a class="sister" href="http://example.com/lacie"  id="link2">Lacie</a>,
	#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

	soup.select("p > a:nth-of-type(2)")
	# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

	soup.select("p > #link1")
	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

	soup.select("body > a")
	# []

找到兄弟节点标签:

	soup.select("#link1 ~ .sister")
	# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
	#  <a class="sister" href="http://example.com/tillie"  id="link3">Tillie</a>]

	soup.select("#link1 + .sister")
	# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

通过CSS的类名查找:

	soup.select(".sister")
	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
	#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
	#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

	soup.select("[class~=sister]")
	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
	#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
	#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

通过tag的id查找:

	soup.select("#link1")
	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

	soup.select("a#link2")
	# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

通过是否存在某个属性来查找:

	soup.select('a[href]')
	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
	#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
	#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

通过属性的值来查找:

	soup.select('a[href="http://example.com/elsie"]')
	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

	soup.select('a[href^="http://example.com/"]')
	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
	#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
	#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

	soup.select('a[href$="tillie"]')
	# [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

	soup.select('a[href*=".com/el"]')
	# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

更多信息参考文档：

[Beautiful Soup文档](http://beautifulsoup.readthedocs.io/zh_CN/latest/#)