
from collections.abc import MutableSequence

from numbers import Complex

class Numero(Complex):
    def __getitem__(self, item):
        super().__getitem__()

    #implementation for abstract methods '__abs__', '__add__', '__complex__', '__eq__', '__mul__', '__neg__', '__pos__', '__pow__', '__radd__', '__rmul__', '__rpow__', '__rtruediv__', '__truediv__', 'conjugate', 'imag', 'real'

class Playlist(MutableSequence):
    pass

    #implementation for abstract methods _delitem__', '__getitem__', '__len__', '__setitem__', 'insert'

# filmes = Playlist()

numero = Numero()