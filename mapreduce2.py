import mysql.connector
import csv
import os
import functools
import time

mydb = mysql.connector.connect(
    host="localhost",
    user="hello",
    passwd='',
    database='db'
)
start_time=time.time()
mycursor = mydb.cursor()

mycursor.execute("select id,topic from MOCK_DATA")
data=[]
freq={}
for row in mycursor:
    data.append(row[1])
    if row[1] in freq:
        freq[row[1]]+=1
    else:
        freq[row[1]]=1
f=[]
for key in freq:
    f.append((key,freq[key]))
f.sort(key=lambda x:x[1],reverse=True)
print(f[:20])
print(time.time()-start_time," nano seconds")



