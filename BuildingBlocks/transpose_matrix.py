"""This is a python Function that computes the transpose of a matrix"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/Matrix/Matrix-Essentials/01_transpose_of_matrix.ipynb.

# %% auto 0
__all__ = ['transpose_matrix']

# %% ../nbs/Matrix/Matrix-Essentials/01_transpose_of_matrix.ipynb 2
from typing import List, Union

# %% ../nbs/Matrix/Matrix-Essentials/01_transpose_of_matrix.ipynb 3
def transpose_matrix(a: List[List[Union[int, float]]] # matrix a of size (n, m)
                     ) -> List[List[Union[int, float]]]: # matrix of size (m, n) 
    n, m = len(a[0]), len(a)  # n = number of columns, m = number of rows
    return [[a[i][j] for i in range(m)] for j in range(n)]
