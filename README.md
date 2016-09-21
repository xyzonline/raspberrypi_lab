# raspberrypi_lab
引脚参考脚本

接线图看这里：(之后有空用工具生成专业的图好了)

![](https://raw.githubusercontent.com/wwj718/gif_bed/master/pi_echo.png)


# 案例
### 在8x8led阵列绘制笑脸
```
import smile
smile.draw_smile()
# 需要一个清理的函数
```

### 用无缘蜂鸣器演奏《葫芦娃》
```
import beep
a = 1 #第一首曲子
buzzer = beep.Buzzer()
buzzer.play(a)
```  

### 综合演示
按照上图接线，往树莓派中接入超声波传感器、无源蜂鸣器、8x8LED阵列

运行:`sudo python echo.py`

把树莓派放到门后，超声波传感器正对前方，当门被打开时，先演奏一曲曲子，点亮笑脸以示欢迎，之后树莓派将在你电脑屏幕中打开ibook（假装在学习:) 

最后一个功能需要本地运行brave中的脚本，并配置好ip


#  实验特性
### 远程运行代码服务
源码见：blockly2sensor_server.py

文档参考：blockly2sensor_server.md

该服务允许树莓派运行通过http发送过来的代码。（假设发送者可信，毕竟树莓派就是人家的啊！）

计划将blockly作为前端，用户通过拖曳生成代码，再通过树莓派控制硬件
