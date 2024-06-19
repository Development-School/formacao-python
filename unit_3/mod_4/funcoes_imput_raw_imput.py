
# Python: A diferença das funções input() e raw_input()
# Ref.: https://www.alura.com.br/artigos/a-diferenca-das-funcoes-input-e-raw-input-no-python

print("-----------------------------------------------")

usuario = input('Insira seu login: ')
print('Olá, ' + usuario)
# Insira seu login: lucas
# Olá, lucas

print("-----------------------------------------------")

import sys

if sys.version_info.major == 2:
    # usuario = raw_input('Insira seu login: ') # Erro pois só funcionava no Python 2
    pass
elif sys.version_info.major == 3:
    usuario = input('Insira seu login: ')
    print('Olá, ' + usuario)

# Insira seu login: lucas
# Olá, lucas

print("-----------------------------------------------")