
from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibe uma mensagem incrível do mundo da programação!
    '''
    return {'Hello':'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)): # Import Query
    '''
    Endpoint para ver os cardápios dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url) # import requests

    if response.status_code == 200:
        dados_json = response.json()

        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante = []
        # dados_restaurante = {}
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })

        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
    else:
        return {'Erro':f'{response.status_code} - {response.text}'}

"""
Testes Navegador: ▼
127.0.0.1:8000/api/hello
127.0.0.1:8000/api/restaurantes

127.0.0.1:8000/api/restaurantes/?restaurante=McDonald’s
127.0.0.1:8000/api/restaurantes/?restaurante=KFC
127.0.0.1:8000/docs
"""