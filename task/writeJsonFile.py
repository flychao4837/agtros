#!/usr/bin/python
# coding=UTF-8
##写、更改json文件

import os
import json
import types
import config
from config import creatRootDirectories

##TODO 1:直接将dict或json格式的数据写入文件 2：讲pandas格式的数据用pandas的to_json方法转换格式写入文件
##编码方式默认中文编码，python json.dumps默认中文是编码

def writeFile(inputfile, data, orient="", ascii=False):
    if type(data) is types.DictType:
        writeJsonFile(inputfile, data, ascii)
    elif type(data) is types.StringType:
        writeJsonFile(inputfile, data, ascii)
    elif type(data) is types.ListType:
        pass
    elif str(type(data)) =="<class 'pandas.core.frame.DataFrame'>":
        writePandasFile(inputfile, data, orient, ascii=False)
    else:
        pass


##写json、dict格式的文件
def writeJsonFile(inputfile, data, ascii):
    if os.path.isfile(inputfile):
        fileIn = open(inputfile, 'w+')
        outStr = json.dumps(data, ensure_ascii=ascii)   # 处理完之后重新转为Json格式
        fileIn.write(outStr)
        fileIn.close()
        return{'errcode':0,"data":'', 'errmsg':'Write Success'}

    else:
        creatRootDirectories()
        fileIn = open(inputfile, 'w+')
        outStr = json.dumps(data, ensure_ascii=ascii)  # 处理完之后重新转为Json格式
        fileIn.write(outStr)
        fileIn.close()
        return {'errcode': 0, "data": '', 'errmsg':'Write Success'}

##写 pandas DataFrame 格式的数据

def writePandasFile(inputfile, data,orient, ascii):
    data.to_json(inputfile, orient=orient, force_ascii=ascii)
    return {'errcode': 0, "data": '', 'errmsg': 'Write Success'}

if __name__ == '__main__':
    data = dict()
    data['name']="测试"
    data['time']="2016-11-01"
    data['code']="000000"
    writeFile(config.listsRootPath+'\\2016-11-25.json',data,"")