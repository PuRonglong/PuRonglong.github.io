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
	
	for i in range(1, 5): print i
	else:
	print 'The for loop is over'

我们所做的只是提供两个数,range返回一个序列的数。这个序列从第一个数开始到第二个数为止。例如,range(1,5)给出序列[1,2,3,4]。默认地,range的步长为1。如果我们为range提供第三个数,那么它将成为步长。例如,range(1,5,2)给出[1,3]。记住,range向上 延伸到第二个数,即它不包含第二个数。

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

	shoplist = ['apple', 'mango', 'carrot', 'banana']

	shoplist.append()，shoplist.sort()，del shoplist[0]

使用元组：

	zoo = ('wolf', 'elephant', 'penguin')

	len(zoo)，zoo[2]

含有0个或1个项目的元组。一个空的元组由一对空的圆括号组成,如myempty=()。然而,含有单个元素的元组就不那么简单了。你必须在第一个(唯一一个)项目后跟一个逗号,这样Python才能区分元组和表达式中一个带圆括号的对象。即如果你想要的是一个包含项目2的元组的时候,你应该指明singleton=(2 , )。

使用元组输出：

	age = 22
	name = 'Swaroop'
	print '%s is %d years old' % (name, age)
	print 'Why is %s playing with that python?' % name

定制可以是%s表示字符串或%d表示整数。元组必须按照相同的顺序来对应这些定制。

使用字典：

	ab = { 'Swaroop' : 'swaroopch@byteofpython.info',
	'Larry' : 'larry@wall.org',
	'Matsumoto' : 'matz@ruby-lang.org',
	'Spammer' : 'spammer@hotmail.com'
	}
	print "Swaroop's address is %s" % ab['Swaroop']

	ab['Guido'] = 'guido@python.org'
	del ab['Spammer']

	for name, address in ab.items():
	print 'Contact %s at %s' % (name, address)

使用序列：

	shoplist = ['apple', 'mango', 'carrot', 'banana']

Python从0开始计数。

索引同样可以是负数,在那样的情况下,位置是从序列尾开始计算的。因此,shoplist[-1]表示序列的最后一个元素而shoplist[-2]抓取序列的倒数第二个项目。

切片操作符中的第一个数(冒号之前)表示切片开始的位置,第二个数(冒号之后)表示切片到哪里结束。如果不指定第一个数,Python就从序列首开始。如果没有指定第二个数,则Python会停止在序列尾。注意,返回的序列从开始位置开始,刚好在结束位置之前结束。即开始位置是包含在序列切片中的,而结束位置被排斥在切片外。

你可以用负数做切片。负数用在从序列尾开始计算的位置。例如,shoplist[:-1]会返回除了最后一个项目外包含所有项目的序列切片。

对象与参考：

如果你想要复制一个列表或者类似的序列或者其他复杂的对象(不是如整数那样的简单对象),那么你必须使用切片操作符来取得拷贝。

备份脚本——版本一：

	time.strftime()

	zip

备份脚本——版本二：

改变的部分主要是使用os.exists函数检验在主备份目录中是否有以当前日期作为名称的目录。如果没有,我们使用os.mkdir 函数创建。

备份脚本——版本三(不工作!)：

记住我们可以使用物理行尾的反斜杠来表示逻辑行在下一物理行继续。所以,我们修正了程序。这被称为修订。

备份脚本——版本四：

这个程序现在工作了!让我们看一下版本三中作出的实质性改进。我们使用raw_input函数得到用户的注释,然后通过len函数找出输入的长度以检验用户是否确实输入了什么东西。如果用户只是按了回车(比如这只是一个惯例备份,没有做什么特别的修改),那么我们就如之前那样继续操作。
然而,如果提供了注释,那么它会被附加到zip归档名,就在.zip扩展名之前。注意我们把注释中的空格替换成 下划线——这是因为处理这样的文件名要容易得多。

创建一个类：

使用class语句后跟类名,创建一个新的类。这下面跟着一个缩进的语句块形成类体。

使用对象的方法：

	class Person:
		def sayHi(self):
			print 'Hello, how are you?'
	p = Person()
	p.sayHi()

这里我们看到了self的用法。注意sayHi方法没有任何参数,但仍然在函数定义时有self。

使用init方法：

	class Person:
		def __init__(self, name):
			self.name = name
		def sayHi(self):
			print 'Hello, my name is', self.name
	p = Person('Swaroop')
	p.sayHi()

最重要的是,我们没有专门调用init方法,只是在创建一个类的新实例的时候,把参数包括在圆括号内跟在类名后面,从而传递给init方法。这是这种方法的重要之处。

使用类与对象的变量：

	class Person:
		population = 0
		
		def __init__(self, name):
			self.name = name
			print '(Initializing %s.)' % self.name
			Person.population += 1

		def __del__(self):
			print '%s say bye.' % self.name

			Person.population -= 1

			if Person.population == 0 :
				print 'del: I am the last one.'
			else:
				print 'There are still %d people.' % Person.population

		def sayHi(self):
			print '%s say Hi.' % self.name

		def howMany(self):
			if Person.population == 1:
				print 'howMany: I am the last one.'
			else:
				print 'We have %d persons here.' % Person.population

	Tom = Person('Tom')
	Tom.sayHi()
	Tom.howMany()

	Bob = Person('Bob')
	Bob.sayHi()
	Bob.howMany()

