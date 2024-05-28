

class Conta:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    # Trabalhando com encapsulamento (Getters and Setters)  ▼
    # Exemplo Getter
    @property
    # def getSaldo(self):
    def saldo(self): # Por boas práticas, é assim que utilizamos
        return self._saldo

    # Exemplo Getter
    @saldo.setter
    def saldo(self, novo_saldo):
        self._saldo = novo_saldo

    def deposita(self, valor):
        # self._saldo += valor
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

    def __str__(self):
        # return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)


print("-----------------------------------------------")

print('Saldo inicial: R$ {:.2f}'.format(Conta(88).saldo))
print(Conta(88))

print("-----------------------------------------------")

lucas = Conta(247)
# print(lucas)

print(f'Saldo do Lucas é R$ {lucas.saldo}')
lucas.deposita(50)
lucas.deposita(50)
lucas.deposita(900)

print(f'Saldo do Lucas é R$ {lucas.saldo}')

lucas.saca(500)
print(f'Saldo do Lucas é R$ {lucas.saldo}')

lucas.saldo = 0
print(f'Saldo do Lucas é R$ {lucas.saldo}')