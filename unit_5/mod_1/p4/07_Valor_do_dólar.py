
"""
A API https://economia.awesomeapi.com.br/last/USD-BRL é uma interface que fornece informações
sobre a última cotação de câmbio entre o dólar americano (USD) e o real brasileiro (BRL). Em outras palavras,
ela retorna o valor mais recente de 1 dólar em reais, com base nas taxas de câmbio disponíveis
no momento da solicitação.

Para entender melhor a resposta, segue uma breve documentação da resposta desta API:

Atributo	Descrição
code	    Código da moeda (USD - Dólar Americano)
codein	    Código da moeda de referência (BRL - Real Brasileiro)
name	    Nome da moeda (Dólar Americano/Real Brasileiro)
high	    Valor mais alto durante o período
low	        Valor mais baixo durante o período
varBid	    Variação do lance (oferta)
pctChange	Percentual de mudança
bid	        Preço de compra (lance)
ask	        Preço de venda (oferta)
timestamp	Carimbo de data/hora UNIX (timestamp)
create_date	Data e hora da criação do registro
"""
print("-----------------------------------------------")

# Sabendo disso, uma pessoa desenvolveu o seguinte código com objetivo de ver a variação do lance: ▼

import requests

url = "https://economia.awesomeapi.com.br/last/USD-BRL"
response = requests.get(url)

# Com base no código acima, marque a opção que descreve a seguinte saída no console: ▼

if response.status_code == 200:
    data = response.json()
    cotacao = float(data['USDBRL']['bid'])
    mensagem = f"U$ {cotacao} dólar corresponde a R$ 1"
    print(mensagem)
else:
    print(f"A requisição falhou com o código de status {response.status_code}")

#-------------------------------------------------------------

# U$ 1 dólar corresponde a R$ 5.02
# U$ 5.4376 dólar corresponde a R$ 1

print("-----------------------------------------------")