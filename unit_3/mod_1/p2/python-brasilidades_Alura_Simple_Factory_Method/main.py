from Cpf_Cnpj import Documento

print("-----------------------------------------------")
print("Trabalhando com CPF ▼")
print("-----------------------------------------------")

objeto_cpf = Documento.cria_documento("05826307030")
print(objeto_cpf) # 058.263.070-30

print("-----------------------------------------------")
print("Trabalhando com CNPJ ▼")
print("-----------------------------------------------")

objeto_cnpj2 = Documento.cria_documento('31292014000150')
print(objeto_cnpj2)

print("-----------------------------------------------")