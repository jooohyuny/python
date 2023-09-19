# -*- coding:utf-8 -*-
from random import randint

# 1. 가위     2. 바위    3. 보
# ----------------------
# 뭐 : 2
# 컴 : 가위
# 나 : 바위
# 승
# ---------------------- 질때까지 반복..
# 3연승 
##########################################
# print("1) 가위     2) 바위    3) 보")
# 함수 
def printRule():
    for i,h in enumerate(handTable):
        if i !=0:
            print("%d) %s" % (i,h))
def userFire():
    uh = int(input("뭐:"))
    if 0 < uh < 4:
        return uh
    return userFire()
def comFire():
    return randint(1,3)
def printHand():
    print("나 : %s" % handTable[userHand])
    print("컴 : %s" % handTable[comHand])
def judge():
    t = userHand - comHand
    if (t == 0):
        print("무승부")
        return 0
    elif t == -1 or t == 2:
        print("유저 패 ")
        return 12345
    else:
        print("유저 승 ")
        return 1
##########################################
handTable,win = [None,"가위","바위","보"],0
printRule()
while True:
    print("----------")
    userHand, comHand = userFire(),comFire()
    printHand()
    
    result = judge()
    if result == 12345:
        break

    win += result
    
print("%d연승" % win)









