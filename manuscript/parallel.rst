.. _parallel_computing:

*****************************
Aspects of parallel computing
*****************************

Today even consumer computers are sold with multi-core processors which allow to
run programs truely in parallel. In numerical calculations, algorithms can often
be parallelized so that the execution time can be reduced by running the code on
several compute cores. A program could thus profit from the use of several cores
within a single processor or from a potentially large number of cores in a
computer cluster accomodating a large number of processors.

Parallel execution of a program can result in problems if the individual
computations are not well synchronized among each other. The final result might
then depend on how fast each of the computations is carried out. Such racing
conditions may lead to problems which are sometimes difficult to debug. CPython,
the most popular implementation of Python, therefore implements the so-called
*Global Interpreter Lock* (GIL) which prevents actual parallel execution within
a single Python process. This aspect will be discussed further in the following
section.

Despite the GIL, parallel processing is possible in Python if several processes
is started. In :numref:`parallel_computing_in_python`, we will demonstrate how
this can be done by considering the calculation of the Mandelbrot set as an
example. This problem is particularly simple because it allows to decompose the
full problem into smaller problems without requiring any exchange of data
between them. This kind of problems is referred to as *embarrassingly parallel*.
Here, we will restrict ourselves to this type of problems. The communication
between processes running in parallel raises a number of difficulties which
are beyond the scope of the present lecture notes. Readers interested more 
deeply in this topic might want to read more on the *message passing interface*
(MPI) and take a look at the ``mpi4py`` package.

In the last section of this chapter, we will address the possibilities offered
by Numba, a sco-called *Just in Time Compiler* (JIT Compiler). The use of Numba
can lead to significant improvements of the run time of a program. Furthermore,
Numba can support the parallel handling of Python code.

Threads, processes and the GIL
==============================

Modern operating systems can seemingly run several tasks in parallel even on a
simple compute core. In practice, this is achieved by in turn allotting compute
time to different tasks so that a single task usually cannot block other
tasks from execution over a longer period of time.

It is important to distinguish two different kinds of tasks: processes and
threads. Processes have at their disposal a reserved range of memory and their
own access to other system ressources. As a consequence, starting a new process
comes with a certain overhead in time. A single process will start first one
and subsequently possibly further threads in order to handle different tasks.
Threads differ from processes by working on the same range of memory and by
accessing the same system ressources. Starting a thread is thus less demanding
than starting a process.

Since threads share a common range of memory, they can access the same data and
easily exchange data among each other. Communication between different threads
thus leads to very little overhead. However, the access to common data is not
without risks. If one does not take care that reading and writing data by
different threads is done in the intended order, it may happen that a thread
does not obtain the data it needs. As the occurrence of such mistakes depends on
details of which thread executes which tasks at a given time, such problems are
not easily reproducible and sometimes quite difficult to identify. There exist
techniques to cope with the difficulties involved in the communication between
different threads, making multithreading, i.e. the parallel treatment in several
threads, possible. We will, however, not cover these techniques in the
present lecture notes.

