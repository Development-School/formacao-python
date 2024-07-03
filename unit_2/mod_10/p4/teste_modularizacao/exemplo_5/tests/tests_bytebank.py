
"""
ATENÇÃO!!!

O Python não reconhece as pastas com hífen como por exemplo "python-tdd"
logo, a importação não funcionará dessa forma, então renomeie as pastas de content com underline

Ex.: "python_tdd"
"""

# from unit_2.mod_10.p4.teste_modularizacao.exemplo_5.codigo.bytebank import Funcionario # OK!
# from ..codigo.bytebank import Funcionario # ERRO


import os, sys  # Não funciona
# print(os.path.abspath(os.curdir))
# D:\Users\Builder\Documents\Projetos e Criações\.Git\formacao-python\unit_2\mod_10\p4\teste_modularizacao\exemplo_5\test
# sys.path.insert(0,os.path.abspath(os.curdir))

# import sys, os # Não funciona
# sys.path.insert(0, 'unit_2.mod_10.p4.teste_modularizacao.exemplo_5.codigo.bytebank')
# from ..codigo.bytebank import Funcionario # ERRO

# Apenas funciona das seguintes formas:
import os, sys # Acusa erro porém funciona  # OK!
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # OK!
# from ..codigo.bytebank import Funcionario  # Erro!
from codigo.bytebank import Funcionario  # Assim funciona # OK!

# from unit_2.mod_10.p4.teste_modularizacao.exemplo_5.codigo.bytebank import Funcionario # OK!

print("-----------------------------------------------")

print(Funcionario('Teste', '13/03/2000', 1111))

print("-----------------------------------------------")