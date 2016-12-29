#!/usr/bin/python
# encoding=utf-8

import datetime
import os
import threading
from readJsonFile import readFile
from getDailyInfo import getDailyData
import config
import time

dateStr = datetime.datetime.now().strftime("%Y-%m-%d")
basicFile = os.path.join(config.listsRootPath, 'stockBasic.json')
basicDate = readFile(basicFile)
scanFile = os.path.join(config.configRootPath, 'scanData.json')
scanConfigDate = readFile(scanFile)

threads = []

if basicDate['errcode'] == 0:
    lists = basicDate['data']

    for k in lists:
        # baseCodeDir = os.path.join(config.dataRootDailyTotal, k)
        # if os.path.isdir(baseCodeDir):
        #     pass
        # else:
        #     os.mkdir(baseCodeDir)
        #

        code = k
        th = threading.Thread(target=getDailyData, args=(code,))
        threads.append(th)

    # 等待线程运行完毕
    for th in threads:
        th.setDaemon(True)
        th.start()

else:
    print basicDate['errmsg']

print "程序结束运行%s" % datetime.datetime.now()