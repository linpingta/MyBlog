---
layout: post
title: "django-blog"
date: 2014-07-03 23:07:53 +0800
comments: true
categories: [Django,Python]
---

[django blog system](https://github.com/linpingta/my-blog-redis)
=============

最开始的目标只是想试用下redis的威力。然后根据redis通常的应用场景（比如获取最热词条，获取
人人关系）（这些在简单的Blog中没有用武之地）在开发过程中对设计做了一些简单扩展，博客系统实现如下
功能：

    1. 用户登录 （没有做注册页，因为也不是真的要用，但是登录需要有，因为好友关系是
    建立在当前浏览用户不同的基础上，没有当前账户的概念，很难描述好友关系）
    2. Archive展示 展示基本的blog信息，包含两部分：
        全部blog的展示 （按照“喜欢”程度排序）
        个人blog的展示  (按照发布时间排序)
    3. Blog详细信息，允许评论
    4. 发布新的Blog
    5. 允许对博客点赞
    6. 允许对博客收藏
    7. 允许对博客按标签过滤
    
设计的不足
	最重要的一点是，没有和redis紧密联系。虽然redis可以作为Django的cache层，但是从网上的资料看，本身可以控制的内容极少，基本可以理解是django本身cache的一种替代。
	所以项目可以理解为简单Django的系统
	
	其它不足：
    1. 现在的博客系统非常简陋，有用户和评论的概念，但只允许新增博客，不允许删除和修改自己的博客
    2. Tag过滤的bug （解释见下）
    3. 标题的限制，因为要用将标题作为url跳转的参数，参数如果有空格或者其它字符可能会导致错误    
    
关于功能2：

    对于首页，无论是否登录，无论是谁登录，看到的东西都是一样的
    对于自主页，首先要求用户登录，同时只显示自己的部分

关于功能5：
    
    需要对于博客有一个like功能：如果通过博客里的字段实现，那么没有办法查到谁lik
    另外需要避免重复like

关于功能6：

    需要对于author有一个收藏的功能：需要另外一个table存储author和blog，表示author喜欢的blog

关于功能4：
    
    对于编辑博客，只允许有非空标题和内容者发布，对于标签，支持分号分隔不同的标签
    （目前不支持标签自动提示功能）

关于功能7：
    
    支持在发布日志时对标签计数变化