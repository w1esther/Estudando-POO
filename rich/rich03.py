from rich import print
from rich.table import Table

tabela  = Table(title='tabela de preços')

tabela.add_column('nome', justify='center')
tabela.add_column('preço', justify='center')
tabela.add_column('cor', justify='center')
tabela.add_row('borracha', 'R$2.00', 'rosa')
tabela.add_row('lápis', 'R$1.50', 'rosa')

print(tabela)