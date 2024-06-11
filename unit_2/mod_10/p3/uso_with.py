"""Compatibilidade
A declaração de with foi adicionado na versão 2.5 da linguagem, porém, é necessário habilitá-la através do código:
"""
# from __future__ import with_statement

"""A partir da versão 2.6, a declaração já está habilitada por padrão.
   Versões anteriores à 2.5 não possuem suporte a esta declaração.

   Gerenciadores de Contexto
   É possível, de forma prática, definir novos gerenciadores de contextos
   a partir da biblioteca contextlib, utilizando o decorador contextmanager.
"""

from contextlib import contextmanager

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("Stack Overflow")

print("-----------------------------------------------")

from contextlib import contextmanager as teste

@teste
def eu(name):
    print(f'Olá, meu nome é {name} ', end="")
    yield

with eu("Lucas"):
    print("e eu amo tecnologia")

print("-----------------------------------------------")

class Foo (object):

    def __enter__ (self):
        print("Enter")
        return 1, 2, 3

    def __exit__ (self, exit, value, exc):
        print("Exit")

with Foo() as (a, b, c):
    print(a, b, c)


print("-----------------------------------------------")

class Foo2 (object):

    def __enter__ (self):
        print("Enter")
        return 1

    def __exit__ (self, exit, value, exc):
        print("Exit")

with Foo2() as foo2:
    print(foo2)