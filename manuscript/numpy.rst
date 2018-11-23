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

The first question to address is how one can stroe such data structures in Python and
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




.. [#numpy] For details see the `NumPy Reference <https://docs.scipy.org/doc/numpy/reference/>`_.
.. [#scipy] For details see the `SciPy API Reference <https://docs.scipy.org/doc/scipy/reference#api-reference>`_.
.. [#matplotlib] See the `matplotlib gallery <https://matplotlib.org/gallery/index.html>`_ to
            obtain an idea of the possibilities offered by matplotlib.
.. [#jupyter] For details see the `homepage of the Jupyter project <https://jupyter.org/>`_.
.. [#pandas] For details see the `pandas homepage <https://pandas.pydata.org/>`_.
.. [#sympy] For details see the `sympy homepage <https://www.sympy.org/>`_.
.. [#skimage] For details see the `scikit-image homepage <https://scikit-image.org>`_.
.. [#sklearn] For details see the `scikit-learn homepage <https://https://scikit-learn.org>`_.
