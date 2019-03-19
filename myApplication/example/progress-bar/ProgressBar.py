#!usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Asher
@file: ProgressBar.py
@time: 2019/03/16
"""

import sys
import time

for i in range(31):
    sys.stdout.write("\r")
    sys.stdout.write("%s%% |%s" % (int(i / 30 * 100), int(i / 30 * 100) * "*"))
    sys.stdout.flush()
    time.sleep(0.3)
