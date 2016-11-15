#!/usr/bin/env python
# encoding: utf-8
'''
# socket client

用于发送事件
'''
import socket
import time
host = 'localhost'
port = 6000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1) #在客户端开启心跳维护
client.connect((host, port))
while True:
    client.send('hello')
    time.sleep(1) #如果想验证长时间没发数据，SOCKET连接会不会断开，则可以设置时间长一点
