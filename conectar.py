import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    database='mega',
    user='root',
    password=''
)

if conexao.is_connected():
    print(f'Conectado a {conexao.get_server_info()}')

cursor = conexao.cursor()
cursor.execute('select database();')
linha = cursor.fetchone()
print(f'Banco => {linha[0]}')