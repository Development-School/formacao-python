
print("-----------------------------------------------")

cpf = 15616987913
# tamanho_cpf = len(cpf) # TypeError: object of type 'int' has no len()
# print(tamanho_cpf)

#-------------------------------------------------------------

cpf = str(cpf)
tamanho_cpf = len(cpf)
print(tamanho_cpf)
# 11

print("-----------------------------------------------")

from Cpf import Cpf
objeto_cpf = Cpf(cpf)
# print(objeto_cpf)
# <CpfCnpj.CpfCnpj object at 0x00000279208AB7D0>
print('Antes da implementação do \"__str__\":\n<CpfCnpj.CpfCnpj object at 0x00000279208AB7D0>')

print("-----------------------------------------------")

# fatia_um = cpf[:3]
# fatia_dois = cpf[3:6]
# fatia_tres = cpf[6:9]
# fatia_quatro = cpf[9:]
#
# cpf_formatado = "{}.{}.{}-{}".format(
#     fatia_um,
#     fatia_dois,
#     fatia_tres,
#     fatia_quatro
# )
#
# print(cpf_formatado)
# 156.169.879-13

print(objeto_cpf)

print("-----------------------------------------------")

# Utilizando pacote externo "pip install validdocbr"
# Ref.: (https://pypi.org/project/validdocbr/)
# Comando para instalação via pip:
# $ pip install validate-docbr

from validate_docbr import CPF

cpf = CPF()

# cpf.validate(15316389756) # TypeError: 'int' object is not iterable
print(cpf.validate("15316389756")) # False
print(cpf.validate("012.345.678-90")) # True

print("-----------------------------------------------")

# Validar CPF
print(cpf.validate("012.345.678-90"))  # True
print(cpf.validate("012.345.678-91"))  # False

print("-----------------------------------------------")

# print(cpf.validate(73639575091))
# SyntaxError: leading zeros in decimal integer literals are not
# permitted; use an 0o prefix for octal integers

print(cpf.validate('73639575091')) # True

print("-----------------------------------------------")