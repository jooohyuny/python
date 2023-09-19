# -*- coding:utf-8 -*-

x = int(input('x :'))
y = int(input('y :'))
a = x+y
b = x-y
c = x*y
d = x/y
e = x%y
print(a,b,c,d,e)
print('--------------')
print(x + y)
# Java : 뭐  + String -> 붙여서 String
# Python : x (str끼리만 가능) 
# print(x + "ㅋ") 
print("ㅋ" + "ㅎ")
print('--------------')
# Java : x (error)
# Python : str * 숫자 -> 반복
print(x * y)
print(x * "ㅋ")
print('--------------')
# Java : int / int -> int 
# Python : ? / ? -> 알아서 소수점 살림 
print(x / y)
print(x // y) # Java에서 쓰던 /
print('--------------')

# x값 5증가
x += 5 # x = x + 5
print(x)

# 글자 1글자 => 프로그램 용량 2byte씩 늘어난다
# Python : 효율성x, 사람이 편하자
#         => 대체품이 있으면 삭제
#         => 공부할거리가 줄어듬

# ++ -- 없음
# y값 1감소
# y = y - 1   
y -= 1      
# y--        
print(y)