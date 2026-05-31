import mysql.connector
import os
from  dotenv import load_dotenv


load_dotenv()
conexao = mysql.connector
def conectar ():
    try:
        conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        if conexao.is_connected():
             print('Conectado')
             return conexao

        
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")


def adicionar_estoque(nome, preco, quantidade, descricao):
    conexao = conectar()
    cursor = conexao.cursor()
    inserir = "INSERT INTO produto (nome, preco, quantidade, descricao) VALUES (%s, %s, %s, %s)"
    valores = (nome, preco, quantidade, descricao)

    cursor.execute(inserir, valores)
    conexao.commit()

    cursor.close()
    conexao.close()
    