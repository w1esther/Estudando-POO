# encapsulamento aplica-se tanto aos atributos quanto aos métodos.

class BaseDeDados:

    def __init__(self):
        
        self.__dados = {}

    #Do acesso aos valores de __dados, posso acessar o metodo como um atributo, não posso configurar ele fora da classe
    @property
    def dados(self):

        return self.__dados

    def inserir_clientes(self, id, nome):

        if 'clientes' not in self.__dados:

            self.__dados['clientes'] = {id: nome}

        else:

            self.__dados['clientes'].update({id: nome})
    
    def listar_clientes(self):

        for id, nome in self.__dados['clientes'].items():

            print(id, nome)

    def remover_cliente(self, id):

        del self.__dados['clientes'][id]

bd = BaseDeDados()

bd.inserir_clientes(1, 'Maria')
bd.inserir_clientes(2, 'Esther')
bd.inserir_clientes(3, 'Ana')
# bd.remover_cliente(1)
bd.listar_clientes()

# obs:

bd.__dados = 'Outra coisa'
print(bd.__dados)
print(bd._BaseDeDados__dados)

print(bd.dados)