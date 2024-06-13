
# from avaliacao import Avaliacao # Error
from .avaliacao import Avaliacao # OK!

class Restaurante:
    restaurantes = []

    #Construtor ▼
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
        self._avaliacao = []

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | '
              f'{"Categoria".ljust(25)} | '
              f'{"Avaliação".ljust(25)} | '
              f'{"Status"}')

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | '
                  f'{restaurante._categoria.ljust(25)} | '
                  # f'{str(restaurante.media_avaliacoes).ljust(25)} | ' # Error
                  f'{str(restaurante.media_avaliacoes()).ljust(25)} | ' # OK!
                  f'{restaurante.ativo}')

    def alternar_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    # @property  # Error
    # @property  # Comentar, não utilizar o @property... OK!
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media