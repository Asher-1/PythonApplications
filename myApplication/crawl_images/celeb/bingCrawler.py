#!usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Asher
@file: bingCrawler.py
@time: 2019/04/28
"""

import os
from icrawler.builtin import BingImageCrawler
path = r'E:\weather_test\BingImage'
f = open('KoreaStarName.txt', 'r')
lines = f.readlines()
for i, line in enumerate(lines):
    name = line.strip('\n')
    file_path = os.path.join(path, name)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    bing_storage = {'root_dir': file_path}
    bing_crawler = BingImageCrawler(parser_threads=2, downloader_threads=4, storage=bing_storage)
    bing_crawler.crawl(keyword=name, max_num=10)
    print('第{}位明星：{}'.format(i, name))