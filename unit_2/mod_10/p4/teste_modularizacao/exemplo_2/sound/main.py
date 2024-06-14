
# Exemplo 1: Mesmo path ▼
import tmp
print(tmp.__name__)
tmp.exec()
# tmp
# Chamada de tmp.py

print("-----------------------------------------------")

# Exemplo 2: "1º andar" para dentro ▼
# Users of the package can import individual modules from the package, for example:
# import sound.effects.echo # Erro: Ref.:(https://docs.python.org/3/tutorial/modules.html#packages)
# from .effects import echo #Erro
from effects import echo
# print(echo.__name__)
echo.echo_exec()
# 1ª Chamada de echo.py

print("-----------------------------------------------")

# Exemplo 3: "1º andar" para dentro (Importando todas as funções) ▼
from effects.reverse import *
reverse_exec()
reverse_exec2()

print("-----------------------------------------------")

# Exemplo 4: Chamando de um arquivo para outro no 1º andar ▼
from effects import surround
print(surround.__name__)
surround.surround_exec()

print("-----------------------------------------------")

# Exemplo 5: Chamando de um arquivo para outro no 1º  andar ▼
from filters import equalizer
print(equalizer.__name__)
equalizer.equalizer_exec()
equalizer.equalizer_exec2()

print("-----------------------------------------------")

from filters import karaoke
print(karaoke.__name__)
karaoke.karaoke_exec()

print("-----------------------------------------------")

from formats import aiffread
print(aiffread.__name__)
aiffread.aiffread_exec_effects_echo()
aiffread.aiffread_exec_filters_karaoke()

print("-----------------------------------------------")