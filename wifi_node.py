#!/usr/bin/env python
# encoding: utf-8

'''
socket客户端
与李老师的无线神经节点通信

问题:
    *  没有机器名
    *  如何连接无线
'''

import socket
HOST ='192.168.12.181'    # The remote host
PORT = 5001 # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('s00d')
#s.sendall('s01d')
#s.sendall('s01d')
data = s.recv(1024).split("#")[0]
s.close()
print'Received', repr(data)
