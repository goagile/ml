"""


[title]: # (Аггрегация данных)


Аггрегация данных
-----------------

    >>> import numpy as np

    >>> x = np.arange(1, 6)
    >>> x
    array([1, 2, 3, 4, 5])

    >>> np.add.reduce(x)
    15

    >>> np.multiply.reduce(x)
    120

    >>> np.add.accumulate(x)
    array([ 1,  3,  6, 10, 15], dtype=int32)

    >>> np.multiply.accumulate(x)
    array([  1,   2,   6,  24, 120], dtype=int32)

Создание матрицы из векторов
----------------------------

    >>> x = np.arange(1, 6)
    >>> x
    array([1, 2, 3, 4, 5])
    >>> y = np.array([2, 2, 2, 2, 2])
    >>> np.multiply.outer(x, y)
    array([[ 2,  2,  2,  2,  2],
           [ 4,  4,  4,  4,  4],
           [ 6,  6,  6,  6,  6],
           [ 8,  8,  8,  8,  8],
           [10, 10, 10, 10, 10]])

Быстрая сумма элементов массива
-------------------------------

    >>> np.random.seed(2)
    >>> big_array = np.random.rand(100000)
    >>> int(np.sum(big_array))
    49922
    >>> int(big_array.sum())
    49922

Минимум и максимум
------------------

    >>> np.min(big_array)
    1.8354603294024052e-05
    >>> big_array.min()
    1.8354603294024052e-05

    >>> np.max(big_array)
    0.99998694190910009
    >>> big_array.max()
    0.99998694190910009

Аггрегаты для матриц
--------------------

    >>> np.random.seed(2)
    >>> m = np.random.random((3, 4))
    >>> m
    array([[ 0.4359949 ,  0.02592623,  0.54966248,  0.43532239],
           [ 0.4203678 ,  0.33033482,  0.20464863,  0.61927097],
           [ 0.29965467,  0.26682728,  0.62113383,  0.52914209]])

Сумма

    >>> m.sum()
    4.7382861037704735
    >>> m.sum(axis=0)
    array([ 1.15601738,  0.62308833,  1.37544494,  1.58373545])
    >>> m.sum(axis=1)
    array([ 1.446906  ,  1.57462222,  1.71675788])

Максимум

    >>> m.max(axis=0)
    array([ 0.4359949 ,  0.33033482,  0.62113383,  0.61927097])

Минимум

    >>> m.min(axis=1)
    array([ 0.02592623,  0.20464863,  0.26682728])

Продукт

    >>> x = np.arange(1, 10).reshape([3, 3])
    >>> x
    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])
    >>> x.prod()
    362880

Any, All
--------

    >>> np.random.seed(2)
    >>> b = np.array([np.random.randint(2) for _ in range(5)])
    >>> b
    array([0, 1, 1, 0, 0])
    >>> b.any()
    True
    >>> b.all()
    False

Пример
------

    >>> heights = np.array([189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175])
    >>> heights.min()
    163
    >>> heights.max()
    189
    >>> heights.sum()
    2295
    >>> heights.mean()
    176.53846153846155
    >>> heights.std()
    8.0155174948383188
    >>> np.percentile(heights, 25)
    171.0
    >>> np.median(heights)
    173.0


"""
