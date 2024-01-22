
from conta import cria_conta, deposita, saca, extrato

conta = cria_conta(123, "Nico", 55.0, 1000.0)
print(conta["saldo"])

print("-----------------------------------------------")

deposita(conta, 15.0)
extrato(conta)
# Saldo é 70.0

print("-----------------------------------------------")

saca(conta, 20.0)
extrato(conta)
# Saldo é 50.0

print("-----------------------------------------------")

conta["saldo"] = conta["saldo"] + 100.0
extrato(conta)
# Saldo é 150,0

print("-----------------------------------------------")

conta3 = {"numero": 321, "limite": 200.0}
deposita(conta3, 2000.0) #Erro pois não possui o atribute saldo

"""Traceback (most recent call last):
  File "D:\Users\Builder\Documents\Projetos e Criações\.Git\formacao-python\unit_1\part5\p1\teste_conta2.py", line 28, in <module>
    deposita(conta3, 2000.0) #Erro pois não possui o atribute saldo
    ^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Users\Builder\Documents\Projetos e Criações\.Git\formacao-python\unit_1\part5\p1\conta.py", line 6, in deposita
    conta["saldo"] += valor
    ~~~~~^^^^^^^^^
KeyError: 'saldo'"""