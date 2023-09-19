# -*- coding:utf-8 -*-
import tensorflow as tf

# (1, 11), (2, 21), ..., (5, ?) => y = 10x + 1
# ([80, 20], [1, 0]), ([95, 5], [1, 0]) => y = ax + b

# 행렬 계산
#    덧셈/뺄셈 : 각 위치끼리 계산 => 두 행렬 모양이 같아야한다
#    곱셈/나눗셈 : 
#        a행 b열 x c행 d열 : b열과 c행의 갯수가 같아야하고
#        결과는 a행 d열의 배열로 나온다
#        ex) 1행 2열 x 2행 2열 => 1행 2열 계산

# ANN(Artificial Neural Network)
#    yData를 one-hot encoding으로 표현한 다차원 회귀분석
xData = [[80, 20], [95, 5], [10, 90],[90, 10], [5, 95]]
# one-hot encoding
#    목록중에 하나만 1로 표현
#    전기가 최종적으로 어디로 흘렀는지 묘사
yData = [[1, 0], [1, 0], [0, 1], [1, 0], [0, 1]]
label = ["액션","조폭"]
#          L     R
################################################################
x = tf.placeholder(tf.float64)
y = tf.placeholder(tf.float64)

# [80, 20] x a +      b     => [1, 0]
# 1행 2열          2행2열         1행2열        1행 2열
a = tf.Variable(tf.random_uniform([len(xData[0]), len(yData[0])], -10, 10, tf.float64))
b = tf.Variable(tf.random_uniform([len(yData[0])], -10, 10, tf.float64))

# sik = x * a + b의 행렬버전
sik = tf.add(tf.matmul(x, a), b)
 
# 실제 y, sik을 통해서 구해진거 거리
d = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=sik)
    )
ao = tf.train.AdamOptimizer(learning_rate=0.0001)
goal = ao.minimize(d)
################################################################
s = tf.Session()
s.run(tf.global_variables_initializer())

while True:
    s.run(goal, {x:xData, y:yData})
    print("y = ", s.run(a), "x + ", s.run(b))
    # print("y = %fx +%f" % (s.run(a), s.run(b)))
    dd = s.run(d,{x:xData, y:yData})
    print(dd)
    print("---------")

    if dd < 10:
        break
################################################################
a = float(input("싸움 : "))
b = float(input("욕 : "))
predictData = [[a, b]]

# [80, 20] -> [1, 0]
# [95, 5] -> [1, 0]

# [50, 30] -> [1, 0]으로 나오지는 않을거고
#            -> [0.123123, 0.456456]정도로 나올건데
# [1, 0] : 액션
# [0, 1] : 조폭
# [0.123123, 0.456456] : 조폭으로...
 
# tf.argmax : 최대값이 있는 인덱스
#        0 : 열방향(기본)
#        1 : 행방향
result = s.run(tf.arg_max(sik,1), {x:predictData}) # list형태
# print(result)
# print(result[0])
print(label[result[0]])

resulttt = s.run(sik,{x:predictData})
print(resulttt)

