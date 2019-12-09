import csv
import time

lst=[]
with open('MOCK_DATA (1).csv') as f:
  reader=csv.reader(f,delimiter=',')
  for row in reader:
    lst.append(row)

def most_common(lst):
    d={}
    for s in lst:
        if s[1] not in d:
            d[s[1]]=1
        else:
            d[s[1]]+=1
    lst2=[]
    for key in d:
        lst2.append([key,d[key]])
    lst2.sort(key=lambda x:x[1],reverse=True)
    for j in lst2:
        print(j)
t1_start=time.perf_counter()
most_common(lst*100000)
t1_stop=time.perf_counter()
print("Elapsed time during the whole program in seconds:",
                                        t1_stop-t1_start)
