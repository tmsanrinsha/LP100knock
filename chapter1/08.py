#!/usr/bin/env python
# coding: utf-8

# 08. 暗号文
#
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#
#     英小文字ならば(219 - 文字コード)の文字に置換
#     その他の文字はそのまま出力
#
# この関数を用い，英語のメッセージを暗号化・復号化せよ

def cipher(text):
    retText = ''
    for char in list(text):
        asciiCode = ord(char)
        if asciiCode >= 97 and asciiCode <= 122:
            retText += chr(219 - ord(char))
        else:
            retText += char

    return retText

def decipher(text):
    retText = ''
    for char in list(text):
        asciiCode = ord(char)
        if asciiCode >= 97 and asciiCode <= 122:
            retText += chr(219 - ord(char))
        else:
            retText += char

    return retText

text = 'Agefuga'
print cipher(text)
print cipher(cipher(text))
