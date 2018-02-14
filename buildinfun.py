# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 19:42:15 2018

@author: hyh
"""

from datetime import datetime
now = datetime.now()
print(now)
dt = datetime(2026,8,17,0,0,0)
print(dt)
dt2 = dt.timestamp()
print(dt2)
dt3 = datetime.utcfromtimestamp(dt2)
print(dt3)
#dt4 = datetime.striptime()

print(now.strftime('%a, %b %d %H:%M'))
from collections import defaultdict
d = defaultdict(lambda: 'N/A')
#d = {}
d['key1'] = 'en'
print(d['key1'])
print(d['key2'])