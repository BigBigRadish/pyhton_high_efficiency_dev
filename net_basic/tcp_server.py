# -*- coding: utf-8 -*-
'''
Created on 2019年5月22日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
import socket
import datetime

HOST='0.0.0.0'
PORT=3434

#AF_INET说明使用IPV4地址，SOCK_STREAM指明TCP
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

while True:
    conn,addr=s.accept()#接收tcp连接，并返回新的Socket对象
    print(u'Client %s connected !'% str(addr))#输出客户端IP地址
    dt=datetime.datetime.now()
    message=u'current time is'+str(dt)
    conn.send(message.encode())#python3需要解码
    print(u'sent',message)
    conn.close()