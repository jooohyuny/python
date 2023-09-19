# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring

# https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1111061500

huc = HTTPSConnection("www.kma.go.kr")
huc.request("GET","/wid/queryDFSRSS.jsp?zone=1111061500")
resBody = huc.getresponse().read()
####################################
# XML파싱
kmaData = fromstring(resBody)
weathers = kmaData.getiterator("data")  #<data></data>들
                                        # $(kmaData).find("data")
for w in weathers:
    print("시간 : " + w.find("hour").text)    #<hour>18</hour>
    print("온도 : " + w.find("temp").text)    #<temp>26.0</temp>
    print("날씨 : " + w.find("wfKor").text)    #<wfKor>비</wfKor>

huc.close()

