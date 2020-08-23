#_*_ coding:utf-8 _*_
#file:sendEmail
#author:ShengFei
#email:petersat@163.com
#time:2020/6/7 16:55

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os
from email.header import Header
import smtplib
from .logClass import Logger

logger=Logger().getLog()
class Email():
    def __init__(self,sender,receiver):
        self.sender=sender
        self.receiver=receiver

    def createEmail(self,subject,content,filename=None,attname=None,filename1=None,attname1=None):
        # 声明一个带附件的邮件对象
        msg = MIMEMultipart()
        From = "<" + self.sender + ">"
        try:
            if filename==None and filename1==None:
                #邮件正文
                msgBody=MIMEText(_text=content,_subtype='plain',_charset='utf-8')
                msg['From']=Header(From)
                msg['To']=Header(self.receiver)
                msg['Subject']=Header(subject,'utf-8')
                msg.attach(msgBody)

            else:
                # 邮件正文
                msgBody = MIMEText(_text=content, _subtype='plain', _charset='utf-8')
                msg['From'] = Header(From)
                msg['To'] = Header(self.receiver)
                msg['Subject'] = Header(subject, 'utf-8')
                msg.attach(msgBody)

                # 获取当前文件名
                # file=os.path.basename(__file__)
                #读取文件的内容，先把内容读出来，然后存进附件中
                with open(filename,'rb') as f:
                    fileContent=f.read()
                    att=MIMEText(fileContent,'base64','utf-8')
                    att["Content-Type"] = 'application/octet-stream'
                    # 附件名称为中文时的写法
                    # att.add_header("Content-Disposition", "attachment", filename=("gbk", "", attname+".html"))
                    att.add_header("Content-Disposition", "attachment", filename=("gbk", "", attname))
                    # 附件名称非中文时的写法
                    # att["Content-Disposition"] = 'attachment; filename="%s"'%(attname+".txt")

                with open(filename1,'rb') as f:
                    fileContent=f.read()
                    att1=MIMEText(fileContent,'base64','utf-8')
                    att1["Content-Type"] = 'application/octet-stream'
                    # 附件名称为中文时的写法
                    # att.add_header("Content-Disposition", "attachment", filename=("gbk", "", attname+".html"))
                    att1.add_header("Content-Disposition", "attachment", filename=("gbk", "", attname1))
                    # 附件名称非中文时的写法
                    # att["Content-Disposition"] = 'attachment; filename="%s"'%(attname+".txt")

                msg.attach(att)
                msg.attach(att1)
            logger.info("邮件构建成功")
            return msg
        except Exception as e:
            logger.error("邮件构建失败:%s"%e)

    def sendEmail(self,emailObj,server,port,code):
        try:
            #邮件发送
            smtpObj=smtplib.SMTP()
            smtpObj.connect(server,port)
            smtpObj.login(self.sender,code)
            smtpObj.sendmail(self.sender,self.receiver,emailObj.as_string())
            smtpObj.close()
            logger.info("邮件发送成功!")
        except Exception as e:
            logger.error("邮件发送失败:",e)