# -*- coding:utf-8 -*-

# range
a = range(5) # 0 ~ (5 - 1)까지
print(a)
print(type(a))

b = range(11)
b = list(b)
print(b)
print(type(b))

c = range(2,10) #2 ~ (10 - 1)
c = list(c)
print(c)

d = range(3,10,2) #3 ~ (10 - 1), 2칸씩
d = list(d)
print(d)

print("------------")

# tuple
e = (213,213,123,56,45,88)
print(e)
print(type(e))
print(e[0])

# Java에서 두 값 바꾸는거
#int a = 10; int b = 20; # int t = a; // t = 10 # a = b; // a = 20 # b = t; // b = 10

# 변수 여러개 값 한꺼번에 바꾸기
f = 100
g = 200
h = 300
(f, g, h) = (g, h, f)
print(f, g, h)

# 변수 여러개 만들고 초기화
(i, j) = (99,88)
print(i,j)

# () 생략가능
# (사실은 tuple쓴거지만) 변수 여러개 만들고 초기화 가능 
k,l = 1,2   
print(k,l)

#가독성 적절히 봐가면서
height, weight = float(input("키 : ")), float(input("몸무게: ")) 






