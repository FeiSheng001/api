#_*_ coding:utf-8 _*_
#Project:autoTest
#File:parasFormat
#Author:ShengFei
#Email:petersat@163.com
#Time: 2020/8/9 11:04

from jsonpath import jsonpath
from .logClass import Logger

logger=Logger().getLog()

class ParamsFormat:
    def jsonFormat(self,params):
        try:
            for key in params.keys():
                if len(params[key]) > 1:
                    value = jsonpath(*params[key])[0]
                    params.update({key:value})
            return params
        except  Exception as e:
            logger.error("%s参数格式化失败:%s"%(params,e))

if __name__ == '__main__':
    userInfo = {"data": [{"nikename": "风清扬","openid": "UEHUXUXU78272SDSassDD",
                "userbalance": 5678.9,"userid": 17890,"username": "admin","userpoints": 4321}], "httpstatus": 200}
    productInfo = {"data": [{"SKU": "FRTSJ7676","price": 29.9,
                "productdesc": "麒麟瓜皮薄瓜瓤嫩,就连翠衣也很清甜,瓤虽是粉红而不是深红,但甜度丝毫不减。",
                "productid": 8888,"productname": "海南麒麟瓜5斤装"}],"httpstatus": 200}

    format = {"userid": (userInfo, "$.data[0].userid"),
              "openid": (userInfo, "$.data[0].openid"),
              "productid": (productInfo, "$.data[0].productid")
              }
    para=ParamsFormat().jsonFormat(format)
    print(para)

