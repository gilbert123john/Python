import mysql.connector

mydb = mysql.connector.connect(host = "localhost",user="root",password = "",database = "newPythonDb")
# print(mydb)
cursor = mydb.cursor()
# cursor.execute("CREATE DATABASE newPythonDb")
# cursor.execute("SHOW DATABASES")
# for x in cursor:
#   print(x)

# cursor.execute("CREATE TABLE pythonOne (name VARCHAR(255), user_name VARCHAR(255))")
# sql = "INSERT INTO pythonOne (name, user_name) VALUES (%s, %s)"
# val = ("Gilbert", "Unknown")
# cursor.execute(sql, val)

# mydb.commit()

# print(cursor.rowcount, "record inserted.")


cursor.execute("SELECT * FROM pythonOne")

myresult = cursor.fetchall()

for x in myresult:
  print(x)