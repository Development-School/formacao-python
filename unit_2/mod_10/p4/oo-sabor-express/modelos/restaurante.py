
from .avaliacao import Avaliacao

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
        # return '✔' if self._ativo else '✘'
        # return '✅' if self._ativo else '❎'
        # return '☑' if self._ativo else '☒'
        # return '✔' if self._ativo else '✖'
        # return '☑' if self._ativo else '☐'
        return '⌧' if self._ativo else '☐'

    # @staticmethod
    # def listar_restaurantes():
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | '
              f'{"Categoria".ljust(25)} | '
              f'{"Avaliação".ljust(25)} | '
              f'{"Status"}')

        # for restaurante in Restaurante.restaurantes:
        for restaurante in cls.restaurantes:
            # print(f'{restaurante._nome} | {restaurante._categoria} | {restaurante._ativo}')
            print(f'{restaurante._nome.ljust(25)} | '
                  f'{restaurante._categoria.ljust(25)} | '
                  # f'{restaurante.media_avaliacoes.ljust(25)} | ' # AttributeError: 'function' object has no attribute 'ljust'
                  # f'{str(restaurante.media_avaliacoes).ljust(25)} | ' # Exibindo objeto e não o valor da média
                  f'{str(restaurante.media_avaliacoes()).ljust(25)} | '
                  f'{restaurante.ativo}')

            # Dica Alura 01 (Não funcionou)
            # print(f'{restaurante._nome.ljust(25)} | '
            #       f'{str(restaurante._categoria.ljust(25))} | '
            #       f'{str(restaurante.media_avaliacoes).ljust(25)} | '
            #       f'{restaurante.ativo}')

    # Dica Alura 02 (Não funcionou)
    # @classmethod
    # def listar_restaurantes(cls):
    #     print(
    #         f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
    #     for restaurante in cls.restaurantes:
    #         print(f'{restaurante._nome.ljust(25)} | {str(restaurante._categoria.ljust(25))} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    def alternar_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    # @property
    # def getAvaliacao(self):
    #     return self._avaliacao

    # def media_avaliacoes(self):
    #     if (self._avaliacao):
    #         soma_avaliacoes = sum(avaliacao._nota for avaliacao in self._avaliacao)
    #         quantidade_avaliacoes = len(self._avaliacao)
    #         return round((soma_avaliacoes / quantidade_avaliacoes), 1)
    #     else:
    #         return 'Não avaliado'


    # @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media