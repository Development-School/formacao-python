from Cpf import Cpf

print("-----------------------------------------------")

# objeto_cpf2 = CpfCnpj("153162647541")
# ValueError: Quantidade de dígitos inválida

objeto_cpf2 = Cpf("15316264754")
print(objeto_cpf2)
# 153.162.647-54

print("-----------------------------------------------")

# objeto_cpf3 = CpfCnpj("11111111112")
# ValueError: CPF inválido!

objeto_cpf3 = Cpf("73639575091")
print(objeto_cpf3)

print("-----------------------------------------------")

from validate_docbr import CPF
cpf = CPF()
print(cpf.validate("736.395.750-91")) # True

print("-----------------------------------------------")

# objeto_cpf4 = CpfCnpj("736.395.750-91")
# print(objeto_cpf4)
# ValueError: Quantidade de dígitos inválida

# Ajuste na função cpf_eh_Valido:
objeto_cpf4 = Cpf("736.395.750-91")
print(objeto_cpf4)
# 002..98.0.6-43-75

print("-----------------------------------------------")