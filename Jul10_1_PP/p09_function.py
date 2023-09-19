# -*- coding:utf-8 -*-

# 1) 함수정의 
# def 함수명(변수명=기본값, 변수명=기본값 ... ):
#    내용
#    return 값

def yaDamdae():
    print("슈퍼 가서")
    print("믹스 콤보사와")
    
def test():
    print("ㅋㅋ")

# : 뒤에 무조건 들여쓰기 들어가야된다           
def test2():
    pass #들여쓰기 자리 차지

def printHab(x=1,y=2):
    print(x)
    print(y)
    print(x + y)
    
def funcTest(a=10,b=20,c=30):
    print(a,b,c)
# 함수 overloading : 함수명 같게, 파라메터 다르게
# 함수 기본값/자료형 안쓰고 -> overloading없음
# 정수 2개 넣으면 더 큰 숫자 출력하는 함수
def printBigger(a=10,b=20):
    if(a>b):
        print(a)
    else:
        print(b)    
# 정수 3개 넣으면 가장 큰 숫자 출력하는 함수
def printBigger2(a=10,b=20,c=30):
    pass
# 정수 2개 넣으면 합을 구해서 출력하는 함수
def calculate(x,y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return (a,b,c,d)
# 문장 하나 넣으면, 첫번째글자/마지막글자 구하는 함수
def getFL(txt):
    result = (txt[0], txt[-1])
    return result
    # 사실은 tuple하나 -> 리턴 여러개같이 생김
#############################    
# 2) 함수호출
# 함수명(값, 값, ...)
# 함수명(변수명=값, 변수명=값, ...)
# aa = calculate(30, 50)
# print(aa,type(aa))
fl = getFL('첫번째글자부터마지막글자')
print(fl,type(fl))

f, l = getFL("마바사아")
print(f)
print(l)

yaDamdae()
test()
printHab(10, 20)
printHab(y=100, x=50)
printHab()
printHab(y=10)
funcTest()
funcTest(b=200,c=300,a=100)
funcTest(1000,c=3000)

aa,bb,cc,dd= calculate(30, 50)
print(aa)
print(bb)
print(cc)
print(dd)
