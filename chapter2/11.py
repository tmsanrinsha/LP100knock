#!/usr/bin/env python
# coding: utf-8
import os

# 11. タブをスペースに置換
#
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

os.chdir(os.path.dirname(__file__))
for line in open('hightemp.txt'):
    print line.expandtabs(1)

os.system("sed -e 's/\t/ /g' < hightemp.txt")
os.system("tr '\t' ' ' < hightemp.txt")
os.system("expand -t 1 hightemp.txt")
