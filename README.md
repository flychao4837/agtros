# astros
数据抓取测试
1：用tushare获取交易数据 （开发中）

文件目录
config ——            配置信息，计划任务参数

data   ——            采集的任务数据
	+
	+--+ dailyInfo   每日分析数据
	   + dailyNews   每日相关新闻
	   + dailyTotal  每日市场交易数据总量表
	   + dailyTrade  每日交易分时

html   ——            html页面，website相关
log    ——            日志、记录操作中的错误和崩溃，便于手动设置节点恢复操作
task   ——            脚本、计划任务