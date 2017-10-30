"""


[title]: # (Равномерное распределение)


Равномерное распределение
=========================

Равномерное (uniform) распределение случайных чисел

    >>> import random
    >>> import matplotlib.pyplot as plt

    >>> n = 500
    >>> x = range(n)
    >>> y = [random.uniform(-1, 1) for _ in range(n)]

    >>> plt.plot(x, y, 'o')
    >>> plt.show()


"""
