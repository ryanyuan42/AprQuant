# author: Tianshu Yuan
# Time: 2017-04-06

import numpy as np


class Arma:
    def __init__(self, order):
        """

        :param order: tuple (AR order, MA order)
        """
        self.order = order

