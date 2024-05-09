
@@ -0,0 +1,42 @@
print("-----------------------------------------------")

texto = "Eu estudo na Alura"
print(texto.find('E'))
# 0

print(texto.find('Eu'))
# 0

print(texto.find('Alura'))
# 13

print(len(texto))
18

print("-----------------------------------------------")

url = "bytebank.com/cambio?moedaOrigem=real"
print(url)

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao] # "omitindo" o valor inicial
print(url_base)

url_parametros = url[indice_interrogacao+1:] # "omitindo" o valor final
print(url_parametros)

print("-----------------------------------------------")

parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)

print(indice_parametro)

print("-----------------------------------------------")

indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_parametros[indice_valor:]

print(valor)

print("-----------------------------------------------")