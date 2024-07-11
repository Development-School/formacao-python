"""
Alura: ▼

from flask import Flask

app = Flask(__name__)

@app.route('/api')
def ola_mundo():
    return 'Olá Mundo!'

if __name__ == '__main__':
    app.run()
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get('/api/developer')
def developer():
    return {'Developer':'Lucas Caminha'}

if __name__ == '__main__':
    app.run()

"""
Terminal: ▼
uvicorn main:app --reload
"""

"""
Testes Navegador: ▼
127.0.0.1:8000/api/hello
"""