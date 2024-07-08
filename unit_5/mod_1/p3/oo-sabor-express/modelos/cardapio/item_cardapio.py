
# Aplicar "métodos de molde" ou médotos modelos para ser implementados;
# Dessa froma é obrigado implementar os métodos destacados como abstratos;
# Para isso aplicaremos métodos abstratos: ▼
from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass