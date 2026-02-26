class Livro:

    def __init__(self, titulo, autor):
        
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        
        return f'{self.titulo} - {self.autor}'
    
class Emprestimo:

    def __init__(self):
        
        self.lista_livros = []

    def adicionar_livro(self, livro):

        self.lista_livros.append(livro)

        # return livro

    def quantidade_livros(self):

        return len(self.lista_livros)

    def listar_livros(self):

        print('LIVROS DO EMPRESTIMO:')

        for i, livros in enumerate(self.lista_livros, start=1):

            print(f'{i} - {livros}')

class Biblioteca:

    def __init__(self):

        self.emprestimos = []

    def novo_emprestimo(self):

        emprestimo = Emprestimo()
        self.emprestimos.append(emprestimo)
        return emprestimo
    
    def listar_emprestimos(self):

        # COMO FIZ SOZINHA

        # for emprestimo in self.emprestimos:
        #     print(emprestimo)

        # VERSÃO MELHORADA

        # enumerate fornece o indice + o elemento respectivamente

        for i, emprestimo in enumerate(self.emprestimos, start=1):
            print(f'Emprestimo {i} - {emprestimo.quantidade_livros()} livros')
        
bib = Biblioteca()

l1 = Livro("Dom Casmurro", "Machado de Assis")
l2 = Livro("1984", "George Orwell")
l3 = Livro("O Hobbit", "Tolkien")

emp1 = bib.novo_emprestimo()
emp1.adicionar_livro(l1)
emp1.adicionar_livro(l2)

emp2 = bib.novo_emprestimo()
emp2.adicionar_livro(l3)

emp3 = bib.novo_emprestimo()
emp3.adicionar_livro(l1)
emp3.adicionar_livro(l2)
emp3.adicionar_livro(l3)

print(bib.listar_emprestimos())

print(emp1.listar_livros())
print(emp2.listar_livros())
print(emp3.listar_livros())