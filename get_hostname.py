#!/usr/bin/env python
# encoding: utf-8
'''
获取树莓派和pc主机的hostname，这样就不需要得到ip

todo:
    *  使用websocket显示网络情况 使用arp
    *  使用scapy处理网络
'''

import socket
hostname_pc = 'wwj-air.local' #放到setttings
hostname_pi = 'raspberrypi.local'

def get_pc_ip(hostname):
    return socket.gethostbyname(hostname)

def get_pi_ip(hostname):
    return socket.gethostbyname(hostname)

#print("pc:",get_pc_ip(hostname_pc))
#print("pi:",get_pi_ip(hostname_pi))
