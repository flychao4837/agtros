#!/usr/bin/python
# coding=UTF-8
import tushare as ts
import time as time
import datetime as datetime
import pandas as pd
import os as os
import config as config

def getAllStockList():
    data = ts.get_industry_classified()
    #h5 = pd.HDFStore(config.dataRootPath+'\stock_list_all.h5', 'w')
    #h5['data'] = data
    #h5.close()

    #datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    dateStr = datetime.datetime.now().strftime("%Y-%m-%d")
    jsonp = data.to_json()
    jsonFile = config.dataRootPath+'\\'+dateStr+'.json'

    if os.path.isfile(jsonFile):
        fp = open(jsonFile, 'w')
        fp.write(jsonp)
        fp.close()
    else:
        fp = open(jsonFile, 'w')
        fp.write(jsonp)
        fp.close()

    print jsonFile

getAllStockList()