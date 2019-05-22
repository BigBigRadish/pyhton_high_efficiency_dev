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

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#ipv4,UDP
s.bind((HOST,PORT))

while True:
    data,addr=s.recvfrom(1024)
    print('Received: %s from %s'%(data,str(addr)))
s.close()    