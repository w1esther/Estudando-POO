class Livro:
    
    def __init__(self, nome):
        
        self.nome_livro = nome

class Estante:

    def __init__(self, nome):
        
        self.nome_estante = nome 
        self.lista_livros = []

    def adicionar_livro(self, livro):

        self.lista_livros.append(livro)

    def exibir_livros(self):

        for livros in self.lista_livros:
            print(f'Estante: {self.nome_estante} \n Livros: \n {livros}')

class Biblioteca:

    def __init__(self, nome):
        
        self.nome_biblioteca = nome 
        self.lista_estantes = []

    def criar_estante(self, nome):

        estante = Estante(nome)
        self.lista_estantes.append(estante)
        return estante
    
    def listar_estantes(self):

        for estante in self.lista_estantes:
            print(estante.nome_estante)
            for livro in estante:
                print('livro')

# criando livros (fora → agregação)
livro1 = Livro("Harry Potter")
livro2 = Livro("Senhor dos Anéis")
livro3 = Livro("Física Básica")
livro4 = Livro("Química Geral")

# criando biblioteca
biblioteca = Biblioteca("Biblioteca Central")

# criando estantes (pela biblioteca → composição)
estante1 = biblioteca.criar_estante("Ficção")
estante2 = biblioteca.criar_estante("Ciência")

# adicionando livros às estantes
estante1.adicionar_livro(livro1)
estante1.adicionar_livro(livro2)

estante2.adicionar_livro(livro3)
estante2.adicionar_livro(livro4)

# exibindo tudo
biblioteca.listar_estantes()