# <center>SM3 optimal实验报告</center>

>**课程名称     <u>创新创业实践课程</u>  **       
>
>**学生姓名   <u>李路岩</u>      学号  <u>202022180198</u>**     
>
>**学院   <u>网络空间安全</u>学院    专业  <u>信息安全</u>**   

[TOC]

## <center>实验思路</center>

>​	**SM3跟对称密码算法SM4不同，SM3无法利用多线程将消息分组同时加密，因为前者的结果会在后面形成依赖。于是采用多次加密不同文件，然后同时调用多个SM3模块进行多线程优化，提高吞吐量。**
>

## **<center>关键代码</center>**

```c++
std::vector<uint32_t> SM3::Implement_SM3(char* filepath)
{
	std::vector<uint32_t> hash_result(32, 0);
	std::ifstream fin;
	uint32_t filesize = 0;
	unsigned char* buffer = new unsigned char[MAXSIZE];
	unsigned char hash_output[32];
	//获取文件的大小
	struct _stat info;
	_stat(filepath, &info);
	filesize = info.st_size;

	fin.open(filepath, std::ifstream::binary);
	fin >> buffer;
	fin.close();

	thread* t = new thread[threadnum];
	for (int i = 0; i < threadnum; i++) {
		t[i] = thread(SM3::Calculate,buffer, filesize, hash_output);
	}
	for (int i = 0; i < threadnum; i++)
	{
		t[i].join();
	}
	

	hash_result.assign(&hash_output[0], &hash_output[32]);

	delete[]buffer;
	return hash_result;
}
```



## <center>实验结果</center>

优化前(orginal)：
<a href="https://img.gejiba.com/image/EyjL2T"><img src="https://img.gejiba.com/images/fdf3eef273bd094aa740a86716c20208.jpg" alt="fdf3eef273bd094aa740a86716c20208.jpg" border="0"></a>



优化后(optimal):

<a href="https://img.gejiba.com/image/EyjwLV"><img src="https://img.gejiba.com/images/eb477304eab25ab015af895637e4732f.jpg" alt="eb477304eab25ab015af895637e4732f.jpg" border="0"></a>