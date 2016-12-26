#!/usr/bin/python
# coding=UTF-8

#获取前十大股东、十大流通股东、十大机构持股名单
import sys
import os
import time
import tushare as ts
import datetime as datetime
import config as config
from readJsonFile import readFile
from writeJsonFile import writeFile

import urllib
import urllib2
import re

basicFile = os.path.join(config.listsRootPath, 'stockBasic.json')
basicDate = readFile(basicFile)
scanFile = os.path.join(config.configRootPath, 'scanData.json')
scanConfigDate = readFile(scanFile)



# 页面爬虫类
# 处理页面标签类
class Tool:
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()将前后多余内容删除
        return x.strip()

class SPIDER:
    # 初始化，传入基地址
    def __init__(self):
        # HTML标签剔除工具类对象
        self.tool = Tool()
        # 默认的标题，如果没有成功获取到标题的话则会用这个标题
        self.file = None

        self.defaultTitle = u"page"
        # 文件起始目录
        self.pageroot = config.dataRoottenShareholder


    # 传入页码，获取该页的代码
    def getPage(self,baseUrl=None):
        try:
            # 构建URL
            if baseUrl is not None:
                url = baseUrl
                request = urllib2.Request(url)
                response = urllib2.urlopen(request)
                # 返回UTF-8格式编码内容
                return response.read().decode('utf-8')
            else:
                pass
        # 无法连接，报错
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接失败,错误原因", e.reason
                return None


    # 获取每一层楼的内容,传入页面内容
    def getContent(self, page):
        # 匹配所有楼层的内容
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            # 将文本进行去除标签处理，同时在前后加入换行符
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode('utf-8'))
        return contents

    def writeData(self, name=None,content=None):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        if content is not None and name is not None:
            self.file = open(name, "w+")
            self.file.write(content)
            self.file.close()
        else:
            print "文件名或内容为空"
            pass

    def start(self):
        #遍历目录
        if basicDate['errcode'] == 0:
            lists = basicDate['data']
            for k in lists:
                contdir = os.path.join(self.pageroot,k)
                print contdir
                if os.path.isdir(contdir):
                    pass
                else:
                    os.mkdir(contdir)

                filename = os.path.join(contdir, "htmlContent.txt");
                url ="http://cuiqingcai.com/993.html"
                try:
                    indexPage = self.getPage(url)
                    #contents = self.getContent(indexPage)
                    self.writeData(filename,indexPage)
                # 出现写入异常
                except IOError, e:
                    print "写入异常，原因" + e.message
                finally:
                    print "写入任务完成"

bdtb = SPIDER()
bdtb.start()