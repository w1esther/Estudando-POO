from rich import print
from rich.panel import Panel

class Produto:

    def __init__(self, nome, preco):
         
        self.nome_produto = nome
        self.preco_produto = str(preco)

    def etiqueta(self):
        
        painel_etiqueta = Panel(f'{self.nome_produto} \n ----------------------\n ........R${self.preco_produto}........', title='Produto', width=30, subtitle_align='center')

        return painel_etiqueta
    
p1 = Produto('Notebook Gamer', 9000)
p2 = Produto('Mouse', 200)

print(p1.etiqueta())
print(p2.etiqueta())