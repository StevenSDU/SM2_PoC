# 任务16：SM2_PoC实现

## 1、服务器端：

（1）服务器端的私钥b为13，从客户端接收数据为key和value并输出。（其中参数取值需要模n，n为我自己定义的参数97）

![image](https://user-images.githubusercontent.com/108848022/181669117-bfcb3516-d87f-48af-92a4-5b886edb9be7.png)

（2）为了简化计算，这里我只使用了数字作为用户名和密码，考虑2^16规模的数据量，然后令用户名和密码作为字符串级联之后进入SHA256函数中进行加密（代替原文中的Argon函数）

![image](https://user-images.githubusercontent.com/108848022/181669376-c78fec32-3da1-4375-b6ff-83a6954644f0.png)

（3）计算h_ab和集合S之后发送给客户端即可。

## 2、客户端：

（1）a表示客户端私钥11，在客户端中有关数字求逆和SHA256加密的函数需要定义。

![image](https://user-images.githubusercontent.com/108848022/181669741-3465db28-c07f-4f61-b4e2-a3b74f13a820.png)

（2）首先连接服务器，连接成功后计算k和v发送过去，并从服务器接收h_ab和集合表S进行输出。

![image](https://user-images.githubusercontent.com/108848022/181669851-3f9d9af0-c1d4-42d4-afab-ee1a41465b3b.png)

（3）最后一步计算并比较，观察用户名和密码是否泄漏。

## 3、结果输出：

（1）服务器端：

![image](https://user-images.githubusercontent.com/108848022/181669928-6f62746c-93b2-47b1-b818-9c47fcd2cf8b.png)

（2）客户端：

![image](https://user-images.githubusercontent.com/108848022/181669958-18ec4246-dbe4-4ddc-a58b-8d0374f57051.png)
