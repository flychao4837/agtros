#!/usr/bin/python
# coding=UTF-8
import datetime as datetime
import os as os
import tushare as ts
import config as config
from readJsonFile import readFile
from getDailyInfo import getDailyData

def getAllStockList():
    ##获取所有列表 （代码、名称、行业） code不全
    data = ts.get_industry_classified()

    ##获取格式化的日期字符串
    dateStr = datetime.datetime.now().strftime("%Y-%m-%d")
    jsonFile = config.listsRootPath + '\\' + dateStr + '.json'

            ## to_json 参数配置 在tushare中 （file,datatype）,datatype可用的格式
            #split dict like {index -> [index], columns -> [columns], data -> [values]}
            #records list like[{column -> value}, ..., {column -> value}]
            #index dict like {index -> {column -> value}}
            #columns dict like {column -> {index -> value}}
            # values just the values array

            # to_json  , force_ascii 设置中文ascii编码 默认True 若直接看 设为False

    ##写json文件方式一
    #jsonp = data.to_json(jsonFile, orient='records', force_ascii =False)

    data.to_json( jsonFile ,orient='records', force_ascii =False)

    ##写json文件方式二
    #jsonp = data.to_json(）
    # if os.path.isfile(jsonFile):
    #     fp = open(jsonFile, 'w')
    #     fp.write(jsonp)
    #     fp.close()
    # else:
    #     fp = open(jsonFile, 'w')
    #     fp.write(jsonp)
    #     fp.close()

    #遍历数据，创建code对应的文件夹
    #readFile 是从 readJsonFile 引进来的方法 但是 readJsonFile 不是molule不能直接引用
    # readJsonFile(jsonFile) 会报错
    tmpDate = readFile(jsonFile)

    if tmpDate['errcode']==0 :
        list = tmpDate['data']
        for listitem in list:

            #print listitem
            baseCodeDir=""
            if bool(listitem['code']):
                baseCodeDir = config.dataRootDailyTrade
                baseCodeDir = baseCodeDir+"\\"+listitem['code']
                if listitem['code'][0] == "2" or listitem['code'][0] == "9":
                    pass
                else:
                    if os.path.isdir(baseCodeDir):
                        pass
                    else:
                        os.mkdir(baseCodeDir)
                        #print baseCodeDir

                    ##单个扫描方式
                    #getDailyData(listitem['code'])

                    getDailyData(listitem['code'],'2016-11-30')
                    ##用并发操作去扫描，单个扫描太慢
            else:
                print 'error code'
    else: #读取文件出错
        print tmpDate['errmsg']


if __name__ == '__main__':
    getAllStockList()