class Conta:

  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0

  def deposita(self, valor):
    self._saldo += valor

  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

class ContaCorrente(Conta):

  def passa_o_mes(self):
    self._saldo -= 2

class ContaPoupanca(Conta):

  def passa_o_mes(self):
    self._saldo *= 1.01
    self._saldo -= 3

class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo

    def __str__(self):
        return "Código: {} e Saldo: {}".format(self._codigo, self._saldo)

print("-----------------------------------------------")

conta1 = ContaSalario(37)
print(conta1)
# Código: 37 e Saldo: 0

conta2 = ContaSalario(37)
print(conta1)
# Código: 37 e Saldo: 0

print("-----------------------------------------------")

print(conta1 == conta2) # As contas não são as mesmas

print("-----------------------------------------------")

# Antes implementação do __eq__
contas = [conta1]
print(conta1 in contas)
print(conta2 in contas)
# True
# False

print("-----------------------------------------------")

# Após implementação do __eq__
print(conta1 in contas)
print(conta2 in contas)
# True
# True

print("-----------------------------------------------")

# Após implementação do __eq__
print(conta1 == conta2)
print(conta1 != conta2)

print("-----------------------------------------------")

# Após implementação do if em __eq__ em relaçãao ao tipo
conta1 = ContaSalario(37)
conta2 = ContaSalario(37)
conta3 = ContaCorrente(37)

print(conta1 == conta2)
print(conta1 == conta3)