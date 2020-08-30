---
layout: post
title: 如何让终端优雅地装X
description: "如何让终端优雅地装X"
tags: [技术, 生活]
comments: true
share: true
cover: https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420154006.png
---

>当使用系统自带的终端使用多了的时候，你会体会到许多不便之处，比如自动补全不够完善，比如界面单调，老早就知道iterm2+oh my zsh的组合，但知道看到一个别人的界面漂亮的不行，才终于打动我也更换成这样的搭配。

主要配置：```iTerm2 + zsh + oh-my-zsh + agnoster```

先来看看那幅打动我的漂亮的命令行是什么样的吧~

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420153842.png)

<!-- more -->

讲真，这个命令行界面美哭了。而且iterm2又是免费的，简直良心有木有。于是决定动手换成这样，折腾起来却碰到不少坑，花了一天才配好，也把遇到的坑说明一下以作参考。

下面我将一步一步讲解配置过程：

1：

当然是下载我们的iterm2啦~

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420153853.png)

2：

打开iterm2。

3：

安装oh-my-zsh。

oh-my-zsh:

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420153901.png)

在iterm2中输入以下：

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420153913.png)

这里我装了几次都不行，连接有问题，进度一直是0%，愁死了，然后官网里给的另外一个方法需要使用wget，结果mac系统又没有自带wget命令，有需要先安装了wget，找了以下发现安装wget好麻烦，需要先下载wget，然后在命令行里进行解压，安装，看起来好麻烦我也就没有用wget安装oh-my-zsh了，还是试了多次第一种安装方法，终于有一次不知道怎么就连接上了，然后就装上了。PS：这里其实蠢了以下，后来才知道wget可以不用手动安装这么麻烦，我们有homebrew啊，执行：

```
    brew install wget
```

后来我通过这样装上了wget命令。

4：

这样装好了iterm2和oh-my-zsh以后为了配成顶图那样的样子我们还要进行如下微调：

在iterm2的偏好设置的profile里，有一个window选项，在这里设置背景图和透明度，还有宽高和停靠选项。示例这里，用了一张雨水滴在窗户的图片为背景，透明度是30+，背景色为黑色，字体默认，字色大概为橙黄，停靠在bottom。

然后去```bing```搜索了找到了示例里的背景图，打开iterm2和示例对比，也没有太大区别了。

后来发现橙色现在看起来好看，但当命令多了以后，就有点乱了。

这个体验完后还是想换成oh-my-zsh推荐的agnoster主题。于是又开始折腾了。

5：

然后才发现弄错了，这样我其实还是使用的dash，只不过iterm2定制化了一下，这和zsh一点关系都没有。更别说使用0h-my-zsh了。

启动iTerm 2 默认使用dash改用zsh解决方法：

```
    chsh -s /bin/zsh
```

以为这样就切换为zsh了，结果我还是天真了，知道看到好几次dash提示才知道我这还是dash，原来还要输入

```
    zsh
```

执行一下才算切换，好几个文章里都没有说明这点让我一直以为执行```chsh -s /bin/zsh```就行了。

6：

安装Powerline：

```
    pip install powerline-status
```

如果没有，则先执行安装pip指令

```
    sudo easy_install pip
```

这里开始还以为这样就可以了结果发现界面还是乱码，原来弄错了一点powerline是一款非常好的代码提示状态栏，但是我们并没有装好powerline字体，原来这是两码东西啊，还以为我们```pip install powerline-status```就是字体呢。

7：

下载安装字体库：

```
    git clone https://github.com/powerline/fonts.git ~/powerline-fonts
```

上面只是下载了字体，下载下来后需要cd到install.sh文件所在目录，执行安装命令，弄了半天都不知道install.sh在哪里。。。最后终于找到了：

```
    source ~/powerline-fonts/install.sh
```

安装完成后提示所有字体均已下载到```/Users/superdanny/Library/Fonts```路径，如下：

```
    All Powerline fonts installed to /Users/superdanny/Library/Fonts
```

8：

设置iTerm 2的```Regular Font```和```Non-ASCII Font```：

安装完字体库之后，把iTerm 2的设置里的Profile中的Text 选项卡中里的Regular Font和Non-ASCII Font的字体都设置成 Powerline的字体，我设置的字体是```12pt Meslo LG S DZ Regular for Powerline```

9：

配色方案solarized：

要先下载：

```
    $ git clone git://github.com/altercation/solarized.git
```

进入上面下载的工程的```solarized/iterm2-colors-solarized```下双击```Solarized Dark.itermcolors```和```Solarized Light.itermcolors```两个文件就可以把配置文件导入到iTerm2里.

通过load presets选择安装的配色主题。

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420153928.jpeg)

10:

使用agnoster主题。字体没有安装好的话使用这个主题会乱码。

进入~/.zshrc打开.zshrc文件，然后将```ZSH_THEME```后面的字段改为```agnoster```。ZSH_THEME="agnoster"（agnoster即为要设置的主题）。

