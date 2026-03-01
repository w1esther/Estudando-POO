from rich import print

class Caneta:

    def __init__(self, cor):
        
        self.cor_caneta = cor
        self.destampada = False

    def destampar(self):

        self.destampada = True

        return

    def escrever(self, frase):

        if self.destampada == True:

            if self.cor_caneta == 'vermelho':
                print(f'[red]{frase}[/]')
                
                return

            if self.cor_caneta == 'verde':
                print(f'[green]{frase}[/]')
                
                return

            if self.cor_caneta == 'azul':
                print(f'[blue]{frase}[/]')

                return

            else:
                print('Cor de caneta indisponível!')

        else:

            print('A caneta está tampada e não é possível escrever!')

            return
        
    def quebrar_linha(self, num):

        for n in range(num):

            print('\n')
        
c1 = Caneta('verde')
c2 = Caneta('vermelho')
c3 = Caneta('azul')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá, tudo bem?')
c1.quebrar_linha(1)
c2.escrever('Olá, Gafanhoto!')
c3.escrever('Vamos exercitar!')