
class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self._titulo = titulo
        self._autor = autor
        self._paginas = paginas

    def __str__(self):
        return f'{self._titulo} por {self._autor} - {self._paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self._titulo} por {self._autor}'

    def aumentar_paginas(self, quantidade):
        self._paginas += quantidade

print("-----------------------------------------------")

l1 = Livro('O Poder da Ação', 'Paulo Vieira')
print(l1)
print(l1.titulo_autor)

print("-----------------------------------------------")

l1.aumentar_paginas(100)
print(l1)

print("-----------------------------------------------")

print(l1._titulo, 'por', l1._autor)

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")