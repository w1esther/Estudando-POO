class ContaBancaria:

    def __init__(self, titular, saldo_incial, limite):

        self.__titular = titular
        self.__saldo = saldo_incial
        self.__limite = limite

    def sacar(self, valor):

        if valor > self.__saldo + self.__limite:
            return False

        else:
            self.__saldo = self.__saldo - valor
            return self.__saldo
        
    def depositar(self, valor):

        if valor <= 0:
            return False
        
        else:
            self.__saldo += valor
            return self.__saldo
        
    @property
    def titular(self):

        return self.__titular

    @property
    def saldo(self):

        return self.__saldo
    
    #serve para definir um novo valor para saldo, não depositar nem sacar, setter não precisa retornar nada

    @saldo.setter
    def saldo(self, valor):

        if valor >= 0:
            self.__saldo = valor
            return self.__saldo
        
        else:
            return self.__saldo
        
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, valor):

        if valor<0:
            False
        else:
            self.__limite = valor
        
conta1 = ContaBancaria("Maria", 1000, 500)

conta1.depositar(200)
conta1.sacar(300)
conta1.sacar(400)

conta1.saldo = 200
conta1.limite = 300

print(f"Titular: {conta1.titular}, Saldo: R${conta1.saldo:.2f}")