import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'project_erp'
)

mycursor = mydb.cursor()


### DELETE TABELA ###
print('DELETE CLIENTE')

where = "WHERE IDCliente = '2'"
sql = f'DELETE FROM Cliente {where}'

mycursor.execute(sql)

mydb.commit()

if(mycursor.rowcount != 0):
    print(mycursor.rowcount, 'record(s) deleted')

else:
    print('Dado inexistente ou já deletado')
