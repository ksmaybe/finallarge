import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="hello",
  passwd='',
  database='db'
)

mycursor = mydb.cursor()
# lst=[]
# with open('MOCK_DATA (1).csv') as f:
#   reader=csv.reader(f,delimiter=',')
#   for row in reader:
#     lst.append(row)
#
# print(lst[1])
# sql="insert into brands (id,name) values (%s,%s)"
# for row in lst[1:]:
#   val=(row[0],row[1])
#   mycursor.execute(sql,val)

# mydb.commit()
mycursor.execute("select * from MOCK_DATA")
for row in mycursor:
  print(row[0],row[1])