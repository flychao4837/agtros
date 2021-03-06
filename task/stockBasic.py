#!/usr/bin/python
# coding=UTF-8
    ##获取股票基本数据
    #code,代码
    # name,名称
    # industry,所属行业
    # area,地区
    # pe,市盈率
    # outstanding,流通股本(亿)
    # totals,总股本(亿)
    # totalAssets,总资产(万)
    # liquidAssets,流动资产
    # fixedAssets,固定资产
    # reserved,公积金
    # reservedPerShare,每股公积金
    # esp,每股收益
    # bvps,每股净资
    # pb,市净率
    # timeToMarket,上市日期
    # undp,未分利润
    # perundp, 每股未分配
    # rev,收入同比(%)
    # profit,利润同比(%)
    # gpr,毛利率(%)
    # npr,净利润率(%)
    # holders,股东人数

import os
import config as config
import tushare as ts
from writeJsonFile import writeFile

def stockBasics():
    jsonFile = os.path.join(config.listsRootPath, "stockBasic.json")
    data = ts.get_stock_basics()
    data.to_json(jsonFile, orient='index', force_ascii =False)

if __name__ == '__main__':
    stockBasics()