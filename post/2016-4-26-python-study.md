layout: post
title: 简明python教程
description: "简明python教程"
tags: [代码]
image:
background: triangular.png
comments: true
share: true
---
> 开启python之旅！

使用带提示符的 Python 解释器：

	~ python
	Python 2.7.10 (v2.7.10:15c95b7d81dc, May 23 2015, 09:33:12)
	[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>>

使用源文件：

	$ python helloworld.py
	Hello World

使用变量和字面意义上的常量：

输入：

	i=5
	print i
	i=i+ 1
	print i
	s = '''This is a multi-line string.
	This is the second line.'''
	print s

输出：

	$ python var.py
	5
	6
	This is a multi-line string. This is the second line.

使用表达式：

输入：

	length = 5
	breadth = 2
	area = length * breadth
	print 'Area is', area
	print 'Perimeter is', 2 * (length + breadth)

输出：

	$ python expression.py 
	Area is 10
	Perimeter is 14

使用 if 语句：

必须在逻辑行结尾处有一个冒号。

使用 while 语句：

使用 for 语句：

使用 break 语句：

跳出循环

使用continue语句：

continue语句会忽略块中的剩余的语句

定义函数：

使用def：

	def sayHello():
		print 'Hello World!' # block belonging to the function
	sayHello() # call the function

使用函数形参：

	def printMax(a, b):
		if a > b:
			print a, 'is maximum'
		else:
			print b, 'is maximum'
	printMax(3, 4)

使用局部变量：

x 是函数的局部变量。所以,当我们在函数内改变 x 的值的时候,在主块中定义的 x 不受影响。

使用global语句：

global语句被用来声明x是全局的——因此,当我们在函数内把值赋给x的时候,这个变化也反映在我们在主块中使用x的值的时候。

使用默认参数值：

	def say(message, times = 1):
	print message * times
	say('Hello')
	say('World', 5)

名为say的函数用来打印一个字符串任意所需的次数。如果我们不提供一个值,那么默认地,字符串将只被打印一遍。我们通过给形参times指定默认参数值1来实现这一功能。

在第一次使用say的时候,我们只提供一个字符串,函数只打印一次字符串。在第二次使用say的时候,我们提供了字符串和参数5,表明我们想要说这个字符串消息5遍。

使用字面意义上的语句：

	def maximum(x, y):
		if x > y:
			return x
		else:
			return y
	print maximum(2, 3)

使用DocStrings：

文档字符串的惯例是一个多行字符串,它的首行以大写字母开始,句号结尾。第二行是空行,从第三行开始是详 细的描述。 强烈建议 你在你的函数中使用文档字符串时遵循这个惯例。

使用sys模块：

sys模块包含了与Python解释器和它的环境有关的函数。

sys.argv变量是一个字符串的列表。特别地,sys.argv包含了命令行参数的列表,即使用命令行传递给你的程序的参数。

使用模块的name：

	if __name__ == '__main__':
		print 'This program is being run by itself'
	else:
		print 'I am being imported from another module'

每个Python模块都有它的name,如果它是'main',这说明这个模块被用户单独运行,我们可以进行相应的恰当操作。

如何创建你自己的模块：

	import mymodule
	mymodule.sayhi()
	print 'Version', mymodule.version

from..import：

下面是一个使用from..import语法的版本：

	from mymodule import sayhi, version
	sayhi()
	print 'Version', version

使用dir函数：

返回当前模块的属性列表

使用列表：