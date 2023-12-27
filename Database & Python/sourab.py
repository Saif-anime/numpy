import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="", database="mohini"
)

cursor = connection.cursor()
email = input('enter the email')
phone = int(input('enter the phone'))

e = [email]
cursor.execute("SELECT * FROM `abc` WHERE email=%s", e)
results = cursor.fetchall()



# print(results)
for row in results:
    print(row)
    if row[3] == phone:
        print("your login ")
    else:
        print('you are not login')
        

cursor.close()
connection.close()
