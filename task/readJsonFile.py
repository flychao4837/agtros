#!/usr/bin/python
# coding=UTF-8
##读取json文件

import os as os
import json as json
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
            jsData = None
            try:
                jsData = json.loads(line)  # 加载Json文件
            except Exception, e:
                print 'bad line'
                continue
            #js["xxx"] = xxx  # 对您需要修改的项进行修改，xxx表示你要修改的内容
            #utStr = json.dumps(jsData, ensure_ascii=False)   # 处理完之后重新转为Json格式
            #print outStr
            #print type(outStr)


            #print jsData
            # print type(jsData)
            #print jsData[0]


            return{'errcode':0,"data":jsData ,'errmsg':''}

    else:
        return {'errcode' : -10000 , 'errmsg' : "Cann't find JSON file"+inputfile,'data':''}


if __name__ == '__main__':
    readFile(config.listsRootPath+'\\stockBasic-bak.json')