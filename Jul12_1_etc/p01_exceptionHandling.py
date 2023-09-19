# -*- coding:utf-8 -*-
#
# error : 문법에 안맞게 써서, 기계어로 번역(compile)이 불가능한 상태
#        최종산출물이 안나옴 -> 실행불가
# warning : 지저분한 소스, 정리가 안된 소스
#        실행은 가능
# exception : 프로그램은 문제없이 완성
#           실행때 뭔가 잘못되어서 정상 진행이 안되는 상황

# error vs EXCEPTION

# .java -compile-> .class -압축-> .jar -실행->
#       error                        exception
# Python은 interpreter방식이라서 error/exception 구별이...

# J : 예외처리 필수
#        try-catch-finally(직접처리), throws(처리를 호출한 쪽에서)
# P : 예외처리 필수 아님
#        try-except-else-finally
# try:
#     x = int(input("x : "))
#     y = int(input("y : "))
#     z = x / y
#     print(z)
#     
#     l = [10,20,30]
#     print(l[y])
# except ZeroDivisionError:
#     print("나누기 0은 없다")
#     
# except IndexError:
#     print("리스트에 없는거")

try:
    x = int(input("x : "))
    y = int(input("y : "))
    z = x / y
    print(z)
     
    l = [10,20,30]
    print(l[y])
except Exception as e:
    print(e) # e.printStackTrace();
else:
    print("문제없으면")
finally:
    print("문제 있든 없든 리턴보다 먼저")









