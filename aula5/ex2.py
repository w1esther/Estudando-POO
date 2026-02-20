class ContaBancaria:
    """
    Cria conta bancária e permite fazer saques e depositos
    """

    def __init__(self, id, nome = '', saldo = 0):
        
        self.id = id
        self.titular = nome
        self.saldo = saldo

        print(f'Conta {self.id} criada com sucesso. Saldo atual de {self.saldo:.2f} reais')

    def __str__(self):

        return f'A conta banacaria {self.id} pertence a {self.titular} e possui saldo de {self.saldo:.2f} reais'
    
    def depositar(self, valor):

        self.saldo += valor

        print(f'deposito de {valor:.2f} reais autorizado na conta {self.id} e feito com sucesso!')

    def saquar(self, valor):

        if valor <= self.saldo:
            self.saldo -= valor

            print(f'saque de {valor:.2f} reais autorizado na conta {self.id} e feito com sucesso!')
        else:
            print(f'Saldo de {valor:.2f} reais NEGADO na conta {self.id}. Saldo na conta insuficiente para o saque! seu saldo é de {self.saldo:.2f} reais')


c1 =ContaBancaria(17, 'Esther', 2000)
c1.depositar(500)
c1.saquar(10000)
print(c1)