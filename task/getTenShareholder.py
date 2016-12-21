#!/usr/bin/python
# coding=UTF-8

#获取前十大股东、十大流通股东、十大机构持股名单

import tushare as ts
import datetime as datetime
import config as config
from readJsonFile import readFile
from getDailyInfo import getDailyData
from writeJsonFile import writeFile
from getTradeDay import isTradeDay

endDate = datetime.datetime.now().strftime("%Y-%m-%d") #以当天为截止日期
basicFile = os.path.join(config.listsRootPath, 'stockBasic.json')
basicDate = readFile(basicFile)  # timeToMarket 上市日期
scanFile = os.path.join(config.configRootPath, 'scanData.json')
scanConfigDate = readFile(scanFile)

## 十大股东



### 十大流通股东