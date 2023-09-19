# -*- coding:utf-8 -*-

# 메소드 : 객체의 액션
# 함수 : 관련있는 작업을 묶어 정의 해놓고
#        여러번 호출해서 쓰는
#        -> 소스 정리

def printHab(a,b):
    print(a,b,a+b)

#printHab(10, 20)    
#printHab(10, 200)    
#printHab(100, 200)

#def getHab(c,d):
#    return c + d
#e = getHab(10, 30)
#print(e)

# lambda : 이름없는, 1회용 -> 값 간단하게 구하기위해쓰는거
# (lambda 파라메터1,파라메터2, ... : 내용)(값1,값2)
# 내용자리에 단순한 식같은거 : return
(lambda a,b : print(a,b,a+b))(10,20)
e = (lambda c,d : c+d)(100,200)
print(e)

#def calculate(x,y):
#    a = x + y
#    b = x - y
#    c = x * y
#    d = x / y
#    return a,b,c,d
#e,f,g,h = calculate(100, 3)
#print(e,f,g,h)

a,b,c,d = (lambda x,y : ((x+y),(x-y),(x*y),(x/y)))(100,5)
print(a,b,c,d)




