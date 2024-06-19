# -------------------------------------------------------------------- #
# 07_Fazendo_uma_requisição
# -------------------------------------------------------------------- #

import requests

def retorna_endereco(cep):
    url = 'https://viacep.com.br/ws/{}/json'.format(cep)
    r = requests.get(url)
    dados = r.json()
    bairro = dados.get('bairro')
    cidade = dados.get('localidade')
    uf = dados.get('uf')
    return bairro, cidade, uf

print("-----------------------------------------------")

cep = '01001000'
bairro, cidade, uf = retorna_endereco(cep)

print(f"Bairro: {bairro}, cidade: {cidade}/{uf}")

print("-----------------------------------------------")