---
layout: post
title: 制作一款jekyll主题
description: "制作一款jekyll主题"
tags: [技术]
comments: true
share: true
cover: https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420160807.png
---
> 制作一款jekyll主题

首先是用jekyll新建一个项目，在命令行中输入：

```
jekyll new jekyll-blog
```

这样就建好了一个jekyll项目，启动：

```
	jekyll serve
```

<!-- more -->

命令行提示如下：

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420161059.png)

可以看到成功启动了服务并且本地地址是http://localhost:4000/。

初始界面如下所示：

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420161111.png)

后续我们就是在这个基础上进行改动了。

首先我引入了bootstrap。

**添加```readmore```按钮功能。**

根目录下的index页做如下修改：

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420161122.png)

可以看到主要的一点是if判断我们post的文章是否含```more```的一段信息，若是包含的话，就使用过滤器将我们文章内容split为两部分，并选取第一部分显示为post.content。

**添加分页功能**

在添加分页功能之前需要先安装```jekyll-paginate```插件：

```
	gem install jekyll-paginate
```

安装完后在_config.yml里配置插件：

```
	paginate: 1
	paginate_path: "page:num"
```

运行serve却提示报错：

```
	Deprecation: You appear to have pagination turned on, but you haven't included the `jekyll-paginate` gem. Ensure you have `gems: [jekyll-paginate]` in your configuration file.
```

问题在于还要在config里添加一句```gems: [jekyll-paginate]```，表示调用这个插件，只有先调用，然后才是配置。

然后是写分页链接代码如下：

```html
<!-- 分页链接 -->
<ul class="pagination">
    <li>
        <a href="/">
            <span>首页</span>
        </a>
    </li>
    <li>
    {.% if paginator.page == 1 %}
        <li class="disabled"><span>&laquo;</span></li>
    {.% else %}
        {.% if paginator.previous_page == 1 %}
        <a href="/">
        {.% else %}
        <a href="/page{{ paginator.previous_page }}">
        {.% endif %}
            <span>&laquo;</span>
        </a>
    {.% endif %}
    </li>
    {.% for i in (1..paginator.total_pages) limit:9 offset:{{paginator.page-1}} %}
        {.% if paginator.page == i %}
    <li class="active">
        {.% else %}
    <li>
        {.% endif %}
        {.% if i == 1 %}
        <a href="/">{{i}}</a>
        {.% else %}
        <a href="/page{{i}}">{{i}}</a>
        {.% endif %}
    </li>
    {.% endfor %}
    <li>
        {.% if paginator.page == paginator.total_pages %}
        <li class="disabled"><span>&raquo;</span></li>
        {.% else %}
        <a href="/page{{ paginator.next_page }}">
            <span>&raquo;</span>
        </a>
        {.% endif %}
    </li>
    <li>
        <a href="/page{{paginator.total_pages}}">
            <span>末页</span>
        </a>
    </li>
    <li class="disabled">
        <span>第{{paginator.page}}页 / 共{{paginator.total_pages}}页</span>
    </li>
</ul>
```

如上所示，在首页的底部添加一个ul，用于存放我们的分页链接，而这个链接我们分为了五个部分，第一个li是首页；第二个li是返回上一页的，这里做判断，如果当前页是第一页，就显示一个上一页的符号，并不可点按，如果当前页的上一页是第一页的话，点击返回到首页，其它情况都返回上一页；第三个li用于产生每一页的链接标签，用了for循环，如果当前页的page和i相等，则给当前的li添加一个class的类；第四个li用于添加下一页功能，原理和上一页功能一样；第五个li是尾页。

效果如下：

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420161134.png)

**文章分类功能：**

每篇文章的开头类似这样：

```ruby
	---
	layout: post
	title:  "jekyll的使用1"
	date:   2016-03-27
	tags: [jekyll, demo]
	---
```

开头信息力的tags存放的就是文章的标签，我们要实现的功能是页面显示部分有文章列表和标签列表。当点击标签的时候，文章列表对应当前标签下的所有文章。

jekyll的云标签有多种实现方法，先介绍第一种：

在_includes文件夹里添加tag.html，然后在页面中将其include进来。页面效果如下：

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420161143.png)

左边文章列表右边标签列表。左边的列表其实有两个，一个是所有文章的列表，也就是对应所有标签的文章列表，还有一个是不同类型的文章列表，我们先来看第一个列表：

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420161154.png)

这是一个带有post-cate属性并且属性值为all的ul列表，for循环遍历所有的文章。第二个列表如下：

