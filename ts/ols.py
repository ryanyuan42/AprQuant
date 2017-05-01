import numpy as np


class OLS:
    def __init__(self):
        pass

    @staticmethod
    def fit(X, y):
        beta = np.linalg.inv(np.transpose(X) * X) * np.transpose(X) * y
        return beta


if __name__ == '__main__':
    X = np.transpose(np.matrix('1,2,3,4,5; 3,4,2,5,7'))
    y = X[:, 0] * 2 + X[:, 1] * 3
    reg = OLS()
    print(OLS.fit(X, y))
