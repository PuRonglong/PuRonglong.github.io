---
layout: post
title: jquery tips(1):判断DOM对象是否为空
description: "jquery tips(1):判断DOM对象是否为空"
tags: [技术]
image:
  background: triangular.png
comments: true
share: true
---

我们在用jquery操作DOM对象的时候，有时需要判断DOM对象是否为空：

<!-- more -->

```js
if ($("#id")){ 
    $("#id").text("hi"); 
}
```

但实际上用jquery方法获取对象会始终返回一个jquery对象，所以if($("#id"))会始终为true，应该判断这个jquery对象下有没有获取到的对象，可以通过长度来判断:

```js
if($('#id').length > 0){
    
}
```

或者原生js：

```js
var id = document.getElementById('id');
if(id){
    
}
```
