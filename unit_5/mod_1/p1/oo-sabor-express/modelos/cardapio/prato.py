
# from ...modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__ (nome, preco) # Herança da classe Mãe
        self.descricao = descricao
        # pass

    def __str__(self):
        return self._nome