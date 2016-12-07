#!/usr/bin/python
# coding=UTF-8
##写、更改json文件

import os as os
import json as json
import config as config
from config import creatRootDirectories

def writeFile(inputfile,data):
    if os.path.isfile(inputfile):

        print inputfile
        print data
        ##方式2 json读取，转成dict对象(类似json对象)，用键值对来访问
        fileIn = open(inputfile, 'w+')
        outStr = json.dumps(data, ensure_ascii=False)   # 处理完之后重新转为Json格式
        fileIn.write(outStr)
        fileIn.close()
        return{'errcode':0,"data":''}

    else:
        creatRootDirectories()
        fileIn = open(inputfile, 'w+')
        outStr = json.dumps(data, ensure_ascii=False)  # 处理完之后重新转为Json格式
        fileIn.write(outStr)
        fileIn.close()
        return {'errcode': 0, "data": ''}


if __name__ == '__main__':
    writeFile(config.dataRootPath+'\\2016-11-07.json')