As already mentioned in the introduction, the most popular implementation of
Python, CPython implemented in C, makes use of the GIL, the global interpreter
lock. The GIL prevents a single Python process to execute more than one thread
in parallel. While it is possible to make use of multithreading in Python
[#CPython]_, the GIL will ensure that individual threads will never run in 
parallel but in turn are allotted their slots of compute time. In this way,
only an illusion of parallel processing is created.

If the time of execution of a Python script is limited by the compute time,
multithreading will not result an in improvement. To the contrary, the overhead
arising from the necessity to change between different threads will lead to
a slow-down of the script. However, there exist scripts which are I/O-bound.
An example could be a script processing data which need to be downloaded from
the internet. While a thread is waiting for new data to arrive, another thread
might use the time to process data already available. For I/O-bounded scripts,
multithreading thus may be a good strategy even in Python.

However, numerical programs are usually not I/O-bound but limited by the
compute time. Therefore, we will not consider multithreading any further but
rather concentrate on multiprocessing, i.e. parallel treatment by means of
several Python processes. It is worth mentioning though that multithreading may
play a role even in numerical applications written in Python when numerical
libraries are used. Such libraries are often based on C code which is not
subject to the restrictions imposed by the GIL. Linear algebra routines
provided by an appropriately compiled version of NumPy may serve as an example.
This includes the NumPy library available through the Anaconda distribution
which is compiled with the Intel® Math Kernel Library (MKL).
:numref:`systemload` demonstrates an example where four cores are used when
determining the eigenvectors and eigenvalues of a large matrix. Another option
to circumvent the GIL is offered by Cython [#Cython]_ which allows to generate
C extensions from Python code.  Those parts of the code not accessing Python
objects can then be executed in a ``nogil`` context outside the control of the
GIL.

.. _systemload:
.. figure:: img/systemload.*
   :width: 15em
   :align: center

   In this example, the graph of the system load shows that during the solution
   of the eigenvalue problem for a large matrix by means of NumPy compiled
   with the Intel® MKL four cores are used at the same time.



.. _parallel_computing_in_python:

Parallel computing in Python
============================

We will illustrate the use of parallel processes in Python by considering a
specific example, namely the calculation of the Mandelbrot set. Mathematically,
the Mandelbrot set is defined as the set of complex numbers :math:`c` for which
the series generated by the iteration

.. math::

   z_{n+1} = z_n^2+c

with the initial value :math:`z_0=0` remains bounded. It is known that the
series is not bound once :math:`\vert z\vert>2` has been reached so that it
suffices to perform the iteration until this threshold has been reached. The
iterations for different values of :math:`c` can be performed completely
independently of each other so that it is straightforward to distribute
different values of :math:`c` to different processes. The problem is thus
*embarrrassingly parallel*. Once all individual calculations are finished,
it suffices to collect all data and to represent them graphically.

We start out with a simple initial version of a Python script to determine
the Mandelbrot set.

.. code-block:: python
   :linenos:

   import matplotlib.pyplot as plt
   import numpy as np
   
   def mandelbrot_iteration(c, nitermax):
       z = 0
       for n in range(nitermax):
           if abs(z) > 2:
               return n
           z = z**2+c
       return nitermax
   
   def mandelbrot(xmin, xmax, ymin, ymax, npts, nitermax):
       data = np.empty(shape=(npts, npts), dtype=np.int)
       dx = (xmax-xmin)/(npts-1)
       dy = (ymax-ymin)/(npts-1)
       for nx in range(npts):
           x = xmin+nx*dx
           for ny in range(npts):
               y = ymin+ny*dy
               data[ny, nx] = mandelbrot_iteration(x+1j*y, nitermax)
       return data
   
   def plot(data):
       plt.imshow(data, extent=(xmin, xmax, ymin, ymax),
                  cmap='jet', origin='bottom', interpolation='none')
       plt.show()
   
   nitermax = 2000
   npts = 1024
   xmin = -2
   xmax = 1
   ymin = -1.5
   ymax = 1.5
   data = mandelbrot(xmin, xmax, ymin, ymax, npts, nitermax)
   plot(data)

Here, the iteration prescription is carried out in the function
``mandelbrot_iteration`` up to maximum number of iterations given by
``nitermax``. The purpose of the function ``mandelbrot`` is to walk through
a grid of complex values :math:`c` and to collect the results in the
array ``data``. For simple testing purposes, it is useful to graphically
represent the results by means of the function ``plot``. 

In a first step, we profile our script as was explained in :numref:`cProfile`.
In this way we avoid using parallelization simply to remedy performance 
deficiencies of our script.

The most relevant lines of the profiling output are the following::

      ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1048576  398.497    0.000  735.577    0.001 mandelbrot.py:4(mandelbrot_iteration)
   357050652  337.080    0.000  337.080    0.000 {built-in method builtins.abs}
           1    2.189    2.189  737.766  737.766 mandelbrot.py:12(mandelbrot)

These data can vary significantly depending on the hardware used but they
clearly show that a significant amount of time is spent in determining the
absolute value in line 7 of our code. Note, however, that there will be a
substantial overhead when profiling a function with a short execution time
which is called as often as is the case here for the absolute value.

The need to determine an absolute value can be avoided by treating the real and
imaginary parts separately. Doing so will be helpful also in later steps to
improve the performance. We replace the functions ``mandelbrot`` and
``mandelbrot_iteration`` by

.. code-block:: python
   :linenos:

   def mandelbrot_iteration(cx, cy, nitermax):
       x = 0
       y = 0
       for n in range(nitermax):
           x2 = x*x
           y2 = y*y
           if x2+y2 > 4:
               return n
           x, y = x2-y2+cx, 2*x*y+cy
       return nitermax

   def mandelbrot(xmin, xmax, ymin, ymax, npts, nitermax):
       data = np.empty(shape=(npts, npts), dtype=np.int)
       dx = (xmax-xmin)/(npts-1)
       dy = (ymax-ymin)/(npts-1)
       for nx in range(npts):
           x = xmin+nx*dx
           for ny in range(npts):
               y = ymin+ny*dy
               data[ny, nx] = mandelbrot_iteration(x, y, nitermax)
       return data

In our case, this change leads to a significant performance improvement::

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  1048576   77.128    0.000   77.128    0.000 mandelbrot.py:4(mandelbrot_iteration)
        1    2.200    2.200   79.328   79.328 mandelbrot.py:15(mandelbrot)


Numba
=====

.. [#CPython] When referring to Python, we always mean CPython. An example
      of an implementation of Python without a GIL is Jython written in Java.
.. [#Cython] Cython should not be confused with CPython, the C implementation of
      Python. More information on Cython can be found at https://cython.org/.
