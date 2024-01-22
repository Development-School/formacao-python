
from conta import cria_conta

conta_niko = cria_conta(123, "Nico", 55.0, 1000.0)
print(conta_niko["numero"])
# 123

print("-----------------------------------------------")

from conta import cria_conta
conta = cria_conta(123, "Nico", 55.0, 1000.0)

print(conta)
# {'numero': 123, 'titular': 'Nico', 'saldo': 55.0, 'limite': 1000.0}

print("-----------------------------------------------")
