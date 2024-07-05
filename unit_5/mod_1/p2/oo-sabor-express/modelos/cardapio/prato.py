
# from ...modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__ (nome, preco) # Herança da classe Mãe
        self.descricao = descricao
        # pass

    def __str__(self):
        return self._nome

    """
    Poliformismo: ▼
    é a característica única de linguagens orientadas a objetos
    que permite que diferentes objetos respondam a mesma mensagem
    cada um a sua maneira...
    """
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)