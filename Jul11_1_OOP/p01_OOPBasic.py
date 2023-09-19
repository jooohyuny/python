# -*- coding:utf-8 -*-

# J : Perfect OOP
#   package(필수) > clas(필수)
# P : Hybrid OOP -> 객체지향 안하려면 안하는거
#   package(안해도) > module(필수) > class(안해도)

# 클래스명을 대문자로 시작 : Java진영 / 파이썬은 클래스명 대문자로 시작 안해도 괜찮다
# 접근제어자 없음 -> 캡슐화 없음, 패턴프로그래밍 없음
class Dog:
    name = None
    age = None
    
    def bark(self): # 메소드는 첫번째 파라메터로 self
        print("멍")
    def printInfo(self):
        print(self.name)
        print(self.age)
####################
d = Dog() # 함수를 부른건지 객체를 부른건지 혼란스럽다
d.name="후추"
d.age = 3
d.type = "푸들" #클래스 외부에서 멤버변수 추가 가능
d.bark() # 메소드 호출떄는 self는 없는취급
print(d.type)
d.bark()
