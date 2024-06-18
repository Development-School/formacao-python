from Cpf_Cnpj import Documento

# print("-----------------------------------------------")
# print("Trabalhando com CPF ▼")
# print("-----------------------------------------------")
#
# objeto_cpf = Documento.cria_documento("05826307030")
# print(objeto_cpf) # 058.263.070-30

# print("-----------------------------------------------")
# print("Trabalhando com CNPJ ▼")
# print("-----------------------------------------------")
#
# objeto_cnpj2 = Documento.cria_documento('31292014000150')
# print(objeto_cnpj2)

print("-----------------------------------------------")
print("Trabalhando com Telefones ▼")
print("-----------------------------------------------")

from TelefonesBr import TelefonesBr

numero = '552126481234'
# print(TelefonesBr(numero))
# <TelefonesBr.TelefonesBr object at 0x000001B7CF13B740>

#-------------------------------------------------------------

import re

telefone = "2126481234"
padrao = r"([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
resposta = re.search(padrao,telefone)

# print(resposta.group())
# 2126481234

#-------------------------------------------------------------

# TelefonesBr(telefone).format_numero() # Antes do __str__
# +None(21)2648-1234

#-------------------------------------------------------------

telefone = "+552126481234"
# TelefonesBr(telefone).format_numero() # Antes do __str__
# +55(21)2648-1234

print(TelefonesBr(telefone))
# +55(21)2648-1234

print("-----------------------------------------------")

telefone = "2126481234"
print(TelefonesBr(telefone))
# +None(21)2648-1234

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")