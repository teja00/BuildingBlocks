# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/Matrix/Algebra/05_eigen_value_matrix.ipynb.

# %% auto 0
__all__ = ['calculate_eigenvalues_2by2', 'calculate_eigenvalues']

# %% ../nbs/Matrix/Algebra/05_eigen_value_matrix.ipynb 3
from typing import Union
import numpy as np

# %% ../nbs/Matrix/Algebra/05_eigen_value_matrix.ipynb 4
def calculate_eigenvalues_2by2(matrix: list[list[Union[float,int]]] # matrix of size 2 x 2
						  ) -> list[float]: # eigenvalues of the matrix 1 x 2
    trace = matrix[0][0] + matrix[1][1]
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    sqrt_value = np.sqrt(trace ** 2 - 4 * det)
    eigen1 = (trace + sqrt_value) / 2
    eigen2 = (trace - sqrt_value) / 2
    return [eigen1, eigen2]

# %% ../nbs/Matrix/Algebra/05_eigen_value_matrix.ipynb 6
def calculate_eigenvalues(matrix: list[list[Union[float,int]]] # matrix of size n x n
						  ) -> list[float]: # result of size 1 x n
    np_matrix = np.array(matrix)
    if np_matrix.shape[0] != np_matrix.shape[1]:
        raise ValueError("Eigenvalues are only defined for square matrices.")
    eigenvalues, _ = np.linalg.eig(np_matrix)
    return eigenvalues.tolist()

