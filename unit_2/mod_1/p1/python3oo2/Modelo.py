class Filme:
    def __init__(self, nome, ano, duracao):
        # self.nome = nome
        # self.nome = nome.capitalize()
        # self.nome = nome.title()
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

vingadores = Filme('vingadres - guerra infinita', 2018, 160)
print(vingadores.nome)

print("-----------------------------------------------")

vingadores.dar_like() # Dar Like!
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}'
      f' - Likes: {vingadores.likes}')

print("-----------------------------------------------")

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like() # Dar Like!
atlanta.dar_like() # Dar Like!
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas}'
      f' - Likes: {atlanta.likes}')

print("-----------------------------------------------")

atlanta.nome = 'Teste'
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas}'
      f' - Likes: {atlanta.likes}')

