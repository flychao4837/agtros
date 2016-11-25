#!/usr/bin/python
# encoding=utf-8
# Filename: put_files_hdfs.py
# 让多条命令并发执行,如让多条scp,ftp,hdfs上传命令并发执行,提高程序运行效率
import datetime
import os
import threading
from readJsonFile import readFile
from getDailyInfo import getDailyData
import config

dateStr = datetime.datetime.now().strftime("%Y-%m-%d")
jsonFile = config.dataRootPath + '\\' + dateStr + '.json'
tmpDate = readFile(jsonFile)
threads = []  # 线程池
if tmpDate['errcode'] == 0:
    list = tmpDate['data']
    for listitem in list:
        baseCodeDir = ""
        if bool(listitem['code']):
            baseCodeDir = config.dataRootPath
            baseCodeDir = baseCodeDir+"\\"+listitem['code']
            if os.path.isdir(baseCodeDir):
                pass
            else:
                os.mkdir(baseCodeDir)


            code = listitem['code']

            th = threading.Thread(target=getDailyData, args=(code,))
            th.start()
            threads.append(th)

            # 等待线程运行完毕
            for th in threads:
                th.join()

            # 等待线程运行完毕
            for th in threads:
                th.join()
        else:
            print 'error code'
else:
    print tmpDate['errmsg']

print "程序结束运行%s" % datetime.datetime.now()