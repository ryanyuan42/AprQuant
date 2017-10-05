def dot(A, B):
    """
    This function used to matrix multiply
    :param A: n * m
    :param B: m * p
    :return: a matrix n * p
    """
    n = len(A)
    m = len(A[0])
    p = len(B[0])
    # final matrix C
    C = [[0 for _ in range(p)] for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C


def transpose(A):
    """
    This function gives transpose of a matrix
    :param A: n * m
    :return: m * n
    """
    n = len(A)
    m = len(A[0])
    res = [[None for i in range(n)] for j in range(m)]

    for i in range(n):
        for j in range(m):
            res[j][i] = A[i][j]
    return res




