
from conta_project.conta import Conta

conta = Conta(123, "Nico", 55.5, 1000.0)
conta.extrato()

outraref = conta
outraref.extrato()

