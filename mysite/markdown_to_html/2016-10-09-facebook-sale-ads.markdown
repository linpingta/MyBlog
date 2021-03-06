---
layout: post
title: "Facebook电商广告投放初步"
date: 2016-10-09 10:23:53 +0800
comments: true
categories: [Facebook,DPA,Advertise] 
keywords: 
description: 
---

此内容基于一次电商广告投放的介绍。

因为是基于一次介绍的信息，因此内容可能看起来层次感会比较差，但从实践的角度讲，无论是技术还是运营，都可以得到一些帮助。

我们假设广告主在网站埋点的工作已完成，假设对install类广告有一定了解。

Facebook 电商广告分为两类：非DPA广告和DPA广告

创建篇
1.非DPA广告

	Campaign：
		选择推广目标为Increase conversions on your website
	Adset：
		大部分设置和install一致，区别在于需要首先设置Conversions，Conversions依赖用户在网站的埋点，预定义的行为包括Add To Cart，Purchase等，没有埋点的事件是不可选的，电商常用的事件就是Add To Cart和Purchase。
		投放技巧上，Adset的目标在投放早期最好设置为Add To Cart而不要直接设置为Purchase，因为早期购买数据积累较少，直接设置目标为Purchase很可能不会得到展现。在投放了一两个月后，再设置目标为Purchase。
	Ad：
		同样设置方法和Install一致，但从投放技巧上，通常会选择轮播图或者轮播视频，让每个图是不同的产品，后续在统计查看时，找到转化好的产品（爆款），然后集中推广
	
2.DPA广告：

	Campaign：
		选择推广目标为Promote a product catalog，同时要选择一个Product Catalog
	
	AdSet：
		设置方法不同于Install和非DPA广告，一开始要从Product Catalog里选择一个Product Set，即推广产品的列表。
		在Audience方面，DPA提供了四种默认的Audience方式：
			Viewed or Added to Cart But Not Purchased
			Added to Cart But Not Purchased
			Upsell Products
			Cross-Sell Products
		同时也支持基于View和Add To Cart这些行为去进一步定义custom audience，从这些设置中可以看出，DPA主要是对老客户的reseller，因为它的Audience至少是View product过，而非DPA广告则是对新客户推广。
		在Placement方面，它默认的方式是automatic placement
	Ad：
		由于是DPA广告，它在文案等内容上支持插入参数，这些参数来自Product Set的预定义

统计篇

	无论是DPA还是非DPA广告，它们相比Install广告会多Add To Cart和Purchase两个指标，分别包含Add To Cart Number（加入购物车的用户数）和Add To Cart Spend（用户在购物车里加了多少钱），Purchase Number和Purchase Spend。
	电商广告主通常优化的唯一目标是ROI，即广告花费spend amounnt相比Purchase Spend的数值。但由于Purchase行为是滞后于花费行为的，因此在投放初期很可能看到只有花费，而没有后续收入的情况，这时依赖产品的ctr和Add to cart spend / spend作为判断依据，即产品ctr较高，以及加入购物车的钱数较多时，后续收回成本的可能性更高。
	另外电商相比Install特殊的一点是，因为它经常会在一个广告里放多个产品，因此在Ad级别breakdown数据观察很重要，对于非DPA广告可以观察每个广告图的投放情况，对于DPA广告，可以按Product ID观察。另外，由于Spend是基于Ad而不能细致到每个产品，因此主要观察Purchase和ctr作为产品判断的依据。

其它技巧及注意

	1. 电商广告投放初期可能会有成本回收不及时的问题，因此要有心理预期，回收时间范围会比install更长
	2. 考虑先用DPA一般投放，找到爆款后再单独建campaign投放指定产品
	3. DPA广告的ROI通常会远高于非DPA广告，因为它投放的是老顾客，相对而言非DPA广告投放的是新顾客
	4. 初期设置Add To Cart为目标，后期设置Purchase为目标
	5. 不要相信Fb的suggest bid
	6. 投放时可以采用小预算，尤其尝试新产品的时候
			
