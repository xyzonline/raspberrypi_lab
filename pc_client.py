#!/usr/bin/env python
# encoding: utf-8

import requests
import get_hostname
pc_ip = get_hostname.get_pc_ip('wwj-air.local')
server_base_url = 'http://{}:5000'.format(pc_ip)
def study():
    requests.get(server_base_url+"/study")
def sox():
    requests.get(server_base_url+"/sox")
def play():
    requests.get(server_base_url+"/play")
def say(content):
    url = server_base_url+"/say"
    payload = {"content":content}
    requests.get(url,params=payload)
def open_ai_talk(content):
    url = server_base_url+"/openbot"
    payload = {"content":content}
    response = requests.get(url,params=payload)
    print(response.json())

open_ai_talk(u'早啊')
