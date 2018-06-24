"""

    Комбинаторика
    =============

    Лабораторная работа

    Сочетания, Размещения, Перестановки

    Уровень 1
    ---------

    Факториал
    >>> f(0), f(1), f(2), f(3), f(4), f(5)
    (1, 1, 2, 6, 24, 120)

    Размещения из 'n' по 'k' с повторениями
    >>> Arep(n=10, k=3)
    1000

    Размещения из 'n' по 'k' без повторений
    >>> A(n=10, k=3)
    720

    Перестановки из 'n' элементов
    >>> P(n=3)
    6

    Сочетания из 'n' элементов по 'k' без повторений
    >>> C(n=10, k=3)
    120

    Сочетания из 'n' элементов по 'k' с повторениями
    >>> Crep(n=10, k=3)
    220

    Уровень 2
    ---------

    >>> len(list(product(range(10), repeat=3)))
    1000

    Размещения из 'n' по 'k' без повторений
    >>> len(list(permutations(range(10), r=3)))
    720

    Перестановки из 'n' элементов
    >>> len(list(permutations(range(3))))
    6

    Сочетания из 'n' элементов по 'k' без повторений
    >>> len(list(combinations(range(10), 3)))
    120

    Сочетания из 'n' элементов по 'k' с повторениями
    >>> len(list(combinations_with_replacement(range(10), 3)))
    220

"""

from itertools import product, permutations, combinations, combinations_with_replacement


def f(n):
    """
        факториал числа 'n'
    """
    if n <= 1:
        return 1
    return n * f(n - 1)


def Arep(n, k):
    """
        Arrangement with repeat
        размещения из 'n' по 'k' с повторениями
    """
    return n ** k


def A(n, k):
    """
        Arrangement
        размещения из 'n' по 'k' без повторений
    """
    return int(f(n) / f(n - k))


def P(n):
    """
        Permutations
        перестановки из 'n' элементов
    """
    return A(n, n)


def C(n, k):
    """
        Combinations
        сочетания из 'n' элементов по 'k' без повторений
    """
    return int(f(n) / (f(k) * f(n - k)))


def Crep(n, k):
    """
        Combinations with repeat
        сочетания из 'n' элементов по 'k' с повторениями
    """
    return C(n + k - 1, k)
