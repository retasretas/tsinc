#!/usr/bin/python

import os
import glob
import datetime

print os.getcwd()
quit()

files = glob.glob('./*')
diffsec = 0
for file in files:
    diffsec += 1
    createdate_tap = datetime.datetime.now() + datetime.timedelta(seconds=diffsec)
    updatedate_tap = datetime.datetime.now() + datetime.timedelta(seconds=diffsec)
    times = (int(createdate_tap.strftime('%s')), int(updatedate_tap.strftime('%s')))
    os.utime(file, times)
