#!/usr/bin/env python
# coding: UTF-8

import os
import glob
import datetime
import commands

pwd = os.getcwd()
files = glob.glob(pwd + '/*')
ran_time = datetime.datetime.now()

diffsec = 0
for file in files:
    # タイムスタンプが重複しないよう秒数をインクリメントする
    diffsec += 1
    # 作成日時を取得する。(0:年、1:時、2:分、3:秒、4:月、5:日)の順の配列を取得
    tmp = commands.getoutput( "ls -lUT %s | awk '{print $9,$8,$6,$7}' | sed 's/:/ /g'" % (file) ).split(' ')
    # intへキャスト
    d = [int(i) for i in tmp]
    # 配列の順序を組み立てて日付に合う文字列を生成する
    old_ctime = datetime.datetime(d[0], d[4], d[5], d[1], d[2], d[3])

    # Macの場合作成日を新しくするのは反映されないっぽいので1時間古くして秒をづらす
    new_ctime = old_ctime + datetime.timedelta(hours=-1, seconds=diffsec)
    new_mdified = ran_time + datetime.timedelta(seconds=diffsec)
    times = (int(new_ctime.strftime('%s')), int(new_mdified.strftime('%s')))
    print file
    print u'>> %s ---> %s' % (old_ctime.isoformat(), new_ctime.isoformat())

    # 実際に日付変更
    commands.getoutput( "touch -t %s %s" % (new_ctime.strftime('%Y%m%d%H%M.%S'), file) )
    os.utime(file, times) # pythonモジュールでの実行(変更日更新用、この処理では作成日は変わらない)
