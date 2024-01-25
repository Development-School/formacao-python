
from conta.conta import Conta

conta = Conta(123, "Nico", 55.5, 1000.0)
print("-----------------------------------------------")

print(conta.get_titular())
print(conta.get_saldo())
print(conta.get_limite())

print("-----------------------------------------------")

conta.set_limite(10000.0)
print(conta.get_limite())
