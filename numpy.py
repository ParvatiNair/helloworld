import numpy as np
a= np.array([10, 20, 30])
print(a)

import numpy
>>> arr= numpy.array([1,78,60])
>>> print(arr)
[ 1 78 60]
>>> a= numpy.array([1,2,3,4,5,6,7,8,9,10])
>>> print(a)
[ 1  2  3  4  5  6  7  8  9 10]
>>> print(a[-1:-4:-2])
[10  8]

>>>a =numpy.arange(10, 16)
>>> print(a)
[10 11 12 13 14 15]
>>> b= a[1:6:2]
>>> print(b)
[11 13 15]
>>> print(a[-2:2:1])
[]
>>> print(a[-2:2:-1])
[14 13]

>>> arr1 =numpy.array([[1,2,3]])
>>> arr1
array([[1, 2, 3]])
>>> arr2= arr1.T
>>> arr2
array([[1],
       [2],
       [3]])

>>> arr1.shape
(1, 3)
>>> arr2.shape
(3, 1)
>>> a= numpy.array([1,2,3])
>>> a.shape
(3,)

>>> arr3= numpy.array([[1,2,3],
                       [4,5,6]])
>>> print(arr3)
[[1 2 3]
 [4 5 6]]
>>> print(arr3.ndim) #no. of dimensions
2
>>> arr3.shape= (3,2)
>>> print(arr3)
[[1 2]
 [3 4]
 [5 6]]
>>> print(arr3.reshape(2,3))
[[1 2 3]
 [4 5 6]]
>>> arr3= numpy.array([[1,2,3],
...                        [4,5,6]])
>>> print(len(arr3))
2

 from numpy import *
>>> arr= matrix('1 2 3; 4 5 6; 7 8 9')
>>> print(arr)
[[1 2 3]
 [4 5 6]
 [7 8 9]]
>>> print(diagonal(arr))
[1 5 9]
>>> m = matrix(arange(12).reshape(3,4))
>>> m
matrix([[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]])

>>> from numpy import *
>>> r,c= [int(a) for a in input("Enter rows, cols:").split()]
Enter rows, cols:2 3
>>> str= input('Enter matrix elements:\n')
Enter matrix elements:
1 2 3 4 5 6
>>> x= reshape(matrix(str), (r,c))
>>> print('The original matrix:')
The original matrix:
>>> print(x)
[[1 2 3]
 [4 5 6]]
>>> y= x.transpose()
>>> print(y)
[[1 4]
 [2 5]
 [3 6]]

>>> a = matrix([[1,2,3], [4,5,6]])
>>> print(a)
[[1 2 3]
 [4 5 6]]
>>> b = matrix([[4,5,6],[1,2,3]])
>>> print(b)
[[4 5 6]
 [1 2 3]]
>>> multiply(a,b)
matrix([[ 4, 10, 18],
        [ 4, 10, 18]])
