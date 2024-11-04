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

coluna = 'Cidade'
valor = 'Votuporanga'

where = f"WHERE {coluna} = '{valor}'"
sql = f'DELETE FROM Cliente {where}'

mycursor.execute(sql)

mydb.commit()

if(mycursor.rowcount != 0):
    print(mycursor.rowcount, 'foram deletadas')

else:
    print('Dado inexistente ou já deletado')
