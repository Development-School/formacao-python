"""Alura ▼

from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def ola_mundo():
    return {"message": "Olá Mundo!"}
"""

from fastapi import FastAPI

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibe uma mensagem incrível do mundo da programação!
    '''
    return {'Hello':'World'}

"""
Terminal: ▼
uvicorn main:app --reload
"""

"""
Testes Navegador: ▼
127.0.0.1:8000/api/hello
"""