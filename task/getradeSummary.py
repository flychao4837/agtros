#!/usr/bin/python
# coding=UTF-8
#获取每日开盘、收盘汇总信息，便于汇总5日、10日线，分析各种指标
import tushare as ts
import datetime as datetime
import config as config
from readJsonFile import readFile
from getDailyInfo import getDailyData
from writeJsonFile import writeFile
from getTradeDay import get_week_day


endDate = datetime.datetime.now().strftime("%Y-%m-%d") #以当天为截止日期
basicFile = config.listsRootPath + '\\stockBasic.json'
basicDate = readFile(basicFile)  # timeToMarket 上市日期
scanFile = config.configRootPath+'\\scanData.json'
scanConfigDate = readFile(scanFile)

def getTradeStock(stock=""):
    if bool(stock) == False:
        #没有参数时，遍历asicB.json取所有的股票交易汇总
        if basicDate['errcode'] == 0:
            lists = basicDate['data']
            name = lists['name']
            if bool(name):
                for k in name:
                    print k
                    getTradeSummary(k)
            else:
                return {'errcode': -10000, 'errmsg': "没找到对应code代码", 'data': ''}
        else:
            print basicDate['errcode']
    else:
        #带有股票参数，就只扫描一只
        getTradeSummary(stock)


def getTradeSummary(stock=""):
    if bool(stock):
        jsonFile = config.dataRootDailyTotal + "\\" + stock + ".json"
        data = ts.get_hist_data(stock)
        data.to_json(jsonFile, orient='index', force_ascii=False)
    else:
        return {'errcode': -1, 'errmsg': 'need stockCode'}


    #ts.get_hist_data('600848',start='2015-01-05',end='2015-01-09')
    #ts.get_hist_data('600848', ktype='W')  # 获取周k线数据
    #ts.get_hist_data('600848', ktype='M')  # 获取月k线数据
    #ts.get_hist_data('600848', ktype='5')  # 获取5分钟k线数据
    #ts.get_hist_data('600848', ktype='15')  # 获取15分钟k线数据
    #ts.get_hist_data('600848', ktype='30')  # 获取30分钟k线数据
    #ts.get_hist_data('600848', ktype='60')  # 获取60分钟k线数据
    #ts.get_hist_data('sh'）  # 获取上证指数k线数据，其它参数与个股一致，下同
    #ts.get_hist_data('sz'）  # 获取深圳成指k线数据
    #ts.get_hist_data('hs300'）  # 获取沪深300指数k线数据
    #ts.get_hist_data('sz50'）  # 获取上证50指数k线数据
    #ts.get_hist_data('zxb'）  # 获取中小板指数k线数据
    #ts.get_hist_data('cyb'）  # 获取创业板指数k线数据

    #     本接口还提供大盘指数的全部历史数据，调用时，请务必设定index参数为True, 由于大盘指数不存在复权的问题，故可以忽略autype参数。
    #
    #     ::
    #
    #     ts.get_h_data('002337')  # 前复权
    #     ts.get_h_data('002337', autype='hfq')  # 后复权
    #     ts.get_h_data('002337', autype=None)  # 不复权
    #     ts.get_h_data('002337', start='2015-01-01', end='2015-03-16')  # 两个日期之间的前复权数据
    #
    #     ts.get_h_data('399106', index=True)  # 深圳综合指数
    #
    #
    # 参数说明：
    #
    # - ** code **:string, 股票代码
    # e.g.
    # 600848
    # - ** start **:string, 开始日期
    # format：YYYY - MM - DD
    # 为空时取当前日期
    # - ** end **:string, 结束日期
    # format：YYYY - MM - DD
    # 为空时取去年今日
    # - ** autype **:string, 复权类型，qfq - 前复权
    # hfq - 后复权
    # None - 不复权，默认为qfq
    # - ** index **:Boolean，是否是大盘指数，默认为False
    # - ** retry\_count **: int, 默认3, 如遇网络等问题重复执行的次数
    # - ** pause **: int, 默认
    # 0, 重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    #
    # 返回值说明：
    #
    # - ** date **: 交易日期(index)
    # - ** open **: 开盘价
    # - ** high **: 最高价
    # - ** close **: 收盘价
    # - ** low **: 最低价
    # - ** volume **: 成交量
    # - ** amount **: 成交金额

if __name__ == '__main__':
    getTradeStock()