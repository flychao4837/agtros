#!/usr/bin/python
# coding=UTF-8
import datetime as datetime
import tushare as ts
import config as config
from readJsonFile import readFile
from getDailyInfo import getDailyData

##指定一个开始日期 扫描从这个日期到今天的所有日内交易详情
##扫描basicjson中的全部股票代码

endDate = datetime.datetime.now().strftime("%Y-%m-%d") #以当天为截止日期
today = datetime.datetime.now().strftime("%Y-%m-%d") #默认当天时间
basicFile = config.listsRootPath + '\\stockBasic.json'
basicDate = readFile(basicFile)  # timeToMarket 上市日期
scanFile = config.configRootPath+'\\scanData.json'
scanConfigDate = readFile(scanFile)

def getSingleStock(stock = "" ,datestr = today):
    if bool(datestr) and len(datestr) == 10 and bool(stock):
        # str格式的时间转成datetime，便于时间操作、比较
        startTime = datetime.datetime.strptime(datestr, "%Y-%m-%d").date()
        endTime = datetime.datetime.strptime(today, "%Y-%m-%d").date()

        if(startTime < endTime):
            ##获取间隔天数，遍历这些日期
            totalDays = (endTime - startTime).days
            for num in range(0, totalDays+1):
                addDate = startTime + datetime.timedelta(days=num)
                scanDate = addDate.strftime("%Y-%m-%d")
                getDailyData(stock=stock, date=scanDate)
        else:
            pass
    else:
        print "参数不能为空"

###循环code
def getSingleStockSomeTimeDate(datestr = today):
    if basicDate['errcode'] == 0:
        lists = basicDate['data']
        for k in lists:
            if bool(k):
                getSingleStock(k, datestr)
            else:
                print '股票代码获取错误'
    else:
        #读取文件出错
        print basicDate['errmsg']

if __name__ == '__main__':
    getSingleStockSomeTimeDate("2017-03-03")
