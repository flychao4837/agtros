#!/usr/bin/python
# coding=UTF-8
#根据给的日期判断是否可交易

import time,datetime

def get_week_day(dateStr):
    try:
        time.strptime(dateStr, "%Y-%m-%d")
        return True
    except:
        return False

    date = datetime.datetime(dateStr)
    week_day_dict = {
        0 : '星期一',
        1 : '星期二',
        2 : '星期三',
        3 : '星期四',
        4 : '星期五',
        5 : '星期六',
        6 : '星期天',
    }
    day = date.weekday()

    #return week_day_dict[day]

print(get_week_day('2016-11-24'))