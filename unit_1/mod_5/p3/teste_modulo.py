

# from .modulo.conta import Conta #ERRO
from modulo.conta import Conta

conta = Conta(numero=123, titular="Lucas", limite=1000, saldo=50.5)
print(conta.titular)

print("-----------------------------------------------")