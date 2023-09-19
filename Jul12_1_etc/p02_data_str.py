# -*- coding:utf-8 -*-

s = "글자,글자"
print(type(s))

s2 = """
    ㅋㅋㅋ
    ㅎㅎㅎ
    ㅅㅅㅅ
"""
print(s2)
print(type(s2))
print("---------")
class dog:
    """
    강아지...
    """
    def bark(self):
        """
         짖는거 
        """
        print("멍")
help(dog)
help(print)
print("---------")

s = "자 그래서 자바때 이것저것  하던거나"
print(s.startswith("자")) # '자'로 시작하나
print(s.replace("자바", "java")) # 자바 -> java
print(s[2]) # 세번째 글자
print(len(s)) # 총 글자 수
print(s.find("하던거")!=-1) # '하던거'가 포함되나

s2 = "        가나다                "
print(s2.strip()) # 앞/뒤 띄어쓰기 없애기
s3 = "ㅋㅋㅋㅋㅋㅋㅋㅋㅋ가나다ㅋㅋㅋㅋㅋㅋㅋㅋ"
print(s3.strip("ㅋ")) # 앞/뒤 불필요한거("ㅋ") 없애기

# String.format("%d",10)
s4 = "키 : %d, 몸무게 : %d" % (180,80)
print(s4)
############################################
# 문자열 붙이기
# J : StringBuffer
# P : 메모리 효율 -x
s5 = "가"
s5 += "나"
s5 += "다"
print(s5)
############################################
# 문자열 분리
# J :
#    s6.split(",") -> [] -> 정형데이터에 유리
#    StringTokenizer -> while -> 비정형데이터에 유리
# P :

s6 = "가,나,다"
s6list = s6.split(",")
for s66 in s6list:
    print(s66)










