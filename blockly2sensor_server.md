* 在树莓派中构建服务，等待来自blockly的请求，请求为代码，把代码存入本地并运行，新的进程，可以杀死
* 可以参考[用python和github构建一只玩具木马](http://blog.just4fun.site/use-python-and-github-create-Trojan-Horse.html)
* 原理上市个http server：https://github.com/wwj718/raspberrypi_api ,也可以用websocket
* 决策：直接运行还是保存为本地文件执行，如果是本地文件意味着，可以开机启动
* 开机自启用supervisor
* watch dog
