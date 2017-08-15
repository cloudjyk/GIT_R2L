#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from datetime import datetime,timedelta,timezone
def to_timestamp(strT,strTZ):
    # t = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
    # print(bool(re.match(r'^[0-9]{4}-[0-1][0-9]-[0-2][0-9]\s[0-1][0-9]:[0-5][0-9]:[0-5][0-9]$',strT)))
    # print(bool(re.match(r'^UTC\+[0-9]:0{2}$',strTZ)))

    # if (re.match(r'^[0-9]{4}-[0-1][0-9]-[0-2][0-9]\s[0-1][0-9]:[0-5][0-9]:[0-5][0-9]$',strT) or re.match(r'^[0-9]{4}-[0-1][0-9]-[0-2][0-9]\s[2][0-4]:[0-5][0-9]:[0-5][0-9]$',strT)) \
    # and (re.match(r'^UTC-[0-9]:0{2}$',strTZ) or re.match(r'^UTC-[1][0-2]:0{2}$',strTZ) or re.match(r'^UTC\+[0-9]:0{2}$',strTZ) or re.match(r'^UTC\+[1][0-2]:0{2}$',strTZ)):
    if datetime.strptime(strT,'%Y-%m-%d %H:%M:%S') \
    and (re.match(r'^UTC(-|\+)[0-9]:0{2}$',strTZ) or re.match(r'^UTC(-|\+)[1][0-2]:0{2}$',strTZ)):
        print('输入格式正确，lets go！')
        if len(strTZ) == 8:
            tz = int(strTZ[4:5])
            # print(tz)
        else:
            tz = int(strTZ[4:6])
        # y=int(strT[0:4])
        # m=int(strT[5:7])
        # d=int(strT[8:10])
        # h=int(strT[11:13])-tz
        # m=int(strT[14:16])
        # s=int(strT[17:19])
        # dt=datetime(y,m,d,h,m,s)
        # print(dt)
        t = datetime.strptime(strT,'%Y-%m-%d %H:%M:%S')
        # print('t=',t)
        if strTZ[3]=='+':
            t_utc_7=t.replace(tzinfo=timezone(timedelta(hours=tz)))
        else:
            t_utc_7=t.replace(tzinfo=timezone(timedelta(hours=-tz)))
        # t_utc_7=t_utc_7.astimezone(timezone(timedelta(hours=0)))

        return t_utc_7.timestamp()

if __name__=='__main__':
    t1 = to_timestamp('2015-06-01 08:10:30', 'UTC+7:00')
    print(t1)
    assert t1 == 1433121030.0
    print('pass\n')
    t1 = to_timestamp('2015-5-31 16:10:30', 'UTC-9:00')
    print(t1)
    assert t1 == 1433121030.0
    print('pass\n')
    t1 = to_timestamp('2015-06-01 08:10:30', 'UTC-7:00')
    print(t1)
    assert t1 == 1433171430.0
    print('pass')