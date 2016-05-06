layout: post
title: 在命令行中启动某个应用
description: "some note"
tags: [代码]
image:
background: triangular.png
comments: true
share: true
---

在命令行中启动某个应用，需要利用Alias来简化命令。比如要在命令行中启动sublime，如下操作：

使用vim打开配置文件：

	vim .zshrc

添加如下一行：

	alias sublime='open -a "Sublime Text"'

保存退出后执行：

	source .zshrc

让配置生效。

通过输入alias可以列出当前所有的别名设置，比如我们可以看到```ll```，```ls```这些常见命令的实际配置：

	l='ls -lah'
	la='ls -lAh'
	ll='ls -lh'
	ls='ls -G'
	lsa='ls -lah'