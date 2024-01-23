
from conta import Conta

conta = Conta(123, "Nico", 55.5, 1000.0)
# Construindo objeto ... <conta.Conta object at 0x7fc4ed132048>

conta2 = Conta(321, "Marcos", 100.0, 1000.0)
# Construindo objeto ... <conta.Conta object at 0x7fc4ed1324a8>

print(conta.titular)
# 'Nico'
print(conta2.titular)
# 'Marcos'
