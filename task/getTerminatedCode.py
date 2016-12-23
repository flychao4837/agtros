#!/usr/bin/python
# coding=UTF-8
import os
import tushare as ts
import config as config
from writeJsonFile import writeFile

##获取终止上市股票列表
    # code：股票代码
    # name：股票名称
    # oDate:上市日期
    # tDate:终止上市日期
def getTerminated():
    jsonFile = os.path.join(config.listsRootPath, "stockTerminated.json")
    data = ts.get_terminated()
    writeFile(jsonFile, data, 'records', False)

###获取被暂停上市的股票列表，数据从上交所获取，目前只有在上海证券交易所交易被终止的股票。
    # code：股票代码
    # name：股票名称
    # oDate:上市日期
    # tDate:暂停上市日期
def getSuspended():
    jsonFile = os.path.join(config.listsRootPath, "stockSuspended.json")
    data = ts.get_suspended()
    writeFile(jsonFile, data, 'records', False)


if __name__ == '__main__':
    getTerminated()
    getSuspended()