
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

print("-----------------------------------------------")

from collections import defaultdict

class Conta:
  def __init__(self):
    print("Criando uma conta")

contas = defaultdict(Conta)
print(contas[15])
# Criando uma conta
# <__main__.Conta object at 0x000002EE6A0A4E30>

print("-----------------------------------------------")

from collections import Counter # já possui o valor zero

aparicoes = Counter(meu_texto.split())
print(aparicoes)
# Counter({'meu': 2, 'gosto': 2, 'muito': 2, 'de': 2, 'e': 2, 'cachorro': 2, 'bem': 1, 'vindo': 1, 'nome': 1, 'é': 1, 'guilherme': 1, 'eu': 1, 'nomes': 1, 'tenho': 1, 'o': 1})

print("-----------------------------------------------")

for x in "guilherme":
  print(x)

print("-----------------------------------------------")

texto1 = """
[00:23] Então o que vamos fazer é o seguinte: vamos pegar dois textos, por exemplo eu posso entrar no blog da Alura e pegar textos do blog da Alura. Eu posso pegar um texto que está falando sobre expressões regulares e posso pegar um outro texto de outro assunto, só para não termos dois assuntos similares. Vou pegar um o outro assunto, temos um de programação e um aqui que é de negócios: B2C, B2B, coisas do gênero. Então dois assuntos distintos, um de programação e um não de programação.
[00:53] Então dois assuntos, dois textos. Vamos separar esses dois textos? Então vou copiar uma parte desse texto aqui, vou copiar três parágrafos. Vou copiar uns três parágrafos iniciais, , então três aspas e três aspas para poder ter várias linhas, então no Python várias linhas, três parágrafos. Repara, eu não vou copiar o código, eu não quero o código, eu quero o texto em português, então vou copiar essas outras aqui, quatro parágrafos, que também é texto em português.
[01:23] Então eu quero copiar o texto em português sobre programação e mais um pouco aqui, copiar tudo isso. Então eu tenho um texto, que é um texto razoável, posso rodar, é um texto sobre programação e vou colocar um texto2 também, três aspas, Enter. E agora um texto sobre B2C, B2B, e por aí vai. Então vou pegar esse texto aqui, e olha, tem bastante texto, tem bastante texto mesmo. Não é programação, então vou copiar todo esse texto, porque não falou de programação. Copiei.
[02:00] Então dois textos de assuntos totalmente diferentes: vendas, negócio, B2B, B2C; programação, expressão regular, e por aí vai, no caso era até com Java Script e HTML, se não me engano. Então vamos lá. Então eu tenho dois textos que eu queria fazer agora era contar as letras. Será que eu consigo contar as letras de um texto? Então vamos parar para pensar: se eu fizer um for palavra in texto1.split( ):. Quando eu faço o texto1.split( ), o que é o texto1.split( ) mesmo? Ele quebra o texto em palavras.
"""
print(texto1.split( ))
# ['[00:23]', 'Então', 'o', 'que', 'vamos', 'fazer', 'é', 'o', 'seguinte:', 'vamos', 'pegar', 'dois', 'textos,', 'por', 'exemplo', 'eu', 'posso', 'entrar', 'no', 'blog', 'da', 'Alura', 'e', 'pegar', 'textos', 'do', 'blog', 'da', 'Alura.', 'Eu', 'posso', 'pegar', 'um', 'texto', 'que', 'está', 'falando', 'sobre', 'expressões', 'regulares', 'e', 'posso', 'pegar', 'um', 'outro', 'texto', 'de', 'outro', 'assunto,', 'só', 'para', 'não', 'termos', 'dois', 'assuntos', 'similares.', 'Vou', 'pegar', 'um', 'o', 'outro', 'assunto,', 'temos', 'um', 'de', 'programação', 'e', 'um', 'aqui', 'que', 'é', 'de', 'negócios:', 'B2C,', 'B2B,', 'coisas', 'do', 'gênero.', 'Então', 'dois', 'assuntos', 'distintos,', 'um', 'de', 'programação', 'e', 'um', 'não', 'de', 'programação.', '[00:53]', 'Então', 'dois', 'assuntos,', 'dois', 'textos.', 'Vamos', 'separar', 'esses', 'dois', 'textos?', 'Então', 'vou', 'copiar', 'uma', 'parte', 'desse', 'texto', 'aqui,', 'vou', 'copiar', 'três', 'parágrafos.', 'Vou', 'copiar', 'uns', 'três', 'parágrafos', 'iniciais,', ',', 'então', 'três', 'aspas', 'e', 'três', 'aspas', 'para', 'poder', 'ter', 'várias', 'linhas,', 'então', 'no', 'Python', 'várias', 'linhas,', 'três', 'parágrafos.', 'Repara,', 'eu', 'não', 'vou', 'copiar', 'o', 'código,', 'eu', 'não', 'quero', 'o', 'código,', 'eu', 'quero', 'o', 'texto', 'em', 'português,', 'então', 'vou', 'copiar', 'essas', 'outras', 'aqui,', 'quatro', 'parágrafos,', 'que', 'também', 'é', 'texto', 'em', 'português.', '[01:23]', 'Então', 'eu', 'quero', 'copiar', 'o', 'texto', 'em', 'português', 'sobre', 'programação', 'e', 'mais', 'um', 'pouco', 'aqui,', 'copiar', 'tudo', 'isso.', 'Então', 'eu', 'tenho', 'um', 'texto,', 'que', 'é', 'um', 'texto', 'razoável,', 'posso', 'rodar,', 'é', 'um', 'texto', 'sobre', 'programação', 'e', 'vou', 'colocar', 'um', 'texto2', 'também,', 'três', 'aspas,', 'Enter.', 'E', 'agora', 'um', 'texto', 'sobre', 'B2C,', 'B2B,', 'e', 'por', 'aí', 'vai.', 'Então', 'vou', 'pegar', 'esse', 'texto', 'aqui,', 'e', 'olha,', 'tem', 'bastante', 'texto,', 'tem', 'bastante', 'texto', 'mesmo.', 'Não', 'é', 'programação,', 'então', 'vou', 'copiar', 'todo', 'esse', 'texto,', 'porque', 'não', 'falou', 'de', 'programação.', 'Copiei.', '[02:00]', 'Então', 'dois', 'textos', 'de', 'assuntos', 'totalmente', 'diferentes:', 'vendas,', 'negócio,', 'B2B,', 'B2C;', 'programação,', 'expressão', 'regular,', 'e', 'por', 'aí', 'vai,', 'no', 'caso', 'era', 'até', 'com', 'Java', 'Script', 'e', 'HTML,', 'se', 'não', 'me', 'engano.', 'Então', 'vamos', 'lá.', 'Então', 'eu', 'tenho', 'dois', 'textos', 'que', 'eu', 'queria', 'fazer', 'agora', 'era', 'contar', 'as', 'letras.', 'Será', 'que', 'eu', 'consigo', 'contar', 'as', 'letras', 'de', 'um', 'texto?', 'Então', 'vamos', 'parar', 'para', 'pensar:', 'se', 'eu', 'fizer', 'um', 'for', 'palavra', 'in', 'texto1.split(', '):.', 'Quando', 'eu', 'faço', 'o', 'texto1.split(', '),', 'o', 'que', 'é', 'o', 'texto1.split(', ')', 'mesmo?', 'Ele', 'quebra', 'o', 'texto', 'em', 'palavras.']

