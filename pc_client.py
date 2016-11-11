#!/usr/bin/env python
# encoding: utf-8

'''
电脑服务的client，在树莓派中用
'''

import requests
import get_hostname
pc_ip = get_hostname.get_pc_ip('wwj-air.local')
server_base_url = 'http://{}:5000'.format(pc_ip)
def study():
    requests.get(server_base_url+"/study")
def sox(delay=3):
    url = "{}/sox?delay={}".format(server_base_url,delay)
    requests.get(url)
def play():
    requests.get(server_base_url+"/play")
def say(content):
    url = server_base_url+"/say"
    payload = {"content":content}
    requests.get(url,params=payload)
