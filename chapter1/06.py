#!/usr/bin/env python
# coding: utf-8

# 05. 集合
#
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

def nlperText(text):
    bigram = []
    for i in range(0, len(text) - 1):
        bigram.append(text[i:i + 2])
    return bigram

x = set(nlperText('paraparaparadise'))
y = set(nlperText('paragraph'))

print x | y
print x ^ y
print x - y
print 'se' in x
print 'se' in y
