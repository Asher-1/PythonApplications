#!usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author: Asher
@file: extractVoices.py
@time: 2019/05/12
"""

import os
from tqdm import tqdm
import subprocess

current = os.getcwd()

dirs = os.listdir(current)

for i in tqdm(dirs):

    if os.path.splitext(i)[1] == ".ts":
        # bname = str(os.path.splitext(i)[0].encode('utf-8')).replace('\\','%').replace(' ','_')
        video_name = 'temp.mp4'
        os.rename(i, video_name)

        getmp3 = 'ffmpeg -i temp.mp4 -f mp3 -vn temp.mp3'

        cutmp3 = 'ffmpeg -i temp.mp3 -ss 00:00:15 -acodec copy tempcut.mp3'

        returnget = subprocess.call(getmp3, shell=True)

        returncut = subprocess.call(cutmp3, shell=True)

        os.remove('temp.mp3')

        os.rename('tempcut.mp3', os.path.splitext(i)[0] + '.mp3')

        os.rename(video_name, i)

        print(returnget, returncut)
