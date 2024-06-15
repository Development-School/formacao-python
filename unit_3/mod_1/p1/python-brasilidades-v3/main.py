from Cpf import Cpf

print("-----------------------------------------------")

# objeto_cpf4 = Cpf("736.395.750-91")
# print(objeto_cpf4)
# ValueError: Quantidade de dígitos inválida

# Ajuste na função cpf_eh_Valido:
# objeto_cpf4 = Cpf("736.395.750-91")
# print(objeto_cpf4)
# 002..98.0.6-43-75

#-------------------------------------------------------------

# Teste de máscada do validate_docbr
from validate_docbr import CPF

cpf = CPF()
cpf_me = "73639575091"

# Mascara o CPF
print(cpf.mask(cpf_me))  # "012.345.678-90"
print(CPF().mask("73639575091")) # 736.395.750-91

print("-----------------------------------------------")

objeto_cpf4 = Cpf("736.395.750-91")
# print(objeto_cpf4)
# 002..98.0.6-43-75

objeto_cpf5 = Cpf("73639575091")
# print(objeto_cpf5)
# 736.395.750-91

#-------------------------------------------------------------

# Após alterar retorno do "__str__":
print(objeto_cpf4)
# 002..98.0.6-43-75

print(objeto_cpf5)
# 736.395.750-91

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")