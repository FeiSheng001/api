#_*_ coding:utf-8 _*_
#Project:Tranning
#File:interface
#Author:ShengFei
#Email:petersat@163.com
#Time: 2020/8/1 11:21

import requests
import json
import jsonpath
import unittest
"""
通过以一个接口为一个testcase的形式实现，unittest直接调用运行
"""
class Interface(unittest.TestCase):
    globalPara={"productId":8888}

    @classmethod
    def setUpClass(cls) -> None:
        print("接口测试执行开始:")

    @classmethod
    def tearDownClass(cls) -> None:
        print("接口测试执行结束")

    def test_alogin(self):
        url="http://39.98.138.157:5000/api/login"
        bodyData={"username":"admin","password":"123456"}
        header={"Content-Type":"application/json"}
        res=requests.post(url=url,headers=header,data=json.dumps(bodyData)).json()
        token=jsonpath.jsonpath(res,"$.token")[0]
        returnMsg=jsonpath.jsonpath(res,"$.msg")[0]
        returnStatus=jsonpath.jsonpath(res,"$.httpstatus")[0]
        self.globalPara['token']=token
        self.assertEqual(returnMsg,"success")
        self.assertEqual(returnStatus,200)

    def test_bgetProductInfo(self):
        url="http://39.98.138.157:5000/api/getproductinfo?productid=%s"%self.globalPara['productId']
        res=requests.get(url=url).json()
        returnStatus=jsonpath.jsonpath(res,"$.httpstatus")[0]
        self.assertEqual(returnStatus,200)

    def test_cgetUserInfo(self):
        url="http://39.98.138.157:5000/api/getuserinfo"
        header={"token":self.globalPara['token']}
        res=requests.get(url=url,headers=header).json()
        returnStatus=jsonpath.jsonpath(res,"$.httpstatus")[0]
        userId=jsonpath.jsonpath(res,"$.data[0].userid")[0]
        openId=jsonpath.jsonpath(res,"$.data[0].openid")[0]
        self.globalPara['userId']=userId
        self.globalPara['openId']=openId
        self.assertEqual(returnStatus,200)

    def test_daddCart(self):
        url="http://39.98.138.157:5000/api/addcart"
        header={"token":self.globalPara['token'],"Content-Type":"application/json"}
        bodyData={"userid":self.globalPara['userId'], "openid":self.globalPara['openId'], "productid":self.globalPara['productId']}
        res=requests.post(url=url,headers=header,data=json.dumps(bodyData)).json()
        returnStatus=jsonpath.jsonpath(res,"$.httpstatus")[0]
        returnResult=jsonpath.jsonpath(res,"$.result")[0]
        cartId=jsonpath.jsonpath(res,"$.data[0].cartid")[0]
        self.globalPara['cartId']=cartId
        self.assertEqual(returnStatus,200)
        self.assertEqual(returnResult,"success")

    def test_ecreateOrder(self):
        url="http://39.98.138.157:5000/api/createorder"
        header={"token":self.globalPara['token'],"Content-Type":"application/json"}
        bodyData={"cartid":self.globalPara['cartId'],
                  "openid":self.globalPara['openId'],
                  "productid":self.globalPara['productId'],
                  "userid":self.globalPara['userId']
                  }
        res=requests.post(url=url,headers=header,data=json.dumps(bodyData)).json()
        returnStatus=jsonpath.jsonpath(res,"$.httpstatus")[0]
        returnResult=jsonpath.jsonpath(res,"$.result")[0]
        self.assertEqual(returnStatus,200)
        self.assertEqual(returnResult,"success")

if __name__ == '__main__':
    unittest.main()