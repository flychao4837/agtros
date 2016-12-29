#!/usr/bin/python
# coding=UTF-8
import datetime as datetime
import os as os
import tushare as ts
import config as config
from readJsonFile import readFile
from getDailyInfo import getDailyData

today = datetime.datetime.now().strftime("%Y-%m-%d")
##获取格式化的日期字符串
jsonFile = os.path.join(config.listsRootPath, 'stockBasic.json')
# 遍历数据，创建code对应的文件夹
basicDate = readFile(jsonFile)
def getAllStockList(date=today):

    if basicDate['errcode']==0 :
        lists = basicDate['data']
        for k in lists:
            if bool(k):
                getDailyData(k, date)
            else:
                print 'error code'
    else:
        #读取文件出错
        print basicDate['errmsg']

if __name__ == '__main__':
    getAllStockList("2016-12-29")