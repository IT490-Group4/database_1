import mysql.connector

cnx = mysql.connector.connect(user='root', password='changeme', host = 'localhost', port = 3308, database='myDB')

cursor = cnx.cursor()

if cnx.is_connected():
	print("connected to sql server")

#Creating table as per requirement
sql ='''CREATE TABLE REGISTRATION(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   USERNAME CHAR(20),
   PASSWORD CHAR(20),
   EMAIL CHAR(50),
   CONFIRM_PASSWORD CHAR(20)
)'''

cursor.execute(sql)


cursor.close()
cnx.close()