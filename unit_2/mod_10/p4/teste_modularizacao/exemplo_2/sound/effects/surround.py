# from reverse import reverse_exec2 # OK!
# import reverse # OK!
# from ..effects import reverse # Erro
# from ..effects.reverse import reverse_exec2 # Erro
# from . reverse import reverse_exec2 # Erro
# from . import reverse # Erro *
# from .. import effects # Erro
# from .. effects.reverse import reverse_exec2 # Erro

# StackOverflow ▼
# import os, sys # OK!
# sys.path.append(os.path.abspath( os.path.basename(__file__) + "../.."))  # OK!
# import reverse # OK!
# Ref.: (https://stackoverflow.com/questions/68351533/the-exact-code-from-python-documentation-doesnt-work-importing-modules)

# from . reverse import reverse_exec2 # Erro interno, OK externo
from . import reverse # Erro # Para funcionar é necessário o arquivo em branco __init__.py na mesma pasta

def surround_exec():
    # reverse_exec2() # OK!
    # reverse.reverse_exec2() # OK!
    # reverse.reverse_exec2() # Erro
    # reverse_exec2() # Erro
    # reverse_exec2() # Erro
    # reverse.reverse_exec2() # Erro
    # effects.reverse.reverse_exec2() # Erro
    # reverse_exec2() # Erro
    # reverse.reverse_exec2() # OK!
    # reverse_exec2() # Erro interno, OK externo
    reverse.reverse_exec2() # Erro interno, OK externo
    # pass

# surround_exec()
# 2ª Chamada de reverse.py