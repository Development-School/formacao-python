# -------------------------------------------------------------------- #
# 09. Para Saber Mais - Outros recursos com a lista
# -------------------------------------------------------------------- #
import errno

valores = [ 0, 0, 0, 1, 2, 3, 4]
print(valores.count(0))
print(valores.count(1))

print("-------------------------------------------------------")

letras_acertadas = ['_','_','_','_','_','_']
letras_faltando = str(letras_acertadas.count('_'))
print( 'Ainda faltam acertar {} letras'.format(letras_faltando))

print("-------------------------------------------------------")

frutas = ['Banana', 'Morango', 'Maçã', 'Uva', 'Maçã', 'Uva']
print(frutas.index('Uva'))

print("-------------------------------------------------------")

frutas = ['Banana', 'Morango', 'Maçã', 'Uva']
# print(frutas.index('Melancia')) #ERRO

print("-------------------------------------------------------")

frutas = ['Banana', 'Morango', 'Maçã', 'Uva']

fruta_buscada = 'Melancia'
if fruta_buscada in frutas:
    print(frutas.index(fruta_buscada))
else:
    print('Desculpe, a {} não está na lista frutas'.format(fruta_buscada))