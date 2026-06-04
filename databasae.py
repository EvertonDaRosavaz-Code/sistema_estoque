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
    

def consultar_estoque():
    conexao = conectar()
    cursor = conexao.cursor()
    slq = "select * FROM produto"
    cursor.execute(slq)
    resultado = cursor.fetchall()
    
    return resultado
    



def remover_estoque(nome):
    conexao = conectar()
    cursor = conexao.cursor()
    buscar_id = f"select * from produto where nome like '%{nome}%'"

    cursor.execute(buscar_id)
    resultado = cursor.fetchall()
    id_produto = resultado[0][0]
    print(id_produto)
    sql_deletar = f"DELETE FROM produto WHERE id = {id_produto}"

    cursor.execute(sql_deletar)    
    conexao.commit()
    
    cursor.close()
    conexao.close()

