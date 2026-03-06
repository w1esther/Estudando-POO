from rich import print
from rich.panel import Panel

# considere: 400g por pessoa
# preco: R$82,40/kg

class Churrasco:

    consumo_padrao = 0.4
    preco_kg = 82.40

    def __init__(self, num_pessoas):
        
        self.qntd_pessoal = int(num_pessoas)

    def qntd_carne(self):

        return Churrasco.consumo_padrao * self.qntd_pessoal
    
    def custo_carne(self):

        return Churrasco.preco_kg * self.qntd_carne()
    
    def custo_pessoa(self):

        return self.custo_carne()/self.qntd_pessoal

    def analisar(self):

        conteudo = f'Aanalisando [green]Churras dos Amigos[/] com [blue]{self.qntd_pessoal} convidados[/] \nCada participante comerá {Churrasco.consumo_padrao}kg e cada kg custa R${Churrasco.preco_kg} \nRecomendo [blue]comprar {self.qntd_carne():.3f}Kg [/] de carne \nO custo total será de [green]R${self.custo_carne():.2f}[/]\nCada pessoa pagará [yellow]R${self.custo_pessoa()}[/] para participar'

        churrasco_dos_amigos = Panel(conteudo, title='Churras dos Amigos')

        return churrasco_dos_amigos
    
c1 = Churrasco(15)
print(c1.analisar())