这是一个很长的例子,但是它有助于说明类与对象的变量的本质。这里,population属于Person类,因此是一个类的变量。name变量属于对象(它使用self赋值)因此是对象的变量。
观察可以发现init方法用一个名字来初始化Person实例。在这个方法中,我们让population增加1,这是因为我们增加了一个人。同样可以发现,self.name的值根据每个对象指定,这表明了它作为对象的变量的本质。

使用继承：

	class SchoolMember:
		'''Represents any school member.'''
		def __init__(self, name, age):
			self.name = name
			self.age = age
			print '(Initialized SchoolMember: %s)' % self.name
		def tell(self):
			'''Tell my details.'''
			print 'Name:"%s" Age:"%s"' % (self.name, self.age),

	class Teacher(SchoolMember):
		'''Represents a teacher.'''
		def __init__(self, name, age, salary):
			SchoolMember.__init__(self, name, age)
			self.salary = salary
			print '(Initialized Teacher: %s)' % self.name
		def tell(self):
			SchoolMember.tell(self)
			print 'Salary: "%d"' % self.salary
	class Student(SchoolMember):
		'''Represents a student.'''
		def __init__(self, name, age, marks):
			SchoolMember.__init__(self, name, age)
			self.marks = marks
			print '(Initialized Student: %s)' % self.name
		def tell(self):
			SchoolMember.tell(self)
			print 'Marks: "%d"' % self.marks

	t = Teacher('Mrs. Shrividya', 40, 30000)
	s = Student('Swaroop', 22, 75)

	print # prints a blank line
	members = [t, s]
	for member in members:
		member.tell() # works for both Teachers and Students

注意,在我们使用SchoolMember类的tell方法的时候,我们把Teacher和Student的实例仅仅作为SchoolMember的实例。

使用文件：

	f = file('poem.txt', 'w') # open for 'w'riting
	f.write(poem) # write text to file
	f.close() # close the file
	f = file('poem.txt')
	# if no mode is specified, 'r'ead mode is assumed by default while True:
	line = f.readline()
	if len(line) == 0: # Zero length indicates EOF
		break
	print line,
	# Notice comma to avoid automatic newline added by Python
	f.close() # close the file

我们通过指明我们希望打开的文件和模式来创建一个file类的实例。模式可以为读模式('r')、写模式('w')或追加模式('a')。

在一个循环中,我们使用readline方法读文件的每一行。这个方法返回包括行末换行符的一个完整行。所以,当一个空的 字符串被返回的时候,即表示文件末已经到达了,于是我们停止循环。

储存与取储存：

	import cPickle as p #import pickle as p
	shoplistfile = 'shoplist.data'
	# the name of the file where we will store the object
	shoplist = ['apple', 'mango', 'carrot']
	# Write to the file
	f = file(shoplistfile, 'w')
	p.dump(shoplist, f) # dump the object to a file
	f.close()

	del shoplist # remove the shoplist
	# Read back from the storage
	f = file(shoplistfile)
	storedlist = p.load(f)
	print storedlist

为了在文件里储存一个对象,首先以写模式打开一个file对象,然后调用储存器模块的dump函数,把对象储存到打开的文件中。这个过程称为储存。

接下来,我们使用pickle模块的load函数的返回来取回对象。这个过程称为取储存 。

处理异常：

	import sys

	try:
		s = raw_input('Enter something --> ')
	except EOFError:
		print '\nWhy did you do an EOF on me?'
		sys.exit() # exit the program
	except:
		print '\nSome error/exception occurred.' # here, we are not exiting the program

	print 'Done'

我们把所有可能引发错误的语句放在try块中,然后在except从句/块中处理所有的错误和异常。except从句可以专门处理单一的错误或异常,或者一组包括在圆括号内的错误/异常。如果没有给出错误或异常的名称,它会处理所有的错误和异常。对于每个try从句,至少都有一个相关联的except从句。

如何引发异常：

这里,我们创建了我们自己的异常类型,其实我们可以使用任何预定义的异常/错误。这个新的异常类型是ShortInputException类。它有两个域——length是给定输入的长度,atleast则是程序期望的最小长度。

使用sys.argv：

在Python程序运行的时候,即不是在交互模式下,在sys.argv列表中总是至少有一个项目。它就是当前运行的程序名称,作为sys.argv[0]，因为Python从0开始计数。其他的命令行参数在这个项目之后。

使用列表综合：

	listone = [2, 3, 4]
	listtwo = [2*i for i in listone if i > 2]
	print listtwo

这里我们为满足条件(if i > 2)的数指定了一个操作(2*i),从而导出一个新的列表。注意原来的列表并没有发生变化。

使用 lambda 形式：

	def make_repeater(n): 
		return lambda s: s*n

	twice = make_repeater(2)

	print twice('word')
	print twice(5)

这里,我们使用了make_repeater函数在运行时创建新的函数对象,并且返回它。lambda语句用来创建函数对象。本质上,lambda需要一个参数,后面仅跟单个表达式作为函数体,而表达式的值被这个新建的函数返回。注意,即便是print语句也不能用在lambda形式中,只能使用表达式。