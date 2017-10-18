#!/usr/bin/python
# coding=UTF-8
##获取指定股票在指定日期内的交易详情

import tushare as ts
import datetime as datetime
import os as os
import config as config
from readJsonFile import readFile
from writeJsonFile import writeFile
from getTradeDay import isTradeDay
import sys

dateStr = datetime.datetime.now().strftime("%Y-%m-%d")
scanFile = config.configRootPath+'\\scanErrorRecord.json'
scanConfigDate = readFile(scanFile)

def getDailyData(stock="", date=""):
    if stock[0] == "2" or stock[0] == "9":
        print "Pass Stock"
        return True
    else:
        if  bool(stock) == False:
            return{'errcode':-1,'errmsg':'need stockCode'}
        else:
            jsonDir = os.path.join(config.dataRootDailyTrade, stock)
            if os.path.isdir(jsonDir):
                pass
            else:
                os.mkdir(jsonDir)


        if bool(date) == False & bool(stock):
            #不带日期的话就检索今天的数据
            jsonFile = os.path.join(config.dataRootDailyTrade, stock, dateStr + ".json")
            if os.path.isfile(jsonFile):
                size = os.path.getsize(jsonFile)
                #print 'There are %f K' % (size / 1024.0)

                if size >60000 :
                    print(stock+" Pass")
                    return True
                else:
                    try:
                        data = ts.get_today_ticks(stock)
                        data.to_json(jsonFile, orient='records', force_ascii =False)
                        print(stock)
                        print(date)
                        return True
                    except:
                        print("scan error " + stock )
            else:
                try:
                    data = ts.get_today_ticks(stock)
                    data.to_json(jsonFile, orient='records', force_ascii =False)

                    return True
                except:
                    print("scan error " + stock)

        elif bool(date) & bool(stock):
            #按日期获取
            isWorkDay = isTradeDay(date)
            if isWorkDay:
                jsonFile = os.path.join(config.dataRootDailyTrade, stock, date + ".json")

                ### 判断该日期下的文件是否大于100KB 是默认历史数据已获取，反正重新获取
                if os.path.isfile(jsonFile):
                    size = os.path.getsize(jsonFile)
                    #print 'There are %f K' % (size / 1024.0)

                    if size >60000 :
                        print(stock+" Pass")
                        return True
                    else:
                        try:
                            data = ts.get_tick_data(stock, date=date)
                            data.to_json(jsonFile, orient='records', force_ascii =False)
                            print(stock)
                            print(date)
                            return True
                        except:
                            print("scan error " + stock + "--" + date)
                            catchError(stock, date)
                else:
                    try:
                        data = ts.get_tick_data(stock, date=date)
                        data.to_json(jsonFile, orient='records', force_ascii =False)
                        print(stock)
                        print(date)
                        return True
                    except:
                        print("scan error "+stock +"--"+date)
                        catchError(stock, date)
            else:
                print ("Weekend Pass")
                pass

##捕获错误，记录位置，保存到scanData.json，从错误点重新开始
def catchError (code,date):
    scanData = scanConfigDate['data']
    scanData['lastScanStock'] = code
    scanData['lastScanDate'] = date
    scanData['currDate'] = dateStr
    writeFile(scanFile, scanData, 'records', False)
    sys.exit()

if __name__ == '__main__':
    getDailyData("002732", "2016-05-04")


##获取当日交易数据
#data = ts.get_today_ticks('601333')
#h5 = pd.HDFStore(config.dataRootPath+'\stock_list_all.h5', 'w')
#h5['data'] = data
#h5.close()
