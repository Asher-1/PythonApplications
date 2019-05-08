#!usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Asher
@file: download_videos.py
@time: 2019/05/06
"""
import requests

url = 'https://github.com/TeXworks/texworks/releases/download/release-0.6.3/TeXworks-win-setup-0.6.3-201903161732-git_a2470ca.exe'
r = requests.get(url, stream=True)
with open('TeXworks.exe', "wb") as mp4:
    for chunk in r.iter_content(chunk_size=1024 * 1024):
        if chunk:
            mp4.write(chunk)
