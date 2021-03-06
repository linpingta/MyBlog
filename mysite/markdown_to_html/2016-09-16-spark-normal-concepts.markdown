---
layout: post
title: "Spark常用概念"
date: 2016-09-16 10:54:51 +0800
comments: true
categories: [Spark] 
keywords: 
description: 
---

这篇博客主要涵盖了我在Spark学习中遇到的一些较为重要的概念。这些概念对我理解服务运行有很大的帮助，但由于网上有更详细更精彩的解释，我在这里并不打算全面的覆盖每个概念的解释，而主要起到对概念索引的作用。如果需要具体查找相关概念，还请在网上搜索相关名词。

概念列表
1. RDD与DataFrame：RDD是Spark计算的基础单位，它是一个逻辑概念，从程序的角度讲，所有操作都包含在RDD transformation和RDD action之上。DataFrame又称为schema RDD，意为包含元数据定义的RDD，它自1.6版本引入，后续会成为MLlib操作的首选对象。
2. action与transformation：RDD的操作都可以划分为这两类行为。它们的区别在于，transformation的输出是另外一个RDD，action的输出是其它对象或文件。执行上讲，transformation操作并不会立即执行，它是lazy的，Spark只是记录它的执行路径，只有遇到action时，相关操作才会转为physical execution plan具体执行。
3. driver, executor, master, worker：有时候会容易把driver, master或者executor，worker混淆。首先，对Spark程序而言，它只有driver和executor两个概念，driver负责生成tasks，executor负责具体执行。master和worker是cluster manager的概念，cluster manager负责对集群的资源进行调度，因此无论driver还是executor，都是执行在worker node上的，同时driver和master的任务目标也是不同的。
4. cluster manager类别：Spark支持三种集群管理方式：standalone，Mesos和YARN，YARN里面又分为yarn-client和yarn-cluster两种模式。Mesos和YARN都是成熟的集群管理方式，在生产环境里用的更多些，也方便与Hadoop任务贡献资源，standalone是单独的集群，意味对资源的单独占用
5. yarn-client和yarn-cluster的区别：主要在于driver的未知，yarn-client的driver是运行的客户端的，如果客户端关闭，任务就结束了，yarn-cluster的driver是运行在集群ApplicatoinMaster上的，任务运行时不要求客户端active
6. ApplicationMaster是什么：这是YARN的一个概念，所有任务必须通过ApplicationMaster作为容器包装， 它负责与ResourceManager交互，申请资源
7. driver-memory和executor-memory应该如何设置：driver-memory通常不需要太大，因为driver上面不执行任务，但如果有collect操作还是要大一些，一般设置1G即可，executor-memory根据任务实际的需要可以大一些
8. Spark执行参数设置：董有一系列[博客](https://www.iteblog.com/archives/1672)，涉及参数设置还有调优，对原理也讲得很多，建议看看
9. DAG：有向无环图，Spark执行任务的基础，每次遇到action时，它会根据依赖，去找所有祖先节点的任务，构成一个DAG后，再作为job执行
10. job,stage和task：相比于RDD是Spark的逻辑概念，job,stage和stask都是Spark物理执行中的概念。它们基本是包含关系，每个job可能会被拆分为多个stage，每个stage里包含多个task。它们都可以在Spark Web UI上查看执行情况。具体而言，每个action操作都会产生一个单独的job，job会根据情况划分stage，主要是根据任务是否可以在本地执行，或者说是否有shuffle，每次shuffle都会划分出两个stage，同一个stage里的任务可以并行执行parallel。
11. shuffle：从底层讲，Spark任何执行也可以划分为map类和reduce类，比如filter,map都是在本地操作，而reduceByKey则需要对key进行归并。每次reduce操作都会引起shuffle，shuffle包括shuffle read和shuffle write，都是对磁盘的操作，因此从性能角度出发，尽可能减少shuffle操作可以提高执行效率
12. Spark Web UI：查看任务执行情况，包括job, stage, storage, task，其中stage里面可以看到执行DAG情况，通常在提交任务机器的4040端口查看，查看只能在任务执行区间，任务结束后不能再查看
13. Spark SQL和Hive QL：区别还是在底层实现框架上，Spark SQL是采用Spark执行，而Hive QL是把任务翻译成map-reduce执行
14. Spark比Hadoop快：并不是绝对的，在某些任务上Spark不一定比Hadoop快。Spark快的主要原因在于：
	
		1.Spark把任务视为一个DAG执行，在任务间可以并行化，Hadoop是把每个任务作为map-reduce执行，并不会对任务间优化
        2.Spark的任务主要是在内存里计算的，而map-reduce每次都会有shuffle操作，因此对于迭代类任务，大量的读写会较慢
        3.Spark的executor在初始化时启动jvm，后续不需要每次都重新启动，Hadoop的jvm会为每个任务新启动，初始化时间消耗也是一个因素
15.Spark cache或者persist：默认情况下，每个action都会重新计算它链路上所有的RDD，但如果有RDD被多次重复使用，可以使用rdd.persist()来做缓存，避免重复计算
16.Spark与内存：Spark并不要求把所有数据都放到内存里才能计算

暂时想到的是这么多，在此记录下。