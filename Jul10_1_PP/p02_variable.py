# -*- coding:utf-8 -*-

# Java : 규칙 -> 소스보기 편함
#        저급언어 -> 컴퓨터 친화적(효율적인 프로그램)
# Python : 자유 -> 혼돈
#        고급언어 -> 사람 친화적(개발 편함)

# Java : 저급언어(사람이 컨트롤)
#       데이터 특징 파악해서 최적의 자료형 찾기

# Python : 고급언어(언어 자체적으로 자동 처리)
#    자료형 자동
#    기본형 X, 전부 다 객체

#Python의 int == Java의 Integer(int가 아님) 
a = 10

print(a)
print(type(a)) # 자료형
print(id(a)) # heap영역 주소값

a = "ㅋ" # a = new String("ㅋ");
print(a)
print(type(a)) 
print(id(a))

a = 20

if(a>10):
    b=30
print(b)