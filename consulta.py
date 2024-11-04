import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'project_erp'
)

mycursor = mydb.cursor()


### CONSULTA TABELA ###
print('CONSULTA TABELA CLIENTE')

consulta = 'SELECT * FROM Cliente'

mycursor.execute(consulta)
myresult = mycursor.fetchall()

for line in myresult:
    print('line: ', line)