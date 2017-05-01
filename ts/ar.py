import numpy as np
import scipy.optimize as spo
import statsmodels.api as sm
from . import ols
import random
__method__ = ['ols', 'mle']


class AR:
    def __init__(self, X, order):
        """

        :param order: int AR order
        :param X: the AR time series
        """
        self. X = X
        self.order = order

    def fit(self, method='mle'):
        if method not in __method__:
            raise NameError('%s method is not supported' % method)
        if method.lower() == 'ols':
            regr = ols.OLS()
            ones = np.ones(len(self.X[:len(self.X)-self.order]))
            X_regr = [ones]

            i = 0
            while i < self.order:
                X_regr.append(self.X[self.order-i-1: len(X)-i-1])
                i += 1
            X_regr = np.vstack(X_regr)

            X_regr = np.transpose(np.asmatrix(X_regr))
            y_regr = np.transpose(np.asmatrix(self.X[self.order:]))
            print(regr.fit(X_regr, y_regr))
        if method.lower() == 'mle':
            init = np.array([random.random() for _ in range(self.order+2)])
            bounds = [(-1, 1) for _ in range(self.order)] + [(0, None), (0, None)]
            min_result = spo.minimize(self.likelihood, init, bounds=tuple(bounds), tol=1e-7)
            print(min_result)

    def likelihood(self, wrapper):
        """
        here is the conditional likelihood funciton of AR(p) process,
        Specific formula, please refer to:
        http://econ.nsysu.edu.tw/ezfiles/124/1124/img/Chapter17_MaximumLikelihoodEstimation.pdf
        Parmameter
        ----------
        phi: array-like, phi_1, phi_2, ..., phi_p
        sigma: int, the standard deviation of the white noise(normal distribution)
        c: int, constant of the AR(p) process
        """
        phi = np.array([phi_ for phi_ in wrapper[:self.order]])
        sigma = wrapper[self.order]
        c = wrapper[self.order + 1]

        T = len(self.X)

        second_part = (T - self.order) * np.log(sigma)
        resids = 0
        for i in range(self.order, T):
            resids += (self.X[i] - c - np.dot(phi, self.X[i - self.order: i])) ** 2
        resids = resids * 0.5 / (sigma ** 2)
        return second_part + resids

if __name__ == '__main__':
    # generate AR(1)
    y = sm.tsa.arma_generate_sample([1, 0.4,0.3,0.5], ma=[1,0],nsample=1000)
    ar = AR(y, 3)
    ar.fit()
