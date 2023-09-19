# -*- coding:utf-8 -*-
a = [10, 20, 30, 40, 50]
b = [1, 2, 3, 4, 5]
c = a + b   # 단순 append
print(c)

d = []
for i,aa in enumerate(a):
    d.append(aa + b[i])
print(d)     

# e = a * b
# print(e)
f = a * 2   # 반복
print(f)
##################### -> 자리별로 계산x, list append
print('------------------')

import numpy as np
a2 = np.array(a)
b2 = np.array(b)
c2 = a2 + b2    # (1x2) + (1x2)
                # 같은모양끼리는 자리같은것끼리 계산
print(c2)
d2 = a2 * b2
print(d2)

e2 = a2 * 3 # (1x2) * (1)
            # broadcasting : 다른모양이면 차원수 높은쪽에 맞춰서 항목별로 계산
print(e2)
print('------------------')

name = np.array(['홍길동','김짱구','권짱구'])
kor = np.array([100,80,55])
eng = np.array([70,20,80])
mat = np.array([30,40,45])
sum = kor + eng + mat   # 자리별로 계산
avg = sum/3             # broadcasting
print(avg)

over50 = avg > 50
print(over50)
print('------------------')

print(avg[over50])  # masking : 위치가 True인것만
print(name[over50])
print(name[kor>90])
print('------------------')
# kor > 90 : [True False False]

# 50 <= 영어점수 <= 70인 학생이름
# and/ or 대신 &/|를 써야된다.
# and(&&), & -> 중간에 안봐도 되면 자르는게 and(&&), or(||)
#            -> 끝까지 확인해보는 게 &, |
print(name[(50<=eng) & (eng <=70)])
print('------------------')








