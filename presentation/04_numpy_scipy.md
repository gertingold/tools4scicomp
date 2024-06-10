---
layout: section
---

# Scientific computing with NumPy and SciPy

---

# Scientific Python ecosystem

<div>

Basis: [NumPy](https://numpy.org)

</div>

<img src="/images/ecosystem.png" style="width: 90%; margin: auto">

---

# Multidimensional Arrays

<div>example: digital colour image, M×N×3 data</div>

<br>

<img src="/images/rgbarray.png" style="width: 40%; margin: auto">

---

# Matrices and lists of lists

<div></div>

$\mathsf{M} = \begin{pmatrix} 1&2 \\ 3&4\end{pmatrix}$

```python
>>> m = [[1, 2], [3, 4]]
>>> m[0]
[1, 2]
>>> m[0][1]
2
>>> m[0][:]
[1, 2]
>>> m[:][0]
[1, 2]
```

<br>

* addressing columns does not work as it works for rows
* lists of lists are not efficient structures for numerical work

<br>

<carbon-arrow-right /> use NumPy arrays (`ndarray`) instead

---

# Import NumPy

```python
from numpy import *
```

* imports a very large namespace
* some of the function names exist also in other modules like `math`
  which can lead to confusion

<br>

```python
from numpy import array, cos, sin
```

* it is better to explicitly state in the code where the function
  comes from, in particular when confusion can arise

<br>

```python
import numpy
```

* this is acceptable but uncommon because `numpy` is unnecessarily long

<br>

```python
import numpy as np
```

* this way of importing NumPy is generally used and recommended <carbon-thumbs-up-filled style="color: #080;"/>

---

# Creating an array

<div>

a look into the documentation of `np.array`

</div>

```python {1-17|all}{maxHeight:'350px'}
>>> np.info(np.array)
array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0,
      like=None)

Create an array.

Parameters
----------
object : array_like
    An array, any object exposing the array interface, an object whose
    ``__array__`` method returns an array, or any (nested) sequence.
    If object is a scalar, a 0-dimensional array containing object is
    returned.
dtype : data-type, optional
    The desired data-type for the array. If not given, NumPy will try to use
    a default ``dtype`` that can represent the values (by applying promotion
    rules when necessary.)
copy : bool, optional
    If true (default), then the object is copied.  Otherwise, a copy will
    only be made if ``__array__`` returns a copy, if obj is a nested
    sequence, or if a copy is needed to satisfy any of the other
    requirements (``dtype``, ``order``, etc.).
order : {'K', 'A', 'C', 'F'}, optional
    Specify the memory layout of the array. If object is not an array, the
    newly created array will be in C order (row major) unless 'F' is
    specified, in which case it will be in Fortran order (column major).
    If object is an array the following holds.

    ===== ========= ===================================================
    order  no copy                     copy=True
    ===== ========= ===================================================
    'K'   unchanged F & C order preserved, otherwise most similar order
    'A'   unchanged F order if input is F and not C, otherwise C order
    'C'   C order   C order
    'F'   F order   F order
    ===== ========= ===================================================

    When ``copy=False`` and a copy is made for other reasons, the result is
    the same as if ``copy=True``, with some exceptions for 'A', see the
    Notes section. The default order is 'K'.
subok : bool, optional
    If True, then sub-classes will be passed-through, otherwise
    the returned array will be forced to be a base-class array (default).
ndmin : int, optional
    Specifies the minimum number of dimensions that the resulting
    array should have.  Ones will be prepended to the shape as
    needed to meet this requirement.
like : array_like, optional
    Reference object to allow the creation of arrays which are not
    NumPy arrays. If an array-like passed in as ``like`` supports
    the ``__array_function__`` protocol, the result will be defined
    by it. In this case, it ensures the creation of an array object
    compatible with that passed in via this argument.

    .. versionadded:: 1.20.0

Returns
-------
out : ndarray
    An array object satisfying the specified requirements.

See Also
--------
empty_like : Return an empty array with shape and type of input.
ones_like : Return an array of ones with shape and type of input.
zeros_like : Return an array of zeros with shape and type of input.
full_like : Return a new array with shape of input filled with value.
empty : Return a new uninitialized array.
ones : Return a new array setting values to one.
zeros : Return a new array setting values to zero.
full : Return a new array of given shape filled with value.


Notes
-----
When order is 'A' and ``object`` is an array in neither 'C' nor 'F' order,
and a copy is forced by a change in dtype, then the order of the result is
not necessarily 'C' as expected. This is likely a bug.

Examples
--------
>>> np.array([1, 2, 3])
array([1, 2, 3])

Upcasting:

>>> np.array([1, 2, 3.0])
array([ 1.,  2.,  3.])

More than one dimension:

>>> np.array([[1, 2], [3, 4]])
array([[1, 2],
       [3, 4]])

Minimum dimensions 2:

>>> np.array([1, 2, 3], ndmin=2)
array([[1, 2, 3]])

Type provided:

>>> np.array([1, 2, 3], dtype=complex)
array([ 1.+0.j,  2.+0.j,  3.+0.j])

Data-type consisting of more than one element:

>>> x = np.array([(1,2),(3,4)],dtype=[('a','<i4'),('b','<i4')])
>>> x['a']
array([1, 3])

Creating an array from sub-classes:

>>> np.array(np.mat('1 2; 3 4'))
array([[1, 2],
       [3, 4]])

>>> np.array(np.mat('1 2; 3 4'), subok=True)
matrix([[1, 2],
        [3, 4]])
```

---

# Converting a list of lists into an `ndarray`

```python
>>> import numpy as np
>>> matrix = [[0, 1, 2],
...           [3, 4, 5],
...           [6, 7, 8]]
>>> myarray = np.array(matrix)
>>> myarray
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
>>> type(myarray)
<class 'numpy.ndarray'>
```
```python
>>> myarray[0, :]
array([0, 1, 2])
>>> myarray[:, 0]
array([0, 3, 6])
```

* In contrast to lists of lists, the `ndarray` allows to access rows and columns
  in a consistent way.

<div class="mt-3 p-2 border-2 border-teal-800 bg-teal-50 text-teal-800">
  <div class="grid grid-cols-[2%_1fr] gap-4">
    <div><carbon-idea class="text-teal-800 text-xl" /></div>
    <div>
    <code>append</code> is frequently used to construct lists. Do not use it for arrays as this
    leads to significant performance loss.
    </div>
  </div>
</div>

---

# The structure of an `ndarray`

<div>

print attributes of an `ndarray`

</div>

```python
def array_attributes(a):
    for attr in ('ndim', 'size', 'itemsize', 'dtype', 'shape', 'strides'):
        print(f'{attr:8s}: {getattr(a, attr)}')
```

```python
>>> matrix = np.arange(16)
>>> matrix
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])
>>> array_attributes(matrix)
ndim    : 1
size    : 16
itemsize: 8
dtype   : int64
shape   : (16,)
strides : (8,)
```

* `int64` requires 64 bits or 8 bytes, in total this array requires 128 bytes
* the stride from one entry to the next amounts to 8 bytes
* due to the homogeneity of the data, the position of a given entry can easily
  be determined

---

# The problem with finite precision

```python
>>> np.arange(1, 160, 10, dtype=np.int8)
array([   1,   11,   21,   31,   41,   51,   61,   71,   81,   91,  101,
        111,  121, -125, -115, -105], dtype=int8)
```

* `int8` refers to signed integers with 8 bits covering the range from -128 to 127
* be aware of the danger of overflow

<br>

<div class="p-2 border-2 border-red-800 bg-red-50 text-red-800">
  <div class="grid grid-cols-[4%_1fr] gap-10">
    <div><carbon-warning-alt class="text-red-800 text-3xl" /></div>
    <div>
     While integers in Python in principle can become arbitrarily large, this is
     not the case for integer <code>ndarray</code>s in NumPy!
    </div>
  </div>
</div>

<br>

#### Data types

<div class="grid grid-cols-[1fr_1fr_1fr_1fr_1fr] gap-6">
  <div>

  * int8
  * int16
  * int32
  * int64

  </div>
  <div>

  * uint8
  * uint16
  * uint32
  * uint64

  </div>
  <div>

  * float16
  * float32
  * float64
  * longdouble

  </div>
  <div>

  * complex64
  * complex128
  * clongdouble

  </div>
  <div>

  * bool
  * object
  * bytes
  * str
  * void

  </div>
</div>

---

# Shapes and strides

<div class="grid grid-cols-[40%_1fr] gap-6">
  <div>

```python
>>> matrix = np.arange(16).reshape(4, 4)
>>> matrix
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])
>>> array_attributes(matrix)
ndim    : 2
size    : 16
itemsize: 8
dtype   : int64
shape   : (4, 4)
strides : (32, 8)
```

 * shapes and strides change the interpretation of data aligned in one dimension
 * data can be reinterpreted without copying data in memory

  </div>
  <div>

<img src="/images/strides.png" style="width: 90%; margin: auto">

  </div>
</div>

---

# Avoid copying arrays

<div class="mt-3 ml-30 mr-30 p-4 border-2 border-teal-800 bg-teal-50 text-teal-800">
  <div class="grid grid-cols-[3%_1fr] gap-4">
    <div><carbon-idea class="text-teal-800 text-xl" /></div>
    <div>
     Moving around large blocks of data in memory can take a lot of time.
     Avoid making copies of arrays, if possible.
    </div>
  </div>
</div>

<br>

#### example: transposition of a matrix

```python
>>> a = np.arange(9).reshape(3, 3)
>>> a
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
>>> a.strides
(24, 8)
>>> a.T
array([[0, 3, 6],
       [1, 4, 7],
       [2, 5, 8]])
>>> a.T.strides
(8, 24)
```

* no data are copied

---

# Be careful when modifiying strides

```python
>>> a = np.arange(16)
>>> a
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15])
```
```python
>>> a.shape = (4, 4)
>>> a.strides = (8, 8)
>>> a
array([[0, 1, 2, 3],
       [1, 2, 3, 4],
       [2, 3, 4, 5],
       [3, 4, 5, 6]])
```

* caution: changing an element here can imply changes of other elements as well

```python
>>> a.strides = (8, 4)
>>> a
array([[          0,  4294967296,           1,  8589934592],
       [          1,  8589934592,           2, 12884901888],
       [          2, 12884901888,           3, 17179869184],
       [          3, 17179869184,           4, 21474836480]])
```

* data are take as is
* not respecting data boundaries can lead to unintended results

---

# Initializing an array

* If an array cannot be created directly, an array of the desired size should
  be initialized. Do not use the `append` method.

```python
>>> a = np.zeros((2, 2))
>>> a
array([[0., 0.],
       [0., 0.]])
>>> a.dtype
dtype('float64')
```

* All elements are set to zero in this case.
* The default data type is `float64`.

```python
>>> a = np.zeros((2, 2), dtype=int)
>>> a
array([[0, 0],
       [0, 0]])
>>> a.dtype
dtype('int64')
```

* If a different data is needed, it should be specified through the `dtype` argument.

---

# Initializing an array (cont'd)

```python
>>> np.empty((3, 3))
array([[4.49105672e-320, 0.00000000e+000, 1.77459490e+248],
       [4.29058029e+270, 1.33733641e+160, 8.59372554e-096],
       [1.01021434e+141, 1.43180994e-065, 9.16526748e+242]])
```

* If all elements will be overwritten before usage anway, it is slightly more efficient
  not to set the elements but to leave the memory as is.

```python
>>> np.ones((2, 2))
array([[1., 1.],
       [1., 1.]])
```
```python
>>> 10*np.ones((2, 2))
array([[10., 10.],
       [10., 10.]])
```

* By multiplication, it is possible to feel an array homogeneously with the desired value.

---

# Structured matrices

```python
>>> np.identity(3)
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
```

* In this way, only square matrices can be created.

```python
>>> np.eye(2, 4)
array([[1., 0., 0., 0.],
       [0., 1., 0., 0.]])
>>> np.eye(4, k=1)
array([[0., 1., 0., 0.],
       [0., 0., 1., 0.],
       [0., 0., 0., 1.],
       [0., 0., 0., 0.]])
```

* With the `eye` method, also non-square unit matrices, possibly with a shifted diagonal, can be created 

```python
>>> 2*np.eye(4)-np.eye(4, k=1)-np.eye(4, k=-1)
array([[ 2., -1.,  0.,  0.],
       [-1.,  2., -1.,  0.],
       [ 0., -1.,  2., -1.],
       [ 0.,  0., -1.,  2.]])
```

---

# Diagonal matrices and diagonals

```python
>>> np.diag([1, 2, 3, 4])
array([[1, 0, 0, 0],
       [0, 2, 0, 0],
       [0, 0, 3, 0],
       [0, 0, 0, 4]])
```

* A two-dimensional diagonal matrix is generated from a one-dimensional sequence.

```python
>>> matrix = np.arange(16).reshape(4, 4)
>>> matrix
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])
>>> np.diag(matrix)
array([ 0,  5, 10, 15])
```

* From a two-dimensional matrix which can even be non-square, the diagonal is extracted.

---

# Generating matrix elements by means of a function

#### Example: multiplication table

```python
>>> np.fromfunction(lambda i, j: (i+1)*(j+1), shape=(6, 6), dtype=int)
array([[ 1,  2,  3,  4,  5,  6],
       [ 2,  4,  6,  8, 10, 12],
       [ 3,  6,  9, 12, 15, 18],
       [ 4,  8, 12, 16, 20, 24],
       [ 5, 10, 15, 20, 25, 30],
       [ 6, 12, 18, 24, 30, 36]])
```

* This works also in more than two dimensions.

```python
>>> np.fromfunction(lambda i, j, k: (i+1)*(j+1)/(k+1), shape=(2, 2, 2))
array([[[1. , 0.5],
        [2. , 1. ]],

       [[2. , 1. ],
        [4. , 2. ]]])
````

---

# Equally-spaced values

```python
np.arange(1, 2, 0.1)
array([1. , 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9])
```

* generalization of `range`
* final value is not generated
* step width is specified

<br>

```python
>>> np.linspace(1, 2, 11)
array([1. , 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2. ])
```

* number of elements is specified

```python
>>> np.linspace([1, 2], [2, -2], 11)
array([[ 1. ,  2. ],
       [ 1.1,  1.6],
       ⋮
       [ 1.9, -1.6],
       [ 2. , -2. ]])
```

* works also for lists and arrays

---

# Equally-spaced values (cont'd)

```python
>>> np.linspace(1, 4, 7, retstep=True)
(array([1. , 1.5, 2. , 2.5, 3. , 3.5, 4. ]), 0.5)
```

* It is possible to obtain the step width.
* It is possible to omit the last value (`endpoint=False`).

<br>

```python
>>> np.logspace(0, 3, 4)
array([   1.,   10.,  100., 1000.])
>>> np.logspace(0, 2, 5, base=2)
array([1.        , 1.41421356, 2.        , 2.82842712, 4.        ])
```

* logarithmic scales are possible as well
* default base is 10
* the first two arguments are to be understood as exponents

---

# Application of linspace

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x, y)
plt.show()
```

<br>

<img src="/images/application_linspace.png" style="width: 40%; margin: auto">

---

# Load data from a file

```python
# mydata.dat

# time position
   0.0   0.0
   0.1   0.1
   0.2   0.4
   0.3   0.9
```

```python
>>> np.loadtxt('mydata.dat')
array([[0. , 0. ],
       [0.1, 0.1],
       [0.2, 0.4],
       [0.3, 0.9]])
```

* `loadtxt` has a number of useful arguments, see [documentation](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy-loadtxt)
* for a even more flexible way of reading data files, see [genfromtxt](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html#numpy-genfromtxt)

---

# Random arrays

```python
>>> rng = np.random.default_rng()
```

```python
>>> rng.random((2, 5))
array([[0.83225433, 0.62066329, 0.8186137 , 0.81388624, 0.93601643],
       [0.51750755, 0.00895467, 0.65958576, 0.59495482, 0.9500244 ]])
>>> rng.random((2, 5))
array([[0.62886203, 0.54529378, 0.73134872, 0.58461308, 0.34375939],
       [0.5687676 , 0.89653199, 0.60219157, 0.84906627, 0.10558733]])
```

* In order to make the random numbers reproducible, a seed can be specified.

```python
>>> rng = np.random.default_rng(1234546)
>>> rng.random((2, 5))
array([[0.41581531, 0.19749742, 0.47628191, 0.07599962, 0.75069401],
       [0.7087109 , 0.58950695, 0.97730533, 0.58801372, 0.81343677]])
>>> rng = np.random.default_rng(1234546)
>>> rng.random((2, 5))
array([[0.41581531, 0.19749742, 0.47628191, 0.07599962, 0.75069401],
       [0.7087109 , 0.58950695, 0.97730533, 0.58801372, 0.81343677]])
```

---

# Displaying an array of random numbers

<div class="grid grid-cols-[1fr_1fr] gap-4">
 <div>

```python
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
data = rng.random((20, 20))
plt.imshow(data, cmap=plt.cm.hot, interpolation='none')
plt.colorbar()
plt.show()
```

  </div>
  <div>
<img src="/images/randomarray.png" style="width: 70%; margin: auto">
  </div>
</div>

* There exist a variety of different random number generators, e.g.:
  * `integers`: random integers between a lower and an upper value
  * `choice`: random choice of elements from an array with or without replacement
  * `shuffle`: shuffles an array in-place
  * `normal`: normally distributed random numbers
  * and many more, see [documentation](https://numpy.org/doc/stable/reference/random/generator.html)

---

# Indexing arrays

```python
>>> a = np.arange(10)
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```
```python
>>> a[:]
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```
```python
>>> a[1:4]
array([1, 2, 3])
```
```python
>>> a[5:-2]
array([5, 6, 7])
```
```python
>>> a[::2]
array([0, 2, 4, 6, 8])
```
```python
>>> a[1::2]
array([1, 3, 5, 7, 9])
```
```python
>>> a[::-1]
array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
```

* corresponds to the usual slicing syntax

---

# Array aliases and copies

<div class="grid grid-cols-[1fr_1fr] gap-4">
  <div>

```python
>>> a = np.arange(10)
>>> b = a
>>> b
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> id(a), id(b)
(133258061830960, 133258061830960)
>>> b[0] = 42
>>> a
array([42,  1,  2,  3,  4,  5,  6,  7,  8,  9])
```

 * `b` is just an alias for `a`, not a different array

  </div>
  <div>

```python
>>> a = np.arange(10)
>>> b = a[:]
>>> b
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> id(a), id(b)
(133258085410128, 133257805172912)
>>> b[0] = 42
>>> a
array([42,  1,  2,  3,  4,  5,  6,  7,  8,  9])
```

 * while a new object is generated, it refers to the same part of the memory

  </div>
</div>
<div class="grid grid-cols-[1fr_1fr] gap-4">
  <div>

```python
>>> a = np.arange(10)
>>> b = np.copy(a)
>>> b[0] = 42
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> b
array([42,  1,  2,  3,  4,  5,  6,  7,  8,  9])
```

  </div>
  <div>

 * a true copy is made by using the `copy`-method

  </div>
</div>

---

# Slicing in higher dimensions

<div class="grid grid-cols-[1fr_1fr] gap-4">
  <div>

```python
>>> a = np.arange(36).reshape(6, 6)
>>> a
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23],
       [24, 25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34, 35]])
```

```python
>>> a[:, :]
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23],
       [24, 25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34, 35]])
```
```python
>>> a[2:4, 3:6]
array([[15, 16, 17],
       [21, 22, 23]])
```

  </div>
  <div>

```python
>>> a[::2, ::3]
array([[ 0,  3],
       [12, 15],
       [24, 27]])
```
```python
>>> a[2::2, ::3]
array([[12, 15],
       [24, 27]])
```
```python
>>> a[2:4]
array([[12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23]])
```

 * In the last example, an implicit slice `::` is
   assumed for the second dimension (axis 1).

  </div>
</div>

---

# Array axes

#### Index notation for matrices

<br>

<div class="grid grid-cols-[3%_1fr_1fr] gap-4">
  <div>

  $a_{ij}$

  </div>
  <div>

 * first index ($i$) refers to row (axes 0)
 * second index ($j$) refers to column (axes 1)

  <br>

  <img src="/images/axes.png" style="width: 75%; margin: auto">

  </div>
  <div>
  Example: summation along different axes

  <br>

```python
>>> a = np.arange(16).reshape(4, 4)
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])
```
```python
>>> a.sum(axis=0)
array([24, 28, 32, 36])
```
```python
>>> a.sum(axis=1)
array([ 6, 22, 38, 54])
```
```python
>>> a.sum()
120
```

  </div>
</div>

---

# Higher-dimensional arrays

<div class="grid grid-cols-[1fr_1fr] gap-4">
  <div>

```python
>>> b = np.arange(24).reshape(2, 3, 4)
>>> b
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]],

       [[12, 13, 14, 15],
        [16, 17, 18, 19],
        [20, 21, 22, 23]]])
```
```python
>>> b[0]
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
```
```python
>>> b[:, 0]
array([[ 0,  1,  2,  3],
       [12, 13, 14, 15]])
```
```python
>>> b[:, :, 0]
array([[ 0,  4,  8],
       [12, 16, 20]])
```

  </div>
  <div>
    <img src="/images/array3d.png" style="width: 75%; margin: auto">
  </div>
</div>

---
layout: gli-two-cols-header
---

# Ellipsis

::left::

```python
>>> b[..., 0]
array([[ 0,  4,  8],
       [12, 16, 20]])
```
```python
>>> c = np.arange(16).reshape(2, 2, 2, 2)
>>> c
array([[[[ 0,  1],
         [ 2,  3]],

        [[ 4,  5],
         [ 6,  7]]],


       [[[ 8,  9],
         [10, 11]],

        [[12, 13],
         [14, 15]]]])
```
```python
>>> c[0, ..., 0]
array([[0, 2],
       [4, 6]])
```

::right::

* ellipsis replaces all missing indices by a colon
* only one ellipsis allowed so that the slice is unambiguous

---
layout: gli-two-cols-header
---

# Columns with different shape

::left::

```python
>>> a = np.arange(16).reshape(4, 4)
>>> a
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])
```
```python
>>> a[:, 0:1]
array([[ 0],
       [ 4],
       [ 8],
       [12]])
```
```python
>>> a[:, 0]
array([ 0,  4,  8, 12])
```

::right::

```python
>>> b = np.arange(4)
>>> b
array([0, 1, 2, 3])
```
```python
>>> b[:, np.newaxis]
array([[0],
       [1],
       [2],
       [3]])
>>> b[:, np.newaxis].shape
(4, 1)
```
```python
>>> b[np.newaxis, :]
array([[0, 1, 2, 3]])
>>> b[np.newaxis, :].shape
(1, 4)
```

<br>

* `np.newaxis` adds a new axis with minimal extension

---

# Fancy indexing

```python
>>> a = np.arange(36).reshape(6, 6)
>>> a
array([[ 0,  1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16, 17],
       [18, 19, 20, 21, 22, 23],
       [24, 25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34, 35]])
```
```python
>>> a[[0, 2, 1], [1, 3, 5]]
array([ 1, 15, 11])
```
```python
>>> id_row = [[2, 0], [1, 3]]
>>> id_col = [[0, 2], [4, 5]]
>>> a[id_row, id_col]
array([[12,  2],
       [10, 23]])
```

* the arrays contain the indices of the corresponding axis
* fancy indexing can be used for arrays of arbitrary dimension if a corresponding
  number of index arrays is given
* the dimension of the index arrays determines the dimension of the resulting array

---

# Fancy indexing with boolean arrays

```python
>>> rng = np.random.default_rng()
>>> randomarray = rng.random(10)
>>> randomarray
array([0.09631035, 0.54061246, 0.7692907 , 0.42787232, 0.54760366,
       0.64386641, 0.0696345 , 0.40970968, 0.24665492, 0.87821191])
```
```python
>>> indexarray = randomarray < 0.5
>>> indexarray
array([ True, False, False,  True, False, False,  True,  True,  True,
       False])
```
```python
>>> randomarray[indexarray] = 0
>>> randomarray
array([0.        , 0.54061246, 0.7692907 , 0.        , 0.54760366,
       0.64386641, 0.        , 0.        , 0.        , 0.87821191])
```
```python
>>> randomarray[np.logical_not(indexarray)]
array([0.54061246, 0.7692907 , 0.54760366, 0.64386641, 0.87821191])
```

* a boolean array selects those entries where the corresponding entry
  of the boolean array is `True`

---

# Application: sieve of Eratosthenes

<img src="/images/eratosthenes.png" style="width: 75%; margin: auto">

---

# Application: sieve of Eratosthenes (cont'd)

```python
import math
import numpy as np

nmax = 49
integers = np.arange(nmax+1)
is_prime = np.ones(nmax+1, dtype=bool)
is_prime[:2] = False
for j in range(2, math.isqrt(nmax)+1):
    if is_prime[j]:
        is_prime[j*j::j] = False
    print(integers[is_prime])
```

```
[ 2  3  5  7  9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49]
[ 2  3  5  7 11 13 17 19 23 25 29 31 35 37 41 43 47 49]
[ 2  3  5  7 11 13 17 19 23 25 29 31 35 37 41 43 47 49]
[ 2  3  5  7 11 13 17 19 23 29 31 37 41 43 47 49]
[ 2  3  5  7 11 13 17 19 23 29 31 37 41 43 47 49]
[ 2  3  5  7 11 13 17 19 23 29 31 37 41 43 47]
```

---

# Multiplication of arrays and scalars

#### Multiplication of two arrays

```python
>>> a = np.array([[1, 2], [-3, 4]])
>>> b = np.array([[-2, 1], [0, -1]])
>>> a*b
array([[-2,  2],
       [ 0, -4]])
```

* the multiplication of two arrays happens elementwise
* matrix multiplication is done by means of `np.dot` or `@`

<br>

#### Multiplication of an array and a scalar

```python
>>> 10 * np.ones(5)
array([10., 10., 10., 10., 10.])
```

#### Comparison with a number
```python
>>> np.arange(6) > 3
array([False, False, False, False,  True,  True])
```

* Why does this work?

---

# Broadcasting

* In order to ensure that two arrays have the same dimensions, axes of length 1 are prepended.
* This rule includes scalars which behave like arrays with shape `(1,)`.
* Axes of length 1 are copied as often as necessary to reach the extent required by the other array.

<br>

<div class="grid grid-cols-[1fr_40%] gap-4">
  <div>
    <img src="/images/broadcast.png" style="width: 90%; margin: auto">
  </div>
  <div>

```python
>>> a = np.arange(1, 13).reshape(3, 4)
>>> v = np.arange(1, 5)
```
```python
>>> a
array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
>>> v
array([1, 2, 3, 4])
```
```python
>>> a*v
array([[ 1,  4,  9, 16],
       [ 5, 12, 21, 32],
       [ 9, 20, 33, 48]])
```

  </div>
</div>

---
layout: gli-two-cols-header
---

# Matrix multiplication

::left::

```python
>>> a = np.arange(4)
>>> b = np.arange(4, 8)
>>> a
array([0, 1, 2, 3])
>>> b
array([4, 5, 6, 7])
```
```python
>>> np.dot(a, b)
38
```
```python
>>> a.dot(b)
38
```
```python
>>> a @ b
38
```

::right::

```python
>>> a = np.array([[1, 2], [-3, 4]])
>>> b = np.array([[-2, 1], [0, -1]])
>>> a
array([[ 1,  2],
       [-3,  4]])
>>> b
array([[-2,  1],
       [ 0, -1]])
```
```python
>>> np.dot(a, b)
array([[-2, -1],
       [ 6, -7]])
```
```python
>>> a.dot(b)
array([[-2, -1],
       [ 6, -7]])
```
```python
>>> a @ b
array([[-2, -1],
       [ 6, -7]])
```

* `@` is preferred for product of two two-dimensional arrays

---

# Matrix-vector multiplication

```python
>>> v = np.array([2, -3])
>>> m = np.array([[1, 3], [-2, 2]])
```
```python
>>> np.dot(m, v)
array([ -7, -10])
```
```python
>>> np.dot(v, m)
array([8, 0])
```
```python
>>> np.dot(v.T, m)
array([8, 0])
```

<br>

#### Multiplication of an N-dimensional array and an M-dimensional array

* sum over last axis of the first array and the second-to-last axis of the second array

```python
dot(a, b)[i,j,k,m] = sum(a[i,j,:] * b[k,:,m])
```

* one-dimensional arrays `v` and `v.T` have the same shape

---

# Universal functions

* universal function cannot only handle scalar arguments but also arrays

```python
>>> import math
>>> x = np.linspace(0, 2, 11)
>>> x
array([0. , 0.2, 0.4, 0.6, 0.8, 1. , 1.2, 1.4, 1.6, 1.8, 2. ])
```
```python
>>> math.sin(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: only length-1 arrays can be converted to Python scalars
```
```python
>>> np.sin(x)
array([0.        , 0.19866933, 0.38941834, 0.56464247, 0.71735609,
       0.84147098, 0.93203909, 0.98544973, 0.9995736 , 0.97384763,
       0.90929743])
```
```python
>>> x = np.array([[0, np.pi/2], [np.pi, 3/2*np.pi]])
>>> np.sin(x)
array([[ 0.0000000e+00,  1.0000000e+00],
       [ 1.2246468e-16, -1.0000000e+00]])
```

* for universal functions available in NumPy see the [documentation](https://numpy.org/doc/stable/reference/routines.math.html)

---

# Universal functions in SciPy

* much larger selection of unctions with many special functions, see the [documentation](https://docs.scipy.org/doc/scipy/reference/special.html)

<br>

<div class="grid grid-cols-[1fr_1fr] gap-4">
  <div>

```python
>>> from scipy.special import airy
>>> import matplotlib.pyplot as plt
>>> x = np.linspace(-20, 5, 300)
>>> ai, aip, bi, bip = airy(x)
>>> plt.plot(x, ai, label="Ai(x)")
[<matplotlib.lines.Line2D object at 0x76a51921bc50>]
>>> plt.plot(x, aip, label="Ai'(x)")
[<matplotlib.lines.Line2D object at 0x76a5147b3710>]
>>> plt.legend()
<matplotlib.legend.Legend object at 0x76a514794710>
>>> plt.show()
```

  </div>
  <div>
    <img src="/images/airy.png" style="width: 90%; margin: auto">
  </div>
</div>

---

# Two-dimensional grids with `np.mgrid`

<div class="grid grid-cols-[1fr_1fr] gap-4">
  <div>

```python
>>> np.mgrid[0:2:0.5, 0:1:0.5]
array([[[0. , 0. ],
        [0.5, 0.5],
        [1. , 1. ],
        [1.5, 1.5]],

       [[0. , 0.5],
        [0. , 0.5],
        [0. , 0.5],
        [0. , 0.5]]])
```

* corresponds to `np.arange`

```python
>>> np.mgrid[0:3:2j, 0:2:5j]
array([[[0. , 0. , 0. , 0. , 0. ],
        [3. , 3. , 3. , 3. , 3. ]],

       [[0. , 0.5, 1. , 1.5, 2. ],
        [0. , 0.5, 1. , 1.5, 2. ]]])
```

 * corresponds to `np.linspace`
 * last argument is purely imaginary

  </div>
  <div>

```python
>>> x, y = np.mgrid[-5:5:100j, -5:5:100j]
>>> plt.imshow(np.sin(x*y))
<matplotlib.image.AxesImage object at 0x76a511a91d10>
>>> plt.show()
```

  <img src="/images/sinxy.png" style="width: 90%; margin: auto">

  </div>
</div>

---

# Two-dimensional grids with `np.ogrid`

<div class="grid grid-cols-[1fr_1fr] gap-4">
  <div>

```python
>>> np.ogrid[0:2:3j, 0:1:5j]
[array([[0.],
       [1.],
       [2.]]), array([[0.  , 0.25, 0.5 , 0.75, 1.  ]])]
```

 * open grid, uses broadcasting

<br>

 * example: Bessel function $J_\nu(x)$

  </div>
  <div>

```python
>>> from scipy.special import jv
>>> nu, x = np.ogrid[0:10:41j, 0:20:100j]
>>> plt.imshow(jv(nu, x), origin='lower')
<matplotlib.image.AxesImage object at 0x76a511a7c050>
>>> plt.xlabel('$x$')
Text(0.5, 0, '$x$')
>>> plt.ylabel(r'$\nu$')
Text(0, 0.5, '$\\nu$')
>>> plt.show()
```

  </div>
</div>

<br>

<img src="/images/besselj.png" style="width: 60%; margin: auto">

---

# Constructing a two-dimensional grid by hand

```python
>>> x = np.linspace(-40, 40, 500)
>>> y = x[:, np.newaxis]
>>> z = np.sin(np.hypot(x-10, y))+np.sin(np.hypot(x+10, y))
>>> plt.imshow(z)
<matplotlib.image.AxesImage object at 0x76a510afde90>
>>> plt.show()
```

<br>

<img src="/images/interference.png" style="width: 30%; margin: auto">

---

# Runtime comparison

<div class="grid grid-cols-[1fr_1fr] gap-4">
  <div>

```python {all}{maxHeight:'440px'}
import math
import time
import matplotlib.pyplot as plt
import numpy as np

def sin_math(nmax):
    xvals = np.linspace(0, 2*np.pi, nmax)
    start = time.time()
    for x in xvals:
        y = math.sin(x)
    return time.time()-start

def sin_math_list(nmax):
    xvals = np.linspace(0, 2*np.pi, nmax)
    start = time.time()
    yvals = []
    for x in xvals:
        yvals.append(math.sin(x))
    return time.time()-start

def sin_numpy(nmax):
    xvals = np.linspace(0, 2*np.pi, nmax)
    start = time.time()
    yvals = np.sin(xvals)
    return time.time()-start

maxpower = 27
nvals = 2**np.arange(0, maxpower+1)
tvals = np.empty((maxpower+1, 3))
for nr, nmax in enumerate(nvals):
    for idx, f in enumerate((sin_math, sin_math_list, sin_numpy)):
        tvals[nr, idx] = f(nmax)
plt.rc('text', usetex=True)
plt.xscale('log')
plt.xlabel('$n_\mathrm{max}$', fontsize=20)
plt.ylabel('$t_\mathrm{math}/t_\mathrm{numpy}$', fontsize=20)
plt.plot(nvals, tvals[:, 0]/tvals[:, 2], 'o', label='no list')
plt.plot(nvals, tvals[:, 1]/tvals[:, 2], 'o', label='list')
plt.legend()
plt.show()
```

  </div>
  <div>
    <img src="/images/math_numpy.png" style="width: 90%; margin: auto">
  </div>
</div>

---
layout: gli-two-cols-header
---

# Linear algebra with NumPy

::left::

#### common way to import the `linalg` module

```python
>>> import numpy.linalg as LA
```

#### norm of a vector

```python
>>> v = np.array([1, -2, 3])
>>> n = LA.norm(v)
>>> n**2
14.0
>>> v_normalized = v/n
>>> LA.norm(v_normalized)
1.0
```

#### determinant
```python
>>> m = np.array([[2, 5], [1, 3]])
>>> m
array([[2, 5],
       [1, 3]])
>>> LA.det(m)
1.0
```

::right::

#### inverse matrix

```python
>>> LA.inv(m)
array([[ 3., -5.],
       [-1.,  2.]])

```

<br>

#### solving a system of linear equations

$$\mathsf{M}\mathbf{x} = \mathbf{v}\quad\longrightarrow\quad
\mathbf{x} = \mathsf{M}^{-1}\mathbf{v}$$

```python
>>> v = np.array([4, 1])
>>> np.dot(LA.inv(m), v)
array([ 7., -2.])
```
```python
>>> LA.solve(m, v)
array([ 7., -2.])
```

---
layout: gli-two-cols-header
---

# Solution of an eigenvalue problem

::left::

$$\begin{pmatrix} -2 & 2\\ 2 & 1\end{pmatrix}\mathbf{x} = \lambda\mathbf{x}$$

```python
m = np.array([[-2, 2], [2, 1]])
```
```python
>>> LA.eigh(m)
EighResult(eigenvalues=array([-3.,  2.]), 
           eigenvectors=array([[-0.89442719, -0.4472136 ],
                               [ 0.4472136 , -0.89442719]]))
```

#### only eigenvalues:

```python
>>> LA.eigvalsh(m)
array([-3.,  2.])
```

<br>

* `eigh`, `eigvalsh` for Hermitian matrices
* `eig`, `eigvals` also for non-Hermitian matrices

::right::

```python
>>> evals, evecs = LA.eigh(m)
```
```python
>>> np.dot(m, evecs[:, 0])
array([ 2.68328157, -1.34164079])
>>> evals[0]*evecs[:, 0]
array([ 2.68328157, -1.34164079])
```
```python
>>> np.dot(m, evecs[:, 1])
array([-0.89442719, -1.78885438])
>>> evals[1]*evecs[:, 1]
array([-0.89442719, -1.78885438])

```

* the eigenvectors are stored as columns of the array
  `eigenvectors` (or here: `evecs`)

<br>

#### analytical eigenvectors

```python
>>> np.array([-2, 1])/np.sqrt(5)
array([-0.89442719,  0.4472136 ])
>>> np.array([-1, -2])/np.sqrt(5)
array([-0.4472136 , -0.89442719])
```

---

# Timing of `eig` vs. `eigh`

```python
>>> import timeit
>>> a = np.random.random(250000).reshape(500, 500)
>>> a = a+a.T
>>> timeit.repeat('LA.eig(a)', number=100, globals=globals())
[29.35714398899927, 28.644749746999878, 28.60115212599976, 28.615708055999676, 28.734661153999696]
>>> timeit.repeat('LA.eigh(a)', number=100, globals=globals())
[3.747801464999611, 4.294489919000625, 4.144420298999648, 4.138807968000037, 4.069388242000059]
```

<br>

* In this example, `eigh` is about a factor of 7 faster than `eig`.
* timing values can fluctuate  

---

# SciPy-Module

<div class="grid grid-cols-[12%_1fr_9%_1fr] gap-4">
  <div><code>cluster</code></div>
  <div><a href="https://docs.scipy.org/doc/scipy/reference/cluster.html">Clustering functionality</a></div>
  <div><code>misc</code></div>
  <div><a href="https://docs.scipy.org/doc/scipy/reference/misc.html">Utility routines (deprecated)</a></div>
  <div><code>constants</code></div>
  <div><a href="https://docs.scipy.org/doc/scipy/reference/constants.html">Physical and mathematical constants and units</a></div>
  <div><code>ndimage</code></div>
  <div><a href="https://docs.scipy.org/doc/scipy/reference/ndimage.html">N-dimensional image processing and interpolation</a></div>
  <div><code>datasets</code></div>
  <div><a href="https://docs.scipy.org/doc/scipy/reference/datasets.html">Load SciPy datasets</a></div>
  <div><code>odr</code></div>
  <div><a href="https://docs.scipy.org/doc/scipy/reference/odr.html">Orthogonal distance regression</a></div>
  <div><code>fft</code></div>
  <div><a href="https://docs.scipy.org/doc/scipy/reference/fft.html">Discrete Fourier and related transforms</a></div>
  <div><code>optimize</code></div>
  <div><a href="https://docs.scipy.org/doc/scipy/reference/optimize.html">Numerical optimization</a></div>
  <div><code>fftpack</code></div>
  <div><a href="https://docs.scipy.org/doc/scipy/reference/fftpack.html">Discrete Fourier transforms (legacy)</a></div>
  <div><code>signal</code></div>
  <div><a href="https://docs.scipy.org/doc/scipy/reference/signal.html">Signal processing</a></div>
  <div><code>integrate</code></div>
  <div><a href="https://docs.scipy.org/doc/scipy/reference/integrate.html">Numerical integration and ODEs</a></div>
  <div><code>sparse</code></div>
  <div><a href="https://docs.scipy.org/doc/scipy/reference/sparse.html">Sparse arrays, linear algebra and graph algorithms</a></div>
  <div><code>interpolate</code></div>
  <div><a href="https://docs.scipy.org/doc/scipy/reference/interpolate.html">Interpolation</a></div>
  <div><code>spatial</code></div>
  <div><a href="https://docs.scipy.org/doc/scipy/reference/spatial.html">Spatial data structures and algorithms</a></div>
  <div><code>io</code></div>
  <div><a href="https://docs.scipy.org/doc/scipy/reference/io.html">Scientific data format reading and writing</a></div>
  <div><code>special</code></div>
  <div><a href="https://docs.scipy.org/doc/scipy/reference/special.html">Special functions</a></div>
  <div><code>linalg</code></div>
  <div><a href="https://docs.scipy.org/doc/scipy/reference/linalg.html">Linear algebra functionality</a></div>
  <div><code>stats</code></div>
  <div><a href="https://docs.scipy.org/doc/scipy/reference/stats.html">Statistical functions</a></div>
</div>

---

# Example: Linear regression of noisy data

<div class="grid grid-cols-[1fr_1fr] gap-4">
  <div>

```python
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x =  np.linspace(0, 10, 101)
rng = np.random.default_rng()
y = 2*x + 1 + rng.normal(0, 1, 101)

result = stats.linregress(x, y)
plt.plot(x, y, 'o')
plt.plot(x, result.slope*x + result.intercept)
plt.show()
print(f"{result.slope = :6.4f}")
print(f"{result.stderr = :6.4f}")
print(f"{result.intercept = :6.4f}")
print(f"{result.intercept_stderr = :6.4f}")
```

```console
result.slope = 2.0293
result.stderr = 0.0382
result.intercept = 0.5772
result.intercept_stderr = 0.2212
```

  </div>
  <div>
    <img src="/images/linregress.png" style="width: 90%; margin: auto">
  </div>
</div>

---

# Example: Curve fitting

<div class="grid grid-cols-[1fr_1fr] gap-4">
  <div>

```python
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

def fitfunc(x, a, b):
    return a*np.sin(x+b)

x = np.linspace(0, 10, 101)
rng = np.random.default_rng()
y = 2*np.sin(x+0.5) + rng.normal(0, 1, 101)
plt.plot(x, y, 'o')

popt, pcov = optimize.curve_fit(fitfunc, x, y)
print(f"a = {popt[0]:6.4f}, b = {popt[1]:6.4f}")
plt.plot(x, popt[0]*np.sin(x+popt[1]))
plt.show()
```

```console
a = 2.2615, b = 0.6587
```

  </div>
  <div>
    <img src="/images/curvefit.png" style="width: 90%; margin: auto">
  </div>
</div>

---

# Example: Finding eigenvalue for finite potential well

<div class="grid grid-cols-[1fr_50%] gap-4">
  <div>

```python
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

def f(energy, alpha):
    sqrt_1me = np.sqrt(1-energy)
    return (np.sqrt(energy)*np.cos(alpha*sqrt_1me)
            -sqrt_1me*np.sin(alpha*sqrt_1me))

alpha = 1
e0, r = optimize.brentq(f, a=0, b=1, args=alpha,
                        full_output=True)
print(f"{e0 = :6.4f}\n")
print(r)

x = np.linspace(0, 1, 400)
plt.plot(x, f(x, alpha))
plt.plot(e0, 0, 'o')
plt.show()
```

```console {all}{maxHeight:'100px'}
e0 = 0.4538

      converged: True
           flag: converged
 function_calls: 7
     iterations: 6
           root: 0.45375316586032827
```

  </div>
  <div>

$$\sqrt{\epsilon}\cos(\alpha\sqrt{1-\epsilon}) - 
  \sqrt{1-\epsilon}\sin(\alpha\sqrt{1-\epsilon}) = 0$$
$$\epsilon = -\frac{E}{V_0}
\qquad\alpha = \sqrt{\frac{2mV_0}{\hbar^2}}\frac{L}{2}$$

<img src="/images/brentq.png" style="width: 90%; margin: auto">

  </div>
</div>

---

# Example: Hanging chain

<div class="grid grid-cols-[30%_1fr] gap-4">
  <div>
  <img src="/images/chainlink.png" style="width: 90%; margin: auto">

  <br>

 * minimiere potentielle Energie (`f_energy`)
 * Endpunkte auf gleicher Höhe (`y_constraint`)
 * Endpunkte mit vorgegebenem horizontalem Abstand
   (`x_constraint`)

  </div>
  <div>

```python {all|13-27}{maxHeight:'450px'}
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

class Chain:
    def __init__(self, nlinks, length):
        if nlinks < length:
            raise ValueError('length requirement cannot be fulfilled with '
                             'the given number of links')
        self.nlinks = nlinks
        self.length = length

    def x_constraint(self, phi):
        return np.sum(np.cos(phi))-self.length

    def y_constraint(self, phi):
        return np.sum(np.sin(phi))

    def f_energy(self, phi):
        return np.sum(np.arange(self.nlinks, 0, -1)*np.sin(phi))

    def equilibrium(self):
        result = optimize.minimize(
                     self.f_energy, np.linspace(-0.1, 0.1, self.nlinks),
                     method='SLSQP',
                     constraints=[{'type': 'eq', 'fun': self.x_constraint},
                                  {'type': 'eq', 'fun': self.y_constraint}])
        return result.x

    def plot_equilibrium(self):
        phis = chain.equilibrium()
        x = np.zeros(chain.nlinks+1)
        x[1:] = np.cumsum(np.cos(phis))
        y = np.zeros(chain.nlinks+1)
        y[1:] = np.cumsum(np.sin(phis))
        plt.axes().set_aspect('equal')
        plt.plot(x, y)
        plt.plot(x, y, 'o')
        plt.show()

chain = Chain(6, 5)
chain.plot_equilibrium()
```

  </div>
</div>

---

# Example: Hanging chain (cont'd)

<div class="grid grid-cols-[1fr_25%] gap-4">
  <div>
<img src="/images/hanging_chain_6.png" style="width: 82%; margin-right: 0; margin-left: auto">
<br>
<img src="/images/hanging_chain_30.png" style="width: 80%; margin-right: 0; margin-left: auto">

<br>

  * im Kontinuumslimes: hyperbolischer Kosinus

  </div>
  <div>

   $n = 6$

   <br> <br> <br> <br> <br> <br>

   $n = 30$

  </div>
</div>

---

# Example: Falling chain – Equation of motion

<div></div>

[W. Tomaszewski, P. Pieranski, J.-C. Geminard, Am. J. Phys. **74**, 776 (2006)](https://doi.org/10.1119/1.2204074)

$$\sum_{j=1}^n m_{i,j}c_{i,j}\ddot{\varphi}_j = -\sum_{j=1}^n m_{i,j}s_{i,j}\dot\varphi^2_j
  + \frac{r}{m\ell^2}\left(\dot\varphi_{i-1}-2\dot\varphi_i+\dot\varphi_{i+1}\right)
  - \frac{g}{\ell}a_ic_i$$

$$c_i = \cos(\varphi_i)\qquad c_{i,j} = \cos(\varphi_i-\varphi_j)\qquad s_{i,j} = \sin(\varphi_i-\varphi_j)$$

$$a_i = n-i+\frac{1}{2}\qquad
  M_{i,j} = \begin{cases}
             n-i+\frac{1}{3} & i=j\\
             n-\max(i,j)+\frac{1}{2} & i\neq j
            \end{cases}$$

* Das Modell berücksichtigt Dämpfung an den Gelenken zwischen den Kettengliedern → Parameter $r$

---

# Example: Falling chain – Code

```python {all|32-37|39-42|44-45|47-53|55-61|63-78|94-101|117-122}{maxHeight:'450px'}
import numpy as np
import numpy.linalg as LA
from scipy import integrate, optimize
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Chain:
    def __init__(self, nlinks, length):
        if nlinks < length:
            raise ValueError('length requirement cannot be fulfilled with '
                             'the given number of links')
        self.nlinks = nlinks
        self.length = length

    def x_constraint(self, phi):
        return np.sum(np.cos(phi))-self.length

    def y_constraint(self, phi):
        return np.sum(np.sin(phi))

    def f_energy(self, phi):
        return np.sum(np.arange(self.nlinks, 0, -1)*np.sin(phi))

    def equilibrium(self):
        result = optimize.minimize(
                     self.f_energy, np.linspace(-0.1, 0.1, self.nlinks),
                     method='SLSQP',
                     constraints=[{'type': 'eq', 'fun': self.x_constraint},
                                  {'type': 'eq', 'fun': self.y_constraint}])
        return result.x

class FallingChain(Chain):
    def __init__(self, nlinks, length, damping):
        super(FallingChain, self).__init__(nlinks, length)
        self.set_matrix_m()
        self.set_vector_a()
        self.set_matrix_damping(damping)
        
    def set_matrix_m(self):
        m = np.fromfunction(lambda i, j: self.nlinks-np.maximum(i, j)-0.5,
                            (self.nlinks, self.nlinks))
        self.m = m-np.identity(self.nlinks)/6

    def set_vector_a(self):
        self.a = np.arange(self.nlinks, 0, -1)-0.5
    
    def set_matrix_damping(self, damping):
        self.damping = (-2*np.identity(self.nlinks, dtype=np.float64)
                        + np.eye(self.nlinks, k=1)
                        + np.eye(self.nlinks, k=-1))
        self.damping[0, 0] = -1
        self.damping[self.nlinks-1, self.nlinks-1] = -1
        self.damping = damping*self.damping

    def solve_eq_of_motion(self, time_i, time_f, nt):
        y0 = np.zeros(2*self.nlinks, dtype=np.float64)
        y0[self.nlinks:] = self.equilibrium()
        self.solution = integrate.solve_ivp(
                            self.diff, (time_i, time_f), y0,
                            method='RK45',
                            t_eval=np.linspace(time_i, time_f, nt))

    def diff(self, t, y):
        momenta = y[:self.nlinks]
        angles = y[self.nlinks:]
        d_angles = momenta
        ci = np.cos(angles)
        cij = np.cos(angles[:, np.newaxis]-angles)
        sij = np.sin(angles[:, np.newaxis]-angles)
        mcinv = LA.inv(self.m*cij)
        d_momenta = -np.dot(self.m*sij, momenta*momenta)
        d_momenta = d_momenta + np.dot(self.damping, momenta)
        d_momenta = d_momenta - self.a*ci
        d_momenta = np.dot(mcinv, d_momenta)
        d = np.empty_like(y)
        d[:self.nlinks] = d_momenta
        d[self.nlinks:] = d_angles
        return d

def angles_to_coords(phi):
    """convert angles to coordinates of link endpoints
        
       phi: angles of links with respect to the horizontal
       x, y: coordinates of link endpoints
           
    """
    dim = phi.shape[0]+1
    x = np.zeros(dim)
    x[1:] = np.cumsum(np.cos(phi))
    y = np.zeros(dim)
    y[1:] = np.cumsum(np.sin(phi))
    return x, y

def animate(i):
    x, y = angles_to_coords(c.solution.y[:, i][c.nlinks:])
    line.set_data(x, y)
    return line,

def init():
    line.set_data([], [])
    return line,

nlinks = 50
length = 40
damping = 1
ti = 0
tf = 200
tsteps = 1000

c = FallingChain(nlinks, length, damping)
c.solve_eq_of_motion(ti, tf, tsteps)
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False,
                     xlim=(-nlinks, nlinks), ylim=(-nlinks, 0.3*nlinks))
ax.set_aspect('equal')
line, = ax.plot([], [])
anim = animation.FuncAnimation(fig, animate, tsteps,
                               interval=20, blit=True,
                               init_func=init)

FFwriter = animation.FFMpegWriter(fps=30)
anim.save('falling_chain.mp4', writer = FFwriter)
```

---

# Example: Falling chain – Results

<video width="560" height="420" controls style="margin: auto;">
  <source src="/movies/falling_chain.mp4" type="video/mp4">
</video>
