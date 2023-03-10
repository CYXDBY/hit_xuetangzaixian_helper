# 背景
由于同学们看课热情过于高涨，甚至要一次性看几十个视频，学校为了学生们的人身安全不得不给网站添加了新的机制，以保证学生们不会废寝忘食地观看课程。
但是我们作为信息时代的一份子，必须要赶上时代的潮流，走信息化、智能化路线，以赛博之身实现看课自由！

## 使用教程
这是需要填写的数据，以下逐一解释

![1](https://user-images.githubusercontent.com/25530367/224272494-4c8a2cad-1ffb-4552-9baa-f1846a7b6213.jpg)

首先打开你的学堂在线，随便进入一节课，按下F12，像这样

![2](https://user-images.githubusercontent.com/25530367/224269118-05595edf-ab5f-447e-b4ee-e6ebc640b77d.jpg)

点击**网络**后点击**重新载入**

![3](https://user-images.githubusercontent.com/25530367/224269132-fc845ded-b9c6-42f2-baf6-eeccf381878b.jpg)

暂停视频等待一段时间，再播放视频，会看到最下方弹出来两个新东西，点击POST那个

![4](https://user-images.githubusercontent.com/25530367/224269163-d754d490-a89c-40f7-817a-58b3ea021138.jpg)

打开右边响应头下面的**请求头**，将对应参数填写进去

![5](https://user-images.githubusercontent.com/25530367/224269361-507f8f5d-9de9-4561-b236-4c1acbdac22d.jpg)

打开**请求**，展开data，填写对应参数

![6](https://user-images.githubusercontent.com/25530367/224271187-bfd22159-5f9b-4a5a-b906-3390b6fc2372.jpg)

打开你课程的**第一节课**和**最后一节**，复制其url最后的数字，填入vStart和vEnd

![7](https://user-images.githubusercontent.com/25530367/224271779-0a47b8a8-62ff-4b86-91d6-826b6f1599da.jpg)

运行脚本，返回200就是成功，400就是有东西填错了，其它一般是wait太短，调长一点就行

## 原理
懒得写了，自己猜吧
