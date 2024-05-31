class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @property
    def codigo(self):
        return self._codigo

    @property
    def saldo(self):
        return self._saldo

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

def extrai_saldo(conta):
    return conta._saldo

print("-----------------------------------------------")

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)
print(conta_do_guilherme.saldo)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)
print(conta_da_daniela.saldo)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)
print(conta_do_paulo.saldo)

print("-----------------------------------------------")

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]
for conta in contas:
  print(conta)
# [>>Codigo 17 Saldo 500<<]
# [>>Codigo 3 Saldo 1000<<]
# [>>Codigo 133 Saldo 510<<]

print("-----------------------------------------------")

print(list(f'Saldo da conta {conta._codigo} é R${conta.saldo}' for conta in contas))

print("-----------------------------------------------")

print(sorted(contas, key=extrai_saldo))
# [<__main__.ContaSalario object at 0x000001742C095100>,
# <__main__.ContaSalario object at 0x000001742C095430>,
# <__main__.ContaSalario object at 0x000001742C095130>]

print("-----------------------------------------------")

for conta in sorted(contas, key=extrai_saldo):
    print(conta)
# [>>Codigo 17 Saldo 500<<]
# [>>Codigo 133 Saldo 510<<]
# [>>Codigo 3 Saldo 1000<<]

print("-----------------------------------------------")

for conta in sorted(contas, key=extrai_saldo, reverse=True):
    print(conta)
# [>>Codigo 3 Saldo 1000<<]
# [>>Codigo 133 Saldo 510<<]
# [>>Codigo 17 Saldo 500<<]
print("-----------------------------------------------")

print(list(conta.__str__() for conta in sorted(contas, key=extrai_saldo)))
# ['[>>Codigo 17 Saldo 500<<]', '[>>Codigo 133 Saldo 510<<]', '[>>Codigo 3 Saldo 1000<<]']

print(list(conta.__str__() for conta in sorted(contas, key=extrai_saldo, reverse=True)))
# ['[>>Codigo 3 Saldo 1000<<]', '[>>Codigo 133 Saldo 510<<]', '[>>Codigo 17 Saldo 500<<]']

print("-----------------------------------------------")

from operator import attrgetter

print(list(f'O saldo da conta {conta.codigo} é R${conta.saldo}' for conta in sorted(contas, key=attrgetter("saldo"))))
print(list(f'O saldo da conta {conta.codigo} é R${conta.saldo}' for conta in sorted(contas, key=attrgetter("codigo"))))
