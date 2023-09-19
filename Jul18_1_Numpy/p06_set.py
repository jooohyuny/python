# -*- coding:utf-8 -*-
import numpy as np

a = np.random.randint(1,11,[10])
b = np.random.randint(1,11,[10])
print(a)
print(b)
print('---------')
c = np.intersect1d(a,b) # 교집합
print(c)
d = np.union1d(a,b) # 합집합
print(d)
e = np.setdiff1d(a,b) # a에서 b에 있는거 빼고
print(e)
f = np.setxor1d(a,b) # a든 b든 
print(f)
g = np.unique(a)
print(g)
