#!/usr/bin/env python
# encoding: utf-8
'''
# socket服务
threading event

多线程

自定义事件
用于监听外部事件

保持长连接:http://www.cnblogs.com/xilouch/p/4618903.html
'''
import socket
BUF_SIZE = 1024
host = 'localhost'
port = 6000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1) #接收的连接数
client, address = server.accept() #因为设置了接收连接数为1，所以不需要放在循环中接收
while True: #循环收发数据包，长连接
    data = client.recv(BUF_SIZE)
    #print(data.decode()) #python3 要使用decode
    print(data)
    # client.close() #连接不断开，长连接
