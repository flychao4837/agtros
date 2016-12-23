#!/usr/bin/python
# coding=UTF-8
import os
import tushare as ts
import config as config
from writeJsonFile import writeFile

##获取上海银行间拆借利率，反映当前一段时间内资金的紧张程度
    # Shibor拆放利率
    # 银行报价数据
    # Shibor均值数据
    # 贷款基础利率（LPR）
    # LPR均值数据

#获取银行间同业拆放利率数据，目前只提供2006年以来的数据。
    # date:日期
    # ON:隔夜拆放利率
    # 1W:1周拆放利率
    # 2W:2周拆放利率
    # 1M:1个月拆放利率
    # 3M:3个月拆放利率
    # 6M:6个月拆放利率
    # 9M:9个月拆放利率
    # 1Y:1年拆放利率

def shibor(year=""):
    jsonFile = os.path.join(config.listsRootPath, "shibor.json")
    data = ts.shibor_data()  # 默认取当前年份的数据
    if str(type(data)) =="<class 'pandas.core.frame.DataFrame'>":
        data.sort('date', ascending=False)
        writeFile(jsonFile, data, 'records', False)



#获取银行间报价数据，目前只提供2006年以来的数据。
    # date:日期
    # bank:报价银行名称
    # ON:隔夜拆放利率
    # ON_B:隔夜拆放买入价
    # ON_A:隔夜拆放卖出价
    # 1W_B:1周买入
    # 1W_A:1周卖出
    # 2W_B:买入
    # 2W_A:卖出
    # 1M_B:买入
    # 1M_A:卖出
    # 3M_B:买入
    # 3M_A:卖出
    # 6M_B:买入
    # 6M_A:卖出
    # 9M_B:买入
    # 9M_A:卖出
    # 1Y_B:买入
    # 1Y_A:卖出
def shibor_quote_data(year=""):
    jsonFile = os.path.join(config.listsRootPath, "shibor_quote_data.json")
    data = ts.lpr_data()
    if str(type(data)) == "<class 'pandas.core.frame.DataFrame'>":
        data.sort('date', ascending=False)
        writeFile(jsonFile, data, 'records', False)

# 获取Shibor均值数据，目前只提供2006年以来的数据。
    # date:日期
    # 其它分别为各周期5、10、20均价，请参考上面的周期含义
def shibor_ma_data(year=""):
    jsonFile = os.path.join(config.listsRootPath, "shibor_ma_data.json")
    data = ts.shibor_ma_data()
    if str(type(data)) == "<class 'pandas.core.frame.DataFrame'>":
        data.sort('date', ascending=False)
        writeFile(jsonFile, data, 'records', False)

# 获取贷款基础利率（LPR）数据，目前只提供2013年以来的数据。
    # date:日期
    # 1Y:1年贷款基础利率
def lpr_data(year=""):
    jsonFile = os.path.join(config.listsRootPath, "lpr_data.json")
    data = ts.shibor_ma_data()
    if str(type(data)) == "<class 'pandas.core.frame.DataFrame'>":
        data.sort('date', ascending=False)
        writeFile(jsonFile, data, 'records', False)

# 获取贷款基础利率均值数据，目前只提供2013年以来的数据。
    # date:日期
    # 1Y_5:5日均值
    # 1Y_10:10日均值
    # 1Y_20:20日均值
def lpr_ma_data(year=""):
    jsonFile = os.path.join(config.listsRootPath, "lpr_ma_data.json")
    data = ts.shibor_ma_data()
    if str(type(data)) == "<class 'pandas.core.frame.DataFrame'>":
        data.sort('date', ascending=False)
        writeFile(jsonFile, data, 'records', False)


if __name__ == '__main__':
    shibor()
    shibor_quote_data()
    shibor_ma_data()
    lpr_data()
    lpr_ma_data()