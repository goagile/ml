"""


[title]: # (Массивы Numpy)


Массивы Numpy
-------------

Создание массивов с помощью numpy

    >>> import numpy as np

1D array
--------

    >>> np.array([1, 2, 3])
    array([1, 2, 3])

2D array
--------

    >>> np.array([[1, 2, 3],
    ...           [4, 5, 6],
    ...           [7, 8, 9]])
    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])

Zeros
-----

    >>> np.zeros(5, dtype=int)
    array([0, 0, 0, 0, 0])
    
Ones
----

    >>> np.ones(3)
    array([ 1.,  1.,  1.])
    
    >>> np.ones((3, 5), dtype=int)
    array([[1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1]])

Full
----

    >>> np.full((2, 2), 3.14)
    array([[ 3.14,  3.14],
           [ 3.14,  3.14]])

Arange
------

    >>> np.arange(0, 100, 20)
    array([ 0, 20, 40, 60, 80])

Linspace
--------

    >>> np.linspace(0, 100, 5, dtype=int)
    array([  0,  25,  50,  75, 100])

Random
------

    >>> np.random.seed(2)
    >>> np.random.random((3, 3))
    array([[ 0.4359949 ,  0.02592623,  0.54966248],
           [ 0.43532239,  0.4203678 ,  0.33033482],
           [ 0.20464863,  0.61927097,  0.29965467]])

Create a 3x3 array of normally distributed random values with mean 0 and standard deviation 1

    >>> np.random.seed(2)
    >>> np.random.normal(0, 1, (3, 3))
    array([[-0.41675785, -0.05626683, -2.1361961 ],
           [ 1.64027081, -1.79343559, -0.84174737],
           [ 0.50288142, -1.24528809, -1.05795222]])

    >>> np.random.seed(2)
    >>> np.random.randint(1, 10, (2, 2))
    array([[9, 9],
           [7, 3]])

    >>> np.eye(3)
    array([[ 1.,  0.,  0.],
           [ 0.,  1.,  0.],
           [ 0.,  0.,  1.]])

    >>> np.empty(3)
    array([ 1.,  1.,  1.])
    
    
"""
