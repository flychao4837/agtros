#!/usr/bin/python
# coding=UTF-8

#获取前十大股东、十大流通股东、十大机构持股名单

import tushare as ts
import datetime as datetime
import config as config
from readJsonFile import readFile
from getDailyInfo import getDailyData
from writeJsonFile import writeFile
from getTradeDay import get_week_day

