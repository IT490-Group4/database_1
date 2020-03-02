import mysql.connector

print("after import")

cnx = mysql.connector.connect(user='root', password='changeme', host = 'localhost', port = 3308, database='testapp')

cursor = cnx.cursor()

if cnx.is_connected():
	print("connected to sql server")

#Creating table as per requirement
sql ='''CREATE TABLE USER(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   USERID INT,
   PASSWORD CHAR(20),
   EMAIL CHAR(50),
   CONFIRM_PASSWORD CHAR(20)
)'''

add_user = """INSERT INTO USER (FIRST_NAME, LAST_NAME, USERID, PASSWORD, EMAIL, CONFIRM_PASSWORD)
               VALUES ('Daniel', 'Drechsel', 12345, 'southpark', 'dd@gamil.com', 'southpark') """


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
	print("CONFIRM_PASSWORD  = ", row[4], "\n" )
	



#cursor.execute(sql)
#cursor.execute(add_user)

cnx.commit()

print("connection worked")

cursor.close()
cnx.close()