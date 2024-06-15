
""" Parte 2:"""

"""Fuso horário com a classe timezone:"""

from datetime import datetime, timezone

data_e_hora_atuais = datetime.now()
# fuso_horario = timezone() # ERROR
# print(fuso_horario)

"""Vamos ver o que é impresso na tela:"""

"""Traceback (most recent call last):
  File "05_Entendendo_a_validação.py", line 4, in >
    fuso_horario = timezone()
TypeError: Required argument 'offset' (pos 1) not found"""

"""A exceção TypeError que recebemos indica que o argumento offset, esperado no construtor timezone,
não foi encontrado. Realmente, não colocamos esse argumento. Mas o que ele significa?"""

"""O parâmetro offset representa a diferença entre o fuso horário que queremos criar e o Tempo
Universal Coordenado (UTC). No nosso caso, em São Paulo, temos uma diferença de -3 horas, mais
conhecida como UTC-3. Sabendo disso, vamos tentar novamente:"""

# fuso_horario = timezone(-3) #ERROR
# print(fuso_horario)

"""Vamos ver o que é impresso na tela:"""

"""Traceback (most recent call last):
  File "05_Entendendo_a_validação.py", line 4, in <module>
    fuso_horario = timezone(-3)
TypeError: timezone() argument 1 must be datetime.timedelta, not int"""

"""Calcular a diferença de horários com a classe timedelta:"""

from datetime import timedelta

diferenca = timedelta()
print(diferenca)

print("-----------------------------------------------")

diferenca = timedelta(-3)
print(diferenca)

print("-----------------------------------------------")

"""Mas o quê? -3 dias? A gente queria -3 horas! O problema é que o construtor timedelta recebe vários
outros argumentos além da hora, nessa ordem:

    days (dias)
    seconds (segundos)
    microseconds (microsegundos)
    milliseconds (milisegundos)
    minutes (minutos)
    hours (horas)
    weeks (semanas)
    
Então se a gente só manda um -3 para ele, esse número é interpretado como se fosse em dias. Podemos
passar 0 para os primeiros 5 parâmetros e -3 para as horas, mas isso é um pouco estranho, considerando
que, de fato, queremos definir apenas as horas.

Usando a funcionalidade que o Python tem dos parâmetros nomeados, é possível especificar que estamos
definindo o parâmetro de horas (hours), da seguinte forma:
"""

diferenca = timedelta(hours=-3)
print(diferenca)

# E dessa vez:
# -1 day, 21:00:00

print("-----------------------------------------------")