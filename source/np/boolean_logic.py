"""


[title]: # (Логические выражения)


Логические выражения
====================

Логические выражения с массивом. Возвращает bool массив элементов.

    >>> import numpy as np

    >>> x = np.array([1, 2, 3, 4, 5])
    >>> x > 3
    array([False, False, False,  True,  True], dtype=bool)
    >>> x < 3
    array([ True,  True, False, False, False], dtype=bool)
    >>> x >= 3
    array([False, False,  True,  True,  True], dtype=bool)
    >>> x == 3
    array([False, False,  True, False, False], dtype=bool)
    >>> (2 * x) == (x ** 2)
    array([False,  True, False, False, False], dtype=bool)

Подсчет ненулевых элементов

    >>> x = np.array([[5, 0, 3, 3],
    ...               [7, 9, 3, 5],
    ...               [2, 4, 7, 6]])

    >>> np.count_nonzero(x < 6)
    8
    >>> np.sum(x < 6)
    8
    >>> np.sum(x < 6, axis=0)
    array([2, 2, 2, 2])
    >>> np.sum(x < 6, axis=1)
    array([4, 2, 2])

    >>> np.any(x > 8)
    True
    >>> np.all(x < 10)
    True
    >>> np.all(x < 8, axis=1)
    array([ True, False,  True], dtype=bool)

"""
