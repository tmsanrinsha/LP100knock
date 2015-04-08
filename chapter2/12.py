#!/usr/bin/env python
# coding: utf-8
import os

# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
#
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

os.chdir(os.path.dirname(__file__))
f1 = open('col1.txt', 'w')
f2 = open('col2.txt', 'w')
for line in open('hightemp.txt'):
    cols = line.split('\t')
    f1.write(cols[0]+"\n")
    f2.write(cols[1]+"\n")

os.system("cut -f 1 < hightemp.txt")
os.system("cut -f 2 < hightemp.txt")
