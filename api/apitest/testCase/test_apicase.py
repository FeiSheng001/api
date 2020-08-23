#_*_coding:utf-8 _*_
#Project:autoTest
#File:main
#Author:ShengFei
#Email:petersat@163.com
#Time: 2020/8/10 0:28

import unittest
import jsonpath
from ddt import ddt, data, unpack
from ..public.getExcelData import getExcel
from ..public.request import Interface
from ..public.convertOperator import convertConvert,depend
import os
import json
from ..public.opExcel import Excel
from ..public.logClass import Logger

# 获取需要测试的接口数据
apicasePath=os.path.abspath('.')+'/apitest/testdata/apicase.xlsx'

#初始化一个日志器
logger=Logger().getLog()
@ddt
class MyTestCase(unittest.TestCase):

    @data(*getExcel(apicasePath).get_listData())
    @unpack
    def test_api(self,id,url,body,header,method,methodtype,returndata,json_path,expect,testresult):
        data = body if body !="" else None
        headers = header if header !="" else None
        newData=None if data is None else convertConvert().convertOp(data) if data.find("$") >=0 else eval(data)
        newHeader=None if headers is None else convertConvert().convertOp(headers) if headers.find("$")>=0 else eval(headers)
        apiObject = Interface(requestMethod=method, url=url, header=newHeader, data=newData, datatype=methodtype)
        res = apiObject.request()
        if len(returndata) >0 and returndata.find("/") < 0:
            depend[returndata]=res
        jsonpathexcept=jsonpath.jsonpath(json.loads(res),json_path)
        assertResult=(expect==jsonpathexcept[0])
        if assertResult==True:
            Excel(apicasePath).set_cellValue('Sheet1',id+1,10,'Pass')
            Excel(apicasePath).set_cellColor('Sheet1', id + 1, 10, 'GREEN')
            Excel(apicasePath).set_cellFont('Sheet1', id + 1, 10, '微软雅黑',15,True)
            Excel(apicasePath).set_cellAlign('Sheet1', id + 1, 10, 'center','center')
        else:
            Excel(apicasePath).set_cellValue('Sheet1', id + 1, 10, 'Fail')
            Excel(apicasePath).set_cellColor('Sheet1', id + 1, 10, 'RED')
            Excel(apicasePath).set_cellFont('Sheet1', id + 1, 10, '微软雅黑', 15, True)
            Excel(apicasePath).set_cellAlign('Sheet1', id + 1, 10, 'center', 'center')

if __name__ == '__main__':
    unittest.main()