#!/usr/bin/env python
# encoding: utf-8
# 启动脚本，在supervisor中使用
/usr/local/bin/gunicorn blockly2sensor_server:app --bind 0.0.0.0:5000 -w 1
