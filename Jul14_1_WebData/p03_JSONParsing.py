# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from json import loads
# JSON : 데이터를 JavaScript에서 객체+배열 표현하는 방식으로
# [] : JS의 배열/Python list
# {} : JS의 객체/Python dict
#######################################################
# 잘 모르겠으면 10_1_PP 다시 참고
# 1) HTTP통신 콘솔
huc = HTTPSConnection("api.openweathermap.org")
huc.request("GET","/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")
resBody = huc.getresponse().read()
# print(resBody.decode())
#######################################################

weatherData = loads(resBody) # JSON -> Python 컬렉션
# print(type(weatherData))
print(weatherData["weather"][0]["description"])
print(weatherData["main"]["temp"])
print(weatherData["main"]["humidity"])
# 날씨, 기온, 습도


huc.close()