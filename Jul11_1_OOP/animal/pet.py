# -*- coding:utf-8 -*-

class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def showInfo(self):
        print(self.name, self.age)

class cat:
    def showInfo(self):        
        print("고양이")
######################################
if __name__ == "__main__":
    from animal.wild import tiger
    t = tiger("호랑이",14)
    t.show()
            
print("ㅋ")
# Python의 import는
# 그 자리에 소스가 들어가는 거
# main이 따로 없는 interpreter방식언어
# => 그냥 실행 다 됨

# if __name__ == "__main__":
#     여기서 실행했을때
#     import당했을때 말고













