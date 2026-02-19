# declaração de classe

class Gafanhoto:
    def __init__(self): # método construtor 

        # atributos de instância

        self.nome = ''
        self.idade = 0

    #métodos de instância

    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade'

# Declaração de Objetos

g1 = Gafanhoto() 

g1.nome = 'Esther'
g1.idade = 16
g1.aniversario()

print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Maria'
g2.idade = 15

print(g2.mensagem())