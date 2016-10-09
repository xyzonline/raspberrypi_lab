#!/usr/bin/env python
# encoding: utf-8

import smtplib
from email.mime.text import MIMEText
from pi_config import mail_host,mail_user,mail_pass
import datetime

def send_mail(to_user_list,sub=u'安全提醒'):
    content=u'有人 于{} 进入您的房间'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = sub
    msg['From'] = mail_user
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(mail_user,to_user_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    content =  '''
<html><body>
<h1>Hello</h1>
<p>send by <a href="http://www.python.org">Python</a>...</p>
</body></html>
'''
    if send_mail("hello",content,mailto_list):
        print "发送成功"
    else:
        print "发送失败"

