
print("-----------------------------------------------")

import re

padrao_molde = "(xx)aaaa-wwww"
padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "eu gosto do numero 2126451234 e gosto também do 2136431234"

resposta = re.search(padrao,texto)
print(resposta.group()) #2126451234

print("-----------------------------------------------")

texto = "2136431234"
resposta = re.findall(padrao, texto)
print(resposta) # ['2126451234', '2136431234']

print("-----------------------------------------------")