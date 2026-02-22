from rich import print
from rich.panel import Panel

# considere: 400g por pessoa
# preco: R$82,40/kg

class Churrasco:

    def __init__(self, num_pessoas):
        
        self.qntd_pessoal = str(num_pessoas)

    def analisar(self):

        pessoas = int(self.qntd_pessoal)

        qntd_carne = 0.4 * pessoas

        custo_carne = 82.40 * qntd_carne

        custo_participante = custo_carne/pessoas

        churrasco_dos_amigos = Panel(f'Aanalisando [green]Churras dos Amigos[/] com [blue]{pessoas} convidados[/] \nCada participante comerá 0.4kg e cada kg custa R$82.40 \nRecomendo [blue]comprar {qntd_carne:.3f}Kg [/] de carne \nO custo total será de [green]R${custo_carne:.2f}[/]\nCada pessoa pagará [yellow]R${custo_participante}[/] para participar', title='Churras dos Amigos')

        return churrasco_dos_amigos
    
c1 = Churrasco(15)
print(c1.analisar())