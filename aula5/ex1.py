class Gafanhoto:
    """
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade

    Para criar uma nova pessoa, use:
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = '', idade = 0): 

        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade = self.idade + 1

    # def mensagem(self):
        # return f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade'
    
    def __str__(self):
        return f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade'
    
    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'

g1 = Gafanhoto('Esther', 16) 
g1.aniversario()

# print(g1.mensagem())

g2 = Gafanhoto('Maria', 15)
# print(g2.mensagem())

g3 = Gafanhoto('Lucas', 14)
# print(g3.mensagem())

# print(g1.__doc__)
# print(g1.__dict__)
# print(g1.__class__)

print(g1)
print(g2)
print(g3)

# print(g1.__getstate__())