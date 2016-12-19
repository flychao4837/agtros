#!/usr/bin/python
# coding=UTF-8
import datetime as datetime
import os as os
import tushare as ts
import config as config
from readJsonFile import readFile
from getDailyInfo import getDailyData


today = datetime.datetime.now().strftime("%Y-%m-%d")
def getAllStockList(date=today):
    ##获取所有列表 （代码、名称、行业） code不全
    data = ts.get_industry_classified()

    ##获取格式化的日期字符串
    dateStr = datetime.datetime.now().strftime("%Y-%m-%d")
    jsonFile = os.path.join(config.listsRootPath, dateStr + '.json')
    data.to_json(jsonFile, orient='records', force_ascii=False)

    #遍历数据，创建code对应的文件夹
    tmpDate = readFile(jsonFile)

    if tmpDate['errcode']==0 :
        list = tmpDate['data']
        for listitem in list:

            if bool(listitem['code']):
                baseCodeDir = os.path.join(config.dataRootDailyTrade, listitem['code'])
                if listitem['code'][0] == "2" or listitem['code'][0] == "9":
                    pass
                else:
                    if os.path.isdir(baseCodeDir):
                        pass
                    else:
                        os.mkdir(baseCodeDir)

                    getDailyData(listitem['code'], date)
            else:
                print 'error code'
    else:
        #读取文件出错
        print tmpDate['errmsg']

if __name__ == '__main__':
    getAllStockList()