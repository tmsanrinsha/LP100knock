#!/usr/bin/env python
# coding: utf-8
import os

# 10. 行数のカウント
#
# 行数をカウントせよ．確認にはwcコマンドを用いよ

print sum(1 for line in open('hightemp.txt'))

os.system('wc hightemp.txt')
