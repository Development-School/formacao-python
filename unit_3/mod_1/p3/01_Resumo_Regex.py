
import re

print("-----------------------------------------------")

padrao = "[0-9][a-z][0-9]" # Ex.: 1a2
texto = "123 1a2 1cc aa1"
resposta = re.search(padrao, texto)

print(resposta.group()) # 1a2

print("-----------------------------------------------")

padrao = "[0-9][a-z]{2}[0-9]" # Ex.: 1aa2
texto = "123 1a2 1cc aa1"
resposta = re.search(padrao, texto)

# Não encontrado
# print(resposta.group()) # AttributeError: 'NoneType' object has no attribute 'group'

#-------------------------------------------------------------

padrao = "[0-9][a-z]{2}[0-9]" # Ex.: 1aa2
texto = "123 1a2 1aa2 1cc aa1"
resposta = re.search(padrao, texto)

print(resposta.group()) # 1aa2

print("-----------------------------------------------")

# padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}" # SyntaxWarning: invalid escape sequence '\w' (Utilizar r"\")
padrao = r"\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "aaabbbcc rodrigo123@gmail.com.br ccbbbaaa"
resposta = re.search(padrao, texto)

print(resposta.group())
# rodrigo123@gmail.com.br

print("-----------------------------------------------")

# [.br]* = [isso]pode ou não vir
padrao = r"\w{5,50}@[a-z]{3,10}.com[.br]*"
texto = "aaabbbcc rodrigo123@gmail.com.br rodrigo123@gmail.com ccbbbaaa"
resposta = re.findall(padrao, texto)

print(resposta)
# ['rodrigo123@gmail.com.br', 'rodrigo123@gmail.com']

print("-----------------------------------------------")

# Agrupandp ()
# padrao = r"(\w{5,50})(@)([a-z]{3,10})(.com)(.br)*"
# ou
padrao = r"(\w{5,50})(@)([a-z]{3,10})(.com)(.br)?"
texto = 'aaa rodrigo123@gmail.com.br rodrigo123@gmail.com ccc'
busca = re.findall(padrao, texto)
print(busca)
# [('rodrigo123', '@', 'gmail', '.com', '.br'), ('rodrigo123', '@', 'gmail', '.com', '')]

print("-----------------------------------------------")

padrao = r"(\w{5,50})(@)([a-z]{3,10})(.com)(.br)"
texto = 'aaa rodrigo123@gmail.com.br rodrigo123@gmail.com ccc'
busca = re.findall(padrao, texto)
print(busca)
# [('rodrigo123', '@', 'gmail', '.com', '.br')]

print("-----------------------------------------------")

padrao2 = r'([+]?[0-9]{2})([0-9]{2})([0-9]{4,5})(-?)([0-9]{4})'
telefone = '5521998765543 fone é +552198765543 teste +552199876-5543'
busca = re.findall(padrao2, telefone)
print(busca)
# [('55', '21', '99876', '', '5543'), ('+55', '21', '9876', '', '5543'), ('+55', '21', '99876', '-', '5543')]

print("-----------------------------------------------")

telefone = 'teste +552199876-5543 teste2'
busca = re.search(padrao2, telefone)
print(busca.group())
# +552199876-5543

print("-----------------------------------------------")

print(busca.group(1))
print(busca.group(2))
print(busca.group(3))
print(busca.group(4))
print(busca.group(5))
# +55
# 21
# 99876
# -
# 5543

print(busca.group(1, 2, 3, 4, 5))
# ('+55', '21', '99876', '-', '5543')

print("-----------------------------------------------")

telefone = 'teste +552198765543 teste2'
busca = re.search(padrao2, telefone)
print(busca.group(1, 2, 3, 4, 5))
# ('+55', '21', '9876', '', '5543')

print("-----------------------------------------------")

telefone = 'teste 5521998765543 teste2'
busca = re.search(padrao2, telefone)
print(busca.group(1, 2, 3, 4, 5))
# ('55', '21', '99876', '', '5543')

print("-----------------------------------------------")

print('' == busca.group(1, 2, 3, 4, 5)) # False
print('' == busca.group(4)) # True
print('' == busca.group(1)) # False

print("-----------------------------------------------")

print('lucas' in busca.group()) # False
print('55' in busca.group()) # True
print('+55' in busca.group()) # False
print('' in busca.group()) # True
print(' ' in busca.group()) # False

print("-----------------------------------------------")

padrao2 = r'([+]?[0-9]{2})?([0-9]{2})([0-9]{4,5})(-?)([0-9]{4})'
telefone = 'teste 2199876-5543 teste2'
busca = re.findall(padrao2, telefone)
print(busca)
# [('', '21', '99876', '-', '5543')]

busca = re.search(padrao2, telefone)
print(busca.group(1))
# None

print("-----------------------------------------------")