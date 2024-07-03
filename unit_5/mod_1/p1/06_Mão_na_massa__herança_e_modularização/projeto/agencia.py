
# from banco import Banco
from .banco import Banco

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self.numero = numero

    def __str__(self):
        return f"Informações do Banco: {self.nome}:\n" \
               f"Emdereço: {self.endereco}\n" \
               f"Código..: {self.numero}"
