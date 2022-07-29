import sys
import json
import random
import socket
from os.path import commonprefix
import hashlib

#b表示服务器端私钥
b = 13
n = 97
HOST = ''
PORT = 2021
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print("服务器连接成功！")

print("从客户端接收数据如下：")
key,addr = server.recvfrom(1024)
key = int(key.decode(),16)
print("接收到的key值为：",key)
value,addr = server.recvfrom(1024)
value = int(value.decode(),16)
print("接收到的value值为：",value)

key_value_table=[]

# 计算SHA-256加密
def hash256(m):
    return hashlib.sha256(m.encode()).hexdigest()

for i in range(1,pow(2,16)):
    h=hash256(str(i)+str(i))
    key_value_table.append(h)

V=[]
for j in key_value_table:
    if j[:2]==key:
        j_=int(j,16)
        V.append(pow(j_,b)%n)

#计算h_ab
h_ab=(pow(value,b))%n

server.sendto(hex(h_ab).encode(),addr)
Set = json.dumps(V)
server.sendto(Set.encode(),addr)
server.close()
