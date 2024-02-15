
from conta import Conta

# conta = Conta()
# print(conta)
# <conta.Conta object at 0x0000025BFEDD0110>

print("-----------------------------------------------")

# conta = Conta()
# Construindo objeto...<conta.Conta object at 0x000002B7A7D202C0>

print("-----------------------------------------------")

conta = Conta(123, "Nico", 55.5, 1000.0)
print(conta.titular)
# Construindo objeto...<conta.Conta object at 0x000002B7A7D202C0>

print("-----------------------------------------------")

conta2 = Conta(321, "Marco", 100.0, 1000.0)
print(conta2.titular)