import mysql.connector
def conectar ():
    try:
        conexao = mysql.connector.connect(
            host="localhost",        
            user="root",
            password="98057640Fbo@",
            database="estoque"
        )

        if conexao.is_connected():
            return print('Conectado')

        
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")



