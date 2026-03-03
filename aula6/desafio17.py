from rich import print
from rich.panel import Panel

class Produto:

    def __init__(self, nome, preco):
         
        self.nome_produto = nome
        self.preco_produto = int(preco)

    def etiqueta(self):

        conteudo = f'{self.nome_produto.center(30, ' ')}'

        conteudo += f'{'-' * 30}'

        precof = f'R${self.preco_produto:.2f}'

        conteudo += f'{precof.center(30, '-')}'
        
        painel_etiqueta = Panel(conteudo, title='Produto', width=34)

        return painel_etiqueta
    
p1 = Produto('Notebook Gamer', 9000)
p2 = Produto('Mouse', 200)

print(p1.etiqueta())
print(p2.etiqueta())