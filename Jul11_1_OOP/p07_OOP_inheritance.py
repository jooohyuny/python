# -*- coding:utf-8 -*-

# J : 
# P : 
class Avengers:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def attack(self):
        print("공격")
        
    def show(self):
        print(self.name, self.age)    
#########################
class Ironman(Avengers):
    # overriding? or overloading?
    # 결국 새로만든... -> 이럴거면 자바가 상속을 안시켰을것..
    def __init__(self, name, age, ai):
        super().__init__(name, age)
        # Avengers.__init__(self, name, age)
        self.ai = ai
        
    def show(self):
        Avengers.show(self)
        print(self.ai)
#########################
class Human:
    
    def __init__(self, home):
        self.home = home
        
    def eat(self):
        print("밥먹기")
        
    def show(self):
        print(self.home)
#########################
class Hulk(Avengers):
    def __init__(self, name, age, pantsSize):
        Avengers.__init__(self, name, age)
        self.pantsSize = pantsSize
        
    def show(self):
        Avengers.show(self)
        print(self.pantsSize)
#########################
# Java : 다중상속x
# Python : 다중상속 가능
#        Avengers/Human 메소드명 같으면?
#        먼저 상속받은걸로 쳐줌
#        다중상속...?
class Spiderman(Avengers,Human):
    pass
#########################
class CaptainAmerica(Avengers,Human):
    def __init__(self,n,a,h):
        Avengers.__init__(self, n, a)
        Human.__init__(self, h)
    
    def show(self):
        Avengers.show(self)
        Human.show(self)
#########################
# 생성자가 상속됨
#    Avengers - 이름, 나이
#    Human    - 기본
#########################
c = CaptainAmerica("스티브",80,"버지니아")
c.show()
print("-----------")
s = Spiderman("피터",20)
s.attack()
s.eat()
s.show()
print("-----------")
i = Ironman("토니",30,"자비스")
i.attack()
i.show()
print("-----------")
h = Hulk("베너", 25, 40)
h.attack()
h.show()
# p : 생성자 상속됨
# overriding : 물려받은 메소드 재정의
# overloading : 함수명 같게, 파라메터 다르게

# OOP : 상속(상위클래스 기능 물려받고, 기능 추가)
