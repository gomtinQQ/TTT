# import os
# import pandas as pd
# import requests
# import pymysql
# import json


# server_url= "http://15.165.21.105:5000/stockcodes?market=kosdaq"
# # server_url= "http://15.165.21.105:5000/stockcodes?market=kospi"

# result = requests.get(server_url).json()
# # result_dict = json.loads(result)
# result_key = result.keys()
# # print(result_dict.keys())
# conn = pymysql.connect(host="3.34.96.193", user="ttt", password="a105A!)%",
#                        db="TTT", charset="utf8")  # 1. DB 연결
# cur = conn.cursor() # 2. 커서 생성 (트럭, 연결로프)

# for tablename in result_key:
#     # sql = "CREATE TABLE IF NOT EXISTS TTT."+tablename+ "( pk INT NOT NULL, date DATETIME NULL,  open INT NULL, high INT NULL,low INT NULL, close INT NULL, PRIMARY KEY (pk),UNIQUE INDEX date_UNIQUE (date ASC) VISIBLE) ENGINE = InnoDB;"
#     # sql = "ALTER TABLE TTT."+tablename+ " CHANGE COLUMN `pk` `pk` INT NOT NULL AUTO_INCREMENT ;"
#     cur.execute(sql) 

# conn.commit() 



