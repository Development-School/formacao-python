
print("-----------------------------------------------")

# Alura
# Ref.: (https://cursos.alura.com.br/forum/topico-duvida-sobre-regex-opcionais-210670)

# [a-z0-9._-]:
"""Buscará por um conjunto de caracteres informados, antes do
arroba (@), independente do tamanho."""

# + (mais):
"""Informa que deverá haver uma ou mais ocorrência do conjunto
informado anteriormente."""

# @[a-z0-9.-]:
"""Buscará por um conjunto de caracteres informados, que
deverá está após o arroba (@), independente do tamanho."""

# \ . (contra barra ponto):
"""Retira a propriedade especial do ponto (.)."""

# [a-z]:
"""Buscará por um conjunto de letras após o ponto."""

# ?.[a-z]:
"""Buscará por um ponto e um conjunto de letras,
podendo = ou não ser informado."""

r"""
[] – conjunto de  caracteres;
 \ – sequência especial de caracteres;
^ – buscar elementos no início da string;
$ – buscar elementos no final da string;
* – buscar zero ou mais repetições de uma substring;
+ – uma ou mais aparições de uma substring;
? – zero ou uma aparição;
| – busca um caractere ou outro.
"""

#-------------------------------------------------------------

import re

padrao = r"[a-z0-9._-]+@[a-z0-9.-]+\.[a-z]?.[a-z]"

email = "Aqui está o email: jorger.abello3@gmail.com.br, favor cadastrar"
resposta = re.search(padrao, email)

print(resposta.group())
# jorger.abello3@gmail.com.br

print("-----------------------------------------------")

padrao = r"[a-z0-9._-]+@[a-z0-9.-]+\.[a-z]?.[a-z]"
email = "teste jorger.abello3@gmail.com, favor cadastrar"
resposta = re.search(padrao, email)
print(resposta.group())

print("-----------------------------------------------")

padrao = r'[0-9]{2}[a-z]{0,99}+[.pdf]{4}'
texto = 'isso é um 01teste.pdf'
busca = re.findall(padrao, texto)
print(busca)

print("-----------------------------------------------")

padrao = r'[0-9]{2}[a-z]{0,99}+[.pdf]{4}'
texto = 'isso é um 01teste.pdf 02teste.pdf'
busca = re.findall(padrao, texto)
print(busca)

print("-----------------------------------------------")

padrao = r'[0-9]{2}[a-z]{0,99}[.pdf]*'
texto = 'isso é um 01teste 02teste.pdf'
busca = re.findall(padrao, texto)
print(busca)

print("-----------------------------------------------")

# padrao = r'([0-9]{2})([a-z]{0,99})(\.pdf)*'
# padrao = r'([0-9]{2})([a-z]{0,99})(\.)?(pdf)?'
padrao = r'([0-9]{2})([a-z]{0,99})(\.pdf)?'
texto = 'isso é um 01teste 02teste.pdf'
busca = re.findall(padrao, texto)
print(busca)

print("-----------------------------------------------")