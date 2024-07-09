
# from ...modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)  # Herança da classe Mãe
        self.tamanho = tamanho
        # pass

    def __str__(self):
        return self._nome

    # Poliformismo
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)