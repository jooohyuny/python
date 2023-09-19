# -*- coding:utf-8 -*-
# pip install nltk
# NLTK(Natural Language Toolkit) : 한글은 부실
from nltk.tokenize import word_tokenize, sent_tokenize


t = "부산가면 뭐 먹을까?? 일단 도착해서 부산역에서 사진찍고 저녁에 도착하니깐 소주 한잔하고, 다음날은 회에 한잔하고, 저녁에 부산 야시장에서 간단하게 맥주 한잔하고"
t += "일요일에는?... 일찍 일어나서 놀다가 부산역 도착해서 짐 맡겨두고, 일단 꼼장어 먹고... 해운대가서  입수하자"
t += "숙소는 좋을까??.... 잘모르겠다"

# 특수문자 목록 다운받기(처음 한번만)
# import nltk
# nltk.download("punkt")
wt = word_tokenize(t)   # 단어 분리(특수문자까지)
print(wt)

st = sent_tokenize(t) # 문장 분리
print(st)