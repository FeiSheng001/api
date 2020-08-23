import json
import jsonpath

# body='{"userid":$uservar.data[0].userid$,"openid":"$uservar.data[0].openid$","productid":$productvar.data[0].productid$}'
#
# depend={
#             "uservar":'{"data":[{"nikename":"风清扬","openid":"UEHUXUXU78272SDSassDD","userbalance":5678.9,"userid":17890,"username":"admin","userpoints":4321}],"httpstatus":200}',
#             "productvar":'{"data":[{"SKU":"FRTSJ7676","price":29.9,"productdesc":"麒麟瓜皮薄瓜瓤嫩,就连翠衣也很清甜,瓤虽是粉红而不是深红,但甜度丝毫不减。","productid":8888,"productname":"海南麒麟瓜5斤装"}],"httpstatus":200}'
#           }

# depend={"loginvar":'{"adress": {"city": "changsha"}, "httpstatus": 200, "info": {"age": 18, "name": "admin"}, "msg": "success", "token": "23657DGYUSGD126731638712GE18271H"}'}
# body='{"token":"$loginvar.token$"}'

"""
按照"userid":$uservar.data[0].userid$的模板去解析数据，
用于接口与接口的数据关联
"""
depend = {}
class convertConvert:
    def convertOp(self,body):
        #切片"$"
        listsplitvar=body.split("$")
        num=0
        for strrequest in listsplitvar:
            #等于1的时候就是要取得块
            if num % 2 == 1:
                #拿到我要取的块
                strchuck = strrequest
                #要把变量取出来
                envar=strchuck[0:strchuck.find(".")]
                #变量拿出来
                varvalue=depend[envar]
                #要把对应的jsonpath取出来
                varjsonpath=strchuck[strchuck.find(".") +1:]
                #通过jsonpath在变量里取值
                varjsonresult=json.loads(varvalue)
                varchuck=jsonpath.jsonpath(varjsonresult,expr="$."+ varjsonpath)
                #替换
                listsplitvar[num]=str(varchuck[0])
               #print(varjsonpath)
            num = num+1
        listsplitvar=eval("".join(listsplitvar))
        return listsplitvar


# if __name__ == '__main__':
#     returnData=convertConvert().convertOp(body)
#     print(returnData)