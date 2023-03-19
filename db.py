import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="alby1234"
)

c = conn.cursor()
c.execute("CREATE DATABASE demoemp")
c.close()
conn.close()