import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="database_name"
)
print(connection)

curser = connection.cursor()
curser.execute('SELECT *  FROM dbo.Customers')
result = curser.fetchall()

for row in result:
    pass

print(row)

curser.close()
connection.close()



print(mydb)