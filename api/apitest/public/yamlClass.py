#_*_ coding:utf-8 _*_
#Project:autoTest
#File:yamlClass
#Author:ShengFei
#Email:petersat@163.com
#Time:2020/7/26 11:09
'''
解析yaml文件数据
'''
import yaml
import os

class exeYaml(object):

    def __init__(self,file):
        self.file=file

    # 读取单个yaml文件数据
    def getYaml(self):
        with open(self.file, 'r', encoding='utf-8') as f:
            streamData=f.read()
            yamlData=yaml.load(streamData,Loader=yaml.FullLoader)
            return yamlData

    # 读取多个yaml文件数据，返回的数据为一个列表形式
    def getmutilYaml(self):
        yamlDataList=[]
        with open(self.file, 'r', encoding='utf-8') as f:
            streamData=f.read()
            yamlDatas=yaml.load_all(streamData,Loader=yaml.FullLoader)
            for yamlData in yamlDatas:
                yamlDataList.append(yamlData)
            return yamlDataList

    # 使用yaml.dump方法生成yaml文档
    def generate_yamlDoc(self,data):
        with open(self.file, 'w', encoding='utf-8') as f:
            yaml.dump(data,f)

if __name__ == '__main__':
    path=os.path.dirname(os.path.abspath('.'))+'/properties/capabilities.yaml'
    data=exeYaml(path).getYaml()
    print(data)