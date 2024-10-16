def transpose(matrix):
    if not matrix or not matrix[0]:
        return []

    max_kolumn = max(len(row) for row in matrix) #största kolumnvärdet
    max_rad = 

    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def powers(lst, start, end):
    return [[num**i for i in range(start, end + 1)] for num in lst]

def matmul(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Incompatible matrix dimensions for multiplication.")
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def invert(A):
    if len(A) != 2 or len(A[0]) != 2:
        raise ValueError("Invert function only supports 2x2 matrices.")
    a, b = A[0][0], A[0][1]
    c, d = A[1][0], A[1][1]
    det = a * d - b * c
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")
    return [[d / det, -b / det], [-c / det, a / det]]

def loadtxt(filename):
    with open(filename, 'r') as file:
        return [[float(num) for num in line.split()] for line in file]
