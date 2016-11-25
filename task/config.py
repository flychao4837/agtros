#!/usr/bin/python
# coding=UTF-8

#系统配置，路径判断、目录生成
import os

#获取文件根路径、相对路径

curFileWorkPath = os.getcwd()
filePath = os.path.split( curFileWorkPath )
curRootPath =filePath[0]
configRootPath = curRootPath+'\config'
dataRootPath = curRootPath+'\data'
logRootPath = curRootPath+'\log'
htmlRootPath = curRootPath+'\html'
taskRootPath = curRootPath+'\task'
listsRootPath = curRootPath+'\lists'

dataRootDailyTotal = dataRootPath  +'\dailyTotal'
dataRootDailyTrade = dataRootPath  +'\dailyTrade'
dataRootDailyInfo = dataRootPath  +'\dailyInfo'
dataRootDailyNews = dataRootPath  +'\dailyNews'


#创建文件根目录
def creatRootDirectories():
    if os.path.isdir(configRootPath):
        pass
    else:
        os.mkdir(configRootPath)

    if os.path.isdir(dataRootPath):
        pass
    else:
        os.mkdir(dataRootPath)

    if os.path.isdir(logRootPath):
        pass
    else:
        os.mkdir(logRootPath)

    if os.path.isdir(htmlRootPath):
        pass
    else:
        os.mkdir(htmlRootPath)

    if os.path.isdir(listsRootPath):
        pass
    else:
        os.mkdir(listsRootPath)

    if os.path.isdir(dataRootDailyTrade):
        pass
    else:
        os.mkdir(dataRootDailyTrade)

    if os.path.isdir(dataRootDailyInfo):
        pass
    else:
        os.mkdir(dataRootDailyInfo)

    if os.path.isdir(dataRootDailyNews):
        pass
    else:
        os.mkdir(dataRootDailyNews)

    if os.path.isdir(dataRootDailyTotal):
        pass
    else:
        os.mkdir(dataRootDailyTotal)


creatRootDirectories()