def faz_processamento_de_visualizacao(lista):
  print(len(lista))
  lista.append(13)

idades = [16, 21, 29, 56, 43]
faz_processamento_de_visualizacao(idades)

print(idades)

print("-----------------------------------------------")

def faz_processamento_de_visualizacao_2(lista = []):
  print(len(lista))
  print(lista)
  lista.append(13)

print(faz_processamento_de_visualizacao_2())
print(faz_processamento_de_visualizacao_2())
print(faz_processamento_de_visualizacao_2())
print(faz_processamento_de_visualizacao_2())

print("-----------------------------------------------")

def faz_processamento_de_visualizacao_3(lista = list()):
  print(len(lista))
  print(f'Dentro da fução: {lista}')
  lista.append(13)

print(faz_processamento_de_visualizacao_3())
print(faz_processamento_de_visualizacao_3())
print(faz_processamento_de_visualizacao_3())
print(faz_processamento_de_visualizacao_3())

print("-----------------------------------------------")

def faz_processamento_de_visualizacao_4(lista = None):
  # lista = list() if lista == None else None
  if lista == None: lista = list()
  print(f'Tamanho: {len(lista)}')
  print(f'Dentro da fução: {lista}')
  lista.append(13)

print(faz_processamento_de_visualizacao_4())
print(faz_processamento_de_visualizacao_4())
print(faz_processamento_de_visualizacao_4())
print(faz_processamento_de_visualizacao_4())