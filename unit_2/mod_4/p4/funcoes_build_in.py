print("-----------------------------------------------")
print('-- Funções Build-In no Pyphon --\n')
print('Replace: Altere o caractere \"X\" por ...')
str = "Márcio"
print(str)

t = str.replace('á', 'a')
print(f't: {t} | str: {str}')

print('\nStartswith: Essa string inicia com ...?')
print(str.startswith('M')) # A string inicia com M? true
print("Teste".startswith('t')) # A string inicia com t? false
print("Teste".startswith('T')) # A string inicia com T? true

print('\nEndswith: Essa string finaliza com ...?')
print(str.endswith('o')) # A string inicia com o? true
print("Amor".endswith('R')) # A string inicia com t? false
print("Amor".endswith('r')) # A string inicia com e? true

print('\nJoin: Retorna a string onde os elementos da sequência foram unidor por um separador \"str\"')
list1 = ['1', '2', '3', '4']
print(list1)
print("-".join(list1))

print("")
t = ['g','e','e','k', 's']
print(t)
print("".join(t))

print('\nCount: Conta quantos caracteres X existes...')
s = 'abcaa'
print(s)
print(s.count('a'))

print('\nFind: Returna 0 se encontrado e -1 se não...')
s = 'abcabcabcc'
print('abc' in s) #True
print(s.find('abc'))
print(s.find('xyz'))

print('\nAppend: Adiccionar elementos')
texto = 'Python é uma linguagem de programação'
print(texto)

# texto.append(" muito popular.") #ERROR
texto = texto.__add__(' muito popular.')
print(texto)

print("-----------------------------------------------")

frase = "Eu gosto de programar em "
frase = frase + "Python"
print(frase)
# Eu gosto de programar em Python

palavras = ["Eu", "gosto", "de", "programar", "em", "Python"]
frase = "-".join(palavras)

print(frase)
# Eu-gosto-de-programar-em-Python

print("-----------------------------------------------")

numeros = [1, 2, 3, 4, 5]
print(numeros)

numeros.insert(1, 10) # insira o elemento "10" no índex 1...
print(numeros)

print("-----------------------------------------------")

print('LISTA:')
cep = ['6', '5', '1', '1', '0', '0', '0', '0']
print(cep)

cep.insert(5, '-')
print(cep)
print(type(cep))

print("")

print('STRING: ERROR')
cep = "65110000"
print(cep)

# cep.insert(5, '-') #ERROR
# print(cep)
print(type(cep))

print("-----------------------------------------------")

cep_part1 = cep[:5]
cep_part2 = cep[5:]
print(cep_part1)
print(cep_part2)

print(cep_part1 + '-' + cep_part2)

cep = cep[:5] + '-' + cep[5:]
print(cep)

print("-----------------------------------------------")
print('Funções Build In no Pyphon'.join('--'))
print("-----------------------------------------------")