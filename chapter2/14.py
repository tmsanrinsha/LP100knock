#!/usr/bin/env python
# coding: utf-8
import os
import sys

# 14. 先頭からN行を出力
#
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

os.chdir(os.path.dirname(__file__))
n = 1;
num = sys.argv[1]
for line in open('hightemp.txt'):
    if n > int(num):
        break
    print line
    n += 1

os.system("head -n " + num + ' hightemp.txt')
