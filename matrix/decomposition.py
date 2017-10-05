from .basic import dot, transpose


def pivot_matrix(A):
    """
    Find the pivot matrix of A
    :param A: n * n matrix
    :return:
    """
    n = len(A)
    res = [[float(i == j) for i in range(n)] for j in range(n)]
    for j in range(n):
        max_value = float('-inf')
        max_row = None
        for i in range(j, n):
            if A[i][j] > max_value:
                max_value = A[i][j]
                max_row = i

        if j != max_row:
            res[max_row], res[j] = res[j], res[max_row]
    return res


def lu_decom(A):
    """
    This funcion implemenets LU decomposition
    A = L * U, where L is lower-triangle matrix, U is upper triangle matrix
    :param A: n * n matrix
    :return: L, U
    """

    n = len(A)
    L = [[0 for _ in range(n)] for _ in range(n)]
    U = [[0 for _ in range(n)] for _ in range(n)]
    P = pivot_matrix(A)
    PA = dot(P, A)
    for j in range(n):
        L[j][j] = 1
        for i in range(j+1):
            to_reduce = 0
            for k in range(i):
                to_reduce += U[k][j] * L[i][k]
            U[i][j] = PA[i][j] - to_reduce
        for i in range(j, n):
            to_reduce = 0
            for k in range(i):
                to_reduce += U[k][j] * L[i][k]
            L[i][j] = (PA[i][j] - to_reduce) / U[j][j]
    inv_P = transpose(P)
    return inv_P, L, U


def inv(A):
    """
    This function gives the inverse of a matrix
    We use LU decomposition to solve this
    :param A: n
    :return:
    """
    n = len(A)
    P, L, U = lu_decom(A)
    Z = [[0 for _ in range(n)] for _ in range(n)]
    X = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        Z[j][j] = 1 / L[j][j]
        for i in range(j+1, n):
            to_sum = 0
            for k in range(i):
                to_sum += L[i][k] * Z[k][j]
            Z[i][j] = -to_sum / L[i][i]
    for i in range(n-1, -1, -1):
        for j in range(n):
            to_sum = 0
            for k in range(i+1, n):
                to_sum += U[i][k] * X[k][j]
            X[i][j] = (Z[i][j] - to_sum) / U[i][i]
    inv_P = transpose(P)
    return dot(X, inv_P)
