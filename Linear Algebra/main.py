"""A module containing basic vector operations."""


apple_prices_store_1 = [100,
                        90,
                        93,
                        87]


apple_prices_store_2 = [95,
                        79,
                        69,
                        88]

def add(v, w):
    """adds corresponding vector elements"""
    assert len(v) == len(w), "Vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1, 2, 3], [1, 3, 4]) == [2, 5, 7]

def subtract(v, w):
    """subtracts corresponding vector elements"""
    assert len(v) == len(w), "Vectors must be the same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([1, 2, 3], [1, 3, 4]) == [0, -1, -1]

def vector_sum(vectors):
    """Sums all corresponding elements"""
    assert vectors, "no vectors provided!"

    # Check the vectors are all the same size
    number_of_elements = len(vectors[0])
    assert all(len(v) == number_of_elements for v in vectors), "all the elements must be of same size"
    return [sum(vector[i] for vector in vectors) for i in range(number_of_elements)]

assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]

def scalar_multiply(c, v):
    "Scalar Multiplication"
    return [c * v_i for v_i in v]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]

def vector_mean(vectors):
    """Mean of the vectors"""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]

def dot(v, w):
    """Dot Product of v and w"""
    assert len(v) == len(w), "Length of v and w must be same"
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32


def sum_of_squares(v):
    """Calculates sum of the squares"""
    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14

import math

def magnitude(v):
    """Returns magintude (length) of the vector."""
    return math.sqrt(sum_of_squares(v))

assert magnitude([3, 4]) == 5

def euclidean_distance(v, w):
    """Returns euclidean distance of two vectors."""
    return int(magnitude(subtract(v, w)))

assert euclidean_distance([1, 2, 3], [4, 5, 6]) == 5

# Matrix operations
def shape(A):
    "Returns shape of the matrix (rxc)"
    num_of_rows = len(A)
    num_of_cols = len(A[0]) if A else 0
    return num_of_rows, num_of_cols

assert shape([[1, 2],[4, 5]]) == (2, 2)

def get_row(A, i):
    """Returns ith row"""
    return A[i]

def get_col(A, j):
    """Returns jth row"""
    return [A_i[j] for A_i in A]

def make_matrix(num_rows, num_cols, entry_fn):
    """Creates a matrix of rows x columns"""
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]

def identity_matrix(n):
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)

assert identity_matrix(3) == [[1, 0, 0],
                              [0, 1, 0],
                              [0, 0, 1]]

