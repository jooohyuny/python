# -*- coding: utf-8 -*-

from konlpy.tag import Okt

# NLTK : 한글은 약함
# KoNLPy
#    Java로 만들어져 있어서 -> 컴에 Java가 있어야함
#    Java 활용하는 Python프로그램 돌리려면 : jpype
#         pip install JPype1
#    pip install konlpy


t = "몽둥이 금지라구요? 당연한 말씀 그럼 방망이? 몽둥이, 회초리 집에가고싶어요 저런 술이나 먹고 싶다"

o = Okt() # Open Korean Text분석기

a = o.normalize(t) # 정규화(정리)
print(a) ; print("----")

b = o.phrases(t) #어구 추출(의미있는 단위로 나누기)
print(b) ; print("----")

c = o.morphs(t) #형태소 분석
print(c) ; print("----")

d = o.morphs(t, stem=True) #형태소 분석(기본형)
print(d) ; print("----")

e = o.pos(t)
print(e) ; print("----") #형태소 분석(품사 태그)
                         # (단어, 품사)의 tuple list

for w,p in e:
    print(w, p)
print("----")

f = o.pos(t, join=True)
print(f) ; print("----") # tuple말고 그냥 단어, 품사 형태로

g = o.pos(t, stem=True) #형태소 분석(품사태그, 기본형으로)
print(g) ; print("----")

h = o.nouns(t) #명사만 list로
for w in h:
    print(w)
