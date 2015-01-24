#!/usr/bin/env python
# coding: UTF-8

import os
import glob
import datetime

pwd = os.getcwd()
files = glob.glob(pwd + '/*')
ran_time = datetime.datetime.now()

diffsec = 0
for file in files:
    diffsec += 1
    old_ctime = datetime.datetime.fromtimestamp(os.stat(file).st_ctime)
    # Macの場合作成日を新しくするのは反映されないっぽいので1時間古くして秒をづらす
    new_ctime = old_ctime + datetime.timedelta(hours=-1, seconds=diffsec)
    new_mdified = ran_time + datetime.timedelta(seconds=diffsec)
    times = (int(new_ctime.strftime('%s')), int(new_mdified.strftime('%s')))
    print file
    print u'>> %s ---> %s' % (old_ctime.isoformat(), new_ctime.isoformat())
    continue
    os.utime(file, times)
