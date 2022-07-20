from gmssl import sm3, func
import random

def str_to_byte(str):  # 字符串转换成byte
    ml = len(str)
    msg_byte = []
    msg_bytearray = str.encode('utf-8')
    for i in range(ml):
        msg_byte.append(msg_bytearray[i])
    return msg_byte

def byte_to_str(byte):  # byte转字符串
    ml = len(byte)
    str1 = b""
    for i in range(ml):
        str1 += b'%c' % byte[i]
    return str1.decode('utf-8')

Rho=set()
count=1
x=2
for c in range(1,100):
  while(count):
    for i in range(0,2^32):
      y=(x*x)+c #生成函数
      # print("y是",y)
      # print("c是",c)
      # print ("x是",x)
      x=y
      y_byte=str_to_byte(str(y))
      y_EN = sm3.sm3_hash(func.bytes_to_list(y_byte))[0:16] #SM3加密
      if(y_EN in Rho):
        print("True")
        print(x)
        count=0
        break
      else:
        Rho.add(y_EN)