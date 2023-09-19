# -*- coding:utf-8 -*-
from random import randint

# for : 반복횟수
# for-each : 컬렉션 탐색용
# while : 반복조건
# do-while : 반복조건(최소 1번은 반복 보장)
# $.each(); : JS배열 대상 for + for-each
# $(선택자).each(); : DOM객체 대상 for + for-each
#############################################
# J : for-each
# P : for
l = [123,454,18,45,25]
for v in l:
    print(v)
print('-----------------')
# list, set, dict, range, tuple, ...
# l2 = [0,1,2,3,4]
# l2 = range(5) #0 ~ 4 range
# l2 = list(l2)
for v in range(5):
    print(v)
print('-----------------')

for v in range(1,10):
    print(v)
print('-----------------')

for i in range(1,10):
    for dan in range(2,10):
        print("%d x %d = %d" %(dan, i, dan*i), end ="\t")
    print()
print('-----------------')

l3 = ['asf','aaasf','vvrf','aage','qwer','yjr'];
# for v in enumerate(l3): #(인덱스, 값) tuple상태로
#    print(v,type(v))
for i,v in enumerate(l3):
    print(i,type(i))
    print(v,type(v))
    print('-----------------')
# 순서x 키-값 쌍 => for랑은...
d = {"기온" : 30, "강수량":15,"습도":100}
for k,v in d.items(): # (키, 값) tuple로
    print(k,type(k))
    print(v,type(v))
    print('-----------------')

print('-----------------')
# 1 ~ 10랜덤, 5나오면 끝
# x = 0
while True:
    x = randint(1,10) # 1 ~ 10 사이 정수 랜덤
    print(x)
    if x == 5:
        break
        # continue
# 반복문 속에서 변수 만들지마라
# -> Python(interpreter방식)에서는 안먹히는 얘기
# -> 효율적인 프로그램 x, 개발용에서 o
print('-----------------')
for i in range(6):
    for j in range(6):
        print(i,j)
        if j == 3:
            break
    if j == 3:
        break
print('-----------------')
# j가 3되면 전체가 끝나게
j3 = False
for i in range(6):
    for j in range(6):
        print(i,j)
        if j == 3:
            j3 = True
            break
    if j3:
        break






