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
def isShiyiHoloday(dateStr):
    if dateStr[5:7] =="10" and (dateStr[8:10] >="01" and dateStr[8:10] <"06"):
        return True
    else:
        return False

def isWuYiHoliday(dateStr):
    if dateStr[5:7] =="05" and (dateStr[8:10] >="01" and dateStr[8:10] <"03"):
        return True
    else:
        return False

def isYuandan(dateStr):
    if dateStr[5:7] =="01" and (dateStr[8:10] >="01" and dateStr[8:10] <"03"):
        return True
    else:
        return False
def isZhongQiuHoliday(dateStr):
    pass
def isCunJieHoliday(dateStr):
    pass

def isTradeDay(dateStr):
    if bool(isWuYiHoliday(dateStr)):
        return False
    elif bool(isShiyiHoloday(dateStr)):
        return False
    elif bool(isYuandan(dateStr)):
        return False
    else:
        return get_week_day(dateStr)
if __name__ == '__main__':
    print(isTradeDay('2016-12-10'))
    print(isTradeDay('2016-10-01'))
    print(isTradeDay('2016-05-03'))
    print(isTradeDay('2016-10-07'))
