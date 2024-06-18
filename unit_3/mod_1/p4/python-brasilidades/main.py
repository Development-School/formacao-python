from Cpf_Cnpj import Documento
#-------------------------------------------------------------

# print("-----------------------------------------------")
# print("Trabalhando com CPF ▼")
# print("-----------------------------------------------")
#
# objeto_cpf = Documento.cria_documento("05826307030")
# print(objeto_cpf) # 058.263.070-30
#
# print("-----------------------------------------------")
# print("Trabalhando com CNPJ ▼")
# print("-----------------------------------------------")
#
# objeto_cnpj2 = Documento.cria_documento('31292014000150')
# print(objeto_cnpj2)
#
# print("-----------------------------------------------")
# print("Trabalhando com Telefones ▼")
# print("-----------------------------------------------")
#
# from TelefonesBr import TelefonesBr
#
# telefone = "+552126481234"
# print(TelefonesBr(telefone)) # +55(21)2648-1234
#
# telefone = "2126481234"
# print(TelefonesBr(telefone)) # +None(21)2648-1234

print("-----------------------------------------------")
print("Trabalhando com Datas ▼")
print("-----------------------------------------------")

from datetime import datetime
print(datetime.today()) # 2024-06-18 13:49:32.842404

print("-----------------------------------------------")

from datas_br import DatasBr
print(DatasBr().momento_cadastro) # 2024-06-18 13:57:03.071444

print("-----------------------------------------------")

print(DatasBr().mes_cadastro()) # junho
print(DatasBr().dia_semana()) # 1
print(DatasBr().dia_semana()) # terça

print("-----------------------------------------------")

"""
%A retorna os dias da semana por extenso, como Sunday;
%d exibe os dias do mês com números de 01 a 31;
%m retorna meses em números de 01 a 12;
%y mostra o ano com apenas dois dígitos;
%Y apresenta o ano em formato de quatro números;
%H retorna o horário no formato decimal, como 00, 001 e etc;
%M exibe os minutos de forma decimal;
%S apresenta os segundos em decimal."""

hoje = datetime.today()
hoje_formatada = hoje.strftime("%d/%m/%Y %H:%M")

print(hoje) # 2024-06-18 14:14:36.491998
print(hoje_formatada) # 18/06/2024 14:14
print(type(hoje_formatada)) # <class 'str'>

print("-----------------------------------------------")

cadastro = DatasBr()
print(cadastro) # 18/06/2024 14:19

print("-----------------------------------------------")

numero = 1
string = "um"
print(len(string)) # 2
# print(len(numero)) # TypeError: object of type 'int' has no len()

print("-----------------------------------------------")

from datetime import timedelta

hoje = datetime.today()
amanha = datetime.today() + timedelta(days=1)

print(hoje) # 2024-06-18 14:34:26.703614
print(amanha) # 2024-06-19 14:34:26.703614
print(amanha - hoje) # 1 day, 0:00:00

amanha = datetime.today() + timedelta(days=1, hours=20)
print(amanha - hoje) # 1 day, 20:00:00

amanha = datetime.today() + timedelta(days=1, hours=24)
print(amanha - hoje) # 2 days, 0:00:00

print("-----------------------------------------------")

hoje = DatasBr()
print(hoje.tempo_cadastro()) # 0:00:00

# Teste: Exemplo01: (suponto que 'o hoje' é daqui a 30 dias)
print(hoje.tempo_cadastro()) # 30 days, 0:00:00

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")
