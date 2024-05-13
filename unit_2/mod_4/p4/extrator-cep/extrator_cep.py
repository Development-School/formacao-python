
endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re  # Regular Expression -- RegEx

# 5 dígitos + hífen (opcional) + 3 dígitos

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789]")
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)

print("-----------------------------------------------")

endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120"

import re  # Regular Expression -- RegEx

# 5 dígitos + hífen (opcional) + 3 dígitos

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
busca = padrao.search(endereco)  # Match

if busca:
    cep = busca.group()
    print(cep)

    print("-----------------------------------------------")

    p = cep.find('-')
    print(p) # Quando não encontrado, retorna -1
    print(bool(cep.find('-'))) # -1 é um valor, por isso retorna True

    print('Encontrado') if (cep.find('-') > 0) == True else print('Não ncontrado')

    print("-----------------------------------------------")

    print(cep)

    cep2 = cep[:5] + '-' + cep[5:]
    print(cep2)
    # 23440120-

    print("-----------------------------------------------")



