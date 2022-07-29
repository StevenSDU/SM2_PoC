import sys
import json
import random
import socket
import hashlib

#a表示客户端私钥
a=11
n=97

# 求value在Fp域的逆——用于分数求逆
def get_inverse(value, p):
    for k in range(1, p):
        if (k * value) % p == 1:
            return k
    return -1

# 计算SHA-256加密
def hash256(m):
    return hashlib.sha256(m.encode()).hexdigest()

username=2022
password=2021

HOST = '127.0.0.1'
PORT = 2021
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    client.connect((HOST, PORT))
    print("客户端连接成功!")
except Exception:
    print('客户端连接失败!')
    sys.exit()
else:
    h=hash256(str(username)+str(password))
    k=h[:2]
    h_=int(h,16)
    v=str(pow(h_,a)%n)

    #客户端发送k，v
    addr = (HOST, PORT)
    client.sendto(k.encode(), addr)
    client.sendto(v.encode(), addr)

    print("从服务器端接收数据如下：")
    h_ab, addr = client.recvfrom(1024*5)
    h_ab = int(h_ab.decode(), 16)
    print("接收到的h_ab值为：", h_ab)
    Set, addr = client.recvfrom(1024*5)
    Set = Set.decode()
    S = json.loads(Set)
    print("接收到的集合表S为：", S)

    a_=get_inverse(a,n)
    h_b=pow(h_ab,a_)
    tmp=0
    for i in S:
        if h_b==i:
            tmp=1
    if tmp==0:
        print("用户名：",username,"验证成功！")
