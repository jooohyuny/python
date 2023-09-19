# -*- coding:utf-8 -*-
import numpy as np

a = np.random.randint(1,11,[2,3])
b = np.random.randint(1,11,[2,3])
print(a)
print(b)
print('---------')
c = a + b   # 연산자로 하면 되는데
print(c)
print('---------')
d = np.add(a,b)         # +
e = np.subtract(a,b)    # -
f = np.multiply(a,b)    # *
g = np.divide(a,b)      # /
h = np.mod(a,b)         # %
i = np.power(a,b)       # ^(제곱)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print('---------')
j = a > b
print(j)
print('---------')
# greater, greater_equal
# less, less_equal
# equal, not_equal
k = np.greater(a,b)
print(k)
print('---------')
name = np.array(['홍길동','김짱구','권짱구'])
mid = np.array([83,75,45])
final = np.array([70,10,60])
avg = np.divide(np.add(mid, final),2)
print(name[np.greater_equal(avg,50)])
print('------------------')
print(a)
print(b)
print('------------------')
l = np.maximum(a,b) # 각 자리별 큰 값
print(l)
m = np.minimum(a,b) # 각 자리별 작은값
print(m)

n = np.random.rand(2,3)
print(n)

o = np.ceil(n) # 소수점 이하 올림
print(o)

p = np.floor(n) # 소수점 이하 버림
print(p)

q = np.rint(n) # 소수점 이하 반올림
print(q)

r = np. round(n,2) # 소수점 이하 2자리로 반올림
print(r)

# 소수점 이하 셋째자리에서 올림
s = np.ceil(n * 100) / 100
print(s)

# np.nan 없음
# np.inf 무한
t = np.array([12,34,1,np.nan,np.inf,88])
print(t)