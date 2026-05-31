#========Sistema de estoque ==========
from databasae import conectar

estoque = []

class Produto():
    def __init__(self,  nome, preco, quantidade, descricao):
        self.nome       = nome
        self.preco      = preco
        self.quantidade = quantidade
        self.descricao  = descricao


    def adicionar(self):
        estoque.append({
            "nome" : self.nome,
            "preco" : self.preco,
            "quantidade" : self.quantidade,
            "descricao": self.descricao
        })


    def remover(self):
        for idx, item in enumerate(estoque):
            if item["nome"] == self.nome:
                estoque.pop(idx)
                

           






produto_1 = Produto( 'Controle PS5', 500.00, 5,"Voltado para PS5 original")
produto_1.adicionar()

produto_2 = Produto('Caixa de som', 700.00, 4, "Caixa de som estério")
produto_2.adicionar()









for i in estoque:
    print(i)




