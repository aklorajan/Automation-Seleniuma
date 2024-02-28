import mysql.connector
from mysql.connector.errors import Error
from mysql.connector import errorcode

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
# --------------------------------------
try:
    cnx = mysql.connector.connect(user='scott', database='employees')
    cursor = cnx.cursor()
    cursor.execute("SELECT * FORM employees")  # Syntax error in query
    cnx.close()
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))

str(Error())
'Unknown error'

str(Error("Oops! There was an error."))
'Oops! There was an error.'
str(Error(errno=2006))
'2006: MySQL server has gone away'

str(Error(errno=2002, values=('/tmp/mysql.sock', 2)))
"2002: Can't connect to local MySQL server through socket '/tmp/mysql.sock' (2)"

str(Error(errno=1146, sqlstate='42S02', msg="Table 'test.spam' doesn't exist"))
"1146 (42S02): Table 'test.spam' doesn't exist"
# -------------------------------------------


cnx = mysql.connector.connect(user='scott', database='test')
cursor = cnx.cursor()
try:
    cursor.execute("DROP TABLE spam")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_TABLE_ERROR:
        print("Creating table spam")
    else:
        raise
# -----------------------------------------
try:
    conn = mysql.connector.connect(database="baddb")
except mysql.connector.Error as e:
    print("Error code:", e.errno)  # error number
    print("SQLSTATE value:", e.sqlstate)  # SQLSTATE value
    print("Error message:", e.msg)  # error message
    print("Error:", e)  # errno, sqlstate, msg values
    s = str(e)
    print("Error:", s)  # errno, sqlstate, msg values
