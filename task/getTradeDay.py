#!/usr/bin/python
# coding=UTF-8
#根据给的日期判断是否可交易

import time,datetime

def get_week_day(dateStr):
    if bool(dateStr):
        date = datetime.datetime.strptime(dateStr, "%Y-%m-%d").date()
        week_day_dict = {
            0: True,
            1: True,
            2: True,
            3: True,
            4: True,
            5: False,
            6: False,
        }
        day = date.weekday()
        return week_day_dict[day]
    else:
        return False

#print(get_week_day('2016-11-28'))