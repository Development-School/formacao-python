# -------------------------------------------------------------------- #
# 07. Avaliando listas e iterações
# -------------------------------------------------------------------- #


projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for i in projetos:
    print(f'Projeto: {i}')

print("-----------------------------------------------")

try:
  for projeto in projetos:
    print(f"Projeto: {projeto}")
except Exception as e:
  print("Ocorreu um erro:", e)

print("-----------------------------------------------")

for i in range(len(projetos)):
  try:
    print(f"Projeto: {projetos[i]}")
  except IndexError:
    print("Índice fora do alcance.")

print("-----------------------------------------------")

# Correto
for projeto in projetos:
  if projeto:
    print(f"Projeto: {projeto}")
  else:
    print("Projeto não disponível.")

print("-----------------------------------------------")

for projeto in projetos:
  try:
    print(f"Projeto: {projeto}")
  except TypeError:
    print("Projeto não disponível.")

print("-----------------------------------------------")