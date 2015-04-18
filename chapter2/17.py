#!/usr/bin/env python
# coding: utf-8
import os

# 17. １列目の文字列の異なり
#
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

os.chdir(os.path.dirname(__file__))
arr = []
filename = 'hightemp.txt'
for line in open(filename):
    tmp = line.split('\t')[0]
    if tmp not in arr:
        arr.append(tmp)

for text in arr:
    print text

os.system("awk '{print $1}' < hightemp.txt | sort | uniq")
