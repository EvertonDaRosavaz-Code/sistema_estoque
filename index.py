#========Sistema de estoque ==========
from databasae import conectar, adicionar_estoque, consultar_estoque, remover_estoque

conectar()


#Codigo do estoque sem o banco de dados
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

        adicionar_estoque(self.nome, self.preco, self.quantidade, self.descricao)

    def remover_estoque(self):
        for indice, elemento in enumerate(estoque):
            if elemento["nome"] == self.nome:
                estoque.pop(indice)

       
        remover_estoque(self.nome)
                


def consultarEstoque():
    lista_estoque  = consultar_estoque() 
    for i in lista_estoque:
        print(f'Id: {i[0]} | Produto: {i[1]} | Preço: {i[2]} | Quantidade: {i[3]} | Descrição: {i[4]}')
    

consultarEstoque()
           
produto_1 = Produto( 'Controle PS5', 500.00, 5,"Voltado para PS5 original")
produto_2 = Produto('Caixa de som', 700.00, 4, "Caixa de som estério")
produto_3 = Produto('Boneco Homem-Aranha' , 49.90 , 100 , "Boneco do Homem-aranha coleção")
produto_4 = Produto('Mochila do Hulk', 59.90, 250, "Mochila do Hulk com estojo e varios bolsos e acessórios")
produto_5 = Produto('Mochila da Barbie', 59.90, 48, "Mochila edição especial da barbie com kit de maquiagens")
produto_6 = Produto('Monitor Lg Ultra Gear', 600.00, 5.000, "Monitor LG UltraGear™ 24G411A-B 24 FHD 144Hz 1ms (MBR) NVIDIA G-SYNC AMD FreeSync HDR10")


