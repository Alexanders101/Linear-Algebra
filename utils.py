from numpy import *
import sympy
from itertools import permutations as _iter_perm
from sympy.matrices import Matrix as sym_mat
from sympy.interactive.printing import init_printing

init_printing()
symbol = sympy.symbols

def mat_print(m, name=None):
    if name is None:
        return sym_mat(m)
    else:
        dim_x = m.shape[0]
        dim_y = m.shape[1]
        return sympy.Eq(sympy.MatrixSymbol(name, dim_x, dim_y), sym_mat(m))


def permutations(l, generate=False):
    if generate:
        return _iter_perm(l)
    return array(list(_iter_perm(l)))


def is_even(n):
    return not (n & 0x1)
