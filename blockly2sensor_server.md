# blockly2sensor_server

* 在树莓派中构建服务，等待来自blockly的请求，请求为代码，把代码存入本地并运行，新的进程，可以杀死
* 可以参考[用python和github构建一只玩具木马](http://blog.just4fun.site/use-python-and-github-create-Trojan-Horse.html)
* 原理上是个http server：https://github.com/wwj718/raspberrypi_api ,也可以用websocket
* 决策：直接运行还是保存为本地文件执行，如果是本地文件意味着，可以开机启动
* 开机自启用supervisor
* watch dog

# 测试
```python
# hello world
http -f post  192.168.0.123:5000/run code='print "hello"' key='test'


# 点亮笑脸
http -f post  192.168.0.123:5000/run code='import smile;smile.draw_smile()' key='test'

# 清理画布
http -f post  192.168.0.123:5000/run code='import smile;smile.clear()' key='test'

# 点亮一颗led
http -f post  192.168.0.123:5000/run code='from Adafruit_LED_Backpack import Matrix8x8;display = Matrix8x8.Matrix8x8();display.set_pixel(3,3, 1);display.write_display()' key='test'  
```

# TODO
*  使用js请求控制树莓派
*  supervisor
*  pyflasks只检查错误，不要检查规范
