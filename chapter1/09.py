#!/usr/bin/env python
# coding: utf-8
import random

# 09. Typoglyemia
#
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

def typoglyemia(text):
    wordArr = text.split(' ')
    retWords = []
    for word in wordArr:
        if len(word) > 4:
            innerChars = list(word[1:-1])
            random.shuffle(innerChars)
            retWords.append(word[0] + ''.join(innerChars) + word[-1])
        else:
            retWords.append(word)

    return ' '.join(retWords)

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print typoglyemia(text)
