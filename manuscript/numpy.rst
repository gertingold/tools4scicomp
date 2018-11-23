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




.. [#numpy] For details see the `NumPy Reference <https://docs.scipy.org/doc/numpy/reference/>`_.
.. [#scipy] For details see the `SciPy API Reference <https://docs.scipy.org/doc/scipy/reference#api-reference>`_.
.. [#matplotlib] See the `matplotlib gallery <https://matplotlib.org/gallery/index.html>`_ to
            obtain an idea of the possibilities offered by matplotlib.
.. [#jupyter] For details see the `homepage of the Jupyter project <https://jupyter.org/>`_.
.. [#pandas] For details see the `pandas homepage <https://pandas.pydata.org/>`_.
.. [#sympy] For details see the `sympy homepage <https://www.sympy.org/>`_.
.. [#skimage] For details see the `scikit-image homepage <https://scikit-image.org>`_.
.. [#sklearn] For details see the `scikit-learn homepage <https://https://scikit-learn.org>`_.
