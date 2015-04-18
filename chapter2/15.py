#!/usr/bin/env python
# coding: utf-8
import os
import sys

# 15. 末尾のN行を出力
#
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

os.chdir(os.path.dirname(__file__))
num = int(sys.argv[1])

filename = 'hightemp.txt'
start = sum(1 for line in open(filename)) - num
i = 1
for line in open(filename):
    if i < start:
        i += 1
        continue
    print line
    i += 1

os.system("tail -n " + str(num) + ' hightemp.txt')
