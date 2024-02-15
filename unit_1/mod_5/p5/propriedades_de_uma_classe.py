# -------------------------------------------------------------------- #
# 03. Usando Propriedades em Classe
# -------------------------------------------------------------------- #

class Produto:

    def __init__(self, codigo, preco, quantidade):
        self.__codigo = codigo
        self.__preco = preco
        self.__quantidade = quantidade

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, nova_quantidade):
        self.__quantidade = nova_quantidade

    def adicionar(self, valor):
        self.set_quantidade(self.get_quantidade() + valor)

    def remover(self, valor):
        self.set_quantidade(self.get_quantidade() - valor)

p = Produto(123, 3.14, 20)
print(p.get_quantidade())

print("-----------------------------------------------")

p.set_quantidade(30) # 30
p.adicionar(70) # 100
p.remover(90) # 10

print(p.get_quantidade())

print("-----------------------------------------------")

