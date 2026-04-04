# agregação e composição

class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Historico:

    def __init__(self):
        
        self.transacoes = []

    def imprime(self):

        print('tramsações: ')
        for i in self.transacoes:
            print(f'- {i}')

class Conta:

    def __init__(self, numero, agencia, saldo, cliente):
        
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo
        self.titular = cliente
        self.historico = Historico()

    def deposita(self, valor):

        if valor > 0:
            self.saldo += valor
            self.historico.transacoes.append(f'foi depositado: {valor}')
        else:
            return False
        
    def saca(self, valor):

        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f'foi retirado: {valor}')

cliente1 = Cliente(1234567, 'Maria', 'Beserra')
conta1 = Conta('1234-5', '1111-1', 200, cliente1)
conta1.deposita(200)
conta1.saca(100)
conta1.historico.imprime()
print(conta1.saldo)