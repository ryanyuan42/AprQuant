# Aimed to solve Ax = b
def solve(A, b):
    """
    :param A: A is a n x n matrix
    :param b: b is a n x 1 vector.
    :return: return the x vector s.t. Ax = b
    """
    n = len(A)
    for i in range(n):
        # Find the Max value in current column
        maxRow = i
        maxValue = A[i][i]
        for j in range(i+1, n):
            if A[j][i] > maxValue:
                maxValue = A[j][i]
                maxRow = j

        # Swap the current row with the Max value row
        tmp = A[i]
        A[i] = A[maxRow]
        A[maxRow] = tmp

        # make the value in current column that is below the current row is 0
        for k in range(i+1, n):
            para = A[k][i] / maxValue
            for l in range(n):
                A[k][l] -= para * A[i][l]
    x = [None for _ in range(n)]
    for i in range(n-1, -1, -1):
        to_reduce = 0
        for j in range(i+1, n):
            to_reduce += A[i][j] * x[j]
        x[i] = (b[i] - to_reduce) / A[i][i]

    return x

