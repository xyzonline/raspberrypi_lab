#coding:utf-8
import sys;reload(sys);sys.setdefaultencoding('utf8')
import distance,send_emails,chatbot_client,cloud_ai,pi_media,DHT11
pi_media.say(cloud_ai.get_response("你好".decode('utf-8')))
