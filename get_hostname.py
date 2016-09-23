#!/usr/bin/env python
# encoding: utf-8

# 获取树莓派和pc主机的hostname，这样就不需要得到ip
# wwj-air.local

# hostname = socket.gethostname()
#IP = socket.gethostbyname(hostname)

import socket
hostname_pc = 'wwj-air.local'
hostname_pi = 'raspberrypi.local'

def get_pc_ip(hostname):
    return socket.gethostbyname(hostname)

def get_pi_ip(hostname):
    return socket.gethostbyname(hostname)

print "hostname_pc", get_pc_ip(hostname_pc)
print "hostname_pi:",get_pi_ip(hostname_pi)
