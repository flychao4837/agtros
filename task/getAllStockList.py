#!/usr/bin/python
# coding=UTF-8
import tushare as ts
import time as time
import datetime as datetime
import pandas as pd
import os as os
import config as config

def getAllStockList():
    ##获取所有列表 （代码、名称、行业）
    data = ts.get_industry_classified()

    ##获取历史数据
    #data= ts.get_tick_data('600848', date='2014-01-09')

    ##获取当日交易数据
    #data = ts.get_today_ticks('601333')
    #h5 = pd.HDFStore(config.dataRootPath+'\stock_list_all.h5', 'w')
    #h5['data'] = data
    #h5.close()

    ##获取格式化的日期字符串
    #datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    dateStr = datetime.datetime.now().strftime("%Y-%m-%d")
    jsonFile = config.dataRootPath + '\\' + dateStr + '.json'

    ## to_json 参数配置 在tushare中 （file,datatype）,datatype可用的格式
    #split dict like {index -> [index], columns -> [columns], data -> [values]}
    #records list like[{column -> value}, ..., {column -> value}]
    #index dict like {index -> {column -> value}}
    #columns dict like {column -> {index -> value}}
    # values just the values array

    ##写json文件方式一
    jsonp = data.to_json( jsonFile ,orient='records')

    ##写json文件方式二
    #jsonp = data.to_json(）
    # if os.path.isfile(jsonFile):
    #     fp = open(jsonFile, 'w')
    #     fp.write(jsonp)
    #     fp.close()
    # else:
    #     fp = open(jsonFile, 'w')
    #     fp.write(jsonp)
    #     fp.close()

    print jsonFile

getAllStockList()