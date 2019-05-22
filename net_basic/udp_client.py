# -*- coding: utf-8 -*-
'''
Created on 2019年5月22日

@author: Zhukun Luo
Jiangxi university of finance and economics
'''
import socket
HOST='127.0.0.1'
PORT=3434

#AF_INET说明使用IPV4地址，SOCK_STREAM指明TCP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data='hello udp'
s.sendto(data.encode(),(HOST,PORT))
print('sent: %s to %s:%d'%(data,HOST,PORT))
s.close()