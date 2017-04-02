@echo off
goto :main
执行每日扫描，根据当前行情提醒
直接执行python命令 文件路径为本地文件实际路径
安装python和tushare
dailyTradeWatch.json是扫描配置文件,格式如下
    {
      "start": "2017-01-19", 开始时间
      "end": "2017-01-29",   截止时间
      "list":[               扫描代码列表 数组格式，子项为object格式
        {
          "name": "海兴电力",   股票名称
          "code": "603556",    股票代码
          "buyprice": 39,      预期买入价格
          "buyrate": -5,       预期跌幅买入 最大-10
          "sellprice":40,      预期卖出价格
          "sellrate":2         预期涨幅卖出 最大10
        },
        {
          "name": "参特科技",
          "code": "603098",
          "buyprice": 20,
          "buyrate": -3,
          "sellprice":22,
          "sellrate":10
        },
        {
          "name": "国海证券",
          "code": "000750",
          "buyprice": 6.5,
          "buyrate": -6,
          "sellprice":7,
          "sellrate":10
        }
      ]
    }
:main
python E:\stockScan\taskmonitor\dailyTradeWatch.py
