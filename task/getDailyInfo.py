#!/usr/bin/python
# coding=UTF-8
##获取日内详情

import tushare as ts
import datetime as datetime
import pandas as pd
import os as os
import config as config
from readJsonFile import readFile
from writeJsonFile import writeFile

fileName = config.configRootPath+'\scanData.json'
dateStr = datetime.datetime.now().strftime("%Y-%m-%d")
jsonFile = config.dataRootPath + '\\' + dateStr + '.json'

scanData = readFile(fileName)
jsonData = readFile(jsonFile)

def getDailyData(stock="",date=""):

    if  bool(stock) == False:
        return{'errcode':-1,'msg':'need stockCode'}

    if bool(date) == False & bool(stock) :
        #不带日期的话就检索今天的数据
        data = ts.get_today_ticks( stock )
        jsonFile = config.dataRootPath + "\\" + stock + "\\" + dateStr + ".json"
        data.to_json(jsonFile, orient='records')
    elif bool(date) & bool(stock) :
        #按日期获取
        pass


# if scanData['errcode'] ==0:
#     lastScanDate = scanData['lastScanDate']
#     lastStockDailyDate = scanData['lastStockDailyDate']
#     lastScanStock = scanData['lastScanStock']
#     task = scanData['task']
#     date = scanData['date']
#     if date == dateStr:
#         getDailyData(lastScanStock)
#
# else:
#     date = {
#         "date": dateStr,
#         "total":2841,
#         "lastScanDate": dateStr,
#         "lastScanStock":"",
#         "lastStockDailyDate":"",
#         "task":"scantotal" ,
#     }
#
#     writeFile(fileName,date)

#getDailyData("600226")