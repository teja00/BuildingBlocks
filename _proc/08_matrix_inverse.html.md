---
description: Writing a Python function that calculates the inverse of a 2x2 matrix.
  Return 'None' if the matrix is not invertible.
output-file: matrix_inverse.html
title: Matrix Inverse

---



<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

The inverse of a matrix \( A \) is another matrix, often denoted \( A^{-1} \), such that:

$$
AA^{-1} = A^{-1}A = I
$$

where \( I \) is the identity matrix. For a 2×2 matrix:

$$
A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}
$$

The inverse is given by:

$$
A^{-1} = \frac{1}{\det(A)} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
$$

provided that the determinant \( \det(A) = ad - bc \) is non-zero.

If \( \det(A) = 0 \), the matrix does not have an inverse.

---

### Importance

Calculating the inverse of a matrix is essential in various applications, such as solving systems of linear equations, where the inverse is used to find solutions efficiently.

---

[source](https://github.com/teja00/BuildingBlocks/blob/main/BuildingBlocks/matrix_transformation.py#L14){target="_blank" style="float:right; font-size:smaller"}

### inverse_2x2

>      inverse_2x2 (matrix:list)

|    | **Type** | **Details** |
| -- | -------- | ----------- |
| matrix | list | matrix to be inverted size (2, 2) |
| **Returns** | **list** | **inverse of the matrix** |


::: {#57c77909 .cell}
``` {.python .cell-code code-fold="show" code-summary="Exported source"}
def inverse_2x2(matrix: list[list[float]] # matrix to be inverted size (2, 2)
				) -> list[list[float]]: # inverse of the matrix
	matrix = np.array(matrix)
	a, b, c, d  = matrix.flatten()
	det = a*d - b*c
	if det == 0:
		return None
	adj_matrix = np.array([[d, -b], [-c, a]])
	inverse = matrix_scalar_multiply_numpy(1/ det, adj_matrix)
	return inverse
```
:::


