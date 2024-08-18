#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                      Python PIP
#-------------------------------------------------------------

print("-----------------------------------------------")

# Using a package

# import camelcase # Error (Necessário instalar o camelcase)
r"""
◘ Instalando camelcase ◘

Pelo cmd rode o seguinte comando ▼
    $ python.exe -m pip install --upgrade pip
    $ pip install camelcase
   
Desistalar ▼
    $ pip uninstall camelcase

Listar todos os pacotes ▼
    $ pip list
"""
r"""
Retorno CMDer ▼
    C:\Apps\.Developer\CMDer Mini\content
    λ pip --version
    pip 24.1 from C:\Users\Builder\AppData\Local\Programs\Python\Python312\Lib\site-packages\pip (python 3.12)
    
    C:\Apps\.Developer\CMDer Mini\content
    λ pip install camelcase
    Collecting camelcase
      Downloading camelcase-0.2.tar.gz (1.3 kB)
      Installing build dependencies ... done
      Getting requirements to build wheel ... done
      Preparing metadata (pyproject.toml) ... done
    Building wheels for collected packages: camelcase
      Building wheel for camelcase (pyproject.toml) ... done
      Created wheel for camelcase: filename=camelcase-0.2-py3-none-any.whl size=1778 sha256=14e07a3cee15fe62d7eeca3fe8a4a6bcccec485c3773d11eaeebc485756c32bb
      Stored in directory: c:\users\builder\appdata\local\pip\cache\wheels\a7\40\a3\900133dd6de3e10c219659fec4118138db05d778e519c0b2bc
    Successfully built camelcase
    Installing collected packages: camelcase
    Successfully installed camelcase-0.2
    
    [notice] A new release of pip is available: 24.1 -> 24.2
    [notice] To update, run: python.exe -m pip install --upgrade pip
    
    C:\Apps\.Developer\CMDer Mini\content
    λ python.exe -m pip install --upgrade pip
    Requirement already satisfied: pip in c:\users\builder\appdata\local\programs\python\python312\lib\site-packages (24.1)
    Collecting pip
      Downloading pip-24.2-py3-none-any.whl.metadata (3.6 kB)
    Downloading pip-24.2-py3-none-any.whl (1.8 MB)
       ---------------------------------------- 1.8/1.8 MB 3.5 MB/s eta 0:00:00
    Installing collected packages: pip
      Attempting uninstall: pip
        Found existing installation: pip 24.1
        Uninstalling pip-24.1:
          Successfully uninstalled pip-24.1
    Successfully installed pip-24.2
    
    C:\Apps\.Developer\CMDer Mini\content
    λ pip install camelcase
    Requirement already satisfied: camelcase in c:\users\builder\appdata\local\programs\python\python312\lib\site-packages (0.2)
    
    C:\Apps\.Developer\CMDer Mini\content
    λ   
"""

import camelcase

c = camelcase.CamelCase()
txt = "lorem ipsum dolor sit amet"

print(c.hump(txt))

#This method capitalizes the first letter of each word.
# Lorem Ipsum Dolor Sit Amet

print("-----------------------------------------------")