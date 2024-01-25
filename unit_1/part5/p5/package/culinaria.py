# -------------------------------------------------------------------- #
# 06. Gerenciando Propriedades no Aplicativo de Culinária
# -------------------------------------------------------------------- #

class Receita:

    def __init__(self, autor, tempo_preparo):
        self.__autor = autor
        self.__tempo_preparo = tempo_preparo

    @property
    def autor(self):
        return self.__autor.title()

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def tempo_preparo(self):
        return self.__tempo_preparo

    @tempo_preparo.setter
    def tempo_preparo(self, tempo_preparo):
        self.__tempo_preparo = tempo_preparo