print("-----------------------------------------------")

aparicoes = Counter(texto1.lower())
print(aparicoes)
# Counter({' ': 344, 'o': 196, 'e': 168, 'a': 143, 's': 128, 't': 124, 'r': 115, 'u': 83, 'p': 61, 'n': 59, 'i': 54, 'm': 52, ',': 39, 'g': 35, 'd': 32, 'ã': 31, 'x': 29, 'c': 27, 'l': 26, 'v': 23, '.': 22, 'q': 21, 'b': 20, 'f': 12, '2': 10, 'é': 10, 'á': 10, 'ê': 10, ':': 9, 'ç': 9, '0': 8, 'h': 7, '\n': 5, 'ó': 5, '[': 4, ']': 4, 'z': 4, '1': 4, '3': 3, '?': 3, '(': 3, ')': 3, 'í': 2, 'õ': 1, '5': 1, 'y': 1, ';': 1, 'j': 1})

print("-----------------------------------------------")

print(aparicoes.values())
# dict_values([5, 4, 8, 9, 10, 3, 4, 344, 168, 59, 124, 31, 196, 21, 83, 23, 143, 52, 128, 12, 4, 115, 10, 35, 54, 61, 32, 29, 39, 26, 20, 22, 10, 1, 5, 9, 27, 10, 1, 3, 7, 1, 4, 2, 1, 1, 3, 3])

