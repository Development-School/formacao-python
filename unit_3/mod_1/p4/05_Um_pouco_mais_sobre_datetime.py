
from datetime import datetime

agora = datetime.now()
agora_formatado = agora.strftime(r"%d/%m/%Y %H:%M:%S")

print("-----------------------------------------------")
print(agora_formatado)
print("-----------------------------------------------")