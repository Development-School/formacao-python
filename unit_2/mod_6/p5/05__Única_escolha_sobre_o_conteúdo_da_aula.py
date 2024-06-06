
from collections import Counter

def analisa_frequencia_de_letras(texto):
  aparicoes = Counter(texto.lower())
  total_de_caracteres = sum(aparicoes.values())

  proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
  proporcoes = Counter(dict(proporcoes))

  mais_comuns = proporcoes.most_common(10)
  for caractere, proporcao in mais_comuns:
      print("{} => {:.2f}%".format(caractere, proporcao * 100))

print("-----------------------------------------------")

meu_texto = """
Nós estamos implementando uma nova funcionalidade (feature) no sistema de uma livraria. Este setor está inserindo uma função para contar a frequência de cada letra nos textos cadastrados. Temos então o seguinte código:
"""

analisa_frequencia_de_letras(meu_texto)
#   => 14.55%
# a => 10.45%
# e => 9.55%
# o => 7.27%
# n => 6.82%
# s => 6.82%
# t => 6.82%
# i => 5.00%
# d => 4.55%
# r => 4.55%

print("-----------------------------------------------")