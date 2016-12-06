#!/usr/bin/python
# coding=UTF-8
import datetime as datetime
import os as os
import time as time
import tushare as ts
import config as config
from readJsonFile import readFile
from getDailyInfo import getDailyData
from writeJsonFile import writeFile
##获取单一票在发行期内的全部日交易数据

endDate = datetime.datetime.now().strftime("%Y-%m-%d") #以当天为截止日期
basicFile = config.listsRootPath + '\\stockBasic.json'
basicDate = readFile(basicFile)  # timeToMarket 上市日期
scanFile = config.configRootPath+'\\scanData.json'
scanConfigDate = readFile(scanFile)

def getSingleStockDate(stock=""):
    if bool(stock):
        ##获取基本数据
        if basicDate['errcode']==0:
            lists = basicDate['data']
            name = lists['name']
            timeToMarket = lists['timeToMarket']
            if  bool(name) and bool(timeToMarket):
                for k in name:
                    if k ==stock:
                        startBasicDate = timeToMarket[k]
                        return str(startBasicDate)
                        break
                        #找到code就退出循环
            else:
                return {'errcode': -10000, 'errmsg': "没找到对应code代码", 'data': ''}
        else:
            print basicDate['errcode']
    else:
        return {'errcode': -10000, 'errmsg': "需要code参数", 'data': ''}



def getSingleStockDailyList(stock=""):

    dateStr = getSingleStockDate(stock)
    print dateStr
    if bool(dateStr) and len(dateStr) == 8:
        startDate = dateStr[:4] + "-" + dateStr[4:6] + "-" + dateStr[6:]
        # str格式的时间转成datetime，便于时间操作、比较
        startTime = datetime.datetime.strptime(startDate, "%Y-%m-%d").date()
        endTime = datetime.datetime.strptime(endDate, "%Y-%m-%d").date()
        if(startTime < endTime):

            addDate = startTime + datetime.timedelta(days=1)  # 逐天扫描
            scanDate = addDate.strftime("%Y-%m-%d")

            totalDays = (endTime -startTime).days

            ##获取间隔天数，遍历这些日期
            for num in range(0, totalDays+1):
                addDate = startTime + datetime.timedelta(days=num)
                scanDate = addDate.strftime("%Y-%m-%d")
                #print scanDate
                result = getDailyData(stock=stock, date=scanDate)
        else:
            pass

    else:
        print "获取的时间不对"


###循环code
def getCodeCircle():
    ##记录已扫描的股票，下次跳过这些
    if scanConfigDate['errcode'] == 0:
        scanData = scanConfigDate['data']
        scanData['date'] = endDate

    if basicDate['errcode'] == 0:
        lists = basicDate['data']
        name = lists['name']
        #D盘工程用于烧苗已添加的代码

        for k in name:
            try:
                isStockScan = scanData['lastScanStock'].index(k)
            except Exception, e:
                isStockScan = False

            if bool(isStockScan):
                getSingleStockDailyList(k)
            else:
                pass


#getSingleStockDailyList("000004") ##执行到那里

<<<<<<< HEAD
def asynDetect():
    counter = 1
    try:
        getCodeCircle()

    except Exception, ex:
        ###这里应该捕获 URIError，IOError
        counter +=1
        if counter <5:
            time.sleep(180)
            asynDetect()
        else:
            print "exit"
            exit(1)

#getSingleStockDailyList("000004") ##执行到那里
#getCodeCircle()

###捕捉错误，多由网络中断引起，延时后重复多次
asynDetect()

=======

if __name__ == '__main__':
    #getSingleStockDailyList("000002") ##执行到那里
    getCodeCircle()
>>>>>>> 15d72b7635683dcfc548676d102380f93f2775db
