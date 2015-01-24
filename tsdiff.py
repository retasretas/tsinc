#!/usr/bin/env python
# coding: UTF-8

import os
import glob
import datetime
import commands

pwd = os.getcwd()
files = glob.glob(pwd + '/*')
ran_time = datetime.datetime.now()

# print commands.getoutput("ls -l")
diffsec = 0
for file in files:
    diffsec += 1
    # old_ctime = datetime.datetime.fromtimestamp(os.stat(file).st_ctime)
    old_ctime = datetime.datetime.fromtimestamp(os.path.getctime(file))
    # Macの場合作成日を新しくするのは反映されないっぽいので1時間古くして秒をづらす
    # new_ctime = old_ctime + datetime.timedelta(hours=-1, seconds=diffsec)
    # どのみち作成日は変更できなかったので追加日をづらす方向で時刻マイナスはなしに
    new_ctime = old_ctime + datetime.timedelta(hours=1, seconds=diffsec)
    new_mdified = ran_time + datetime.timedelta(seconds=diffsec)
    times = (int(new_ctime.strftime('%s')), int(new_mdified.strftime('%s')))
    print file
    print u'>> %s ---> %s' % (old_ctime.isoformat(), new_ctime.isoformat())
    # continue
    os.utime(file, times)
