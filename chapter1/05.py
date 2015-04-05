#!/usr/bin/env python
# coding: utf-8

# 05. n-gram
#
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

# [N-gram - Negative/Positive Thinking](http://d.hatena.ne.jp/jetbead/20110904/1315147133)
# 単語bi-gram: 文字列を単語ごとに分解して、その中でbi-gramを作る -> [I-am, am-an, an-NLPer]
# 文字bi-gram: 2文字ごとにbi-gramを作る -> ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']

def nlperWord(text):
    wordArr = text.split(' ')
    bigram = []
    for i in range(0, len(wordArr) - 1):
        bigram.append(wordArr[i] + '-' + wordArr[i + 1])
    return bigram

def nlperText(text):
    bigram = []
    for i in range(0, len(text) - 1):
        bigram.append(text[i:i + 2])
    return bigram

text = 'I am an NLPer'
print nlperWord(text)
print nlperText(text)