![img](https://puronglong-blog-image.oss-cn-beijing.aliyuncs.com/20200420161202.png)

这里的一个不同是ul是放在for循环里的，循环所有的标签，

index.js中有一个函数：

```js
function categoryDisplay(){
	// show all
	$('.home>ul[post-cate!=all]').hide();

	// show tag post list when click tag link
	$('.categary-p').click(function(){
		var cate = $(this).attr('cate');

		$('.home>ul[post-cate!=' + cate + ']').hide(250);
		$('.home>ul[post-cate=' + cate + ']').show(400);
	});
}
```

初始时先将post-cate属性值不为all的ul隐藏掉，也就是将第二个列表隐藏掉，当我们点击某个标签的时候，获取到当前标签的标签属性值，如果ul的post-cate这个属性的值不是点击的标签，就将其隐藏，否则显示。

通过这样两个列表和点击选择属性通过js控制显示隐藏的方法实现了博客的标签功能。

另一种标签方法：

通过新建文件夹tag, 然后在其中再新建各标签名文件夹, 在各文件夹下创建index.html或者index.md文件, 填写标签模板内容;
在根目录下创建jekyll.md文件, 然后在文章头文件的基础上加上permalink: /tag/jekyll即可。原理相当于给每一个标签写个首页。

还有一种标签方法原理和上面一样，只是各个标签文件是自动生成不是手动创建的，需要编写一段代码。因为jekyll是用ruby写的，所以这段代码是ruby代码，我是直接找一个复制的，将此段代码保存到_plugins文件夹下，当启动jekyll serve的时候会自动创建文件夹。下面来看具体过程。

首先创建一个tag页的模板，也就是当我们点击的时候希望显示的页面，比如我在_layout文件里新建了一个tagpage.html用于存放我的tag模板。我选择了和首页的页面一样的模板，将首页的模板内容复制过来以后要注意需要修改一点。在首页里我们通过如下：

```html
	{.% for post in site.posts %}
		<li>
```

来循环li，也就是对site.posts进行遍历，这样便会遍历出全站所有的posts，展示所有文章，但在tag页的首页我们要展示的只是含有某些标签的文章，所以这里遍历的对象不同，应该是遍历所有该标签的文章：

```html
	{.% assign posts = site.tags[page.tag] %}
		<ul class="post-list" post-cate="all">
		{.% for post in posts %}
			<li>
```

如上，循环posts输出li，这个posts就是前面通过assign定义的posts，page变量是页面专属的信息，通过YAML头文件定义的信息都可以在这里被获取到，所以这个page.tag就是post所属的tag，site来自_config.yml文件，表示全站范围的信息+配置，site.tags表示所有该标签下的文章，所以```site.tags[page.tag]```表示该标签的所有文章。

通过如下的标签就能链接到每个tag的首页了。

```html
	<a class="page-link" href="/tag/{{ tag | first }}">{{ tag | first }}</a>
```

**jekyll插件安装：**

这里介绍两种插件安装方式：

1.在根目录下新建```_plugins```文件夹，然后把对应的```*.rb```文件放进去。

2.在_config.yml文件中新建一个gems关键字，然后把要引用的插件用数组形式存储其中即可。

这两种方法可以同时使用。

**jekyll代码高亮：**

我们写博客的时候经常会需要放代码，如果博文中的示例代码能够高亮显示，无疑会提升读者的阅读体验。那么看看jekyll中如何让代码高亮吧。

要让代码高亮需要使用到代码高亮插件，插件的原理就是查找特定的节点，然后对其赋予特定的css，也就是“上色”。

以```Pygments```为例：

首先安装：

```
	pip install Pygments
```

在_config.yml文件中配置：

```
	highlighter: pygments
```

表明启用pygments进行代码高亮了，但光配置了还不行，还需要添加css代码，可以在pygments网站上查找想要的css配置，方法如下，打开网页：http://pygments.org/demo/3666780/ 右边可以选择样式，选择GO就可以看见效果，而此时打开浏览器调试，可以看见其中有一个pygments.css文件，下载下来，在项目中引用即可。

我选用了一个monokai的style的css，如果没有效果的话，修改一下css里的class名就可以了。

代码高亮可以了。可以我们还不满足，当一段代码太长的时候，让它显示滚动条比自动换行会方便阅读很多，于是对代码块添加一下属性：

```
	pre code { white-space: pre }
	overflow-x: auto;
```

pre值表明空白会被浏览器保留。其行为方式类似HTML中的<pre>标签。```overflow-x: auto```让x轴过长时滚动显示。

pygments插件对应的md文件中写如下：

```html
{.% highlight html %}
def show
@widget = Widget(params[:id])
respond_to do |format|
    format.html # show.html.erb
    format.json { render json: @widget }
end
end
{.% endhighlight %}
```

如果想要代码块简单一点可以如下写：

	```js

	```

中间存放代码块，这样使用的话就需要不使用pygments，而使用rouge。修改以后同样需要修改css文件里的class名。

关于 jekyll 里时间格式可以看这篇。[Jekyll Date Formatting Examples](http://alanwsmith.com/jekyll-liquid-date-formatting-examples)