*****************************************
Scientific computing with NumPy and SciPy
*****************************************

Python scientific ecosystem
===========================

Python comes with a rich variety of freely available third-party packages
including quite a number of packages which are routinely used in scientific
computing. Before developing code for a standard problem like an eigenvalue
analysis or numerical quadrature to name just two examples, it is recommended
to first check the functionality provided by the existing libraries. It is
very likely that such libraries are more reliable and more efficient than
self-developed code. This does not mean though that such libraries are guaranteed
to be error-free and there may exist reasons to develop even basic numerical
code oneself.

NumPy [#numpy]_ constitutes the basis of the Python scientific ecosystem. The
multi-dimensional array datatype defined in NumPy is pivotal for a huge number
of scientific applications and is made use of in many ways in the other two
core packages SciPy and matplotlib. SciPy provides submodules in many areas
relevant for scientific applications like optimization, signal processing,
linear algebra, statistics, special functions and several more [#scipy]_. Part
of the code is written in C or Fortran resulting in fast execution speed.
Matplotlib offers comprehensive support for graphical presentation of data
[#matplotlib]_.

In recent year, the Jupyter notebook, formerly known as IPython notebook, has
become very popular, in particular among the data scientists [#jupyter]_. The
notebook can be used with Python and a number of other programming languages
like Julia and R and allows to integrate code, text as well as images and
other media in a single file.

In addition, there are a number of more dedicated packages of which we will
name a few. The Python data analysis library pandas [#pandas]_ offers high-performance,
easy-to-use data structures and data analysis tools. Symbolic computation is
possible in Python with the help of the sympy package [#sympy]_. Image-processing
routines can be found in scikit-image [#skimage]_. Among the many features of this
package, we mention image segmentation which can for example be used to analyse
electron microscope images of heterogeneous surfaces. Machine learning has recently
developed into a very active field which receives excellent support in Python
through the scikit-learn package [#sklearn]_.

We emphasize that the list of packages briefly described here, is not exhaustive
and there exist more interesting Python packages useful in scientific applications.
A recommended source of information on the Python scientific ecosystem are the
`Scipy lecture notes <https://www.scipy-lectures.org/>`_.

NumPy
=====

Python lists and matrices
-------------------------

It is rather typical in scientific applications to deal with homogeneous data,
i.e. data of the same datatype, organized in arrays. An obvious example for
one-dimensional arrays are vectors in their coordinate representation and
matrices would naturally be stored in two-dimensional arrays. There also exist
applications for even higher-dimensional arrays. The data representing a
digital colour image composed of :math:`N\times M` pixels can be stored in an
:math:`N\times M\times 3` array with three planes representing the three colour
channels red, green, and blue as visualized in :numref:`rgbarray`. 

.. _rgbarray:
.. figure:: img/rgbarray.*
   :width: 15em
   :align: center

   The data of a digital colour image composed of :math:`N\times M` pixels can be
   represented as a :math:`N\times M\times 3` array where the three planes correspond
   to the red, green, and blue channels.

The first question to address is how one can store such data structures in Python and
how can one make sure that the data can be processed fast. Among the standard datatypes
available in Python, a natural candidate would be lists. In Python, lists are very
flexible objects which allow to store element of all kinds of datatypes including lists.
While this offers us in principle the possibility to represent multi-dimensional data,
the flexibility comes with a significant computational overhead. As we will see later,
homogeneous data can be handled more efficiently. Leaving the question of efficiency
aside for a moment, we can ask whether list are suited at all to represent matrices.

Let us consider a two-dimensional matrix

.. math::

   \mathsf{M} = \begin{pmatrix} 1.1 & 2.2 & 3.3\\ 4.4 & 5.5 & 6.6\\ 7.7 & 8.8 & 9.9\end{pmatrix}\,.

It seems natural to store these data in a list of lists

.. sourcecode:: python

   >>> matrix = [[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]]

of which a single element can be accessed by first selecting the appropriate row and then
the desired entry

.. sourcecode:: python

   >>> matrix[0]
   [1.1, 2.2, 3.3]
   >>> matrix[0][2]
   3.3

The only difference with respect to the common mathematical notation is that the indices start
at 0 and not at 1. In order to access a single row in a way which makes the two-dimensional
character of the matrix more transparent, we could use

.. sourcecode:: python

   >>> matrix[0][:]
   [1.1, 2.2, 3.3]

But does this also work for a column? Let us give it a try.

.. sourcecode:: python

   >>> matrix[:][0]
   [1.1, 2.2, 3.3]
   >>> matrix[:]
   [[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]]

The result is rather disappointing because interchanging the two slices yields again the
first row. The reason can be seen from the lower two lines. In the first step, we obtain
again the full list and in the second step we access its first element, i.e. the first
row, not the first column. Even though there are ways to extract a column from a list of
lists, e.g. by means of a list comprehension, there is now consistent approach to extracting
rows and columns from a list of lists. Our construction is certainly not a good one and
we are in need of a new datatype.

NumPy arrays
------------

The new datatype provided by NumPy is a multidimensional homogeneous array of fixed-size
items called ``ndarray``. Before starting to explore this datatype, we need to import
the NumPy package. While there are different ways to do so, there is one recommended way.
Let us take a look at the various alternatives::

   from numpy import *                # don't do this!
   from numpy import array, sin, cos  # not recommended
   import numpy                       # ok, but the following line is better
   import numpy as np                 # recommended way

Importing the complete namespace of NumPy as done in the first line is no good idea because
the namespace is rather large. Therefore, there is a danger of name conflicts and loss of
control. As an alternative, one could restrict the import to the functions actually needed
as shown in the second line. However, as can be seen in our example, there exist functions
like sine (``sin``) and cosine (``cos``) in NumPy. In the body of the code it might not always
be evident whether these functions are taken from NumPy or rather the ``math`` or ``cmath``
module. It is better to more explicit. The import given in the third line is acceptable but
it requires to put ``numpy.`` in front of each object taken from the NumPy namespace.
The usual way to import NumPy is given in the fourth line. Virtually every user seeing ``np.``
in the code will assume that the corresponding object belongs to NumPy. It is always a
good idea to stick to such conventions to render the code easily understandable.

As the next step, we need to create an array and fill it with data. Whenever we
are simply referring to an array, we actually mean an object of datatype
``ndarray``. Given certain similarities with Python lists, it is tempting to
use the ``append`` method for that purpose as one often does with lists. In
fact, NumPy provides an ``append`` method. However, because Python lists and
NumPy arrays are conceptually quite different, there exist good reasons for
avoiding this method if at all possible.

The objects contained in a Python list are typically scattered in memory and the
position of each chunk of data is stored in a list of pointers. In contrast, the
data of a NumPy array are stored in one contiguous piece of memory. As we will
see later, this way of storing an array allows to determine by means of a simple
calculation where a certain element can be found. Accessing elements therefore is
very efficient. 

When appending data to an array, there will generally be no place for the data
in memory to guarantee the array to remain contiguous. Appending data in NumPy
thus implies the creation of an entirely new array. As a consequence, the data
constituting the original array have to be moved to a new place in memory. The
time required for this process can become significant for larger arrays and
ultimately is limited by the hardware. Using the ``append`` method can thus
become a serious performance problem.

Generally, when working with NumPy arrays, it is a good idea to avoid the creation
of new arrays as much as possible as this may drastically degrade performance.
In particular, one should not count on changing the size of an array during the
calculation. Already for the creation of the array one should decide how large
it will need to be.

One way to find out how a NumPy array can be created it to search the NumPy documentation.
This can be done even within Python::

   >>> np.lookfor('create array')
   Search results for 'create array'
   ---------------------------------
   numpy.array
       Create an array.
   numpy.memmap
       Create a memory-map to an array stored in a *binary* file on disk.
   numpy.diagflat
       Create a two-dimensional array with the flattened input as a diagonal.
   numpy.fromiter
       Create a new 1-dimensional array from an iterable object.
   numpy.partition
       Return a partitioned copy of an array.

Here, we have only have reproduced a small part of the output. Furthermore, here and
in the following, we assume that NumPy has been imported in the way recommended above
so that its namespace can be accessed via the abbreviation ``np``.

Already the first entry in the list of proposed methods is the one to use in our
present situation. More information can be obtained as usual by means of ``help(np.array)``
or alternatively by ::

   >>> np.info(np.array)
   array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)

   Create an array.

   Parameters
   ----------
   object : array_like
       An array, any object exposing the array interface, an object whose
       __array__ method returns an array, or any (nested) sequence.
   dtype : data-type, optional
       The desired data-type for the array.  If not given, then the type will
       be determined as the minimum type required to hold the objects in the
       sequence.  This argument can only be used to 'upcast' the array.  For
       downcasting, use the .astype(t) method.

Again, only the first part of the output has been reproduced. It is recommended
though to take a look at the rest of the help text as it provides a nice example
how doctests can be used both for documentation purposes and for testing.

As can be seen from the help text, we need at least one argument ``object`` which
should be an object with an ``__array__`` method or a possibly nested sequence.
Let us consider a first example::

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

We have started with a list of lists which is a valid argument for ``np.array``.
Printing out the result indicates indeed that we have obtained a NumPy array.
A confirmation is obtained by asking for the type of ``myarray``.

The data of an array are stored contiguously in memory but what does that really
mean for the two-dimensional array which we have just created? Natural ways would
be store the date columnwise or rowwise. The first variant is realized in the
programming language C while the second variant is used by Fortran. Apart from
the actual data, an array obviously needs a number of metadata in order to know
how to interpret the content of the memory space attributed to the area. These
metadata are a powerful concept because they make it possible to change the
interpretation of the data without copying them, thereby contributing to the
efficiency of Numpy arrays.

It is useful to get some basic insight into how a Numpy array works. In order
to analyze the metadata, we use a short function enabling us to list the 
attributes of an array.

.. code-block:: python

   def array_attributes(a):
       for attr in ('ndim', 'size', 'itemsize', 'dtype', 'shape', 'strides'):
           print(f'{attr:8s}: {getattr(a, attr)}')

A convenient way of generating an array for test purposes is the ``arange`` function
which works very much like the standard ``range`` iterator as far as its basic
arguments ``start``, ``stop``, and ``step`` are concerned. In this way, we can
easily construct a one-dimensional array with integer entries from 0 to 15 and
inspect its properties::

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

Let us take a look at the different attributes. The attribute ``ndim`` indicates
the number of dimension of the array which in our example is one-dimensional and
therefore ``ndim`` equals 1. The ``size`` of 16 means that the array contains a
total of 16 items. Each item has an ``itemsize`` of 8 bytes or 64 bits, resulting
in a total size of 128 bytes::

   >>> matrix.nbytes
   128

The attribute ``dtype`` represents the datatype which in our example is ``int64``,
i.e. an integer type of a length of 64 bits. Quite in contrast to the usual integer
type in Python which can in principle handle integers of arbitrary size, the integer
values in our array are clearly limited. An example using integers of only 8 bits
length can serve to illustrate the problem of overflows::

   >>> np.arange(1, 160, 10, dtype=np.int8)
   array([   1,   11,   21,   31,   41,   51,   61,   71,   81,   91,  101,
           111,  121, -125, -115, -105], dtype=int8)

Take a look at the items in this array and try to understand what is going on.

   >>> for k, v in np.core.numerictypes.sctypes.items():
   ...     print(k)
   ...     for elem in v:
   ...         print(f'    {elem}')
   ... 
   int
       <class 'numpy.int8'>
       <class 'numpy.int16'>
       <class 'numpy.int32'>
       <class 'numpy.int64'>
   uint
       <class 'numpy.uint8'>
       <class 'numpy.uint16'>
       <class 'numpy.uint32'>
       <class 'numpy.uint64'>
   float
       <class 'numpy.float16'>
       <class 'numpy.float32'>
       <class 'numpy.float64'>
       <class 'numpy.float128'>
   complex
       <class 'numpy.complex64'>
       <class 'numpy.complex128'>
       <class 'numpy.complex256'>
   others
       <class 'bool'>
       <class 'object'>
       <class 'bytes'>
       <class 'str'>
       <class 'numpy.void'>

The first four groups of datatypes include integers, unsigned integers, floats and
complex numbers of different sizes. Among the other types, booleans as well as strings
are of some interest. Note, however, that the data in an array always should be homogeneous.
If different datatypes are mixed in the assignment to an array, it may happen that a datatype
is cast to a more flexible one. For strings, the size of each entry will be determined by
the longest string.

Probably the most interesting attributes of an array are ``shape`` and ``strides`` because
the allow us to reinterprete the data of the original one-dimensional array in different
ways without the need to copy from memory to memory. Let us first try to understand the meaning
of the tuples ``(16,)`` for ``shape`` and ``(8,)`` for ``strides``. Both tuples have the same
size which equals one because the considered array is one-dimensional. Therefore, ``shape`` does
not contain any new information. It simply reflects the size of the array as does the attribute
``size``. The value of ``strides`` means that in order to move from the beginning of an item
in memory to the beginning of the next one, one needs to more eight bytes. This information
is consistent with the ``itemsize``. What seems like redundant information becomes more
interesting when we go from a one-dimensional array to a multi-dimensional array. For simplicity
we convert the our one-dimensional array ``matrix`` into a two-dimensional square array.
To this purpose we make use of the ``reshape`` method::

   >>> matrix = matrix.reshape(4, 4)
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

In the first line, we bring our one-dimensional array with 16 elements into a
:math:`4\times4` array.  Three attributes change their value in this process.
``ndim`` is now 2 because we created a two-dimensional array. The ``shape`` attribute
with value ``(4, 4)`` reflects the fact that now we have 4 rows and 4 columns.
Finally, the ``strides`` are given by the tuple ``(32, 8)``. To go in memory from
an item to the item in the next column and in the same row means that we should move
by 8 bytes. The two items are neighbors in memory. However, if we stay within the
same column and want to move to the next row, we have to jump by 32 bytes in memory.

To further illustrate the meaning of ``shape`` and ``strides`` we consider a second
example. A linear arangement of six data in memory can be interpreted in three
different ways as depicted in :numref:`strides`. In the uppermost example, ``strides``
is set to ``(8,)``. The tuple ``strides`` tuple contains only one element and we
are therefore dealing with a one-dimensional array. Assuming the datasize to be 8,
the array consists of all six data elements. In the second case, ``strides`` are
set to ``(24, 8)``. Accordingly, the matrix consists of two rows and three columns.
Finally, in the bottom example with ``strides`` equal to ``(16, 8)``, the data
are interpreted as a matrix consisting of two columns and three rows. Note that
no rearrangement of data in memory is required in order to go from one matrix
to another one. Only the way, how the position of a certain element in memory
is obtained, changes when ``strides`` is modified. 

.. _strides:
.. figure:: img/strides.*
   :width: 12cm
   :align: center

   Linear data in memory can be interpreted in different ways by appropriately
   choosing the ``strides`` tuple.

A two-dimensional matrix can easily be transposed. Behind the scenes the values
in the ``strides`` tuple are interchanged::

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

Strides are a powerful concept. However, one should be careful not to violate
the boundaries of the data because otherwise memory might be interpreted in a
meaningless way. In the following two examples, the first demonstrates an
interesting way to create a special pattern of data. The second example, where
one of the strides is only half of the datasize, shows how useless results
can be produced::

   >>> a = np.arange(16).reshape(4, 4)
   >>> a
   array([[ 0,  1,  2,  3],
          [ 4,  5,  6,  7],
          [ 8,  9, 10, 11],
          [12, 13, 14, 15]])
   >>> a.strides = (8, 8)
   >>> a
   array([[0, 1, 2, 3],
          [1, 2, 3, 4],
          [2, 3, 4, 5],
          [3, 4, 5, 6]])
   >>> a.strides = (8, 4)
   >>> a
   array([[          0,  4294967296,           1,  8589934592],
          [          1,  8589934592,           2, 12884901888],
          [          2, 12884901888,           3, 17179869184],
          [          3, 17179869184,           4, 21474836480]])

In the end, the user manipulating ``strides`` is responsible for all consequences
which his or her action may have.

Creating arrays
---------------

We have seen in the previous section that an array can be created by providing ``np.array`` 
with an object possessing an ``__array__`` method or a nested sequence. However, this
requires to create the object or nested sequence in the first place. Often, more convenient
methods exist. As we have pointed out earlier, when creating an array, one should have an
idea of the desired size and usually also of the datatype to be stored in the array. Given
this information, there exists a variety of methods to create an array depending on the
specific needs.

It is not unusual to start with an array filled with zeros. Let us create a :math:`2\times2` array::

   >>> a = np.zeros((2, 2))
   >>> a
   array([[0., 0.],
          [0., 0.]])
   >>> a.dtype
   dtype('float64')  

As we can see, the default type is ``float64``. If we prefer an array of integers, we could specify
the ``dtype``::

   >>> a = np.zeros((2, 2), dtype=np.int)
   >>> a
   array([[0, 0],
          [0, 0]])
   >>> a.dtype
   dtype('int64')

As an alternative, one can create an empty array which should however not be confused with an array
filled with zeros. An empty array will just claim the necessary amount of memory without doing anything
to the data present in that piece of memory. This is fine if one is going to specify the content of all
array data subsequently before using the array. Otherwise, one will deal with random data::

   >>> np.empty((3, 3))
   array([[6.94870988e-310, 6.94870988e-310, 7.89614591e+150],
          [1.37038197e-013, 2.08399685e+064, 3.51988759e+016],
          [8.23900250e+015, 7.32845376e+025, 1.71130458e+059]])

An alternative to filling an array with zeros could be to fill it with ones or another value which
can be obtained by multiplication::

   >>> np.ones((2, 2))
   array([[1., 1.],
          [1., 1.]])
   >>> 10*np.ones((2, 2))
   array([[10., 10.],
          [10., 10.]])

As one can see in this example, the multiplication by a number acts on all elements of the array.
This behavior is probably what one would expect at this point. We will see later, that we are
making use at this point of a more general concept referred to as broadcasting.

Often, one needs arrays with more structure than the one we have created so far. It is not uncommon,
that the diagonal entries take a special form. An identity matrix can easily be created::

   >>> np.identity(3)
   array([[1., 0., 0.],
          [0., 1., 0.],
          [0., 0., 1.]])

The result will always be a square matrix. A more general method to fill the diagonal or a shifted
diagonal is provided by ``np.eye``::

   >>> np.eye(2, 4)
   array([[1., 0., 0., 0.],                                                                     
          [0., 1., 0., 0.]])                                                                    
   >>> np.eye(4, k=1)                                                                           
   array([[0., 1., 0., 0.],                                                                     
          [0., 0., 1., 0.],                                                                     
          [0., 0., 0., 1.],                                                                     
          [0., 0., 0., 0.]])                                                                    
   >>> 2*np.eye(4)-np.eye(4, k=1)-np.eye(4, k=-1)                                              
   array([[ 2., -1.,  0.,  0.],                                                                 
          [-1.,  2., -1.,  0.],                                                                 
          [ 0., -1.,  2., -1.],                                                                 
          [ 0.,  0., -1.,  2.]])

These examples show that ``np.eye`` does not expect a tuple specifying the shape. Instead, the
first two arguments give the number of rows and columns. If the second argument is absent,
the resulting matrix is a square matrix. In the second and third example, the missing second
argument is the reason why we have to specify that the second argument is intended as the
shift ``k`` of the diagonal. The third example gives an idea of how the Hamiltonian for the
kinetic energy in a tight-binding model can be constructed.

It is also possible to generate diagonals or, by specifying ``k``, shifted diagonals with
different values::

   >>> np.diag([1, 2, 3, 4])
   array([[1, 0, 0, 0],
          [0, 2, 0, 0],
          [0, 0, 3, 0],
          [0, 0, 0, 4]])

Using a two-dimensional array as argument, its diagonal elements can be extracted by means
of the same function::

   >>> matrix = np.arange(16).reshape(4, 4)
   >>> matrix
   array([[ 0,  1,  2,  3],
          [ 4,  5,  6,  7],
          [ 8,  9, 10, 11],
          [12, 13, 14, 15]])
   >>> np.diag(matrix)
   array([ 0,  5, 10, 15])

If the elements of an array can be expressed as a function of the indices, ``fromfunction``
can be used to generate the elements. As a simple example, we create a multiplication table::

   >>> np.fromfunction(lambda i, j: (i+1)*(j+1), shape=(6, 6), dtype=np.int)
   array([[ 1,  2,  3,  4,  5,  6],
          [ 2,  4,  6,  8, 10, 12],
          [ 3,  6,  9, 12, 15, 18],
          [ 4,  8, 12, 16, 20, 24],
          [ 5, 10, 15, 20, 25, 30],
          [ 6, 12, 18, 24, 30, 36]])

Even though we present a two-dimensional example, the latter approach can be used
to create arrays of an arbitrary dimension.

The function used in the previous example was a very simple one. Occasionally, one might
need more complicated functions like one of the trigonometric functions. In fact, NumPy
provides a number of so-called universal functions which we will discuss in :numref:`ufuncs`.
Such functions accept an array as argument and return an array. Here, we will concentrate
on creating arguments for universal functions.

A first function is ``arange`` which we have used before for integers. It is a generalization
of the standard ``range`` which works even for floats::

   >>> np.arange(1, 2, 0.1)
   array([1. , 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9])

As with ``range``, the first argument is the start value while the second argument refers
to the final value which is not included. Because of rounding errors, the last statement
is not always true. Finally, the third argument is the stepwidth. An alternative is offered
by the ``linspace`` function which by default will make sure that the start value and the
final value are part of the array. Instead of the stepwidth, the number of points is specified::

   >>> np.linspace(1, 2, 11)
   array([1. , 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2. ])

A common mistake is to assume that the last argument gives the number of intervalls which,
however, is not the case. Thus, there is some danger that one is off by one in the last
argument. Sometimes it is useful to ask for the stepwidth::

   >>> np.linspace(1, 4, 7, retstep=True)
   (array([1. , 1.5, 2. , 2.5, 3. , 3.5, 4. ]), 0.5)

Here, the stepwidth does not need to be determined by hand.

Occasionally, a logarithmic scale can be useful. In this case, the start value and the final
value refer to the exponent. The base by default is ten but can be modified, if necessary::

   >>> np.logspace(0, 3, 4)
   array([   1.,   10.,  100., 1000.])
   >>> np.logspace(0, 2, 5, base=2)
   array([1.        , 1.41421356, 2.        , 2.82842712, 4.        ])

The following example illustrate the application of ``linspace`` in a universal function
to produce a graphical representation of the function::

   >>> import matplotlib.pyplot as plt
   >>> x = np.linspace(0, 2*np.pi, 100)
   >>> y = np.sin(x)
   >>> plt.plot(x, y)
   [<matplotlib.lines.Line2D object at 0x7f22d619cc88>]

The generated graph is reproduced in :numref:`mpl_numpy_1`.

.. _mpl_numpy_1:
.. figure:: img/mpl_numpy_1.*
   :width: 20em
   :align: center

   Simple example of a function graph generated by operating with a universal function
   on an array generated by ``linspace``.

Arrays can also be filled with data taken from a file. This can for example be the case
if data obtained from a measurement are first stored in a file before being processed
or if numerical data are stored before a graphical representation is produced. Assume
that we have a data file called ``mydata.dat`` with the following content::

   # time position
      0.0   0.0
      0.1   0.1
      0.2   0.4
      0.3   0.9

Loading the data from the file, we obtain::

   >>> np.loadtxt('mydata.dat')
   array([[0. , 0. ],
          [0.1, 0.1],
          [0.2, 0.4],
          [0.3, 0.9]])

By default, lines starting with ``#`` will be considered as comments and are ignored.
The function ``loadtxt`` offers a number of arguments to load data in a rather flexible
way. Even more possibilities are offered by ``genfromtxt`` which is also able to deal with
missing values. See the documentation of `loadtxt <https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html#numpy.loadtxt>`_ and `genfromtxt <https://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt>`_ for more information.

In numerical simulations, it is often necessary to generate random numbers and if many
of them are needed, it may be efficient to generate an array filled with random numbers.
While NumPy offers many different distributions of random numbers, we concentrate on
equally distributed random numbers in an interval from 0 to 1. An array of a given shape
filled with such random numbers can be obtained as follows::

   >>> np.random.rand(2, 5)
   array([[0.76455979, 0.09264023, 0.47090143, 0.81327348, 0.42954314],
          [0.37729755, 0.20315983, 0.62982297, 0.0925838 , 0.37648008]])
   >>> np.random.rand(2, 5)
   array([[0.23714395, 0.22286043, 0.97736324, 0.19221663, 0.18420108],
          [0.14151036, 0.07817544, 0.4896872 , 0.90010128, 0.21834491]])

Clearly, the set of random numbers changes at each call to ``random.rand``. Occasionally,
one would like to have reproducible random numbers, for example during unit tests or to
reproduce a particularly interesting scenario in a simulation. Then one can set a seed::

   >>> np.random.seed(123456)
   >>> np.random.rand(2, 5)
   array([[0.12696983, 0.96671784, 0.26047601, 0.89723652, 0.37674972],
          [0.33622174, 0.45137647, 0.84025508, 0.12310214, 0.5430262 ]])
   >>> np.random.seed(123456)
   >>> np.random.rand(2, 5)
   array([[0.12696983, 0.96671784, 0.26047601, 0.89723652, 0.37674972],
          [0.33622174, 0.45137647, 0.84025508, 0.12310214, 0.5430262 ]])

Sometimes, it is convenient to graphically represent the matrix elements. :numref:`mpl_numpy_2`
shows an example generated by the following code::

   >>> import matplotlib.pyplot as plt
   >>> np.random.seed(42)
   >>> data = np.random.rand(20, 20)
   >>> plt.imshow(data, cmap=plt.cm.hot, interpolation='none')
   <matplotlib.image.AxesImage object at 0x7f39027afe48>
   >>> plt.colorbar()
   <matplotlib.colorbar.Colorbar object at 0x7f39027e58d0>
   >>> plt.show()

Not that the argument ``interpolation`` of ``plt.imshow`` is set to ``'none'`` to ensure
that no interpolation is done which might blur the image.

.. _mpl_numpy_2:
.. figure:: img/mpl_numpy_2.*
   :width: 20em
   :align: center

   Graphical representation of an array filled with random numbers.


Indexing arrays
---------------

One way of accessing sets of elements of an array makes use of slices which we know
from Python lists. A slice is characterized by a ``start`` index, a ``stop`` index
whose corresponding element is excluded, and ``step`` which indicates the stepsize.
Negative indices are counted from the end of the corresponding array dimension and
a negative value of ``step`` implies walking in the direction of decreasing indices.

We start by a few examples of slicing for a one-dimensional array::

   >>> a = np.arange(10)
   >>> a
   array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
   >>> a[:]
   array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
   >>> a[1:4]
   array([1, 2, 3])
   >>> a[5:-2]
   array([5, 6, 7])
   >>> a[::2]
   array([0, 2, 4, 6, 8])
   >>> a[1::2]
   array([1, 3, 5, 7, 9])
   >>> a[::-1]
   array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

The third input, i.e. ``a[:]`` leaves the ``start`` and ``stop`` values open so
that all array elements are returned because by default ``step`` equals 1. In
the next example, we recall that indices in an array as in a list start at 0.
Therefore, we obtain the second up to the fourth element of the array. In the
fifth input, the second element counted from the end of the array is not part
of the result so that we obtain the numbers from 5 to 7. We could have used
``a[5:8]`` instead. In the sixth input, ``start`` and ``stop`` values are again
left open, so that the resulting array starts with 0 but then proceeds in steps
of 2 according to the value of ``step`` given. In the following example,
``start`` is set to 1 and we obtain the elements left out in the previous
example. The last example inverts the sequence of array elements by specifying
a ``step`` of -1.

It is rather straightforward to extend the concept of slicing to higher
dimensions and we again go through a number of examples to illustrate the
idea. Note that in no case a new array is created in memory so that slicing
is an efficient way of extracting a certain subset of array elements. Our
base array is::

   >>> a = np.arange(36).reshape(6, 6)
   >>> a
   array([[ 0,  1,  2,  3,  4,  5],
          [ 6,  7,  8,  9, 10, 11],
          [12, 13, 14, 15, 16, 17],
          [18, 19, 20, 21, 22, 23],
          [24, 25, 26, 27, 28, 29],
          [30, 31, 32, 33, 34, 35]])

In view of the two dimensions, we now need two slices separated by a comma,
the first one for the rows and the second one for the columns. The full
array is thus recovered by::

   >>> a[:, :]
   array([[ 0,  1,  2,  3,  4,  5],
          [ 6,  7,  8,  9, 10, 11],
          [12, 13, 14, 15, 16, 17],
          [18, 19, 20, 21, 22, 23],
          [24, 25, 26, 27, 28, 29],
          [30, 31, 32, 33, 34, 35]])

A sub-block can be extracted as follows::

   >>> a[2:4, 3:6]
   array([[15, 16, 17],
          [21, 22, 23]])

As already mentioned, the first slice pertains to the rows, so that we
choose elements from the third and fourth row. The second slice refers
to columns four to six so that we indeed end up with the output reproduced
above.

Sub-blocks do not need to be contiguous. We can even choose different
values for ``step`` in different dimensions::

   >>> a[::2, ::3]
   array([[ 0,  3],
          [12, 15],
          [24, 27]])

In this example, we have selected every second row and every third column.
If we want to start with the third row, we could write::

   >>> a[2::2, ::3]
   array([[12, 15],
          [24, 27]]) 

The following example illustrates a case where only one slice is specified::

   >>> a[2:4]
   array([[12, 13, 14, 15, 16, 17],
          [18, 19, 20, 21, 22, 23]])

The first slice still applies to the row and the missing second slice is replaced
by default by ``::`` representing all columns.

.. _ufuncs:

Universal functions
-------------------

Broadcasting
------------

.. [#numpy] For details see the `NumPy Reference <https://docs.scipy.org/doc/numpy/reference/>`_.
.. [#scipy] For details see the `SciPy API Reference <https://docs.scipy.org/doc/scipy/reference#api-reference>`_.
.. [#matplotlib] See the `matplotlib gallery <https://matplotlib.org/gallery/index.html>`_ to
            obtain an idea of the possibilities offered by matplotlib.
.. [#jupyter] For details see the `homepage of the Jupyter project <https://jupyter.org/>`_.
.. [#pandas] For details see the `pandas homepage <https://pandas.pydata.org/>`_.
.. [#sympy] For details see the `sympy homepage <https://www.sympy.org/>`_.
.. [#skimage] For details see the `scikit-image homepage <https://scikit-image.org>`_.
.. [#sklearn] For details see the `scikit-learn homepage <https://https://scikit-learn.org>`_.
