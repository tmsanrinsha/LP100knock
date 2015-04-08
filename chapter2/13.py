#!/usr/bin/env python
# coding: utf-8
import os

# 13. col1.txtとcol2.txtをマージ
#
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

os.chdir(os.path.dirname(__file__))
f1 = open('col1.txt')
f2 = open('col2.txt')
f3 = open('col3.txt' , 'w')
line1 = f1.readline()
line2 = f2.readline()

while line1:
    f3.write(line1.rstrip('\n') + '\t' + line2)
    line1 = f1.readline()
    line2 = f2.readline()

os.system("paste col1.txt col2.txt")
