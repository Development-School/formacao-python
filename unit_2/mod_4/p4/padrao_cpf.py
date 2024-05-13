import re

# cpf = '002.980.643-75'
cpf = '00298064375'

# padrao = re.compile('[0-9]{3}[.]{1}[0-9]{3}[.]{1}[0-9]{3}[-]{1}[0123456789]{2}')
padrao = re.compile('[0-9]{3}[.]{0,1}[0-9]{3}[.]{0,1}[0-9]{3}[-]{0,1}[0123456789]{2}')
busca = padrao.search(cpf)

if busca:
    cpf2 = busca.group()
    print(cpf2)