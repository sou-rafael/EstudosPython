class Stack:
     def __init__(self):    # Método construtor
         '''cria uma nova pilha vazia. Não necessita parâmetros e retorna uma pilha vazia.'''
         self.items = []

     def isEmpty(self):
         '''testa se a pilha está vazia.
         Não necessita parâmetros e retorna um valor booleano;
         valor do tipo bool, True or False.'''
         return self.items == []

     def push(self, item):
         '''insere um novo item na pilha. A operação necessita o item e não retorna coisa alguma.'''
         self.items.append(item)

     def pop(self):
         ''' remove o item que está no topo da pilha.
         Não necessita parametros e retorna o item removido.
         A pilha é modificada.'''
         return self.items.pop()

     def peek(self):
         '''retorna o item no topo da pilha mas não o remove da pilha.
         Não necessita de parâmetros.
         A pilha não é modificada.'''
         return self.items[len(self.items)-1]

     def size(self):
         '''retorna o número de item na pilha.
         Não necessita parâmetros e retorna um inteiro;
         valor do tipo int.'''
         return len(self.items)
