# -*- coding:utf-8 -*-
# call by value, call by reference

d = 10
e = 10
##############################
def test(a,b,c):
    print(a,b[0],c[0])
    a=100
    b[0]=100
    c = [100,200]
    d = 100 #4번줄 d가 아니고, 새로만든 d/ 밖에있는 d와는 아무상관이없다
    global e    # 지금부터 쓰는 e는 밖에있는 e(5번줄)
    e = 100
    print(a,b[0],c[0], d, e)
##############################
a=10
b=[10,20]
c=[10,20]
print(a, b[0], c[0], d, e)
test(a, b, c)
print(a, b[0], c[0], d, e)



