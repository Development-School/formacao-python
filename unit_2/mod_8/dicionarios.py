print("-----------------------------------------------")

telefones = ['1234-5678', '9999-9999', '8765-4321', '8877-7788']
print(telefones)
# ['1234-5678', '9999-9999', '8765-4321', '8877-7788']

print("-----------------------------------------------")

contato = ('Yan', '1234-5678')
print(contato)
# ('Yan', '1234-5678')

print("-----------------------------------------------")

contatos_lista = [('Yan', '1234-5678'), ('Pedro', '9999-9999'),
                  ('Ana', '8765-4321'), ('Marina', '8877-7788')]

print(contatos_lista[3][1])
# 8877-7788

print("-----------------------------------------------")

for nome, telefone in contatos_lista:
    print(f'Nome => {nome} | Contato: {telefone}')

# Nome => Yan | Contato: 1234-5678
# Nome => Pedro | Contato: 9999-9999
# Nome => Ana | Contato: 8765-4321
# Nome => Marina | Contato: 8877-7788

print("-----------------------------------------------")

contatos = {'Yan': '1234-5678'}
print(type(contatos))
# <class 'dict'>

print("-----------------------------------------------")

contatos = dict(contatos_lista)
print(contatos)
# {'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321', 'Marina': '8877-7788'}

print("-----------------------------------------------")

print(contatos['Ana'])
# 8765-4321

# print(contatos['João']) # Error pois joão não existe
print(contatos.get('João', 'Não existe'))
# Não existe

print("-----------------------------------------------")

print(contatos.get('Yan', 'Contato não encontrado'))
print(contatos.get('João', 'Contato não encontrado'))
# 1234-5678
# Contato não encontrado

print("-----------------------------------------------")

print('Yan' in contatos)
# True

print("-----------------------------------------------")

print('9999-9999' in contatos)
# False

print("-----------------------------------------------")

print('9999-9999' in contatos.values())
# True

print("-----------------------------------------------")

print(contatos)
# {'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321', 'Marina': '8877-7788'}

contatos['João'] = '8887-7778'
print(contatos)
# {'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321', 'Marina': '8877-7788', 'João': '8887-7778'}

print("-----------------------------------------------")

print(contatos)
# {'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321', 'Marina': '8877-7788', 'João': '8887-7778'}

del contatos['Marina']
print(contatos)
# {'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321', 'João': '8887-7778'}

print("-----------------------------------------------")

print(contatos)
# {'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321', 'João': '8887-7778'}
# del contatos['Catarina'] #Error
print(contatos.pop('Pedro', 'Contato não encontrado'))
# 9999-9999
print(contatos)
# {'Yan': '1234-5678', 'Ana': '8765-4321', 'João': '8887-7778'}
print()
print(contatos.pop('Catarina', 'Contato não encontrado'))
# Contato não encontrado
print()
print(contatos)
# {'Yan': '1234-5678', 'Ana': '8765-4321', 'João': '8887-7778'}

print("-----------------------------------------------")

meus_contatos = {'Yan': '1234-5678', 'Pedro': '9999-9999',
                    'Ana': '8765-4321', 'João': '8887-7778'}

contatos_do_pedro = {'Yan': '1234-5678', 'Fernando': '4345-5434',
                        'Luiza': '4567-7654'}

for nome in contatos_do_pedro:
    meus_contatos[nome] = contatos_do_pedro[nome]

print(meus_contatos)
# {'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321', 'João': '8887-7778', 'Fernando': '4345-5434', 'Luiza': '4567-7654'}

print("-----------------------------------------------")

contatos_do_pedro.update({'Lucas' : '8718-5950'})
print(contatos_do_pedro)
# {'Yan': '1234-5678', 'Fernando': '4345-5434', 'Luiza': '4567-7654', 'Lucas': '8718-5950'}

print("-----------------------------------------------")

print(meus_contatos)
# {'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321', 'João': '8887-7778', 'Fernando': '4345-5434', 'Luiza': '4567-7654'}

meus_contatos.update(contatos_do_pedro)
print(meus_contatos)
# {'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321', 'João': '8887-7778', 'Fernando': '4345-5434', 'Luiza': '4567-7654', 'Lucas': '8718-5950'}

print("-----------------------------------------------")

meus_contatos_novo = {nome: '9' + meus_contatos[nome] for nome in meus_contatos}
print(meus_contatos_novo)
# {'Yan': '91234-5678', 'Pedro': '99999-9999', 'Ana': '98765-4321', 'João': '98887-7778', 'Fernando': '94345-5434', 'Luiza': '94567-7654', 'Lucas': '98718-5950'}

print("-----------------------------------------------")

valores = meus_contatos_novo.values()
print(valores)
# ['91234-5678', '99999-9999', '98765-4321', '98887-7778', '94345-5434', '94567-7654']

print("-----------------------------------------------")

valores = meus_contatos_novo.values()
print(valores)

print("-----------------------------------------------")

meus_contatos_novo['Yan'] = '91122-3344'
print(valores)

print("-----------------------------------------------")

print(valores.__sizeof__())
# Com a lista no Python 2, o resultado:
# 112

# Agora, com a view no Python 3:
# 24

print("-----------------------------------------------")