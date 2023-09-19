# -*- coding:utf-8 -*-

# 메뉴
# 메뉴명이 김치찌개    #가격이 9000원    #정보출력
class Menu:
    name = None
    price = None
    
    # constructor(생성자)
    #     overloading이 안되니 -> 생성자는 하나만 가능
    # def __init__(self):
    #    print("메뉴객체 만들어짐")
    #    print("생성자 전혀 건들지 않으면 자동으로")
    
    def __init__(self,n,p):
        self.name = n
        self.price = p
    
    # destructor(소멸자)
    def __del__(self):
        print("메뉴객체 없어짐")
        
    def printMenu(self):
        print(self.name, self.price)

# 멤버변수 써봐야 의미가 없고(외부에서 넣을수있으니)
# 메소드는 정해진대로 쓰고        
# Overloading이 안되니 생성자는 하나만 가능하고
# => 생성자에서 멤버변수를 결정하는 경향이...
class Product:        
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def __del__(self):
        print("상품객체 없어짐")

    def showInfo(self):
        print(self.name, self.price)
##############################        
p = Product("종이컵",300)
p.showInfo()

m = Menu("김치찌개",9000)
m.printMenu()







