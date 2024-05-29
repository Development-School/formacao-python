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

class ContaSalario(Conta):
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

class ContaMultiploSalario(ContaSalario):
    # pass
    def __eq__(self, outro):
        if type(outro) != ContaMultiploSalario:
            return False

print("-----------------------------------------------")

conta1 = ContaSalario(37)
conta2 = ContaCorrente(37)
conta3 = ContaMultiploSalario(37)


print(conta1 == conta2)
print(conta1 == conta3) # Antes da implementação do __eq__ dentro de ContaMultiploSalario
# False
# True

print("-----------------------------------------------")

print(conta1 == conta2)
print(conta1 == conta3) # Depois da implementação do __eq__ dentro de ContaMultiploSalario
# False
# False

print("-----------------------------------------------")

print(isinstance(conta1, ContaSalario))
print(isinstance(ContaSalario, ContaCorrente))
print(isinstance(conta3, ContaSalario))
# True
# False
# True

print("-----------------------------------------------")