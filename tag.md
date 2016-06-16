---
layout: page
title: Tag
permalink: /tag/
---

<article>
	{% for tag in site.tags %}
		<div class="tag-life" id="{{tag[0]}}">
			<h3 >{{ tag[0] }}：{{ tag | last | size }}篇</h3>
			<ul >
			{% assign pages_list = tag[1] %}
			{% for node in pages_list %}
				{% if node.title != null %}
				{% if group == null or group == node.group %}
					<li><a href="{{ site.BASE_PATH }}{{node.url}}">{{node.title}}</a> <span class="text-muted tag-li-span">—{{ node.date | date: "%Y年%m月%d日" }}</span></li>
				{% endif %}
				{% endif %}
			{% endfor %}
			{% assign pages_list = nil %}
			</ul>
		</div>
	{% endfor %}
</article>