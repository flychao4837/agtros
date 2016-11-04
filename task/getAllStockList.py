#!/usr/bin/python
# coding=UTF-8
import tushare as ts
import time as time
import datetime as datetime
import pandas as pd

def getAllStockList():
    data = ts.get_industry_classified()
    h5 = pd.HDFStore('./data/stock_list_all.h5', 'w')
    h5['data'] = data
    h5.close()

getAllStockList()