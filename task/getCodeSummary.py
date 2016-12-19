#!/usr/bin/python
# coding=UTF-8
import datetime as datetime
import os as os
import config as config
from readJsonFile import readFile
from writeJsonFile import writeFile
from stockBasic import stockBasics
from industryClassified import stockIndustryClassified

## 列表code汇总、统计,主要是抓取的分类和列表code不全，有冗余差
## get_stock_basics()
## get_industry_classified()

##先把所有列表数据拉取到
def getCode(self):
    self.stockBasics()
    self.stockIndustryClassified()

##合并列表、并生成最终报表
def mergeCodeList():
    endDate = datetime.datetime.now().strftime("%Y-%m-%d")  # 以当天为截止日期
    basicFile = os.path.join(config.listsRootPath, 'stockBasic.json')
    basicDate = readFile(basicFile)  # timeToMarket 上市日期
    indusrtyFile = os.path.join(config.listsRootPath, 'stockIndustryClassified.json')
    indusrtyDate = readFile(indusrtyFile)
    if basicDate['errcode'] == 0 and indusrtyDate['errcode'] == 0 :
        mergeDate=dict();

    else:
        return {'errcode':-1, 'errmsg' : "stockBasic.json或stocIndustryClassified.json获取失败",}
