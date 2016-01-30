---
layout: post
title: 从GitHub遭受攻击看DDoS
description: "Git"
tags: [技术,Git]
image:
  background: triangular.png
comments: true
share: true
---

>3月底，GitHub遭受了有史以来最为严重的DDoS攻击

<figure>
    <a href="http://7vznhl.com1.z0.glb.clouddn.com/2015-4-12-GitHub-DDoS.PNG">
        <img src="http://7vznhl.com1.z0.glb.clouddn.com/2015-4-12-GitHub-DDoS.PNG" alt="photo" />
    </a>
    <figcaption>GitHub官方微博的声明</figcaption>
</figure>

由于网站是托管在GitHub上的，所以也受到了影响，即使现在GitHub恢复了，也有时不稳定。

别的一些DDoS攻击案例，比如暴雪战网，Valve Steam和EA Origin都遭受过大规模DDoS攻击，致使大批玩家无法登陆进行游戏。(战网，steam,origin都是著名的游戏平台)

<!--more-->

还有就是学校选课的时候，经常会碰到网站挂掉的情况，这就是一个最简单的DDoS原理，因为它虽然是正规的访问，但所体现的就是一个DDoS的效果

了解了这些案例，那么什么是DDoS呢，它有什么危害，又该如何防御呢？

在了解DDos之前我们先来了解下什么是DoS

DoS是Denial of Service的缩写，阻断式服务攻击，也称为洪水攻击，是一种恶意的网络攻击手段。其目标在于使连接上网络的目标电脑的网络资源及系统资源耗尽，使这个连上网络的主机暂停中断或停止服务，使它无法对正常用户提供

DDoS是指黑客可以利用网络上已被攻陷的电脑作为“僵尸”，向某一特定的目标电脑发动密集式的“拒绝服务”式攻击，这称为分布式拒绝服务攻击，英文是Distributed Denial of Service，缩写为DDoS。

也许这么说还是不太清楚，下面用几个例子来说明：

例1：

