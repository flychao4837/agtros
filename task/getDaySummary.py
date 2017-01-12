#!/usr/bin/python
# coding=UTF-8

#获取每日交易收盘汇总数据
import os
import tushare as ts
import datetime as datetime
import config as config
from readJsonFile import readFile
from writeJsonFile import writeFile

basicFile = os.path.join(config.listsRootPath, 'stockBasic.json')
basicDate = readFile(basicFile)
today = datetime.datetime.now().strftime("%Y-%m-%d")

##获取三年的历史行情
def getHistData(stock=None):
    if stock is None:
        print "代码为空"
        return {'errcode': -1, 'errmsg': "代码为空", 'data': ''}
    else:
        jsonDir = os.path.join(config.dataRootDailyTotal, stock)
        if os.path.isdir(jsonDir):
            pass
        else:
            os.mkdir(jsonDir)

        filename = os.path.join(config.dataRootDailyTotal, stock, "histroySummary3Y.json")
        data = ts.get_hist_data(stock)
        writeFile(filename, data, 'index', False)
        print stock
        #data.to_json(filename, orient='records', force_ascii=False)


##获取全部历史数据 需加开始时间和结束时间，最多获取三年的时间段，需手动拼接数据
#get_h_data()
def getHData(stock=None):
    if stock is None:
        print "代码为空"
        return {'errcode': -1, 'errmsg': "代码为空", 'data': ''}
    else:
        jsonDir = os.path.join(config.dataRootDailyTotal, stock)
        if os.path.isdir(jsonDir):
            pass
        else:
            os.mkdir(jsonDir)

        df = ts.get_stock_basics()
        datestr = str(df.ix[stock]['timeToMarket'])  # 上市日期YYYYMMDD
        datelen = len(datestr)
        timeToMarket = datestr[:4] + "-" + datestr[4:6] + "-" + datestr[6:]
        print timeToMarket

        filename = os.path.join(config.dataRootDailyTotal, stock, "histroySummaryAllParts.json")
        data = ts.get_h_data(stock, start='2010-01-08', end='2012-01-06')
        writeFile(filename, data, 'index', False)

##get_today_all()
def getTodayAll():
    pass

def getCodeCircle():
    ##记录已扫描的股票，下次跳过这些
    if basicDate['errcode'] == 0:
        lists = basicDate['data']
        for k in lists:
            getHistData(k)

if __name__ == '__main__':
    getHData('600048')
    #getCodeCircle()