class Aluno:

    def __init__(self, nome, matricula):
        
        self.__nome = nome
        self.__matricula = matricula
        self.__notas = []

    def adicionar_nota(self, nota):

        if nota > 10 or nota < 0:
            return False
        else:
            self.__notas.append(nota)
            return self.__notas
        
    def calcular_media(self):

        soma_notas = 0

        if not self.__notas:
            return soma_notas
        
        else:
            
            for elemento in self.__notas:
                soma_notas += elemento
            
            num_notas = len(self.__notas)
            media_notas = soma_notas/num_notas
            return media_notas
    
    def verificar_situacao(self):

        media_notas = self.calcular_media()

        if media_notas >= 7:
            return 'Aprovado'
        
        elif 5 <= media_notas < 7:
            return 'Prova Final'

        elif media_notas < 5:
            return 'Reprovado'
        
    @property
    def nome(self):
        
        return self.__nome
    
    @nome.setter
    def nome(self, nome):

        if nome != '':

            self.__nome = nome

    @property
    def notas(self):

        return self.__notas
    
    def remover_ultima_nota(self):

        if not self.__notas:
            return False
        
        else:

            self.__notas.pop()
            return self.__notas
        
aluno1 = Aluno("Maria", "2024001")

aluno1.adicionar_nota(8)
aluno1.adicionar_nota(6)
aluno1.adicionar_nota(11)  # inválida

print(f"Média: {aluno1.calcular_media():.2f}")
print(f"Situação: {aluno1.verificar_situacao()}")

aluno1.remover_ultima_nota()

print(f"Notas: {aluno1.notas}")