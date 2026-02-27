from rich import print
from rich.table import Table

class Gamer:

    def __init__(self, nome, nick):
        
        self.nome = nome
        self.nick = nick
        self.lista_favoritos = []

    def add_favoritos(self, jogo_fav):

        self.lista_favoritos.append(jogo_fav)

    def ficha(self):

        ficha_favs = Table(title=None)

        ficha_favs.add_column(f'Jogador {self.nick}')

        ficha_favs.add_row(f'nome rela: {self.nome}')

        ficha_favs.add_row('Jogpos favoritos:')

        for jogo in self.lista_favoritos:

            ficha_favs.add_row(jogo)

        print(ficha_favs)

        return
    
j1 = Gamer('Olivia Souza', 'jogadora_souza')
j1.add_favoritos('Mario Boss')
j1.add_favoritos('Call of Duty')
j1.ficha()