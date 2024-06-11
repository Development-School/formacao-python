class Restaurante:
    restaurantes = []

    #Construtor ▼
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @property
    def status(self):
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
              f'{"Status"}')

        # for restaurante in Restaurante.restaurantes:
        for restaurante in cls.restaurantes:
            # print(f'{restaurante._nome} | {restaurante._categoria} | {restaurante._ativo}')
            print(f'{restaurante._nome.ljust(25)} | '
                  f'{restaurante._categoria.ljust(25)} | '
                  f'{restaurante.status.ljust(25)}')

    def alternar_status(self):
        self._ativo = not self._ativo