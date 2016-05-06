layout: post
title: 安装scrapy遇到的一些问题
description: "some note"
tags: [代码]
image:
background: triangular.png
comments: true
share: true
---

在安装scrapy的过程中遇到了一些问题记录一下。

![img](./images/article/2016-5-3/1.png)

进入命令行，执行：

	pip install scrapy

但是执行到最后的时候报错如下：

![img](./images/article/2016-5-3/2.png)

于是安装```xcode-select```

执行：

	xcode-select --install

然后安装libxml2：

	brew install --with-python libxml2

但是执行完毕又报错：

![img](./images/article/2016-5-3/3.png)

执行：

	echo /usr/local/opt/libxml2/lib/python2.7/site-packages >> /usr/local/lib/python2.7/site-packages/libxml2.pth

却提示：

	zsh: no such file or directory: /usr/local/lib/python2.7/site-packages/libxml2.pth

好吧，没有就新建一个吧，于是新建一个文件再次执行：

	zsh: permission denied: /usr/local/lib/python2.7/site-packages/libxml2.pth

还是不行啊，没有libxml2就安装不了scrapy呀，一般安装错误有可能就是缺少了某些包，直接下载吧：

	wget ftp://xmlsoft.org/libxml2/libxml2-git-snapshot.tar.gz//下载
	tar -zxvf libxml2-git-snapshot.tar.gz//解压
	cd libxml2-2.9.2/
	./configure

下载，解压，安装......好险，终于没有又报什么错误了。

这个时候再安装scrapy:

	pip install scrapy

提示：

	Installing collected packages: scrapy
	Successfully installed scrapy-1.0.6

安装成功。

执行scrapy提示：

	zsh: command not found: scrapy

不对呀，成功安装了scrapy为什么说not found呢？

最后终于找到问题，执行：

	ln -s  /Library/Frameworks/Python.framework/Versions/2.7/bin/scrapy /usr/local/bin/scrapy

呼~终于好了。问题在于我调用的不是系统的python，比如执行which python，路径显示:

	/usr/local/bin/python

如果是系统自带的python应该显示：

	/usr/bin/python

所以需要执行上面的```ln -s```命令，

那么这个命令是什么意思呢？Linux/Unix 档案系统中，有所谓的连结(link)，我们可以将其视为档案的别名，而连结又可分为两种 : 硬连结(hard link)与软连结(symbolic link)，硬连结的意思是一个档案可以有多个名称，而软连结的方式则是产生一个特殊的档案，该档案的内容是指向另一个档案的位置。硬连结是存在同一个档案系统中，而软连结却可以跨越不同的档案系统。

ln source dist是产生一个连结(dist)到source，至于使用硬连结或软链结则由参数决定。

不论是硬连结或软链结都不会将原本的档案复制一份，只会占用非常少量的磁碟空间。

参数格式 :

	　　-f : 链结时先将与 dist 同档名的档案删除

	　　-d : 允许系统管理者硬链结自己的目录

	　　-i : 在删除与 dist 同档名的档案时先进行询问

	　　-n : 在进行软连结时，将 dist 视为一般的档案

	　　-s : 进行软链结(symbolic link)

	　　-v : 在连结之前显示其档名

	　　-b : 将在链结时会被覆写或删除的档案进行备份

	　　-S SUFFIX : 将备份的档案都加上 SUFFIX 的字尾

	　　-V METHOD : 指定备份的方式

	　　--help : 显示辅助说明

	　　--version : 显示版本


ln是linux中一个非常重要命令，它的功能是为某一个文件在另外一个位置建立一个不同的链接，这个命令最常用的参数是-s，具体用法是：ln –s 源文件 目标文件。

范例 :

将档案yy产生一个symbolic link : zz

	ln -s yy zz

将档案yy产生一个hard link : zz

	ln yy xx

linux通过链接文件能共享几乎所有类型的文件。

再有一个问题就是执行:

	sudo pip install scrapy

的时候，会收到这样的提示：

![img](./images/article/2016-5-3/5.png)

google出stackoverflow上一个回答解释了这个问题：

![img](./images/article/2016-5-3/6.png)

就是添加一个-H参数。

那么添加这个参数是什么意思呢？sudo还有哪些参数呢？这就要让我们来看看sudo这个命令了。

语法：

	sudo(选项)(参数)

选项：

	-b：在后台执行指令；
	-h：显示帮助；
	-H：将HOME环境变量设为新身份的HOME环境变量；
	-k：结束密码的有效期限，也就是下次再执行sudo时便需要输入密码；
	-l：列出目前用户可执行与无法执行的指令；
	-p：改变询问密码的提示符号；
	-s：执行指定的shell；
	-u<用户>：以指定的用户作为新的身份。若不加上此参数，则预设以root作为新的身份；
	-v：延长密码有效期限5分钟；
	-V ：显示版本信息。

推荐一个linux系统命令查询的网站：

http://man.linuxde.net/

有兴趣的可以参考这些文档：

http://www.cnblogs.com/rwxwsblog/p/4557123.html?utm_source=tuicool&utm_medium=referral
这个楼主安装的时候也是遇到了很多问题。
