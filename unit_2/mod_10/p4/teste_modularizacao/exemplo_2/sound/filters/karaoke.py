
# from pathlib import Path
# print('Running' if __name__ == '__main__' else 'Importing'
#       , Path(__file__).resolve())

# from . import equalizer
from .equalizer import equalizer_exec # Para funcionar é necessário o arquivo em branco __init__.py na mesma pasta

def karaoke_exec():
    # equalizer.equalizer_exec()
    equalizer_exec()

# karaoke_exec()
# 1ª Chamada de equalizer.py

