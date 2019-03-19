#!usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Asher
@file: re-cakc.py
@time: 2019/03/16
"""

import re

# EXPRESS = "1 - 2*3 + ((67-23+2) * (40/5) + 40 - (324/43))/23 + 32"
EXPRESS = "1 + ((25-23-1) * (40/5) + 2 - (1+2)/3)/9 + 6"


def calculator(expression):
    return eval(expression)


while True:
    result = re.split("\(([^()]+)\)", EXPRESS, 1)

    if len(result) == 3:
        before, content, after = result
        EXPRESS = before + str(calculator(content)) + after
    else:
        final = calculator(EXPRESS)
        print(final)
        break
