import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1838',
    database='SistemaSupermercado',
)

cursor = conexao.cursor()
