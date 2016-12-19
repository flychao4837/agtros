#!/usr/bin/python
# coding=UTF-8
#获取每日开盘、收盘汇总信息，便于汇总5日、10日线，分析各种指标
import os
import types
import tushare as ts
import datetime as datetime
import config as config
from readJsonFile import readFile
from getDailyInfo import getDailyData
from writeJsonFile import writeFile
from getTradeDay import get_week_day


endDate = datetime.datetime.now().strftime("%Y-%m-%d") #以当天为截止日期
basicFile = os.path.join(config.listsRootPath, 'stockBasic.json')
basicDate = readFile(basicFile)  # timeToMarket 上市日期
scanFile = os.path.join(config.configRootPath, 'scanData.json')
scanConfigDate = readFile(scanFile)

def getTradeStock(stock=""):

    #没有参数时，遍历asicB.json取所有的股票交易汇总
    if basicDate['errcode'] == 0:
        lists = basicDate['data']
        if bool(lists):
            for k in lists:
                dateStr = str(lists[k]['timeToMarket'])
                startDate = dateStr[:4] + "-" + dateStr[4:6] + "-" + dateStr[6:]

                kdatedir = os.path.join(config.dataRootDailyTotal, k)
                if os.path.isdir(kdatedir):
                    pass
                else:
                    os.mkdir(kdatedir)
                print k
                if bool(stock) == False:
                    getTradeSummary(k, startDate, endDate)
                else:
                    #带有股票参数，就只扫描一只
                    if k ==stock:
                        getTradeSummary(stock, startDate, endDate)
                        break
        else:
            return {'errcode': -10000, 'errmsg': "没找到对应code代码", 'data': ''}
    else:
        print basicDate['errcode']



def getTradeSummary(stock="", start="", end=""):
    if bool(stock):
        print start
        print end
        jsonFile = os.path.join(config.dataRootDailyTotal, stock, "daySummary.json")
        data = ts.get_hist_data(stock, start=start, end=end)
        if str(type(data)) =="<class 'pandas.core.frame.DataFrame'>":
            data.to_json(jsonFile, orient='index', force_ascii=False)
        else:
            print stock+" is Not DataFrame"
            pass
        # ts.get_hist_data('600848', ktype='W')  # 获取周k线数据
        jsonFile = os.path.join(config.dataRootDailyTotal, stock, "weekSummary.json")
        data = ts.get_hist_data(stock, start=start, end=end, ktype='W')
        if str(type(data)) == "<class 'pandas.core.frame.DataFrame'>":
            data.to_json(jsonFile, orient='index', force_ascii=False)
        else:
            print stock + " is Not DataFrame"
            pass
        # ts.get_hist_data('600848', ktype='M')  # 获取月k线数据
        jsonFile = os.path.join(config.dataRootDailyTotal, stock, "monthSummary.json")
        data = ts.get_hist_data(stock, start=start, end=end, ktype='M')
        if str(type(data)) == "<class 'pandas.core.frame.DataFrame'>":
            data.to_json(jsonFile, orient='index', force_ascii=False)
        else:
            print stock + " is Not DataFrame"
            pass
        # ts.get_hist_data('600848', ktype='5')  # 获取5分钟k线数据
        jsonFile = os.path.join(config.dataRootDailyTotal, stock, "5minSummary.json")
        data = ts.get_hist_data(stock, start=start, end=end, ktype='5')
        if str(type(data)) == "<class 'pandas.core.frame.DataFrame'>":
            data.to_json(jsonFile, orient='index', force_ascii=False)
        else:
            print stock + " is Not DataFrame"
            pass
        # ts.get_hist_data('600848', ktype='15')  # 获取15分钟k线数据
        jsonFile = os.path.join(config.dataRootDailyTotal, stock, "15minSummary.json")
        data = ts.get_hist_data(stock, start=start, end=end, ktype='15')
        if str(type(data)) == "<class 'pandas.core.frame.DataFrame'>":
            data.to_json(jsonFile, orient='index', force_ascii=False)
        else:
            print stock + " is Not DataFrame"
            pass
        # ts.get_hist_data('600848', ktype='30')  # 获取30分钟k线数据
        jsonFile = os.path.join(config.dataRootDailyTotal, stock, "30minSummary.json")
        data = ts.get_hist_data(stock, start=start, end=end, ktype='30')
        if str(type(data)) == "<class 'pandas.core.frame.DataFrame'>":
            data.to_json(jsonFile, orient='index', force_ascii=False)
        else:
            print stock + " is Not DataFrame"
            pass
        # ts.get_hist_data('600848', ktype='60')  # 获取60分钟k线数据
        jsonFile = os.path.join(config.dataRootDailyTotal, stock, "60minSummary.json")
        data = ts.get_hist_data(stock, start=start, end=end, ktype='60')
        if str(type(data)) == "<class 'pandas.core.frame.DataFrame'>":
            data.to_json(jsonFile, orient='index', force_ascii=False)
        else:
            print stock + " is Not DataFrame"
            pass

    else:
        return {'errcode': -1, 'errmsg': 'need stockCode'}

if __name__ == '__main__':
    getTradeStock("000099")