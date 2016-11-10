#!/usr/bin/python
# coding=UTF-8

import os as os
import json as json
import pandas as pd
import config

def readFile(inputfile):
    if os.path.isfile(inputfile):
        #方式1 直接读取，转成pandas数据表格
        # DataFrame = pd.read_json(inputfile)
        # print DataFrame

        ##方式2 json读取，转成dict对象(类似json对象)，用键值对来访问
        fileIn = open(inputfile , 'r')
        for eachLine in fileIn:
            line = eachLine.strip().decode('utf-8')  # 去除每行首位可能的空格，并且转为Unicode进行处理
            line = line.strip(',')  # 去除Json文件每行大括号后的逗号
            js = None
            try:
                js = json.loads(line)  # 加载Json文件
            except Exception, e:
                print 'bad line'
                continue
            #js["xxx"] = xxx  # 对您需要修改的项进行修改，xxx表示你要修改的内容
            outStr = json.dumps(js, ensure_ascii=False)   # 处理完之后重新转为Json格式
            #print outStr
            #print type(outStr)
            print js
            print type(js)
            print js['code']
            print js['code']['344']

    else:
        return {'errcode' : -10000 , 'errmsg' : "Cann\\'t find JSON file"+inputfile}




readFile(config.dataRootPath+'\\2016-11-07.json')