#_*_ coding:utf-8 _*_
#file:opDatabase
#author:ShengFei
#email:petersat@163.com
#time:2020/6/7 16:53

import mysql.connector
from .yamlClass import exeYaml
import os

mysqlPath=os.path.dirname(os.path.abspath('.'))+'/properties/mysql.yaml'
#获取mysql的配置信息
mysqlData=exeYaml(mysqlPath).getYaml()
address=mysqlData['server']
username=mysqlData['username']
password=mysqlData['password']
port=mysqlData['port']
database=mysqlData['database']

class Sqlresult(object):

    def getSqlresult(self,sql):
        conn=mysql.connector.connect(host=address,user=username,password=password,
                                     database=database,port=port,buffered=True)
        cursor=conn.cursor()
        resultList = []
        for a in sql:
            cursor.execute(a)
            result = cursor.fetchall()
            resultList.append(result)
        cursor.close()
        conn.close()
        return resultList

if __name__=='__main__':
    sql=("select * from course where cname='语文';",
         "select * from course where cname='数学';")
    result=Sqlresult().getSqlresult(sql)
    print(result)