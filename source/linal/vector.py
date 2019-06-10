"""

    Линейная алгебра
    ================

    Лабораторная работа

    Векторы

    Уровень 1
    ---------

    Сложение векторов
    >>> v = [1, 2]
    >>> w = [2, 3]
    >>> vector_add(v, w)
    [3, 5]

    Вычитание векторов
    >>> v = [3, 5]
    >>> w = [1, 1]
    >>> vector_sub(v, w)
    [2, 4]

    Умножениие вектора на число
    >>> v = [2, 3]
    >>> c = 2
    >>> scalar(v, c)
    [4, 6]

    Сумма нескольких векторов
    >>> v = [1, 3, 4]
    >>> w = [3, 2, 5]
    >>> z = [2, 2, 1]
    >>> vector_sum(v, w, z)
    [6, 7, 10]

    Скалярное произведение векторов
    >>> v = [1, 2, 1]
    >>> w = [3, 1, 1]
    >>> dot(v, w)
    6

    Сумма квадратов
    >>> v = [2, 3]
    >>> sum_of_squares(v)
    13

    Квадратное расстояние
    >>> v = [0, 0]
    >>> w = [0, 3]
    >>> distance(v, w)
    3.0


"""
import math


def vector_add(v, w):
    """ сложение двух векторов """
    return [v[i] + w[i] for i in range(len(v))]


def vector_sub(v, w):
    """ вычитание двух векторов """
    return [v[i] - w[i] for i in range(len(v))]


def scalar(v, c):
    """ умножение вектора на число """
    return [x * c for x in v]


def vector_sum(*vectors):
    """ сумма нескольких векторов """
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result


def dot(*vectors):
    """ скалярное произведение векторов """
    muls = vectors[0]
    for vector in vectors[1:]:
        for i, x in enumerate(vector):
            muls[i] *= x
    return sum(muls)


def sum_of_squares(v):
    """ сумма кваратов элементов вектора """
    return dot(v, v)


def distance(v, w):
    """ Евклидово расстояние """
    return math.sqrt(sum_of_squares(vector_sub(v, w)))
