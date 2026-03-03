from rich import print

class Funcionario:

    empresa = 'Hostnet'

    def __init__(self, nome, setor, cargo, empresa):
        
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = empresa

    def apresentacao(self):
        
        return f':wave: Olá sou [blue]{self.nome}[/] e sou {self.cargo} do setor {self.setor} da empresa {Funcionario.empresa}'
    
c1 = Funcionario('Maria', 'Administração', 'Diretora', 'Curso em Video')

print(c1.apresentacao())

c2 = Funcionario('Pedro', 'TI', 'Programador', 'Curso em Video')

print(c2.apresentacao())