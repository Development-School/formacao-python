import re

# cpf = '736.395.750-91'
cpf = '73639575091'

# padrao = re.compile('[0-9]{3}[.]{1}[0-9]{3}[.]{1}[0-9]{3}[-]{1}[0123456789]{2}')
padrao = re.compile('[0-9]{3}[.]{0,1}[0-9]{3}[.]{0,1}[0-9]{3}[-]{0,1}[0123456789]{2}')
busca = padrao.search(cpf)

if busca:
    cpf2 = busca.group()
    print(cpf2)