#-------------------------------------------------------------
#                     Python Examples
#-------------------------------------------------------------
#                     Python Modules
#-------------------------------------------------------------

#-------------------------------------------------------------
""" Pré-requisitos: ▼
1. Criar o arquivo "mymodule.py";
2. Incluir a seguinte rotina no arquivo criado:

    def greeting(name):
      print("Hello, " + name)

    person1 = {
      "name": "John",
      "age": 36,
      "country": "Norway"
    }

Pronto, agora iremos importar com o comando:

    import mymodule
"""
print("-----------------------------------------------")

# Use a module
import mymodule
mymodule.greeting("Jonathan")
# Hello, Jonathan

print("-----------------------------------------------")

# Variables in module
import mymodule
a = mymodule.person1["age"]

print(a)
# 36

print("-----------------------------------------------")

# Re-naming a module
import mymodule as mx
a = mx.person1["age"]
print(a)
# 36

print("-----------------------------------------------")

# Built-in modules
import platform
x = platform.system()
print(x)
# Windows

print("-----------------------------------------------")

# Using the dir() function
import platform
x = dir(platform)

print(x)
# ['DEV_NULL', '_UNIXCONFDIR', 'WIN32_CLIENT_RELEASES',
# 'WIN32_SERVER_RELEASES', '__builtins__', '__cached__',
# '__copyright__', '__doc__', '__file__', '__loader__',
# '__name__', '__package __', '__spec__', '__version__',
# '_default_architecture', '_dist_try_harder', '_follow_symlinks',
# '_ironpython26_sys_version_parser', '_ironpython_sys_version_parser',
# '_java_getprop', '_libc_search', '_linux_distribution',
# '_lsb_release_version', '_mac_ver_xml', '_node', '_norm_version',
# '_perse_release_file', '_platform', '_platform_cache',
# '_pypy_sys_version_parser', '_release_filename', '_release_version',
# '_supported_dists', '_sys_version', '_sys_version_cache',
# '_sys_version_parser', '_syscmd_file', '_syscmd_uname',
# '_syscmd_ver', '_uname_cache', '_ver_output', 'architecture',
# 'collections', 'dist', 'java_ver', 'libc_ver', 'linux_distribution',
# 'mac_ver', 'machine', 'node', 'os', 'platform', 'popen', 'processor',
# 'python_branch', 'python_build', 'python_compiler',
# 'python_implementation', 'python_revision', 'python_version',
# 'python_version_tuple', 're', 'release', 'subprocess',
# 'sys', 'system', 'system_aliases', 'uname', 'uname_result',
# 'version', 'warnings', 'win32_ver']
print("-----------------------------------------------")

# Import from module
from mymodule import person1
print(person1["age"])
# 36

print("-----------------------------------------------")