class Aluno:
    def __init__(self):
        
        self.nome = ''
        self.nota = 0

    def mostrar_dados(self):
        return f'o nome do aluno(a) é: {self.nome} e sua nota é: {self.nota}'
    
    def situacao(self):
        if self.nota >= 7:
            return 'Aprovado'
        
        elif 5<= self.nota < 7:
            return 'Prova final'
        
        elif self.nota < 5:
            return 'Reprovado'
        
a1 = Aluno()
a1.nome = 'Esther'
a1.nota = 10

print(a1.mostrar_dados())
print(a1.situacao())

a2 = Aluno()
a2.nome = 'Caio'
a2.nota = 6

print(a2.mostrar_dados())
print(a2.situacao())

a3 = Aluno()
a3.nome = 'Arthur'
a3.nota = 4

print(a3.mostrar_dados())
print(a3.situacao())