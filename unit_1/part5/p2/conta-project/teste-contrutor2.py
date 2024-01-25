
from conta import Conta

conta1 = Conta(1, "Fulano", 0.0, 1000.0)
conta2 = Conta(2, "Beltrano", 0.0, 1000.0)
conta3 = Conta(3, "Sicrano", 0.0, 2000.0)

print(conta1, conta2, conta3, sep="\n")

print(conta1.titular, conta2.titular, conta3.titular, sep="\n")