from rich import print
from rich.table import Table

class Produto:

    def __init__(self, nome, preco):
        
        self.nome = nome
        self.preco = float(preco)

    def __str__(self):
        
        return f'{self.nome} - R${self.preco:.2f}'
    
class Pedido:

    def __init__(self):

        self.lista_produtos = []

    def adicionar_produto(self, produto):

        self.lista_produtos.append(produto)

    def calcular_total(self):

        total = 0

        for produto in self.lista_produtos:
            total += produto.preco

        return total
    
    def listar_itens(self):

        tabela_itens = Table(title='Tabela de Produtos')

        tabela_itens.add_column('#', justify='center')
        tabela_itens.add_column('nome', justify='center')
        tabela_itens.add_column('preço', justify='center')

        i = 1

        for produto in self.lista_produtos:

            tabela_itens.add_row(str(i), produto.nome, f'{produto.preco:.2f}')

            i += 1

        return tabela_itens

class Lanchonete:

    def __init__(self):

        self.pedidos = [] 
        
    def novo_pedido(self):

        pedido = Pedido()
        self.pedidos.append(pedido)
        return pedido
    
    def listar_pedidos(self):

        tabela_pedidos = Table(title='Tabela de Produtos')

        tabela_pedidos.add_column('#', justify='center')
        tabela_pedidos.add_column('Qntd Itens', justify='center')
        tabela_pedidos.add_column('Total', justify='center')

        i = 1

        for pedido in self.pedidos:

            qntd_itens = len(pedido.lista_produtos)
            total = pedido.calcular_total()

            tabela_pedidos.add_row(str(i), str(qntd_itens), f'R${total:.2f}')

            i += 1

        return tabela_pedidos

lanche = Lanchonete()

p1 = Produto("X-Burguer", 12)
p2 = Produto("Suco", 5)
p3 = Produto("Batata Frita", 8)
p4 = Produto("Pizza", 30)

pedido1 = lanche.novo_pedido()
pedido1.adicionar_produto(p1)
pedido1.adicionar_produto(p2)

pedido2 = lanche.novo_pedido()
pedido2.adicionar_produto(p3)
pedido2.adicionar_produto(p4)

print("\n[bold cyan]PEDIDOS DA LANCHONETE[/bold cyan]")
print(lanche.listar_pedidos())

print("\n[bold green]ITENS DO PEDIDO 1[/bold green]")
print(pedido1.listar_itens())

print("\n[bold magenta]ITENS DO PEDIDO 2[/bold magenta]")
print(pedido2.listar_itens())