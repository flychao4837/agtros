#!/usr/bin/python
# coding=UTF-8
##获取日内详情

import tushare as ts
import datetime as datetime
import os as os
import config as config
from readJsonFile import readFile
from writeJsonFile import writeFile
from getTradeDay import get_week_day
fileName = config.configRootPath+'\scanData.json'
dateStr = datetime.datetime.now().strftime("%Y-%m-%d")

#scanData = readFile(fileName)


def getDailyData(stock="", date=""):
    if stock[0] == "2" or stock[0] == "9":
        print "Pass Stock"
        return True
    else:
        if  bool(stock) == False:
            return{'errcode':-1,'msg':'need stockCode'}

        if bool(date) == False & bool(stock):
            #不带日期的话就检索今天的数据
            jsonFile = config.dataRootDailyTrade + "\\" + stock + "\\" + dateStr + ".json"
            if os.path.isfile(jsonFile):
                size = os.path.getsize(jsonFile)
                #print 'There are %f K' % (size / 1024.0)

                if size >30000 :
                    print(stock+" Pass")
                    return True
                else:
                    data = ts.get_today_ticks(stock)
                    data.to_json(jsonFile, orient='records', force_ascii =False)
                    print(stock)
                    print(date)
                    return True
            else:
                data = ts.get_today_ticks(stock)
                data.to_json(jsonFile, orient='records', force_ascii =False)
                print(stock)
                print(date)
                return True

        elif bool(date) & bool(stock):
            #按日期获取
            isWorkDay = get_week_day(date)
            if isWorkDay:
                jsonFile = config.dataRootDailyTrade + "\\" + stock + "\\" + date + ".json"

                ### 判断该日期下的文件是否大于100KB 是默认历史数据已获取，反正重新获取
                if os.path.isfile(jsonFile):
                    size = os.path.getsize(jsonFile)
                    #print 'There are %f K' % (size / 1024.0)

                    if size >20000 :
                        print(stock+" Pass")
                        return True
                    else:
                        data = ts.get_tick_data(stock, date=date)
                        data.to_json(jsonFile, orient='records', force_ascii =False)
                        print(stock)
                        print(date)
                        return True
                else:
                    data = ts.get_tick_data(stock, date=date)
                    data.to_json(jsonFile, orient='records', force_ascii =False)
                    print(stock)
                    print(date)
                    return True
            else:
                print ("Weekend Pass")

#getDailyData("002732")


##获取当日交易数据
#data = ts.get_today_ticks('601333')
#h5 = pd.HDFStore(config.dataRootPath+'\stock_list_all.h5', 'w')
#h5['data'] = data
#h5.close()
