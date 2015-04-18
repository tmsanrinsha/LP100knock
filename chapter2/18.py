#!/usr/bin/env python
# coding: utf-8
import os

# 18. 各行を3コラム目の数値の降順にソート
#
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

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
