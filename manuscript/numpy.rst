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
Confirmation is obtained by asking for the type of ``myarray``.







.. [#numpy] For details see the `NumPy Reference <https://docs.scipy.org/doc/numpy/reference/>`_.
.. [#scipy] For details see the `SciPy API Reference <https://docs.scipy.org/doc/scipy/reference#api-reference>`_.
.. [#matplotlib] See the `matplotlib gallery <https://matplotlib.org/gallery/index.html>`_ to
            obtain an idea of the possibilities offered by matplotlib.
.. [#jupyter] For details see the `homepage of the Jupyter project <https://jupyter.org/>`_.
.. [#pandas] For details see the `pandas homepage <https://pandas.pydata.org/>`_.
.. [#sympy] For details see the `sympy homepage <https://www.sympy.org/>`_.
.. [#skimage] For details see the `scikit-image homepage <https://scikit-image.org>`_.
.. [#sklearn] For details see the `scikit-learn homepage <https://https://scikit-learn.org>`_.
