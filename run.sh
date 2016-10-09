#!/usr/bin/env python
# encoding: utf-8

/usr/local/bin/gunicorn blockly2sensor_server:app --bind 0.0.0.0:5000 -w 4
