
from package.conta import Conta

conta = Conta(123, "Nico", 55.5, 1000.0)
# Construindo objeto ... <conta.Conta object at 0x110839668>

# print(conta.saldo)
# 55.5

print("-----------------------------------------------")

# conta.saca(1200.0)
# print(conta.saldo)
# -1144.5

# conta.saca(1200.0)
# print(conta.saldo)
# O valor 1200.0 passou o limite
# 55.5

conta.saca(1200.0)
print(conta.saldo)
# O valor 1200.0 passou o limite
# 55.5

print("-----------------------------------------------")

conta.saca(100.0)
print(conta.saldo)
# -44.5
