# url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
url = " "

# Sanitização da URL
# url = url.replace(" ", "")
url = url.strip()

# Validação da URL
if url == "":
    # raise ValueError("A URL está vazia")
    print('raise ValueError("A URL está vazia")')

# Separa base e parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
if len(url) != 0: print(url_parametros) # Imprima se a url não estiver vazia

# Busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

# print(valor) if len(url) != 0 else print('Teste')
if (len(url) != 0): print(valor)