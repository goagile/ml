"""


[title]: # (Гистограмма равномерного распределения)


Гистограмма равномерного распределения
======================================

    >>> import matplotlib.pyplot as plt
    >>> import random

    >>> y = [random.random() for _ in range(10**3)]

    >>> plt.hist(y, 20)
    >>> plt.show()


"""
