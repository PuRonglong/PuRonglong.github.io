layout: post
title: 制作一款jekyll主题
description: "制作一款jekyll主题"
tags: [代码]
image:
background: triangular.png
comments: true
share: true
---
> 制作一款jekyll主题

首先是用jekyll新建一个项目，在命令行中输入：

	jekyll new jekyll-blog

这样就建好了一个jekyll项目，启动：

	jekyll serve

命令行提示如下：

![img](./images/article/2016-5-22/1.png)

可以看到成功启动了服务并且本地地址是http://localhost:4000/。

初始界面如下所示：

![img](./images/article/2016-5-22/2.png)

后续我们就是在这个基础上进行改动了。

首先我引入了bootstrap。

**添加```readmore```按钮功能。**

根目录下的index页做如下修改：

	<ul class="post-list">
	<!-- site.posts一个按照时间倒序的所有 Posts 的清单。 -->
	{% for post in site.posts %}
		<li>
			<h2>
				<a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
			</h2>
			<span class="post-meta">{{ post.date | date: "%Y-%m-%d" }}</span>
			{% if post.content contains '<!-- more -->' %}
				{{ post.content | split:'<!-- more -->' | first %}}
				<p class="readmore-p"><a class="btn btn-info" href="{{ post.url }}">Read more</a></p>
			{% else %}
				{{ post.content }}
			{% endif %}
		</li>
	{% endfor %}
	</ul>

可以看到主要的一点是if判断我们post的文章是否含```<!-- more -->```，若是包含的话，就使用过滤器将我们文章内容split为两部分，并选取第一部分显示为post.content。

**添加分页功能**

在添加分页功能之前需要先安装```jekyll-paginate```插件：

	gem install jekyll-paginate

安装完后在_config.yml里配置插件：

	paginate: 1
	paginate_path: "page:num"

运行serve却提示报错：

	Deprecation: You appear to have pagination turned on, but you haven't included the `jekyll-paginate` gem. Ensure you have `gems: [jekyll-paginate]` in your configuration file.

问题在于还要在config里添加一句```gems: [jekyll-paginate]```，表示调用这个插件，只有先调用，然后才是配置。

然后是写分页链接代码如下：

	<!-- 分页链接 -->
	<ul class="pagination">
        <li>
            <a href="/">
                <span>首页</span>
            </a>
        </li>
        <li>
        {% if paginator.page == 1 %}
            <li class="disabled"><span>&laquo;</span></li>
        {% else %}
            {% if paginator.previous_page == 1 %}
            <a href="/">
            {% else %}
            <a href="/page{{ paginator.previous_page }}">
            {% endif %}
                <span>&laquo;</span>
            </a>
        {% endif %}
        </li>
        {% for i in (1..paginator.total_pages) limit:9 offset:{{paginator.page-1}} %}
            {% if paginator.page == i %}
        <li class="active">
            {% else %}
        <li>
            {% endif %}
            {% if i == 1 %}
            <a href="/">{{i}}</a>
            {% else %}
            <a href="/page{{i}}">{{i}}</a>
            {% endif %}
        </li>
        {% endfor %}
        <li>
            {% if paginator.page == paginator.total_pages %}
            <li class="disabled"><span>&raquo;</span></li>
            {% else %}
            <a href="/page{{ paginator.next_page }}">
                <span>&raquo;</span>
            </a>
            {% endif %}
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

如上所示，在首页的底部添加一个ul，用于存放我们的分页链接，而这个链接我们分为了五个部分，第一个li是首页；第二个li是返回上一页的，这里做判断，如果当前页是第一页，就显示一个上一页的符号，并不可点按，如果当前页的上一页是第一页的话，点击返回到首页，其它情况都返回上一页；第三个li用于产生每一页的链接标签，用了for循环，如果当前页的page和i相等，则给当前的li添加一个class的类；第四个li用于添加下一页功能，原理和上一页功能一样；第五个li是尾页。

效果如下：

![img](./images/article/2016-5-22/3.png)

**文章分类功能**

每篇文章的开头类似这样：

	---
	layout: post
	title:  "jekyll的使用1"
	date:   2016-03-27
	tags: [jekyll, demo]
	---

开头信息力的tags存放的就是文章的标签，我们要实现的功能是页面显示部分有文章列表和标签列表。当点击标签的时候，文章列表对应当前标签下的所有文章。

jekyll的云标签有多种实现方法，先介绍第一种：

在_includes文件夹里添加tag.html，然后在页面中将其include进来。页面效果如下：

img1

左边文章列表右边标签列表。左边的列表其实有两个，一个是所有文章的列表，也就是对应所有标签的文章列表，还有一个是不同类型的文章列表，我们先来看第一个列表：

	<ul class="post-list" post-cate="all">
	{% for post in site.posts %}
		<li>
			<h2>
				<a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
			</h2>
			<span class="post-meta">{{ post.date | date: "%Y-%m-%d" }}</span>
			<span class="post-meta">all</span>
			<span class="text-info pull-right">字数：{{ page.content | number_of_words }}</span>
			{% if post.content contains '<!-- more -->' %}
				{{ post.content | split:'<!-- more -->' | first %}}
				<p class="readmore-p"><a class="btn btn-info" href="{{ post.url }}">Read more</a></p>
			{% else %}
				{{ post.content }}
			{% endif %}
		</li>
	{% endfor %}
	</ul>

这是一个带有post-cate属性并且属性值为all的ul列表，for循环遍历所有的文章。第二个列表如下：

	{% for tag in site.tags %}
	<ul class="post-list" post-cate="{{ tag | first }}">
		{% for posts in tag %}
			{% for post in posts %}
				{% if post.url %}
					<li>
						<h2>
							<a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
						</h2>
						<span class="post-meta">{{ post.date | date: "%Y-%m-%d" }}</span>
						<span class="post-meta">{{ tag | first }}</span>
						<span class="text-info pull-right">字数：{{ page.content | number_of_words }}</span>
						{% if post.content contains '<!-- more -->' %}
							{{ post.content | split:'<!-- more -->' | first %}}
							<p class="readmore-p"><a class="btn btn-info" href="{{ post.url }}">Read more</a></p>
						{% else %}
							{{ post.content }}
						{% endif %}
					</li>
				{% endif %}
			{% endfor %}
		{% endfor %}
	</ul>
	{% endfor %}

这里的一个不同是ul是放在for循环里的，循环所有的标签，

index.js中有一个函数：

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

初始时先将post-cate属性值不为all的ul隐藏掉，也就是将第二个列表隐藏掉，当我们点击某个标签的时候，获取到当前标签的标签属性值，如果ul的post-cate这个属性的值不是点击的标签，就将其隐藏，否则显示。

通过这样两个列表和点击选择属性的方法实现博客的标签功能。