#!/usr/bin/env python
# coding: utf-8
import os
import sys

# 16. ファイルをN分割する
#
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

os.chdir(os.path.dirname(__file__))
num = int(sys.argv[1])

filename = 'hightemp.txt'
i = 0
for line in open(filename):
    print line
    if i % num == num - 1:
        print ''
    i += 1

os.system("split -l " + str(num) + ' hightemp.txt')
