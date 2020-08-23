#_*_ coding:utf-8 _*_
#Project:autoTest
#File:api_runner
#Author:ShengFei
#Email:petersat@163.com
#Time: 2020/8/23 11:22

#运行主文件类

import unittest
from HTMLTestRunner import HTMLTestRunner
import os
import time
from apitest.public.sendEmail import Email
from apitest.public.yamlClass import exeYaml
from apitest.testCase.test_apicase import MyTestCase

# 根目录
rootPath=os.path.dirname(os.path.abspath(__file__))
#配置文件目录
confPath=rootPath+'/apitest/properties/email.yaml'
#测试报告目录
reportPath=rootPath+'/apitest/Report/'
#测试案例目录
casePath=rootPath+'/apitest/testCase/'
#读取邮件配置
emailInfo=exeYaml(confPath).getYaml()
send = emailInfo['sender']
receive = emailInfo['receiver']
smtpServer = emailInfo['server']
smtpPort = emailInfo['port']
authcode = emailInfo['authcode']

loader=unittest.TestLoader()
testSuit=unittest.TestSuite()
# cases=loader.discover(start_dir=casePath,pattern="test_apicase.py")
cases=loader.loadTestsFromTestCase(MyTestCase)
testSuit.addTests(cases)
reportName=reportPath+time.strftime("%Y-%m-%d-%H-%M-%S")+'.html'
case_reportName="测试案例执行情况"+'-'+time.strftime("%Y-%m-%d-%H-%M-%S")+'.xlsx'
caseFile=rootPath+'/apitest/testdata/apicase.xlsx'
#初始化一个邮件对象
emailObj=Email(send,receive)
emailSubject="自动化测试报告"+'-'+time.strftime("%Y%m%d%H%M%S")
emailContent="今日自动化测试报告如附件所示，还请查看\n谢谢！"
with open(reportName,'wb+') as f:
    runner=HTMLTestRunner(stream=f,verbosity=2,title="测码学院自动化测试报告"+time.strftime("%Y%m%d"),description="用例详情")
    runner.run(testSuit)
emailMessage = emailObj.createEmail(subject=emailSubject,content=emailContent,filename=reportName,attname=emailSubject+'.html',filename1=caseFile,attname1=case_reportName)
emailObj.sendEmail(emailMessage,smtpServer,smtpPort,authcode)