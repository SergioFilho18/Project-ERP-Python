import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'project_erp'
)

mycursor = mydb.cursor()


### INSERINDO NA TABELA ###
print('INSERT CLIENTE')

nome = 'Sergio'
telefone = '9999999'
cidade = 'VotuMilGrau'

if(nome != '' and cidade != ''):
    sql = "INSERT INTO Cliente (Nome, Telefone, Cidade) values (%s, %s, %s)"
    values = (nome, telefone, cidade)
    mycursor.execute(sql, values)
elif nome == '' and cidade == '':
    print('Preencha o campo nome e cidade')
elif nome == '':
    print('Preencha o campo nome')
elif cidade == '':
    print('Preencha o campo cidade')


mydb.commit()

if(mycursor.rowcount > 0):
    print(mycursor.rowcount, 'foram inseridas')
