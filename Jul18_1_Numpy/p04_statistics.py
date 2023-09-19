# -*- coding:utf-8 -*-
import numpy as np

a = np.random.randint(1,11,[2,3])
print(a)
print('---------')
b = np.sum(a)
print(b)
print('---------')
c = np.mean(a)
print(c)

d = a - c # 각 값에서 평균을 뺸 값
d = d ** 2 # 제곱해서
d = np.mean(d) # 그거의 평균
print(d)

e = np.var(a) # 분산
print(e)

f = np.sqrt(e) # 분산에 루트
print(f)

g = np.std(a) # 표준편차
print(g)

# 분산/표준편차 : 평균에서 얼마나 떨어져있나

h = np.max(a)
print(h)
i = np.min(a)
print(i)

j = np.sum(a, axis=0)
print(j)
k = np.mean(a, axis=1)
print(k)
print('------------')
print(a)
print('------------')
l = np.argmax(a) # 최대값 인덱스
print(l)
m = np.argmin(a) # 최소값 인덱스
print(m)
print('------------')
n = np.argmax(a, axis=0)
print(n)
o = np.argmax(a, axis=1)
print(o)
print('------------')
p = np.cumsum(a) # 누적합
print(p)


print('------------')
