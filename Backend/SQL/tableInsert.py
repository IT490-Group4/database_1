import mysql.connector

cnx = mysql.connector.connect(user='root', password='changeme', host = 'localhost', port = 3308, database='myDB')

cursor = cnx.cursor()

if cnx.is_connected():
	print("connected to sql server")


add_user = """INSERT INTO USER (FIRST_NAME, LAST_NAME, USERID, PASSWORD, EMAIL, CONFIRM_PASSWORD)
               VALUES ('Daniel', 'Drechsel', 12345, 'southpark', 'dd@gamil.com', 'southpark') """


cursor.execute(add_user)

cnx.commit()

cursor.close()
cnx.close()