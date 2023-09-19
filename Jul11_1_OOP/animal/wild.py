# -*- coding:utf-8 -*-

# import
#     Java타입
#     Python타입 : 필수사항
class tiger:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        
    def show(self):
        print(self.name, self.age)
###############################
if __name__ == "__main__":
    from animal.pet import dog
    d = dog("후추",2)    
    d.showInfo()    
