
from .avaliacao import Avaliacao
from .cardapio.item_cardapio import ItemCardapio

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome} | {self._categoria}'

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '⌧' if self._ativo else '☐'

    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{"Nome do restaurante".ljust(25)} | '
              f'{"Categoria".ljust(25)} | '
              f'{"Avaliação".ljust(25)} | '
              f'{"Status"}')

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | '
                  f'{restaurante._categoria.ljust(25)} | '
                  f'{str(restaurante.media_avaliacoes).ljust(25)} | '
                  f'{restaurante.ativo}')

    def alternar_status(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    # Métodos repetitivos... ▼
    # def adicionar_bebida_no_cardapio(self, bebida):
    #     self._cardapio.append(bebida)
    #
    # def adicionar_prato_no_cardapio(self, prato):
    #     self._cardapio.append(prato)

    # Refatorando...▼
    def adicionar_no_cardapio(self, item):
        # "isinstance" vai ser verdadeira...
        # Se...o "item" que estamos passando for...
        # uma isinstance do "ItemCardapio"
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f"Cardapio do restaurante {self._nome}:\n")

        # for i,item in enumerate(self._cardapio, start=1):
        #     mensagem = f"{i}. Nome: {item._nome.ljust(20)} | " \
        #                f"Preço: R${item._preco}"
        #     print(mensagem)

        for i,item in enumerate(self._cardapio, start=1):
            # Se a instancia do item tiver um atributo "descricao"...
            # método da classe "def __init__(self, nome, preco, descricao):"
            # if hasattr(item, 'descricao'):
            #     mensagem = f"{i}. Nome: {item._nome.ljust(20)} | " \
            #                f"Preço: R${str(item._preco).ljust(5)} | " \
            #                f"Descrição: {item.descricao}"
            #     print(mensagem)

            # Se a instancia do item possuir um atributo "tamanho"...
            # método da classe "def __init__(self, nome, preco, tamanho):"
            # elif hasattr(item, 'tamanho'):
            #     mensagem = f"{i}. Nome: {item._nome.ljust(20)} | " \
            #                f"Preço: R${str(item._preco).ljust(5)} | " \
            #                f"Tamanho: {item.tamanho}"
            #     print(mensagem)
            # Se a instancia do item tiver um atributo "descricao"...
            # método da classe "def __init__(self, nome, preco, descricao):"

            # Refatorando...▼
            # mensagem = f"{i}. Nome: {item._nome.ljust(20)} | " \
            #            f"Preço: R${str(item._preco).ljust(5)} | " \
            #            f"{'Descrição: {}'.format(item.descricao) if hasattr(item, 'descricao') else 'Tamanho: {}'.format(item.tamanho)}"

            # Refatorando...▼
            # mensagem = f"{i}. Nome: {item._nome.ljust(20)} | " \
            #            f"Preço: R${str(item._preco).ljust(5)} | " \
            #            f"{'Descrição: ' + item.descricao if hasattr(item, 'descricao') else 'Tamanho: ' + item.tamanho}"
            #
            # print(mensagem)

            # Refatorando... (Inclusão da Classe Sobremesa) ▼
            r""" 
            Atributos das instancias: ▼ 
                → prato tem 'descricao'
                → bebida tem 'tamanho'
                → sobremesa tem 'descricao', 'tamanho', 'tipo'
            """

            # Trabalhando com lambda: ▼
            x = lambda a, b, c="", d="", e="", f="": (a + b + c + d + e + f)
            mensagem_final = ""

            # Se o nome da classe do item for igual a "Prato"...
            if (item.__class__.__name__ == 'Prato'):
                mensagem_final = x('Descrição: ', item.descricao)
            elif (item.__class__.__name__ == 'Bebida'):
                mensagem_final = x('Tamanho: ', item.tamanho)
            elif (item.__class__.__name__ == 'Sobremesa'):
                mensagem_final = x(
                    'Descricao: ', f"{item.descricao.ljust(25)} |",
                    'Tamanho: ', f"{item.tamanho.ljust(10)} |",
                    'Tipo: ', item.tipo
                )

            mensagem = f"{i}. Nome: {item._nome.ljust(20)} | " \
                       f"Preço: R${str(item._preco).ljust(5)} | " \
                       f"{mensagem_final}"

            print(mensagem)