#========Sistema de estoque ==========
from databasae import conectar, adicionar_estoque, consultar_estoque, Remover_estoque, editar_estoque

conectar()



class Produto():
    def __init__(self,  nome, preco, quantidade, descricao):
        self.nome       = nome
        self.preco      = preco
        self.quantidade = quantidade
        self.descricao  = descricao


    def adicionar(self):
        adicionar_estoque(self.nome, self.preco, self.quantidade, self.descricao)

  
        

def consultarEstoque():
    lista_estoque  = consultar_estoque() 
    for i in lista_estoque:
        print(f'Id: {i[0]} | Produto: {i[1]} | Preço: {i[2]} | Quantidade: {i[3]} | Descrição: {i[4]}')
    


        
#Apresentação para o usuário interagir
print("=" * 45)
print("   🗄️  SISTEMA DE ESTOQUE - BEM VINDO!  🗄️")
print("=" * 45)
print()
print("  O que deseja fazer?")
print()
print("  [1] 📦 Cadastrar produto")
print("  [2] 📋 Listar produtos")
print("  [3] ✏️  Editar produto")
print("  [4] 🗑️  Remover produto")
print("  [0] 🚪 Sair")
print()
print("=" * 45)



while True:
    escolha = int(input('Numero:'))
    if escolha == 1:

        nome = input('Nome: ')
        valor = input('Valor: ')
        quantidade = input('Quantidade: ')
        descricao = input('Descrição: ')

        produto = Produto(nome,valor,quantidade, descricao)
        produto.adicionar()

        #=-=-=-=-=-=-=-=-=-=-=-=-=-
        sair  = int(input('Sair:(0)'))
        if sair == 0: break
        #=-=-=-=-=-=-=-=-=-=-=-=-=-

    elif escolha == 2:
        consultarEstoque()

        #=-=-=-=-=-=-=-=-=-=-=-=-=-
        sair  = int(input('Sair:(0)'))
        if sair == 0: break
        #=-=-=-=-=-=-=-=-=-=-=-=-=-

    elif escolha == 3:
        nome = input('Nome do produto na qual vai editar: ')
        editar_estoque(nome)

        #=-=-=-=-=-=-=-=-=-=-=-=-=-
        sair  = int(input('Sair:(0)'))
        if sair == 0: break
        #=-=-=-=-=-=-=-=-=-=-=-=-=-

    elif escolha == 4:
        name = input('Nome do produto na qual quer remover : ')
        Remover_estoque(name)

        #=-=-=-=-=-=-=-=-=-=-=-=-=-
        sair  = int(input('Sair:(0)'))
        if sair == 0: break
        #=-=-=-=-=-=-=-=-=-=-=-=-=-

    