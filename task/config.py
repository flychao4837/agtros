#!/usr/bin/python
# coding=UTF-8

#系统配置，路径判断、目录生成
import os
import sys

# 2f66cdc59fb70fa0675fdf34c1c1f86ce6d5c21419b33936ebc27029d9ae5511
##磁盘根目录
path = os.path.abspath(os.path.dirname(sys.argv[0]))
#获取文件根路径、相对路径
curFileWorkPath = os.getcwd()
filePath = os.path.split(curFileWorkPath)
curRootPath =filePath[0]
configRootPath = os.path.join(curRootPath, 'config')
dataRootPath = os.path.join(curRootPath, 'data')
logRootPath = os.path.join(curRootPath, 'log')
htmlRootPath = os.path.join(curRootPath, 'html')
taskRootPath = os.path.join(curRootPath, 'task')
listsRootPath = os.path.join(dataRootPath, 'lists')

dataRootDailyTotal = os.path.join(dataRootPath, 'dailyTotal')
dataRootDailyTrade = os.path.join(dataRootPath, 'dailyTrade')
dataRootDailyInfo = os.path.join(dataRootPath, 'dailyInfo')
dataRootDailyNews = os.path.join(dataRootPath, 'dailyNews')

####常用扫描文件
basicFile = os.path.join(listsRootPath, 'stockBasic.json')
scanFile = os.path.join(configRootPath, 'scanData.json')
industryFile = os.path.join(listsRootPath, "stockIndustryClassified.json")

###手动指定存放的磁盘位置
##syndir = "d://download/test"

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


if __name__ == '__main__':
    creatRootDirectories()