#!/usr/bin/python
# coding=UTF-8
##读取json文件

import os as os
import json as json
import config

def readFile(inputfile,filetype=""):
    if os.path.isfile(inputfile):
        jsData = None

        ##dumps是将dict转化成str格式，loads是将str转化成dict格式。
        ###dump和load也是类似的功能，只是与文件操作结合起来了

        #方式1 直接读取，强制用JSON解析
        if  not bool(filetype):
            jsonobject = json.load(file(inputfile))
            #jsData = json.dumps(jsonobject, ensure_ascii="ascii", sort_keys=True, indent=0)
            jsData = jsonobject
        else:
            ##方式2 文本逐行读取，转成dict对象(类似json对象)，用键值对来访问
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
        return {'errcode':0,"data":jsData ,'errmsg':''}

    else:
        return {'errcode' : -10000 , 'errmsg' : "Cann't find JSON file"+inputfile,'data':''}


if __name__ == '__main__':
    readFile(config.listsRootPath+'\\stockBasic-bak.json')