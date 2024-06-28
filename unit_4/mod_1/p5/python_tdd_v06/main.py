
# import bytebank
from codigo.bytebank import Funcionario

#-------------------------------------------------------------

# lucas = bytebank.Funcionario('Lucas Carvalho', 2000, 1000)
# lucas = Funcionario('Lucas Carvalho', 2000, 1000)

print("-----------------------------------------------")

# print(lucas) # Funcionario(Lucas Carvalho, 2000, 1000)
# print(lucas.idade()) # 24

print("-----------------------------------------------")

# lucas = Funcionario('Lucas Carvalho', '13/03/2000', 1000)
# print(lucas.idade()) # ValueError: invalid literal for int() with base 10: '13/03/2000'

# data = '13/03/2000'
# data_quebrada = data.split('/')
# print(data_quebrada) # ['13', '03', '2000']

# ano = data_quebrada[-1]
# print(ano) # 2000

# print(data.split('/')[-1])

# print(lucas)
# print(lucas.idade())
# Funcionario(Lucas Carvalho, 13/03/2000, 1000)
# 24

print("-----------------------------------------------")

# código anterior omitido

# def teste_idade():
#     funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
#     print(f'Teste = {funcionario_teste.idade()}')
#
#     funcionario_teste1 = Funcionario('Teste', '13/03/1999', 1111)
#     print(f'Teste = {funcionario_teste1.idade()}')
#
#     funcionario_teste2 = Funcionario('Teste', '01/12/1999', 1111)
#     print(f'Teste = {funcionario_teste2.idade()}')
#
# teste_idade()
# Teste = 24
# Teste = 25
# Teste = 25

r"""
D:\tmp\projetos_PATH\.system\interpretador_python\Scripts\python.exe "C:/Apps/.Developer/JetBrains PyCharm Professional v.2023.1.3 [Portable]/content/plugins/python/helpers/pycharm/_jb_pytest_runner.py" --path "D:\Users\Builder\Documents\Projetos e Criações\.Git\formacao-python\unit_4\mod_1\p4\python_tdd_v05\codigo\main.py" 
Testing started at 13:15 ...
Launching pytest with arguments D:\Users\Builder\Documents\Projetos e Criações\.Git\formacao-python\unit_4\mod_1\p4\python_tdd_v05\codigo\main.py --no-header --no-summary -q in D:\Users\Builder\Documents\Projetos e Criações\.Git\formacao-python\unit_4\mod_1\p4\python_tdd_v05\codigo
============================= test session starts =============================
collecting ... collected 1 item

main.py::teste_idade PASSED                                              [100%]Teste = 24
Teste = 25
Teste = 25
============================== 1 passed in 0.17s ==============================

Process finished with exit code 0
"""

print("-----------------------------------------------")

ana = Funcionario('Ana', '12/03/1997', 1000)
print(ana.calcular_bonus())
# 100.0

print("-----------------------------------------------")

# Trabalhando com Exceptions ▼
# print('evfvf'))
"""
    print('evfvf'))
                  ^
SyntaxError: unmatched ')'
"""

# print(0/0)
"""
    print(0/0)
          ~^~
ZeroDivisionError: division by zero
"""

print("-----------------------------------------------")

ana = Funcionario('Ana', '12/03/1997', 100000000)
# print(ana.calcular_bonus())
'''
    raise Exception('O salário é muito alto para receber um bônus')
Exception: O salário é muito alto para receber um bônus
'''

print(ana)

print("-----------------------------------------------")