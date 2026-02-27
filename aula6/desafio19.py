from time import sleep

class Livro():

    def __init__(self, livro, paginas):
        
        self.livro = livro
        self.paginas_livro = int(paginas)
        self.pagina_atual = 1

        if self.pagina_atual == 1:

            return print(f'Voce acabou de abrir o livro {self.livro} que tem {self.paginas_livro} paginnas e agora está na pagina 1. ')
        
    def avancar_paginas(self, num_paginas):

        # pagina_avancadas = num_paginas 

        pagina_destino = min(self.pagina_atual + num_paginas, self.paginas_livro)

        if pagina_destino == self.paginas_livro:

            print(f'Você está na página {self.paginas_livro}, e chegou ao final do livro!')

            self.pagina_atual = self.paginas_livro

            return


        for n in range(self.pagina_atual +1, pagina_destino + 1):
                
            print(f'Pág {n}')
            
            sleep(1)

        avancou = pagina_destino - self.pagina_atual
            
        self.pagina_atual += num_paginas

        return print(f'Você avançou {avancou} páginas e agora está na página {self.pagina_atual}')
        
l1 = Livro('10 coisas que aprendi', 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)