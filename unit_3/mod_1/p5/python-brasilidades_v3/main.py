from Cpf_Cnpj import Documento
#-------------------------------------------------------------

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
print("Trabalhando com Telefones ▼")
print("-----------------------------------------------")

from TelefonesBr import TelefonesBr

telefone = "+552126481234"
print(TelefonesBr(telefone)) # +55(21)2648-1234

telefone = "2126481234"
print(TelefonesBr(telefone)) # +None(21)2648-1234

print("-----------------------------------------------")
print("Trabalhando com Datas ▼")
print("-----------------------------------------------")

from datas_br import DatasBr
"""
%A retorna os dias da semana por extenso, como Sunday;
%d exibe os dias do mês com números de 01 a 31;
%m retorna meses em números de 01 a 12;
%y mostra o ano com apenas dois dígitos;
%Y apresenta o ano em formato de quatro números;
%H retorna o horário no formato decimal, como 00, 001 e etc;
%M exibe os minutos de forma decimal;
%S apresenta os segundos em decimal."""

cadastro = DatasBr()
print(cadastro) # 18/06/2024 14:19
print(f"A data de hoje é: "
      f"{cadastro.dia_semana()}, "
      f"dia {cadastro.data().day} de "
      f"{cadastro.mes_cadastro()} de "
      f"{cadastro.data().year}")

# day
# month
# year

print("-----------------------------------------------")
print("Trabalhando com CEP ▼")
print("-----------------------------------------------")

# from acesso_cep import BuscaEndereco
#
# # cep = 2587014 # ValueError: CEP inválido!!
# # cep = 258701455 # ValueError: CEP inválido!!
# cep = 25870145
# objeto_cep = BuscaEndereco(cep)
# # print(objeto_cep) # <acesso_cep.BuscaEndereco object at 0x00000252837777A0>
#
# # print(f'{str(cep)[:5]}-{str(cep)[5:]}')
# print(objeto_cep) #
#
# print("-----------------------------------------------")
#
# import requests
#
# # r = requests.get('https://api.github.com/events')
# r = requests.get('https://viacep.com.br/ws/01001000/json/')
# print(r) # <Response [200]>
#
# print("-----------------------------------------------")
#
# print(r.json())
# # {'cep': '01001-000', 'logradouro': 'Praça da Sé', 'complemento': 'lado ímpar', 'bairro': 'Sé', 'localidade': 'São Paulo', 'uf': 'SP', 'ibge': '3550308', 'gia': '1004', 'ddd': '11', 'siafi': '7107'}
#
# print("-----------------------------------------------")
#
# # r.encoding = 'ISO-8859-1'
# # print(r.encoding) # ISO-8859-1
#
# # print(r.text)
# """
# {
#   "cep": "01001-000",
#   "logradouro": "PraÃ§a da SÃ©",
#   "complemento": "lado Ã­mpar",
#   "bairro": "SÃ©",
#   "localidade": "SÃ£o Paulo",
#   "uf": "SP",
#   "ibge": "3550308",
#   "gia": "1004",
#   "ddd": "11",
#   "siafi": "7107"
# }
# """
#
# # print(r.encoding) # utf-8
# # r.encoding = 'utf-8'
#
# print(r.text)
# """
# {
#   "cep": "01001-000",
#   "logradouro": "Praça da Sé",
#   "complemento": "lado ímpar",
#   "bairro": "Sé",
#   "localidade": "São Paulo",
#   "uf": "SP",
#   "ibge": "3550308",
#   "gia": "1004",
#   "ddd": "11",
#   "siafi": "7107"
# }
# """
#
# print("-----------------------------------------------")
#
# print(type(r.text)) # <class 'str'>
#
# print("-----------------------------------------------")
#
# cep = '01001000'
# objeto_cep = BuscaEndereco(cep)
#
# r = objeto_cep.acessa_via_cep()
# print(r) # <Response [200]>
# print(type(r)) # <class 'requests.models.Response'>
#
# print(dir(r))
# # ['__attrs__', '__bool__', '__class__', '__delattr__',
# # '__dict__', '__dir__', '__doc__', '__enter__', '__eq__',
# # '__exit__', '__format__', '__ge__', '__getattribute__',
# # '__getstate__', '__gt__', '__hash__', '__init__',
# # '__init_subclass__', '__iter__', '__le__', '__lt__',
# # '__module__', '__ne__', '__new__', '__nonzero__',
# # '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
# # '__setstate__', '__sizeof__', '__str__', '__subclasshook__',
# # '__weakref__', '_content', '_content_consumed', '_next',
# # 'apparent_encoding', 'close', 'connection', 'content',
# # 'cookies', 'elapsed', 'encoding', 'headers', 'history',
# # 'is_permanent_redirect', 'is_redirect', 'iter_content',
# # 'iter_lines', 'json', 'links', 'next', 'ok',
# # 'raise_for_status', 'raw', 'reason', 'request',
# # 'status_code', 'text', 'url']
#
# print("-----------------------------------------------")
#
# print(r.text)
# """{
#   "cep": "01001-000",
#   "logradouro": "Praça da Sé",
#   "complemento": "lado ímpar",
#   "bairro": "Sé",
#   "localidade": "São Paulo",
#   "uf": "SP",
#   "ibge": "3550308",
#   "gia": "1004",
#   "ddd": "11",
#   "siafi": "7107"
# }"""
#
# print(r.json())
# """
# {'cep': '01001-000', 'logradouro': 'Praça da Sé', 'complemento': 'lado ímpar', 'bairro': 'Sé', 'localidade': 'São Paulo', 'uf': 'SP', 'ibge': '3550308', 'gia': '1004', 'ddd': '11', 'siafi': '7107'}
# """
#
# print("-----------------------------------------------")
#
# print(type(r.text))
# # <class 'str'>
#
# print(type(r.json()))
# # <class 'dict'>

#-------------------------------------------------------------

from acesso_cep import BuscaEndereco

import requests

cep = '01001000'
objeto_cep = BuscaEndereco(cep)

r = objeto_cep.acessa_api_via_cep()
# print(type(r)) # <class 'tuple'>

#-------------------------------------------------------------

bairro, cidade, uf = objeto_cep.acessa_api_via_cep()
print(bairro, cidade, uf) # Sé São Paulo SP

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")