total_de_caracteres = sum(aparicoes.values())
print(total_de_caracteres)
# 1962

print("-----------------------------------------------")

for letra, frequencia in aparicoes.items():
  # 'a' 182/1821 ==> 10% (0.1)
  tupla = (letra, frequencia / total_de_caracteres)
  print(tupla)

# ('\n', 0.0025484199796126403)
# ('[', 0.0020387359836901123)
# ('0', 0.004077471967380225)
# ...

print("-----------------------------------------------")

print([(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()])
# [('\n', 0.0025484199796126403), ('[', 0.0020387359836901123), ('0', 0.004077471967380225), (':', 0.0045871559633027525), ('2', 0.0050968399592252805), ('3', 0.0015290519877675841), (']', 0.0020387359836901123), (' ', 0.17533129459734964), ('e', 0.0856269113149847), ('n', 0.030071355759429153), ('t', 0.06320081549439348), ('ã', 0.01580020387359837), ('o', 0.0998980632008155), ('q', 0.010703363914373088), ('u', 0.042303771661569824), ('v', 0.011722731906218144), ('a', 0.0728848114169215), ('m', 0.026503567787971458), ('s', 0.0652395514780836), ('f', 0.0061162079510703364), ('z', 0.0020387359836901123), ('r', 0.058613659531090725), ('é', 0.0050968399592252805), ('g', 0.01783893985728848), ('i', 0.027522935779816515), ('p', 0.03109072375127421), ('d', 0.0163098878695209), ('x', 0.014780835881753314), (',', 0.019877675840978593), ('l', 0.013251783893985729), ('b', 0.010193679918450561), ('.', 0.011213047910295617), ('á', 0.0050968399592252805), ('õ', 0.0005096839959225281), ('ó', 0.0025484199796126403), ('ç', 0.0045871559633027525), ('c', 0.013761467889908258), ('ê', 0.0050968399592252805), ('5', 0.0005096839959225281), ('?', 0.0015290519877675841), ('h', 0.003567787971457696), ('y', 0.0005096839959225281), ('1', 0.0020387359836901123), ('í', 0.0010193679918450561), (';', 0.0005096839959225281), ('j', 0.0005096839959225281), ('(', 0.0015290519877675841), (')', 0.0015290519877675841)]

print("-----------------------------------------------")

proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
# proporcoes = dict(proporcoes)
proporcoes = Counter(dict(proporcoes))
print(proporcoes)
# {'\n': 0.0025484199796126403, '[': 0.0020387359836901123, '0': 0.004077471967380225, ':': 0.0045871559633027525, '2': 0.0050968399592252805, '3': 0.0015290519877675841, ']': 0.0020387359836901123, ' ': 0.17533129459734964, 'e': 0.0856269113149847, 'n': 0.030071355759429153, 't': 0.06320081549439348, 'ã': 0.01580020387359837, 'o': 0.0998980632008155, 'q': 0.010703363914373088, 'u': 0.042303771661569824, 'v': 0.011722731906218144, 'a': 0.0728848114169215, 'm': 0.026503567787971458, 's': 0.0652395514780836, 'f': 0.0061162079510703364, 'z': 0.0020387359836901123, 'r': 0.058613659531090725, 'é': 0.0050968399592252805, 'g': 0.01783893985728848, 'i': 0.027522935779816515, 'p': 0.03109072375127421, 'd': 0.0163098878695209, 'x': 0.014780835881753314, ',': 0.019877675840978593, 'l': 0.013251783893985729, 'b': 0.010193679918450561, '.': 0.011213047910295617, 'á': 0.0050968399592252805, 'õ': 0.0005096839959225281, 'ó': 0.0025484199796126403, 'ç': 0.0045871559633027525, 'c': 0.013761467889908258, 'ê': 0.0050968399592252805, '5': 0.0005096839959225281, '?': 0.0015290519877675841, 'h': 0.003567787971457696, 'y': 0.0005096839959225281, '1': 0.0020387359836901123, 'í': 0.0010193679918450561, ';': 0.0005096839959225281, 'j': 0.0005096839959225281, '(': 0.0015290519877675841, ')': 0.0015290519877675841}
# Counter({' ': 0.17533129459734964, 'o': 0.0998980632008155, 'e': 0.0856269113149847, 'a': 0.0728848114169215, 's': 0.0652395514780836, 't': 0.06320081549439348, 'r': 0.058613659531090725, 'u': 0.042303771661569824, 'p': 0.03109072375127421, 'n': 0.030071355759429153, 'i': 0.027522935779816515, 'm': 0.026503567787971458, ',': 0.019877675840978593, 'g': 0.01783893985728848, 'd': 0.0163098878695209, 'ã': 0.01580020387359837, 'x': 0.014780835881753314, 'c': 0.013761467889908258, 'l': 0.013251783893985729, 'v': 0.011722731906218144, '.': 0.011213047910295617, 'q': 0.010703363914373088, 'b': 0.010193679918450561, 'f': 0.0061162079510703364, '2': 0.0050968399592252805, 'é': 0.0050968399592252805, 'á': 0.0050968399592252805, 'ê': 0.0050968399592252805, ':': 0.0045871559633027525, 'ç': 0.0045871559633027525, '0': 0.004077471967380225, 'h': 0.003567787971457696, '\n': 0.0025484199796126403, 'ó': 0.0025484199796126403, '[': 0.0020387359836901123, ']': 0.0020387359836901123, 'z': 0.0020387359836901123, '1': 0.0020387359836901123, '3': 0.0015290519877675841, '?': 0.0015290519877675841, '(': 0.0015290519877675841, ')': 0.0015290519877675841, 'í': 0.0010193679918450561, 'õ': 0.0005096839959225281, '5': 0.0005096839959225281, 'y': 0.0005096839959225281, ';': 0.0005096839959225281, 'j': 0.0005096839959225281})

mais_comuns = proporcoes.most_common(3) # 3 mais comuns
print(mais_comuns)
# [(' ', 0.17533129459734964), ('o', 0.0998980632008155), ('e', 0.0856269113149847)]

print("-----------------------------------------------")

def analisa_frequencia_de_letras(texto):
  aparicoes = Counter(texto.lower())
  total_de_caracteres = sum(aparicoes.values())

  proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
  proporcoes = Counter(dict(proporcoes))
  mais_comuns = proporcoes.most_common(10)
  for caractere, proporcao in mais_comuns:
    print((caractere, proporcao))

analisa_frequencia_de_letras(texto1)

# (' ', 0.17533129459734964)
# ('o', 0.0998980632008155)
# ('e', 0.0856269113149847)
# ('a', 0.0728848114169215)
# ('s', 0.0652395514780836)
# ('t', 0.06320081549439348)
# ('r', 0.058613659531090725)
# ('u', 0.042303771661569824)
# ('p', 0.03109072375127421)
# ('n', 0.030071355759429153)

print("-----------------------------------------------")

def analisa_frequencia_de_letras(texto):
  aparicoes = Counter(texto.lower())
  total_de_caracteres = sum(aparicoes.values())

  proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
  proporcoes = Counter(dict(proporcoes))
  mais_comuns = proporcoes.most_common(10)

  for caractere, proporcao in mais_comuns:
    print("{} => {:.2f}%".format(caractere, proporcao * 100))

analisa_frequencia_de_letras(texto1)

#   => 17.53%
# o => 9.99%
# e => 8.56%
# a => 7.29%
# s => 6.52%
# t => 6.32%
# r => 5.86%
# u => 4.23%
# p => 3.11%
# n => 3.01%

print("-----------------------------------------------")
