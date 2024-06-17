from Cpf_Cnpj import CpfCnpj

print("-----------------------------------------------")
print("Trabalhando com CPF ▼")
print("-----------------------------------------------")

objeto_cpf = CpfCnpj("05826307030", 'cpf')
print(objeto_cpf) # 058.263.070-30

print("-----------------------------------------------")

objeto_cpf2 = CpfCnpj("058.263.070-30", 'cpf')
print(objeto_cpf2) # 058.263.070-30

print("-----------------------------------------------")
print("Trabalhando com CNPJ ▼")
print("-----------------------------------------------")

# from validate_docbr import CNPJ
#
# cnpj = CNPJ()
# print(cnpj.validate('31.292.014/0001-50')) # True
# print(cnpj.validate('31292014000150')) # True

objeto_cnpj = CpfCnpj('31.292.014/0001-50', "cnpj")
print(objeto_cnpj)

print("-----------------------------------------------")

objeto_cnpj2 = CpfCnpj('31292014000150', "cnpj")
print(objeto_cnpj2)

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")