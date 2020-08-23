#_*_ coding:utf-8 _*_
#file:logClass
#author:ShengFei
#email:petersat@163.com
#time:2020/6/7 16:55

import logging
import os
import time

logPath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/Log/'

class Logger(object):
    def getLog(self):
        logger=logging.getLogger("logger")
        logger.level=logging.ERROR
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        fileName=logPath+time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())+'.log'
        if not logger.handlers:
           sh=logging.StreamHandler()
           fh=logging.FileHandler(filename=fileName, mode='a', encoding='utf-8')
           formater=logging.Formatter(fmt="[%(filename)s] %(asctime)s %(module)s.%(funcName)s 第%(lineno)d行 %(levelname)s:%(message)s",datefmt="%Y-%m-%d %H:%M:%S")
           sh.setFormatter(formater)
           fh.setFormatter(formater)
           logger.addHandler(sh)
           logger.addHandler(fh)
        return logger

