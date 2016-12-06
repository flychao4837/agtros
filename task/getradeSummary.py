#!/usr/bin/python
# coding=UTF-8
#获取每日开盘、收盘汇总信息，便于汇总5日、10日线，分析各种指标
import tushare as ts
import datetime as datetime
import config as config
from readJsonFile import readFile
from getDailyInfo import getDailyData
from writeJsonFile import writeFile
from getTradeDay import get_week_day


endDate = datetime.datetime.now().strftime("%Y-%m-%d") #以当天为截止日期
basicFile = config.listsRootPath + '\\stockBasic.json'
basicDate = readFile(basicFile)  # timeToMarket 上市日期
scanFile = config.configRootPath+'\\scanData.json'
scanConfigDate = readFile(scanFile)

def getTradeStock(stock=""):
    if bool(stock) == False:
        #没有参数时，遍历asicB.json取所有的股票交易汇总
        if basicDate['errcode'] == 0:
            lists = basicDate['data']
            name = lists['name']
            if bool(name):
                for k in name:
                    print k
                    getTradeSummary(k)
            else:
                return {'errcode': -10000, 'errmsg': "没找到对应code代码", 'data': ''}
        else:
            print basicDate['errcode']
    else:
        #带有股票参数，就只扫描一只
        getTradeSummary(stock)


def getTradeSummary(stock=""):
    if bool(stock):
        jsonFile = config.dataRootDailyTotal + "\\" + stock + ".json"
        data = ts.get_hist_data(stock)
        data.to_json(jsonFile, orient='index', force_ascii=False)
    else:
        return {'errcode': -1, 'errmsg': 'need stockCode'}



if __name__ == '__main__':
    getTradeStock()