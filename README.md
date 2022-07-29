# <center>长度扩展攻击实验报告</center>

>**课程名称     <u>创新创业实践课程</u>  **       
>
>**学生姓名   <u>李路岩</u>      学号  <u>202022180198</u>**     
>
>**学院   <u>网络空间安全</u>学院    专业  <u>信息安全</u>**   

[TOC]

## <center>实验思路</center>

>1.随机生成一条消息note，然后计算这条消息的hash，记为hash1
>
>2.将hash1作为iv加密你想要添加的消息append_message，并计算hash，记为hash2
>
>3.构造一条消息“note+padding+append_message”记为hash3
>
>4.验证hash2与hash3是否相等

## <center>关键代码</center>

首先将gmssl库中的sm3进行修改，使得在加密时候，可以自行选择iv：

<img src="https://img.gejiba.com/images/b5c4d56b8981334ebac55397e3dac08a.jpg" alt="newsm3" border="0">

然后是长度扩展部分：

<img src="https://img.gejiba.com/images/2269a609d3b9d0abe2756214be8c89bb.jpg" alt="guess len extension" border="0">



## <center>实验结果</center>

<img src="https://img.gejiba.com/images/7fa93cc098d676debe1179f395353a7c.jpg" alt="len extension 结果" border="0">
