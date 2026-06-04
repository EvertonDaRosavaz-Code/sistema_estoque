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
    

def Remover_estoque(nome):
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

def editar_estoque(nome):
    #Para editar vamos fazer com que o usuario procure o produto pelo nome
    conexao  = conectar()
    cursor = conexao.cursor()


    #================Pegar o ID pro produto============================
    slq_GetidProduto = f"select * from produto where nome like '%{nome}%'"
    cursor.execute(slq_GetidProduto)
    resultado_Id = cursor.fetchall()
   
    #==================================================================

    #Tratar erro caso o nome ditado pelo usuário nao exista no banco de dados
    if len(resultado_Id) == 0:
        print(f'Nome "{nome}" não encontrado no banco de dados')
        return


    #=======Mostrar os dados na tela para orientar o usuário============
    slq_Getproduto = f"select * from produto where  id = {resultado_Id[0][0]}"
    cursor.execute(slq_Getproduto)
    resultado_Produto = cursor.fetchall()
    for i in resultado_Produto:
        print(f'Id: {i[0]} | Produto: {i[1]} | Preço: {i[2]} | Quantidade: {i[3]} | Descrição: {i[4]}')
    #==================================================================
   

   


    print('Dos dados acima do produto, qual alteração fazer?')
    print('1 - Nome')
    print('2 - Preço')
    print('3 - Quantidade')
    print('4 - Descrição')
    numero = int(input('Escolha:'))
    

    if numero == 1:

        new_name = input("Novo nome do produto:")
        new_sql = f"UPDATE produto SET nome = '{new_name}' WHERE id = {resultado_Id[0][0]}"

        cursor.execute(new_sql)
        conexao.commit()
        conexao.close()


    elif numero == 2:

        new_preco = input("Preço do produto:")
        new_sql = f"UPDATE produto SET preco = '{new_preco}' WHERE id = {resultado_Id[0][0]}"

        cursor.execute(new_sql)
        conexao.commit()
        conexao.close()


    elif numero == 3:

        new_quantidade = input("Nova quantidade do produto:")
        new_sql = f"UPDATE produto SET quantidade = '{new_quantidade}' WHERE id = {resultado_Id[0][0]}"

        cursor.execute(new_sql)
        conexao.commit()
        conexao.close()


    elif numero == 4:

        new_descricao = input("Nova descrição do produto:")
        new_sql = f"UPDATE produto SET descricao = '{new_descricao}' WHERE id = {resultado_Id[0][0]}"

        cursor.execute(new_sql)
        conexao.commit()
        conexao.close()

