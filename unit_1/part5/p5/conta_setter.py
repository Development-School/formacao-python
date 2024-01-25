# -------------------------------------------------------------------- #
# 04. Implementando métodos setter na classe Conta
# -------------------------------------------------------------------- #

from conta.conta import Conta

conta = Conta(123, "Nico", 55.5, 1000.0)

print("-----------------------------------------------")

print("Titular: {}".format(conta.get_titular()))
print("Saldo: {}".format(conta.get_saldo()))
print("Limite: {}".format(conta.get_limite()))

print("-----------------------------------------------")

conta.set_titular("Marco")
conta.set_saldo(100)

print("Titular: {}".format(conta.get_titular()))
print("Saldo: {}".format(conta.get_saldo()))
print("Limite: {}".format(conta.get_limite()))