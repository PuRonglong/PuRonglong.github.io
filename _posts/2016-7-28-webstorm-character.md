---
layout: post
title: WebStorm11输入中文标点符号的问题
description: "WebStorm11输入中文标点符号的问题"
tags: [技术]
image:
  background: triangular.png
comments: true
share: true
---

webstorm11输入中文标点符号的时候有问题，比如，即使你切换到中文输入法下输入标点符号，结果还是输出的还是英文字符，以前还一直奇怪难道没有人遇到这个问题么，先前解决了这个问题，今天重装webstorm后又遇到这个问题，所以这里记录一下。

<!-- more -->

![img](/images/article/2016-7-28/2.png)

问题出在JDK，什么是JDK呢，百科上说，JDK是java语言的软件开发工具包，是整个java开发的核心，它包含了java的运行环境，java工具和java基础的类库。

JDK(Java Development Kit) 是 Java 语言的软件开发工具包(SDK)。<br  />
SE(J2SE)，standard edition，标准版，是我们通常用的一个版本，从JDK 5.0开始，改名为Java SE。<br  />
EE(J2EE)，enterprise edition，企业版，使用这种JDK开发J2EE应用程序，从JDK 5.0开始，改名为Java EE。<br  />
ME(J2ME)，micro edition，主要用于移动设备、嵌入式设备上的java应用程序，从JDK 5.0开始，改名为Java ME。

没有JDK的话，无法编译Java程序，如果想只运行Java程序，要确保已安装相应的JRE。

webstorm11内置的jdk版本有问题，存在中文标点输入后被转成英文标符号的bug，jetbrains上有人提到了这个问题[Cannot input full width punctuation in IDEs with bundled JDK 8 on Mac](https://youtrack.jetbrains.com/issue/IDEA-142652#u=1438065675248)

问题的解决办法在于让webstorm使用一个版本可用的jdk，比如JDK 8u45，新版的jdk如8u51可能也会有问题。有两种方法，我们先从oracle上下载该版本的jdk，[jdk-8u45-macosx-x64](http://www.oracle.com/technetwork/java/javase/downloads/java-archive-javase8-2177648.html#jdk-8u45-oth-JPR)，这么多别选错了哦。

方法一：

在webstorm中按下快捷键：commond + shift + a，在调出的输入框中输入jdk，回车，选择我们刚安装的8u45就好了，重启，然后就能愉快地输入了。

![img](/images/article/2016-7-28/1.png)

方法二：

移除 /Applications/WebStorm.app/Contents/ 里面的 jre 文件夹，这是mac系统下的地址哦，webstorm找不到自己的jdk就会去寻找系统中的jdk，就是我们刚才安装的版本咯。

如果jetbrains其它软件如pycharm要是也遇到此问题也可以试试这个方法哦。
