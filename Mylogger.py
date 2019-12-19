#!/usr/bin/env python3.6
#-*- coding: utf-8 -*-
import time
import os
import logging
from logging.handlers import TimedRotatingFileHandler as _TimedRotatingFileHandler
# base_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.getcwd()

#日志器
mylogger = logging.getLogger('logger1')
mylogger.setLevel(logging.INFO)
myhandler = _TimedRotatingFileHandler('{}/logs/dnsapi.log'.format(base_dir), when='D', backupCount=7)
myhandler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - [line:%(lineno)d] - %(module)s - %(funcName)s - %(message)s'))
mylogger.addHandler(myhandler)
