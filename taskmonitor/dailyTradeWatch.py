#!/usr/bin/python
# coding=UTF-8

#监视列表中的股票价格波动和波动幅度，及时提醒

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import os
import win32api, win32con
import tushare as ts
import config
from readJsonFile import readFile
from getTradeDay import isTradeDay
from datetime import date, time, datetime, timedelta

global _G_STATUS  ##全文状态
_G_STATUS = True
today = datetime.now().strftime("%Y-%m-%d")
##获取格式化的日期字符串
jsonFile = os.path.join(config.moniterPath, 'dailyTradeWatch.json')

##获取实时分笔
def getRealTimeQuotes(data=None):
    global _G_STATUS
    if data is not None:
        stock = data["code"]
        warnprice = data["price"]
        warnrate = data["rate"]
        df = ts.get_realtime_quotes(stock)
        compute(df, stock, warnprice, warnrate)
    else:
        _G_STATUS = False
        win32api.MessageBox(0, u"数据获取错误", u"警告", win32con.MB_IConERROR)

###计算
def compute(data, stock, price, rate ) :
    ##  name    open  pre_close   price    high     low     bid     ask
    L = data.head(1)

    diff = round((float(L["bid"]) - float(L["pre_close"]))/float(L["pre_close"])*100,2)
    name = L["name"][0]
    outstr = "{} open：{} ,报价：{} ,幅度：{}".format(str(name), float(L["pre_close"]), float(L["bid"]), diff)
    print outstr
    ask = float(L["ask"][0])
    if ask < price:
        ###下跌到目标价位
        warnText = u"{} 达到目标价位{} ,现价{}".format(stock, price, ask)
        win32api.MessageBox(0, warnText, u"消息提醒", win32con.MB_OK)
    elif diff <=rate:
        ##下跌幅度达到，包括跌停
        warnText = u"{} 跌幅达到 {} 超过{}".format(stock, diff, rate)
        win32api.MessageBox(0, warnText, u"消息提醒", win32con.MB_OK)
    else:
        pass

def main():
    global _G_STATUS
    watchData = readFile(jsonFile)
    if watchData["errcode"] ==0:
        data = watchData["data"]
        ##如果当天不在任务时间内，提示改扫描时间
        if isTradeDay(today):
            if today < data["start"]:
                print u"还未到预警时间"
                _G_STATUS = False
                win32api.MessageBox(0, u"还未到预警时间", u"消息提醒", win32con.MB_OK)
            elif today > data["end"]:
                print u"预警时间已结束"
                _G_STATUS = False
                win32api.MessageBox(0, u"预警时间已结束", u"消息提醒", win32con.MB_OK)
            else:
                #TODO 扫描
                for k in data["list"]:
                    getRealTimeQuotes(k)
                #print "在预警期内"
        else:
            _G_STATUS = False
            pass
    else:
        win32api.MessageBox(0, u"任务Json文件读取错误", u"消息提醒", win32con.MB_OK)

def runTask(func, day=0, hour=0, min=0, second=0):
    global _G_STATUS
    now = datetime.now()
    strnow = now.strftime('%Y-%m-%d %H:%M:%S')
    print "now:",strnow
    # First next run time
    period = timedelta(days=day, hours=hour, minutes=min, seconds=second)
    next_time = now + period
    strnext_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
    while _G_STATUS:
        # Get system current time
        iter_now = datetime.now()
        iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
        if str(iter_now_time) >= str(strnext_time):
            # Call task func
            func()
            # Get next iteration time
            iter_time = iter_now + period
            strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
            print "next_iter: %s" % strnext_time
            continue
    else:
        exit()

if __name__ == '__main__':
    runTask(main, day=0, hour=0, min=0, second=10)