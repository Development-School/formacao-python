
"""
Ex.: Arquivo jSON: ▼

[
    {
        "Company":"McDonald’s",
        "Item":"Hamburger",
        "price":32.42,
        "description":"Uma explosão de sabores em cada mordida."
    },
    {
        "Company":"McDonald’s",
        "Item":"Cheeseburger",
        "price":38.81,
        "description":"Uma opção saudável e equilibrada."
    },
"""
import requests
import json

#-------------------------------------------------------------

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

print(response) # <Response [200]>

print("-----------------------------------------------")

url_teste_error = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.jsonTESTE'
response = requests.get(url_teste_error)

print(response) # <Response [404]>

print("-----------------------------------------------")

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
        dados_json = response.json()
        print(dados_json)
else:
        print(f"O erro foi: {response.status_code}")

"""
[{'Company': 'McDonald’s', 'Item': 'Hamburger', 'price': 32.42, 
'description': 'Uma explosão de sabores em cada mordida.'}, 
{'Company': 'McDonald’s', 'Item': 'Cheeseburger', 'price': 38.81, 
'description': 'Uma opção saudável e equilibrada.'}, {'Company': 'McDonald’s', 
'Item': 'Double Cheeseburger', 'price': 50.18, 
'description': 'Leve e saboroso, perfeito a qualquer hora.'}, 
{'Company': 'McDonald’s', 'Item': 'McDouble', 'price': 55.73, 
[...]
"""

print()
print("-----------------------------------------------")
print()

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
        dados_json = response.json()
        # print(dados_json)

        dados_restaurante = {}

        for item in dados_json:
                nome_do_restaurante = item['Company']
                if nome_do_restaurante not in dados_restaurante:
                        dados_restaurante[nome_do_restaurante] = []

                dados_restaurante[nome_do_restaurante].append({
                        "item": item['Item'],
                        "price": item['price'],
                        "description": item['description']
                })

                # Criando arquivo com Python ▼
                for nome_do_restaurante, dados in dados_restaurante.items():
                        nome_do_arquivo = f'{nome_do_restaurante}.json'

                        with open(nome_do_arquivo, 'w') as arquivo_restaurante:
                                json.dump(dados, arquivo_restaurante, indent=4) # import json

                # Vai demorar um pouquinho (alguns segundos), mas no final iremos fazer um print
                # para mostrar quando finalizar...
                # print(f"dump... \"{arquivo_restaurante}\" ...")
                print(f"Gerando arquivo de \"{nome_do_restaurante}\" ...")

        print(f"Arquivos gerados!!")

else:
        print(f"O erro foi: {response.status_code}")

# print(dados_restaurante['McDonald’s'])
"""
[{'item': 'Hamburger', 'price': 32.42, 'description': 'Uma explosão de sabores em cada mordida.'}, 
{'item': 'Cheeseburger', 'price': 38.81, 'description': 'Uma opção saudável e equilibrada.'}, 
{'item': 'Double Cheeseburger', 'price': 50.18, 'description': 'Leve e saboroso, perfeito a qualquer hora.'}, 
[...]
"""

print(f"Finalizado!!")

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")

# ...

print("-----------------------------------------------")