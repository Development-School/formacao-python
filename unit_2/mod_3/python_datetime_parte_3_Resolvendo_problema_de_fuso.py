
""" Parte 3:"""

"""Resolvendo o problema do fuso horário:"""

"""Vamos, agora, criar um objeto timezone correspondente ao UTC-3, indicando essa diferença do UTC
como parâmetro do construtor:"""

from datetime import date, datetime, timezone, timedelta

data_e_hora_atuais = datetime.now()
diferenca = timedelta(hours=-3)

fuso_horario = timezone(diferenca)
print(fuso_horario)

# Temos justamente o que queríamos:
# UTC-03:00

print("-----------------------------------------------")

"""Finalmente, podemos converter o tempo da máquina para o de São Paulo, usando o método astimezone():"""

data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_sao_paulo_em_texto)

# Agora está tudo padronizado:
# 01/03/2018 12:30

print("-----------------------------------------------")