这里开始的时候还不知道怎么找.zshrc，原来.开头的文件mac都会默认将他们隐藏，这时候又得去查找怎么找到隐藏的文件，在终端输入：

```
    defaults write com.apple.finder AppleShowAllFiles -bool true//显示

    defaults write com.apple.finder AppleShowAllFiles -bool false//隐藏
```

注意执行完显示隐藏后要重启finder才生效。怎么重启finder呢？

```
    killalll Finder
```

于是先执行显示，找到了文件后使用常用的文本编辑器sublime打开，然后修改主题。

矮油，真是麻烦死了，于是只得先去把vim学习一下，于是才有了那篇vim的博文，这样就不用来回切换。vim又是一个大坑，宝宝心里那个苦啊。当然那是熟练操作而言，这里这种小小的修改不用那么熟练掌握vim了。再说，题目让终端优雅地装X，不使用vim怎么能算有逼格呢，怎么能说是优雅呢？

11:

增加指令高亮效果——```zsh-syntax-highlighting```。

指令高亮效果作用是当用户输入正确命令时指令会绿色高亮，错误时命令红色高亮。

1）cd到.zshrc所在目录。这里要说明的是其实默认打开的就是.zshrc所在目录。

2）执行指令将工程克隆到当前目录

```
    git clone git://github.com/zsh-users/zsh-syntax-highlighting.git
```

3）打开.zshrc文件，在最后添加下面内容

```
    source XXX/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
```

保存文件。

注意：xxx代表.zshrc所在目录

4）

```
    cd ~/.oh-my-zsh/custom/plugins
```

5）再次打开.zshrc文件，在最后面添加下面内容

```
    plugins=(zsh-syntax-highlighting)
```

完成以上以后基本上已经使用上iterm2 + oh-my-zsh了。

12：

可是看着每次打开看着那么多文件都是一个颜色太单调了，也不明显，于是折腾着想要怎么加上颜色：

先说Vim语法高亮吧。

在Vim中输入命令:syntax on激活语法高亮，若需要Vim启动时自动激活，在~/.vimrc中添加一行syntax on即可。

Mac OSX的ls是没有颜色的，需要设置。

1、打开～目录下的```.bash_profile```（没有此文件的话新建一个，注意前景有.，是隐藏文件）：vim .bash_profile

2、在.bash_profile里添加下面两个语句：

```
    export CLICOLOR=1

    export LSCOLORS=1212121212121212121212
```

3、LSCOLORS的具体设置看下面：

LSCOLORS的1对应前景色，2对应背景色。

实际应用中，将1和2改成下面的字母——对应不同颜色。

LSCOLORS共有11组”12”设置，每组12对应文件类型为

1、   directory

2、   symbolic link

3、   socket

4、   pipe

5、   executable (可执行文件，x权限)

6、   block special

7、   character special

8、   executable with setuid bit set (setuid=Set User ID，属主身份)

9、   executable without setgid bit set

10、  directory writable to others, with sticky bit

11、  directory writable to others, without sticky bit

字母代表的颜色如下：

a     black

b     red

c     green

d     brown

e     blue

f     magenta

g     cyan

h     light grey

A     bold black, usually shows up as dark grey

B     bold red

C     bold green

D     bold brown, usually shows up as yellow

E     bold blue

F     bold magenta

G     bold cyan

H     bold light grey; looks like bright white

x     default foreground or background (透明)

我不设背景色，于是将所有2变成x。

文件夹颜色一般设为红色，蓝色或青色，我试了一下还是觉得蓝色好看

最后，我用的颜色设置为：

```
    export LSCOLORS=exfxaxdxcxegedabagacad #指定颜色
```

13：

可是看着看着还是有点不习惯的地方就是命令行前面的前缀太长了。

在终端里面当前行会显示```username@FirstName-LastnamedeMacBook-Pro ~$```

这里的username是当先登陆的用户名，@后面是机器名称，~是当前路径。我都用的是自己的全称puronglong，这样前缀就太长了。看着也烦，早就想去掉了。

找到一个以下方法：

```
    vim .profile
    # append
    PS1="\W $ "
    # or
    # PS1 = "\w $"
    export $PS1
```

然而实验了一下发现并不能。愁。

还有一个方法可以在系统偏好设置 --> 共享 --> 更改电脑名称里把机器名称改短一点，这样是可以，可是前端的用户名还是有啊，机器名还是想保留自己名字只把后面的MacBook-Pro改为了MBP，这样还是很长诶~愁。

最后找到这个方法：

```
    DEFAULT_USER="puronglong"  #增加这一项，可以隐藏掉路径前面那串用户名
```

在.zshsrc中添加这一行，引号里面要填的是你的用户名。

通过以上种种，最后终于用上干净整洁功能更完善的命令行了。

看看我的新效果，哇哦~

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420154006.png)

终于折腾完了~
