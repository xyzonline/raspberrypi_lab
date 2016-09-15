#!/usr/bin/env python
# encoding: utf-8

import requests
import get_hostname
def study():
    pc_host = get_hostname.get_pc_ip('wwj-air.local')
    pc_server = "http://{}:5000".format(pc_host)
    requests.get('{}/study'.format(pc_server))
