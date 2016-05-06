layout: post
title: Mac显示隐藏文件
description: "some note"
tags: [代码]
image:
background: triangular.png
comments: true
share: true
---

Mac上修改隐藏文件。有时候我们会遇到需要修改隐藏文件的情况，比如以```.```开头的文件，有两种方法可以实现：

第一种是通过```ls -all``命令显示出所有的文件，这个命令可以显示出隐藏和没有隐藏的所有文件，然后用vim打开文件进行编辑即可。

第二种是使用命令行修改隐藏显示：

	defaults write com.apple.finder AppleShowAllFiles -bool true//显示

	defaults write com.apple.finder AppleShowAllFiles -bool false//隐藏

	killalll Finder

需要注意的是，执行完显示或者隐藏的命令之后，需要重启Finder才能生效，重启Finder的命令为```killall Finder```