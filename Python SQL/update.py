import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='project_erp'
)

mycursor = mydb.cursor()

### UPDATE NA TABELA ###
print('UPDATE CLIENTE')

### VARIÁVEIS ###
column = 'Cidade'
ColValue = 'Valentim Gentil'
where = 'IDCliente'
WValue = '8'

# Verifica se todos os campos obrigatórios estão preenchidos
if not (column and where and ColValue and WValue):
    
    if not column:
        print("Preencha o campo 'coluna'")
    if not where:
        print("Preencha o campo 'where'")
    if not ColValue:
        print("Preencha o campo 'valor da coluna'")
    if not WValue:
        print("Preencha o campo 'valor do where'")
else:
    sql = f'UPDATE Cliente SET {column} = %s WHERE {where} = %s'
    values = (ColValue, WValue)
    mycursor.execute(sql, values)

    mydb.commit()

    if mycursor.rowcount > 0:
        print(mycursor.rowcount, 'linha(s) foram atualizadas')
    else:
        print('Nenhuma linha foi atualizada')
