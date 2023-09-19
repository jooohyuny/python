# -*- coding:utf-8 -*-

class Coffee:
    def __init__(self,line):
        line = line.split(",")
        self.name = line[0]
        self.cate = line[1]
        self.price = int(line[2])
        
    def show(self):
        print(self.name, self.cate, self.price)
#########################################################
# csv불러서 coffee객체 list로
f = open("C:/yun/coffee.csv","r",encoding= "utf-8")

coffees = []    # ArrayList<Coffee>
for line in f.readlines():
    line = line.replace("\n", "")
    c = Coffee(line)
    coffees.append(c)
    # c.show()

f.close()
#########################################################
# 1) 평균가
hab = 0
for c in coffees:   # for (coffee c : coffees)
    hab += c.price  # c.getPrice()
print("평균가:", (hab/len(coffees)))
print("-----------")

# 2) 메뉴가 총 몇 종류
print(len(coffees))    
print("-----------")
# 3) 최고가 메뉴 / 최저가 메뉴? 
coffees.sort(key=(lambda cf:cf.price), reverse=True)
coffees[0].show()
coffees[-1].show()







