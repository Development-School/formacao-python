
m = {'BB' : "Banco do Brasil", 'Caixa' : 'Caixa Economica Federal'}

print(m.get('BB')) #ou print(m['BB'])
# Banco do Brasil

print("-----------------------------------------------")

print(m.keys())
# dict_keys(['BB', 'Caixa'])

print("-----------------------------------------------")

for i in m.keys(): print(i)
# BB
# Caixa

print("-----------------------------------------------")

print(m.values())
# dict_values(['Banco do Brasil', 'Caixa Economica Federal'])

print("-----------------------------------------------")

print(m.items())
# dict_items([('BB', 'Banco do Brasil'), ('Caixa', 'Caixa Economica Federal')])

print("-----------------------------------------------")

print(m.get('Banco do Brasil'))