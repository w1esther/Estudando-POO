from rich import print
from rich.table import Table

class Tarefa:

    def __init__(self, descricao = ''):
        
        self.descricao = descricao
        self.concluida = False

    def concluir(self):

        self.concluida = True

class GerenciadorTarefas:

    def __init__(self):
        
        self.lista_tarefas = []

    def adicionar_tarefa(self, descricao):

        nova_tarefa = Tarefa(descricao)
        self.lista_tarefas.append(nova_tarefa)

    def listar_tarefas(self):

        tabela_tarefas = Table(title='Tabela de Tarefas')

        tabela_tarefas.add_column('#', justify='center')
        tabela_tarefas.add_column('Tarefa',justify='center')
        tabela_tarefas.add_column('Status', justify='center')

        i = 1

        for tarefa in self.lista_tarefas:
            
            if tarefa.concluida:
                status = '[green]Concluida[/]'
            else:
                status = '[red]Pendente[/]'

            tabela_tarefas.add_row(str(i), tarefa.descricao, status)

            i += 1

        print(tabela_tarefas)

t1 = GerenciadorTarefas()
t1.adicionar_tarefa('Estudar POO')
t1.listar_tarefas()

t2 = GerenciadorTarefas()
t2.adicionar_tarefa('Estudar Trigonometria')
t2.adicionar_tarefa('Estudar lógica matematica')
t2.lista_tarefas[0].concluir()
t2.listar_tarefas()
