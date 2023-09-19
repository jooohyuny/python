# -*- coding:utf-8 -*-
import numpy as np

# Numpy를 tensorflow 등 후속기술에서 사용
# -> 인공신경망 초기값
# 더미데이터 만들때 

a = np.zeros([3, 2]) # 모든 값이 0으로 구성된 3x2 행렬 
print(a)

b = np.ones([3, 2]) # 모든 값이 1로 구성된 3x2 행렬
print(b)

c = np.empty([3, 2]) # 의미없는 값들
print(c)

print('----------')

d = np.arange(5) # 0 ~ (5-1)까지
print(d)

e = np.arange(2,6) # 2 ~ (6-1)까지
print(e)

f = np.arange(2, 10, 3) # 2 ~ (10-1)까지 3칸씩 
print(f)
print('----------')

g = np.random.rand(3, 2) # 0.0 ~ 0.99까지 랜덤의 수를 3x2행렬로
print(g)

h = np.random.randn(3, 2) # 평균이 0 표준편차가 1인  랜덤의 수를 3x2행렬로
print(h)

# 2 ~ (10-1)까지의 랜덤한 정수를 3x2행렬로
i = np.random.randint(2, 10, [3,2]) # 2 ~ (10-1)까지의 랜덤한 정수를 3x2행렬로
print(i)


