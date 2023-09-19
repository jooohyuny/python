# -*- coding:utf-8 -*-
import numpy as np

a = np.random.randint(1,101,[3,5])
b = np.random.randint(1,101,[3,5])
print(a)
print(b)
print('---------')
c = a + b
print(c)
print('---------')
d = np.concatenate([a,b]) # 붙이기
print(d)
print('---------')
e = np.append(a,b)
print(e) # 붙여서 1차원으로 - 인공신경망때 사용...
print('---------')
# NumPy, Pandas, TF, ...
# axis = 0 : 열방향
# axis = 1 : 행방향
f = np.concatenate([a,b], axis=1)
print(f)
print('---------')
g = np.append(a,b,axis=0) # d랑(concatnate 열방향)
print(g)
print('---------')
h = np.append(a,b,axis=1) # f랑(concatnate 행방향)
print(h)
print('===========================')

aa = np.array_split(a, 2) # 대책없이 2개로 나누기
print(aa)
print('---------')
# bb = np.split(b,2) # 똑같이 2개로 나누기
# print(bb)
print('---------')
bb = np.split(b,3) # 똑같이 3개로 나누기
print(bb)










