# -*- coding:utf-8 -*-rm

class Coffee:
    name = None
    price = None

    def __init__(self):
        print("커피생성")
        
    def __del__(self):
        print("커피없어짐")
            
    def printInfo(self):
        print(self.name, self.price)
###########################
c = Coffee()
c.name = "아메리카노"
c.price = 4000
c.printInfo()

c2 = Coffee()
c2.name = "카페라떼"
c2.price = 5000
Coffee.printInfo(c2)

c3 = c
c3.name = "아메리카노  + 샷"
c3.printInfo()

c.printInfo()

c = None
c3 = None
c2 = None
print("ㅋㅋㅋㅋㅋㅋㅋ")

# static/stack : 프로그램 종료되면 메모리 정리
# heap : 메모리는 수동으로 정리해야

# Garbage Collection : heap영역 자동정리 시스템
#    그 자동이 언제 : 그 번지 더이상 못쓰게 되면
#    Java/Python개발자는 메모리 관리 몰라도 되지만 알고 있으면 좋다
#    BD/AI에서는...


