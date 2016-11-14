#!/usr/bin/python
# coding=UTF-8
##写、更改json文件

import os as os
import json as json
import confg

def writeFile(inputfile,data):
    if os.path.isfile(inputfile):

        ##方式2 json读取，转成dict对象(类似json对象)，用键值对来访问
        fileIn = open(inputfile , 'rw')

        outStr = json.dumps(data, ensure_ascii=False)   # 处理完之后重新转为Json格式

        fileIn.write(outStr)
        fileIn.close()

        return{'errcode':0,"data":''}

    else:
        confg.creatRootDirectories()


        fileIn = open(inputfile, 'rw')

        outStr = json.dumps(data, ensure_ascii=False)  # 处理完之后重新转为Json格式

        fileIn.write(outStr)
        fileIn.close()

        return {'errcode': 0, "data": ''}




# readFile(config.dataRootPath+'\\2016-11-07.json')