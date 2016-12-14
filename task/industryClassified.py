#!/usr/bin/python
# coding=UTF-8

import config as config
import tushare as ts
from writeJsonFile import writeFile

##获取股票行业分类


def stockIndustryClassified():
    jsonFile = config.listsRootPath + "\\stockIndustryClassified.json"
    data = ts.get_industry_classified()
    data.to_json(jsonFile, orient='records', force_ascii =False)


if __name__ == '__main__':
    stockIndustryClassified()