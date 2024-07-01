
class Exemplo:
    def add(self, a, b):
        return a + b

    def add(self, a, b):
        return str(a) + str(b)

obj = Exemplo()
resultado = obj.add(5, 3)
print(resultado)

print("-----------------------------------------------")

class Cofre:
    def __init__(self, nome):
        self.pessoa = nome
        self._deposito = []
        self.desconto = 0

    def adicionar(self, valor):
        return self._deposito.append(valor)

    def total(self):
        total = 0
        for valor in self._deposito:
            total += valor

        return (total - self.desconto)

    # Sobrecarga (Não existe em python... utilizamos de artifício)▼
    def aplicar_desconto(self, desconto=None):
        if desconto is None:
            self.desconto = 0
        else:
            self.desconto = desconto

    def __str__(self):
        return f'{self.pessoa.title()} possui um total de R$ {self.total()}\n' \
               f'Foi descontado do {self.pessoa.title()} R$ {self.desconto}'

#-------------------------------------------------------------

lucas = Cofre('Lucas')
print(lucas)

print("-----------------------------------------------")

lucas.adicionar(100)
print(lucas)

print("-----------------------------------------------")

lucas.adicionar(50)
lucas.adicionar(50)
lucas.adicionar(100)
lucas.aplicar_desconto()
print(lucas)

print("-----------------------------------------------")

lucas.aplicar_desconto(300)
print(lucas)

print("-----------------------------------------------")