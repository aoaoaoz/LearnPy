# -*- coding: utf-8 -*-

' a test module '
__author__ = 'aoaoao'

import re
from datetime import datetime, timezone, timedelta
def to_timestamp(dt_str, tz_str):
    cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    reg = re.compile(r'^UTC([\+\-])(\d+)\:00$')
    x = reg.match(tz_str)
    if x.group(1)=='-':
        num = -int(x.group(2))
    else:
        num = int(x.group(2))
    dt = cday.replace(tzinfo=timezone(timedelta(hours=num)))
    return dt.timestamp()
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')