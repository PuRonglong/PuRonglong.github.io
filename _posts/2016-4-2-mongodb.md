---
layout: post
title: Mac下Mongodb的启动
description: "记Mac下Mongodb的启动"
tags: [技术]
comments: true
share: true
cover: https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420170111.png
---

> 在启动Monggodb服务的过程中，失败了几次，看到有别的同学也遇到了相同的问题，开此一贴以示说明。

安装是通过brew安装的：

```
	brew install mongodb
```

遇到的问题开始是这样的。首先是通过yeoman构建一个项目，构建好后使用```gulp```命令启动项目时报如下错误：

<!-- more -->

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420153332.png)

别看提示这么长，其实就是说连不上我们的```mongodb```了。道理很简单，我们的项目依赖```mongodb```，那在启动项目前是不是应该先启动我们的```mongodb```服务呢。搜噶。下面来启动我们的```mongodb```：

启动```mongodb```数据库服务端，shell执行：

```
	mongod
```

结果：

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420153349.png)

咦，怎么又报错了捏？

原来，默认```mongodb```数据文件是放到根目录data/db目录下，如果没有这个文件，就需要自行创建，我们看到报错信息里提示/data/db not found，所以自建一个吧，执行命令：

```
	mkdir -p /data/db
```

再来启动我们的数据库服务端，执行：

```
	mongod
```

运行结果：

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420153358.png)

怎么还有错呢？

看提示信息，可能是权限不够。执行：

```
	sudo mongod
```

可以看到运行结果有：

```
	 waiting for connections on port 27017
```

如果能在localhost://27017里打开，看到如下内容，就说明启动成功啦~

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420153407.png)

OK，启动数据库服务成功。
