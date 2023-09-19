# -*- coding:utf-8 -*-
# cmd
#    pip install numpy

# 2차원 list : 객체list는 어쩌고...
score = [[100,90,80],[80,95,70]]
print(type(score)) #무슨 객체인지
print(score)
print(score[0])
print(score[0][1]) 
print(score[1][2]) 
score[1][0] = 0
# score[1][0:3] = 0    # 한꺼번에 여러개 값 바꾸는게 불가능
print(score)
print('-------------')

# Numpy(Numpy의 array) : 기본 Python list보다 기능 좋은 list
import numpy as np # import 모듈명 as 별칭 -> 별칭.???
# score2 = np.array(score)
score2 = np.array(score , dtype = np.float64)    # 자료형을 바꾸고 싶을때 
print(type(score2))
print(score2)   # 출력형태 가독성이 좀 낫다?
print(score2[0])
print(score2[0][1]) # Python list스타일
print(score2[1,2])  # Numpy스타일
#score2[1][0] = 100
score2[1,0] = 100
score2[1,0:3] = 0   # slicing(한꺼번에 여러개 값 바꾸기)
print(score2)
print(score2.dtype) # 자료형
print(score2.shape) # 몇행몇열
print(score2.size)  # 총 갯수

# Numpy를 Pandas/Maplotlib/Tensorflow등이 활용



