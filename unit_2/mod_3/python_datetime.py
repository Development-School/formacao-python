
""" Conhecemos o módulo datetime da biblioteca nativa do Python, então até sabemos pegar a data atual
    através da classe date, basta a importarmos e chamarmos o método today():"""

from datetime import date

data_atual = date.today()
print(data_atual)

print("-----------------------------------------------")

"""Formatando nossa data em uma string:"""

data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)
print(data_em_texto)

print("-----------------------------------------------")

data_em_texto = '0{}/0{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)
print(data_em_texto)

"""O que daria certo, mas traria problemas caso o dia ou o mês fossem maiores ou iguais a 10: """
data_em_texto = '0{}/0{}/{}'.format(data_atual.day, 12, data_atual.year)
print(data_em_texto)

print("-----------------------------------------------")

"""Formatando datas em strings usando o método strftime():"""

data_em_texto = data_atual.strftime('%d/%m/%Y')
print(data_em_texto)

print("-----------------------------------------------")

from datetime import datetime

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')

print(data_e_hora_em_texto)

print("-----------------------------------------------")

data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
print(data_e_hora_em_texto)

print("-----------------------------------------------")

"""Convertendo uma string em datetime:"""

# from datetime import datetime

data_e_hora_em_texto = '01/03/2018 12:30'
data_e_hora = datetime.strptime(data_e_hora_em_texto, '%d/%m/%Y %H:%M')
print(data_e_hora)

print("-----------------------------------------------")



