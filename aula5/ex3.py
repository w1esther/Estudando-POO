class Livro:
    
    def __init__(self, titulo = '', autor = ''):

        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):

        return f'o livro é {self.titulo} do autor {self.autor} e sua situação de disponibilidade é {self.disponivel}'
    
class Usuario:

    def __init__(self, nome = ''):

        self.nome = nome
        self.livro_emprestado = None

    def emprestar_livro(self, livro):

        if livro.disponivel:
            livro.disponivel = False
            self.livro_emprestado = livro
            return f'{self.nome} pegou o livo {livro.titulo}'
        else:
            return 'Livro indisponível para emprestimo!'
        
    def devolver_livro(self):

        if self.livro_emprestado is not None:
            self.livro_emprestado.disponivel = True
            titulo = self.livro_emprestado.titulo
            self.livro_emprestado = None
            return f'o livro {titulo} foi devolvido!'
        else:
            return 'nenhum livro para devolver!'

l1 = Livro('Dom Casmurro', 'Machado de Assis')
u1 = Usuario('Maria')

print(l1)
print(u1.emprestar_livro(l1))
print(l1)
print(u1.devolver_livro())
print(l1)