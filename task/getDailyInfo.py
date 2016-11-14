#!/usr/bin/python
# coding=UTF-8
##获取日内详情

import tushare as ts
import time as time
import datetime as datetime
import pandas as pd
import os as os
import config as config
import readJsonFile
import writeJsonFile

fileName = config.configRootPath+'\scanData.json'
dateStr = datetime.datetime.now().strftime("%Y-%m-%d")
scanData = readJsonFile(fileName)



def getDailyData(stock="",date=""):

    if stock=="":
        return{'errcode':-1,'msg':'need stockCode'}

    if date == "" & stock != "":

        data = ts.get_today_ticks('601333')
        jsonFile = config.dataRootPath + "\\" + stock + "\\" + dateStr + ".json"
        data.to_json(jsonFile, orient='records')
    elif date!="" & stock!="":
        pass


if scanData.errcode =='0':
    lastScanDate = scanData['lastScanDate']
    lastStockDailyDate = scanData['lastStockDailyDate']
    lastScanStock = scanData['lastScanStock']
    task = scanData['task']
    date = scanData['date']
    if date == dateStr:
        getDailyData(lastScanStock)

else:
    date = {
        "date": dateStr,
        "total":2841,
        "lastScanDate": dateStr,
        "lastScanStock":"",
        "lastStockDailyDate":"",
        "task":"scantotal" ,
    }

    writeJsonFile(fileName,date)

