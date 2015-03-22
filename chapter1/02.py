#!/usr/bin/env python
# coding: utf-8

# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
#
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．


text1 = u'パトカー'
text2 = u'タクシー'
print ''.join(list(sum(zip(text1,text2), ()))).encode('utf-8')
