
"""Nesse artigo vou mostrar como funciona o operador de igualdade no Python e como alteramos seu comportamento,
controlando mais nosso código."""

"""Tenho um sistema em Python que armazena os filmes que eu tenho em uma lista, para organização,
com uma função que pega todos os filmes e retorna uma lista com eles:"""

class Filme():
    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor

    def __str__(self):
        return self.titulo + ' - ' + self.diretor

    # Implementação para correção da comparação:
    def __eq__(self, outro_filme):
        return self.titulo == outro_filme.titulo

class MeusFilmes:
    def __init__(self, filmes):
        self._filmes = filmes

    def __getitem__(self, item):
        return self._filmes[item]

    @property
    def listagem(self):
        return self._filmes

    def __len__(self):
        return len(self._filmes)

def pega_todos_os_filmes(lista):
    ## implementação da função
    # pass
    return lista

print("-----------------------------------------------")

filmes = []
filmes.append(Filme('A Teoria de Tudo', 'James Marsh'))
filmes.append(Filme('La La Land', 'Damien Chazelle'))
filmes.append(Filme('O Poderoso Chefão', 'Francis Ford Coppola'))

todosOsFilmes = MeusFilmes(filmes)

print(f'Total de filmes: {len(todosOsFilmes)}')
print(f'1º Filme: {todosOsFilmes[0]}')

print("-----------------------------------------------")

meus_filmes = pega_todos_os_filmes(filmes)
for filme in meus_filmes:
    print(filme)

print("-----------------------------------------------")

# Ok, temos nossa lista de filmes!

"""Comparando objetos com o operador =="""

def tenho_o_filme(filme_procurado):
    # meus_filmes = pega_todos_os_filmes(filmes)
    # for filme in meus_filmes:
    #     if filme_procurado == filme:
    #         return True
    # return False
    meus_filmes = pega_todos_os_filmes(filmes)
    return filme_procurado in meus_filmes

busca = Filme('A Teoria de Tudo', 'James Marsh')
filme_procurado = busca

print('Buscando filme \"{}\"'.format(filme_procurado))

if tenho_o_filme(filme_procurado):
    print('Tenho o filme!')
else:
    print('Não tenho :(')

"""Rodamos nosso código e esse foi o resultado: Não tenho :(
   Para solucionar este problema iremos implementar o método "__eq__"
"""

print("-----------------------------------------------")

print('Teste de Comparação 01:')
x = 700
y = 700
print(x == y)

a = 'Yan'
b = 'Yan'
print(a == b) # true

print("-----------------------------------------------")

"""Como o Python compara objetos?"""

print('Teste de Comparação 02:')
a = Filme('A Teoria de Tudo', 'James Marsh')
b = Filme('A Teoria de Tudo', 'James Marsh')

print(id(a))
print(id(b))

print(a == b) # False

print("-----------------------------------------------")

print('Teste de Comparação 03:')
a = Filme('A Teoria de Tudo', 'James Marsh')
b = a

print(a == b) # true

print("-----------------------------------------------")