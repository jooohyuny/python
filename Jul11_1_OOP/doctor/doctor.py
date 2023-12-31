# -*- coding:utf-8 -*-
# package(doctor) > module(doctor) > class(doctor)
from guest.guest import guest 


class doctor:
    def start(self):
        g = self.callGuest()
        self.ask(g)
        self.calculate(g)
        self.tellResult(g)
    def callGuest(self):
        return guest()
    
    def ask(self,g):
        g.name = g.tellName()
        g.height = g.tellHeight()
        if g.height > 3:
            g.height /= 100
        g.weight = g.tellWeight()
        
    def calculate(self,g):
        g.bmi = g.weight/(g.height * g.height)
    
        g.status ="저체중";
        if g.bmi >=35 :
            g.status = "고도비만"
        elif g.bmi>=30 : 
            g.status = "중도비만"
        elif g.bmi>=25 :
            g.status = "경도비만"
        elif g.bmi>=23 :
            g.status = "과체중" 
        elif g.bmi>=18.5 :
            g.status = "정상"
        
    
    def tellResult(self, g):
        print("BMI : %.1f" % g.bmi)
        print("%s씨는  %s" % (g.name, g.status))








        