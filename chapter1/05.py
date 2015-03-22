#!/usr/bin/env python
# coding: utf-8

# 05. n-gram
#
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

def nlperWord(text):
    textArr = text.split(' ')
    bigram = []
    for i in range(0, len(textArr) - 1):
        bigram.append(textArr[i] + textArr[i + 1])
    return bigram

def nlperText(text):
    bigram = []
    for i in range(0, len(text) - 1):
        bigram.append(text[i:i + 2])
    return bigram

text = 'I am an NLPer'
print nlperWord(text)
print nlperText(text)
