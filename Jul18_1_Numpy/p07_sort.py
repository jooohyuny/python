# -*- coding:utf-8 -*-
import numpy as np

# 1차원
a = np.random.randint(1,101,[10])
print(a)
print(a[0])
print(a[1:5])
print(a[1:8:2]) # 1 ~ (8-1)까지 2개씩
print(a[:8:2])  # 0 ~ (8-1)까지 2개씩
                # 안쓰면 알아서 끝까지
print(a[::2])  # 0 ~ 끝까지 2개씩
print(a[::-1])  # 역순
print('---------')
print(a)
b = np.sort(a)      # 오름차순
print(b)
c = np.sort(a)[::-1]# 내림차순
print(c)
print('---------')

# 2차원
d = np.random.randint(1,101,[3,5])
print(d)
e = np.sort(d)  # 행 방향 정렬
print(e)
# f = np.sort(d, axis=1)
# print(f)
g = np.sort(d, axis=0) # 열 방향
print(g)
print("============================")
print(d)
print('--------------')
h = np.sort(d, axis=0)[::-1] # 열 방향 역순
print(h)
print('--------------')
i = np.sort(d)[::-1] # 행 방향 역순
print(i)
print('--------------')

print(d)
print('--------------')
j =[]
for row in d:
    j.append(np.sort(row)[::-1])
j =np.array(j)
print(j)


