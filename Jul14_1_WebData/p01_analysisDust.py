# -*- coding:utf-8 -*-
from cx_Oracle import connect

con = connect("yun/yun@195.168.9.85:1521/xe")
cur = con.cursor()

sql = "select sd_MSRRGN_NM , avg(sd_pm10 + sd_pm25) "
sql += "from seoul_dust  "
sql += "group by sd_MSRRGN_NM "
sql += "order by sd_MSRRGN_NM"

cur.execute(sql)
for msrrgn_nm, dust in cur:
    print(msrrgn_nm, dust)
    
cur.close()
con.close()   