最近出现了一款手机网游，小明正玩的很嗨，这个时候女友的夺命连环Call(一直打电话)来了，因为正在玩游戏不方便接电话，于是两分钟内来了四通电话，都拒接了，拒接了第五通电话的时候，游戏掉线了，至于为什么掉线原理可见[手机打电话的时候，为什么手机网络就自动掉线](http://zhidao.baidu.com/link?url=QLxqOnZbOkcRCUH1eVU_7jumY95OF4TMLK1c5z4RFtr6_kfZPMxpUEmIGlVzdvJdvlnBPpL-pGsIcSnUKGne4_)

通过这个案例我们可以知道什么呢？原来夺命连环Call，就是一种DoS攻击。为什么这么说呢，因为会造成以下这些后果：

没有办法接其他人电话：网络频宽消耗型攻击

没办法玩游戏：这被称为应用资源消耗攻击

Call到你手机没电：这被称为系统资源消耗攻击

这是DoS，那DDoS是什么呢？

就是一群女友对你进行夺命连环Call

在现实中的攻击一般是这样，如图，

<figure>
    <a href="http://7vznhl.com1.z0.glb.clouddn.com/2015-4-12-DDoS.PNG">
        <img src="http://7vznhl.com1.z0.glb.clouddn.com/2015-4-12-DDoS.PNG" alt="photo" />
    </a>
</figure>

攻击者通过一个服务器节点，下发命令到所有的客户机上，然后来攻击这一个网站使其瘫痪，这就是一个最常见的DDoS案例，著名的攻击者有如：ANONYMOUS(匿名者)组织

互联网思维不仅体现在网上，也体现在生活的许多细节中，DDoS也不例外

例子2：

现实版DDoS

Lyft是 Uber 的竞争对手。去在2014年某段时间 Lyft的司机收到很多假订单：有人定了车，等司机出发后又取消预定。最后发现这些假订单中至少有5560个来自177名Uber员工。甚至有1名Uber员工用14个假帐号向Lyft的司机发出了680次假订单。Uber对此作出了解释，大概意思就是说这是临时工干的。Uber 此员工的行为就是现实版DDOS。

例子3：

一群恶霸试图让对面那家有着竞争关系的商铺无法正常营业，他们会采取什么手段呢？恶霸们扮作普通客户一直拥挤在对手的商铺，赖着不走，真正的购物者却无法进入；或者总是和营业员有一搭没一搭的东扯西扯，让工作人员不能正常服务客户；也可以为商铺的经营者提供虚假信息，商铺的上上下下忙成一团之后却发现都是一场空，最终跑了真正的大客户，损失惨重。此外，恶霸们完成这些坏事有时凭单干难以完成，需要叫上很多人一起。嗯，网络安全领域中DoS和DDoS攻击就遵循着这些思路。

例子4：

双十一快递爆仓。。。赶着“便宜”的浪潮买一大波并非真正需要的东西导致加急包裹无法按时送达

例子5：

<figure>
    <a href="http://7vznhl.com1.z0.glb.clouddn.com/2015-4-12-freebuf.png">
        <img src="http://7vznhl.com1.z0.glb.clouddn.com/2015-4-12-freebuf.png" alt="photo" />
    </a>
    <figcaption>这个段子很形象</figcaption>
</figure>

DNS 是域名系统 (Domain Name System) 的缩写，是因特网的一项核心服务，它作为可以将域名和IP地址相互映射的一个分布式数据库，能够使人更方便的访问互联网。DNS劫持其实就是段子中的东头煎饼摊派人将想去西头煎饼摊子的人“劫持”到自己的煎饼摊子去。

西头煎饼摊子表示已哭晕······

而回过头来，这次GitHub遭受的攻击，据悉，攻击者先后使用了四种DDoS技术攻击GitHub：

+ 第一波是创造性的劫持百度JS文件利用中国海外用户的浏览器每2秒向托管在GitHub上的两个反审查项目发出请求，这一手段被GitHub用弹出JS警告alert()防住；

+ 第二轮是跨域<img> 攻击，被GitHub检查Referer挡住；

+ 第三波是DDoS攻击GitHub Pages；//楼猪的博客表示很桑心

+ 第四波是正在进行中的TCP SYN洪水攻击，利用TCP协议缺陷发送大量伪造的TCP连接请求，让GitHub耗尽资源。对于Greatfire所实现的collateral freedom(PDF)，也有许多人对此表达了不满，Greatfire的做法让一些CDN服务商遭到了封杀，而GitHub是最新的受害者。

什么是服务器劫持：

如果一个网站包含了指向第三方托管JavaScript文件的script标签，那么该网站的所有访问者都会下载该文件并执行它。如果攻击者攻陷了这样一个托管JavaScript文件的服务器，并向文件中添加了DDoS代码，那么所有访问者都会成为DDoS攻击的一部分。

这种攻击之所以有效是因为HTTP中缺少一种机制使网站能够禁止被篡改的脚本运行。为了解决这一问题，W3C已经提议增加一个新特性子资源一致性。即SRI(Subresource Integrity)概念。该特性允许网站告诉浏览器，只有在其下载的脚本与网站希望运行的脚本一致时才能运行脚本。如果不匹配，则说明目标脚本被篡改，浏览器将不使用它。这是通过密码散列实现的。

中间人攻击是攻击者向网站插入恶意JavaScript代码的最新方式。在通过浏览器访问网站时，中间会经过许多节点。如果任意中间节点向网页添加恶意代码，就形成了中间人攻击。

"异步加载内容"技术是使Web2.0时代爆发的关键因素之一。由于新内容的加载可以完全脱离传统的打开链接或加载页面的方式，网页交互形式也显得愈加丰富。但事有两面，JavaScript的HTTP(S)请求使网站交互更加有趣的同时，也使浏览器更容易变成攻击者的武器。

网络战争正在进行

VERIZON资料外泄报告出炉，9成网络间谍攻击，来自国家级机构发动

网络间谍大增，2014年第一季度比2013年同比暴增三倍。此类攻击最为复杂，往往柔和多种攻击手段。来自东欧的网络间谍活动显著增长，占比超过20%，仅次于中国。据路透社报道，VERIZON,英特尔旗下的MCAFEE，卡巴斯基实验室以及其他提供数据的私人企业和公共机构的调查人员称，11%的网络间谍攻击活动来自犯罪团伙，87%来自政府。

网络战争的目的是什么

+ 窃取国家情报
+ 瘫痪网络
+ 勒索
+ 宣扬自我理念

该如何防范DDoS？

防火墙<br  />
增加频宽与设备性能<br  />
CDN<br  />
Cleaning Center<br  />
交换机速率限制/ACL功能<br  />
装DDS<br  />
定期扫描<br  />
在骨干节点配置防火墙<br  />
用足够的机器承受黑客攻击<br  />
充分利用网络设备保护网络资源<br  />
过滤不必要的服务和端口<br  />
检查访问者的来源<br  />
过滤所有RFC1918 IP地址<br  />
限制SYN/ICMP流量<br  />
等等

而回到现在，若有时网站打不开可以翻墙：

现在github的外网访问比较迅速，挂VPN，如果不是软件需要翻墙，只是网页翻墙，推荐使用收费的浏览器插件——[红杏](http://honx.in/i/U_hVln8mTjXTdlq3),名字就很骚气有木有！

免费的推荐这款浏览器插件[时空隧道插件](http://www.suidao.in/invi/WSJnNx),每天有2小时免费时间，即开即关，目前正在使用，棒棒哒~

其实可以转到GitCafe，GitCafe的空间是国内的，只是目前还没有精力去弄哒~

参考资料：<br  />
[不懂DDoS攻击，不敢去卖煎饼](http://www.freebuf.com/news/63506.html)<br  />
[那个动不动就黑了我们服务器的DDoS到底为何物](http://www.leiphone.com/news/201503/Ke6wjIO5opVpUdz0.html)
[浅谈 JavaScript DDoS 攻击原理与防御](http://www.codeceo.com/article/js-ddos.html)
[An introduction to JavaScript-based DDoS](https://blog.cloudflare.com/an-introduction-to-javascript-based-ddos/)