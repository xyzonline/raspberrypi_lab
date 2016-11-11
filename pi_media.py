#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
import subprocess
from threading import Timer
import local
import re

'''
树莓派本地媒体 控制脚本 和pc_server相似

todo：写一个media_common.py
'''


def play():
    recording_file = "" # todo
    command = ["play","./data/recording.wav"]
    subprocess.call(command)
    return '播放成功!'



kill = lambda process: process.kill()
def sox(delay):
    # 控制程序运行时长: https://dzone.com/articles/python-101-how-to-timeout-a-subprocess
    #http://127.0.0.1:5000/sox?delay=3
    #delay = int(request.args.get('delay',3)) #get 传参,录音时长
    play_mp3("./data/begin_recording.mp3")
    command = ["sox","-d","./data/recording.wav"]
    sox = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    my_timer = Timer(delay, kill, [sox])
    try:
        my_timer.start()
        stdout, stderr = sox.communicate()
    finally:
        #print (stdout, stderr)
        play_mp3("./data/end_recording.mp3")
        my_timer.cancel()
        return '录音成功!'


def play_mp3(uri):
    subprocess.call(['mpg123',uri])


def text2audio_url(content):
    access_token = local.baidu_access_token
    url = "http://tsn.baidu.com/text2audio?tex={content}&lan=zh&per=0&pit=9&spd=6&cuid=wwj_pi&ctp=1&tok={access_token}".format(content=content,access_token=access_token)
    #print(url)
    return url


def say(content):
    #content = request.args.get('content')
    play_mp3(text2audio_url(content))
    return '说话成功！'

def lirc_record(delay=2):
    '''
    功能：录红外线
    http://blog.just4fun.site/raspberrypi-lirc.html

    1.录制时间2秒
    2.取出录制内容
    3.用sed填充到/etc/lirc/lircd.conf里

    开始录制/结束录制

    # 开启restart
    '''
    play_mp3("./data/begin_infrared.mp3") #提示
    #command_raw = "mode2  -d /dev/lirc0 > /tmp/temp.code"
    command = ["mode2","-d","/dev/lirc0"]
    mode2 = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    my_timer = Timer(delay, kill, [mode2])
    try:
        my_timer.start()
        stdout, stderr = mode2.communicate()
        raw_num = get_raw_num(stdout)
        # 把数字插入到功能里 /etc/lirc/lircd.conf 放置锚点
        insert_lirc_key(raw_num)
    finally:
        play_mp3("./data/end_infrared.mp3")
        my_timer.cancel()
        # restart
        subprocess.call(["/etc/init.d/lirc", "restart"])
        return '录音成功!'

def get_raw_num(raw_code):
    # 清理出数字，正则
    #raw_num = re.split(r"[(space)|(pulse)|\n]",raw_code)
    raw_num = re.findall(r"\d+",raw_code)[1:]
    return " ".join(raw_num)

def insert_lirc_key(raw_num):
    conf = "/etc/lirc/lircd.conf"
    template = "/etc/lirc/lircd.conf_template"
    print raw_num
    with open(template, 'r') as file1:
          filedata = file1.read()
    content = re.sub(r"KEY_BLOCKLY(.+\d+)","KEY_BLOCKLY\n               {}\n".format(raw_num),filedata,flags=re.DOTALL)
    # 必须用KEY_BLOCKLY,倒过来会报错
    with open(conf, 'w') as file2:
          file2.write(content)
    #把内容塞到文件的锚点里

def send_infrared(key="KEY_BLOCKLY"):
    command = ["irsend","SEND_ONCE","/home/pi/lircd.conf",key]
    subprocess.call(command)
    print("红外信号发射成功")


if __name__ == '__main__':
    say("开始红外录制")
