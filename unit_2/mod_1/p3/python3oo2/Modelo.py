class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    # def imprime(self):
    #     print(f'{self._nome} - {self.ano} - {self._likes} Likes')
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        # self._nome = nome.title()
        # self.ano = ano
        self.duracao = duracao
        # self._likes = 0

    # def imprime(self):
    #     print(f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes')
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        # self._nome = nome.title()
        # self.ano = ano
        self.temporadas = temporadas
        # self._likes = 0

    # def imprime(self):
    #     print(f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes')
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'

vingadores = Filme('vingadres - guerra infinita', 2018, 160)
print(vingadores.nome)

print("-----------------------------------------------")

vingadores.dar_like() # Dar Like!
# print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}'
#       f' - Likes: {vingadores.likes}')

print(f'{vingadores.nome} - {vingadores.ano} - {vingadores.duracao} : {vingadores.likes}')

print("-----------------------------------------------")

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like() # Dar Like!
atlanta.dar_like() # Dar Like!
# print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas}'
#       f' - Likes: {atlanta.likes}')

print(f'{atlanta.nome} - {atlanta.ano} - {atlanta.temporadas} : {atlanta.likes}')

print("-----------------------------------------------")

atlanta.nome = 'Teste'
# print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas}'
#       f' - Likes: {atlanta.likes}')

print(f'{atlanta.nome} - {atlanta.ano} - {atlanta.temporadas} : {atlanta.likes}')

print("-----------------------------------------------")

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    # "if" ternário:
    # detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas

    # "if" normal:
    # if hasattr(programa, 'duracao'):
    #     detalhes = programa.duracao
    # else:
    #     detalhes = programa.temporadas
    #
    # print(f'{programa.nome} - {detalhes} D - {programa.likes}')
    # programa.imprime()

    print(programa)

print("-----------------------------------------------")

if(__name__ == "__main__"):
    pass