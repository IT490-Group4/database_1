import mysql.connector

cnx = mysql.connector.connect(user='root', password='changeme', host = 'localhost', port = 3308, database='testapp')

cursor = cnx.cursor()

if cnx.is_connected():
	print("connected to sql server")


sql_select_Query = "select * from USER"
   
cursor.execute(sql_select_Query)
records = cursor.fetchall()
print("Total number of rows in Laptop is: ", cursor.rowcount)

print("\nPrinting each User")
for row in records:
	print("FIRST_NAME = ", row[0])
	print("LAST_NAME = ", row[1])
	print("USERID= ", row[2])
	print("PASSWORD  = ", row[3])
	print("EMAIL  = ", row[4])
	print("CONFIRM_PASSWORD  = ", row[5], "\n" )


cnx.commit()


cursor.close()
cnx.close()