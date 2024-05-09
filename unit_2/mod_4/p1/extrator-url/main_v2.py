

url = "bytebank.com/cambio?moedaOrigem=real"
print(url)

url_base = url[0:19]
print(url_base)

url_parametros = url[20:36]
print(url_parametros)

print("-----------------------------------------------")

texto = 'abcde'
print(texto.find('c'))
# 2

print("-----------------------------------------------")

url = "bytebank.com/cambio?moedaOrigem=real"
print(url)

indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao] # sem "omitir" o valor inicial
print(url_base)

url_parametros = url[indice_interrogacao+1:36] # sem "omitir" o valor final
print(url_parametros)

print("-----------------------------------------------")

url = "bytebank.com/cambio?moedaOrigem=real"
print(url)

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao] # "omitindo" o valor inicial
print(url_base)

url_parametros = url[indice_interrogacao+1:] # "omitindo" o valor final
print(url_parametros)