import mysql.connector
import csv
import os
import functools
import time
import collections

def chunkify(lst,number_of_chunks):
    return [ lst[i::number_of_chunks] for i in range(number_of_chunks)]

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

data_chunks=chunkify(data,number_of_chunks=36)
def mapper(str):
    return len(str)
mapped=map(mapper,data)
mapped=zip(data,mapped)
def reducer():
    pass
reduced=functools.reduce(reducer,mapped,)
cnt=collections.Counter()
for word in data:
    cnt.update(word)

print(cnt.most_common(20))

print(time.time()-start_time," nano seconds")





