

from package.conta import Conta

print(Conta.codigo_banco())
# 001

print("-----------------------------------------------")

print(Conta.codigos_bancos())
# {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

print("-----------------------------------------------")

print(Conta.codigos_bancos()["BB"])
# 001

print("-----------------------------------------------")

print(Conta.codigos_bancos()["Caixa"])
# 104