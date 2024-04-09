# -------------------------------------------------------------------- #
# 07. Decifrando dicionários com ternários
# -------------------------------------------------------------------- #


credenciais_clientes = {
    'alice123': {'username': 'alice123', 'password': 'alic3P@ssw0rd', 'status': 'active'},
    'bob456': {'username': 'bob456', 'password': 'b0bP@ssword!', 'status': 'inactive'},
    'charlie789': {'username': 'charlie789', 'password': 'Ch@rlieP@ss9', 'status': 'active'}
}

alerta = 'Enviar alerta!' if credenciais_clientes.get('bob456', {}).get('status') == 'active' else 'Sem alerta'
print(alerta)

alerta = 'Sem alerta' if credenciais_clientes['bob456']['status'] else 'Enviar alerta!'
print(alerta)

alerta = 'Enviar alerta!' if 'inactive' in credenciais_clientes['bob456'].values() else 'Sem alerta'
print(alerta)

alerta = 'Enviar alerta!' if credenciais_clientes['bob456']['status'] == 'inactive' else 'Sem alerta'
print(alerta)

alerta = 'Enviar alerta!' if credenciais_clientes['bob456'] else 'Sem alerta'
print(alerta)

