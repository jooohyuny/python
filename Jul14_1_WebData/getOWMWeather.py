# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from json import loads
from cx_Oracle import connect
#######################################
# 요청받고 JSON파싱한거 -> JSON 파싱은 파싱할때 loads를 사용
# JSON -> Python dict + list
# list : 변수명[인덱스]
# dict : 변수명[키]
#######################################
huc = HTTPSConnection("api.openweathermap.org")
huc.request("GET","/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")
resBody = huc.getresponse().read()


weatherData = loads(resBody) 

con = connect("yun/yun@195.168.9.85:1521/xe")
# DB작업 총괄객체 겸 결과객체
cur = con.cursor()

sql = "insert into owm_weather values(sysdate,"
sql += "'%s'," % weatherData["weather"][0]["description"]
sql += "%.2f," % weatherData["main"]["temp"]
sql += "%d)" % weatherData["main"]["humidity"]
# 실행
cur.execute(sql)
# 반영
con.commit()
con.close()
huc.close()