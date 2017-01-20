#!/usr/bin/python
# coding=UTF-8

#监视列表中的股票价格波动和波动幅度，及时提醒

import os
import win32api, win32con
import tushare as ts
import config
from readJsonFile import readFile
from getTradeDay import isTradeDay
from datetime import date, time, datetime, timedelta


today = datetime.now().strftime("%Y-%m-%d")
##获取格式化的日期字符串
jsonFile = os.path.join(config.moniterPath, 'dailyTradeWatch.json')

##获取实时分笔
def getRealTimeQuotes(data=None):
    if data is not None:
        stock = data["code"]
        warnprice = data["price"]
        warnrate = data["rate"]
        df = ts.get_realtime_quotes(stock)
        compute(df, stock, warnprice, warnrate)
    else:
        win32api.MessageBox(0, u"数据获取错误", u"警告", win32con.MB_IConERROR)

###计算
def compute(data, stock, price, rate ) :
    ##  name    open  pre_close   price    high     low     bid     ask
    L = data.head(1)
    print L
    diff = (float(L["bid"]) - float(L["pre_close"]))/float(L["pre_close"])*100
    print diff
    if float(L["ask"]) < price:
        print "达到目标位"
        win32api.MessageBox(0, stock+u"达到目标价位", u"消息提醒", win32con.MB_OK)
    elif diff <=rate:
        win32api.MessageBox(0, stock + u"跌幅达到"+rate, u"消息提醒", win32con.MB_OK)
    else:
        pass

def main():
    watchData = readFile(jsonFile)
    if watchData["errcode"] ==0:
        data = watchData["data"]
        ##如果当天不在任务时间内，提示改扫描时间
        if isTradeDay(today):
            if today < data["start"]:
                print u"还未到预警时间"

            elif today > data["end"]:
                print u"预警时间已结束"

            else:
                #TODO 扫描
                for k in data["list"]:
                    getRealTimeQuotes(k)
                #print "在预警期内"

    else:
        win32api.MessageBox(0, u"任务Json文件读取错误", u"消息提醒", win32con.MB_OK)

def runTask(func, day=0, hour=0, min=0, second=0):
  # Init time
  now = datetime.now()
  strnow = now.strftime('%Y-%m-%d %H:%M:%S')
  print "now:",strnow
  # First next run time
  period = timedelta(days=day, hours=hour, minutes=min, seconds=second)
  next_time = now + period
  strnext_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
  while True:
      # Get system current time
      iter_now = datetime.now()
      iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
      if str(iter_now_time) == str(strnext_time):
          # Call task func
          func()
          # Get next iteration time
          iter_time = iter_now + period
          strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
          print "next_iter: %s" % strnext_time
          # Continue next iteration
          continue

if __name__ == '__main__':
    runTask(main, day=0, hour=0, min=0, second=30)