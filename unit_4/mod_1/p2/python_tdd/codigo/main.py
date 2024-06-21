
# import bytebank
from bytebank import Funcionario

#-------------------------------------------------------------

# lucas = bytebank.Funcionario('Lucas Carvalho', 2000, 1000)
# lucas = Funcionario('Lucas Carvalho', 2000, 1000)

print("-----------------------------------------------")

# print(lucas) # Funcionario(Lucas Carvalho, 2000, 1000)
# print(lucas.idade()) # 24

print("-----------------------------------------------")

lucas = Funcionario('Lucas Carvalho', '13/03/2000', 1000)
# print(lucas.idade()) # ValueError: invalid literal for int() with base 10: '13/03/2000'

# data = '13/03/2000'
# data_quebrada = data.split('/')
# print(data_quebrada) # ['13', '03', '2000']

# ano = data_quebrada[-1]
# print(ano) # 2000

# print(data.split('/')[-1])

print(lucas)
print(lucas.idade())
# Funcionario(Lucas Carvalho, 13/03/2000, 1000)
# 24

print("-----------------------------------------------")

# código anterior omitido

def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
    print(f'Teste = {funcionario_teste.idade()}')

    funcionario_teste1 = Funcionario('Teste', '13/03/1999', 1111)
    print(f'Teste = {funcionario_teste1.idade()}')

    funcionario_teste2 = Funcionario('Teste', '01/12/1999', 1111)
    print(f'Teste = {funcionario_teste2.idade()}')

teste_idade()
# Teste = 24
# Teste = 25
# Teste = 25

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")