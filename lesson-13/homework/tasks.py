import numpy as np

# 1. Create a vector with values ranging from 10 to 49
vector = np.arange(10, 50)

# 2. Create a 3x3 matrix with values ranging from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)

# 3. Create a 3x3 identity matrix
identity_matrix = np.eye(3)

# 4. Create a 3x3x3 array with random values
random_3x3x3 = np.random.random((3, 3, 3))

# 5. Create a 10x10 array with random values and find the minimum and maximum values
random_10x10 = np.random.random((10, 10))
min_value = np.min(random_10x10)
max_value = np.max(random_10x10)

# 6. Create a random vector of size 30 and find the mean value
random_vector = np.random.random(30)
mean_value = np.mean(random_vector)

# 7. Normalize a 5x5 random matrix
random_5x5 = np.random.random((5, 5))
normalized_5x5 = (random_5x5 - np.min(random_5x5)) / (np.max(random_5x5) - np.min(random_5x5))

# 8. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
matrix_5x3 = np.random.random((5, 3))
matrix_3x2 = np.random.random((3, 2))
matrix_product_5x2 = np.dot(matrix_5x3, matrix_3x2)

# 9. Create two 3x3 matrices and compute their dot product
matrix_A = np.random.random((3, 3))
matrix_B = np.random.random((3, 3))
dot_product_3x3 = np.dot(matrix_A, matrix_B)

# 10. Given a 4x4 matrix, find its transpose
matrix_4x4 = np.random.random((4, 4))
transpose_4x4 = matrix_4x4.T

# 11. Create a 3x3 matrix and calculate its determinant
matrix_3x3_det = np.random.random((3, 3))
determinant = np.linalg.det(matrix_3x3_det)

# 12. Create two matrices (A) (3x4) and (B) (4x3), and compute the matrix product (A · B)
matrix_A_3x4 = np.random.random((3, 4))
matrix_B_4x3 = np.random.random((4, 3))
matrix_product_3x3 = np.dot(matrix_A_3x4, matrix_B_4x3)

# 13. Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product.
matrix_3x3 = np.random.random((3, 3))
vector_3x1 = np.random.random((3, 1))
matrix_vector_product = np.dot(matrix_3x3, vector_3x1)

# 14. Solve the linear system (Ax = b) where (A) is a 3x3 matrix, and (b) is a 3x1 column vector.
A_system = np.random.random((3, 3))
b_system = np.random.random((3, 1))
x_solution = np.linalg.solve(A_system, b_system)

# 15. Given a 5x5 matrix, find the row-wise and column-wise sums.
matrix_5x5 = np.random.random((5, 5))
row_sums = np.sum(matrix_5x5, axis=1)
column_sums = np.sum(matrix_5x5, axis=0)

# Output results
vector, matrix_3x3, identity_matrix, random_3x3x3, (min_value, max_value), mean_value, normalized_5x5, matrix_product_5x2, dot_product_3x3, transpose_4x4, determinant, matrix_product_3x3, matrix_vector_product, x_solution, (row_sums, column_sums)
