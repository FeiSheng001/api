# _*_ coding:utf-8 _*_
# @file:request
# @author:ShengFei
# @email:petersat@163.com
# @time:2020/6/25 13:07
import requests
from .logClass import  Logger
import json
"""
接口对象的封装，调用时直接向对象中传入对应的参数即可
"""
# 初始化一个日志器
logger = Logger().getLog()
depency={}
class Interface(object):

    def __init__(self, requestMethod, url, header=None, data=None, datatype=None):
        self.reqType = requestMethod.lower()
        self.url = url
        self.header=header
        self.data =self.getDatatype(data, datatype)

    @staticmethod
    def getDatatype(data, type):
        if str(type).lower() == 'form':
            reqData = data
        elif str(type).lower() == 'json':
            reqData = json.dumps(data)
        else:
            reqData = data
        return reqData

    def request(self):
        try:
            response = getattr(requests,self.reqType)
            responseBody=response(url=self.url, headers=self.header, data=self.data).text
            return responseBody
        except Exception as e:
            logger.error("接口调用异常:%s" % e)