*****************
Run-time analysis
*****************

General remarks
===============

Frequently, the numerical treatment of scientific problems can lead to
time-consuming code and the question arises how its performance can be
improved. There exist a variety of different kinds of approaches. One could for
example choose to make use of more powerful hardware or distribute the task on
numerous compute nodes of a compute cluster. Even though today, human resources
tend to be more costly than hardware resourse, the latter should not be wasted
by very inefficient code.

In certain cases, speed can be improved by making use of graphical processors (GPU)
which are able to handle larger data sets in parallel. While writing code for
GPUs may be cumbersome, there exists for example the CuPy library [#cupy]_ which
can serve as a drop-in replacement for most of the NumPy library and will run
on NVIDIA GPUs.

On the software side, an option is to make use of optimized code provided by
numerical libraries like NumPy and SciPy discussed in
:numref:`scientific_libraries`. Sometimes, it can make sense to to implement
particularly time-consuming parts in the programming language C for which 
highly optimizing compilers are available. This approach does not necessarily
require to write proper C code. One can make use of Cython [#cython]_ instead,
which will autogenerate C code from Python-like code.

Another option is the use of *just in time* (JIT) compilers as is done in PyPy
[#pypy]_ and Numba [#numba]_. The latter is readily available through the
Anaconda distribution and offers an easy approach to speeding up time-critical
parts of the code by simply adding a decorator to a function. Generally, JIT
compilers analyze the code before its first execution and create machine code
allowing to run the code faster in subsequent calls.

While some of the methods just mentioned can easily be implemented, others may
require a signficant investment of time. One therefore needs to assess whether
the gain in compute time really exceeds the cost in developer time. It is worth
following the advice of the emminent computer scientist Donald E. Knuth
[#dek_tex]_ who wrote already 45 years ago [#knuth_quote]_

   There is no doubt that the grail of efficiency leads to abuse. Programmers
   waste enormous amounts of time thinking about, or worrying about, the speed
   of noncritical parts of their programs, and these attempts at efficiency
   actually have a strong negative impact when debugging and maintentance are
   considered. We *should* forget about small efficiencies, say about 97 % of the
   time: premature optimization is the root of all evil.

   Yet we should not pass up our opportunities in that critical 3 %. A good
   programmer will not be lulled into complacency by such reasoning, he will be
   wise to look carefully at the critical code; but only after that code has
   been identified.

Before beginning to optimize code, it is important to identify the parts where
most of the time is spent and the rest of this chapter will be devoted to
techniques allowing to do so. At this point, it is worth emphasizing that a 
piece of code executed relatively fast can be more relevant than a piece of
code executed slowly if the first one is executed very often while the second
one is executed only once. 

Code optimization often entails a risk for bugs to enter the code. Obviously,
fast-running code is not worth anything if it does not produce correct results.
It can then be very reassuring if one can rely on a comprehensive test suite
(:numref:`testing`) and if one has made use of a version control system
(:numref:`version_control`) during code development and code optimization.

Before discussing techniques for timing code execution, we will discuss a few
potential pitfalls.

Some pitfalls in run-time analysis
==================================

A simple approach to performing a run-time analysis of code could consist in taking
the time before and after the code is executed. The ``time`` module in the Python
standard library offers the possibility to determine the current time::

   >>> import time
   >>> time.ctime()
   'Thu Dec 27 11:13:33 2018'

While this result is nicely readable, it is not well suited to calculate time differences.
For this purpose, the seconds passed since the beginning of the epoch are better suited.
On Unix systems, the epoch starts on January, 1970 at 00:00:00 UTC::

   >>> time.time()
   1545905769.0189064

Now, it is straightforward to determine the time elapsed during the execution of a
piece of code. The following code repeats the execution several times to convey an
idea of the fluctuations to be expected.

.. code-block:: python

   import time

   for _ in range(10):
       sum_of_ints = 0
       start = time.time()
       for n in range(1000000):
           sum_of_ints = sum_of_ints + 1
       end = time.time()
       print(f'{end-start:5.3f}s', end='  ')

Executing this code yields::

   0.142s  0.100s  0.093s  0.093s  0.093s  0.093s  0.092s  0.091s  0.091s  0.091s

Duing a second run on the same hardware, we obtained::

   0.131s  0.095s  0.085s  0.085s  0.088s  0.085s  0.084s  0.085s  0.085s  0.085s

While these numbers give an idea of the execution time, they should not be taken too
literally. In particular, it makes sense to average over several loops. This is 
facilitated by the ``timeit`` module in the Python standard library which we will
discuss in the following section.

When performing run-time analysis as just described, one should be aware that a
computer may be occupied by other tasks as well. In general, the total elapsed
time will thus differ from the time actually needed to execute a specific piece
of code. The ``time`` module therefore provides two functions. In addition to
the ``time`` function which records the wall clock time, there exist a
``process_time`` function which counts the time attributed to the specific
process running our Python script. The following example demonstrates the
difference by intentionally letting the program pause for a second once in a
while. Note, that although the execution of ``time.sleep`` occurs within the
process under consideration, the time needed is ignored by ``process_time``.
Therefore, we can use ``time.sleep`` to simulate other activities of the computer,
even if it is done in a somewhat inappropriate way.

.. code-block:: python

   import time

   sum_of_ints = 0
   start = time.time()
   start_proc = time.process_time()
   for n in range(10):
       for m in range(100000):
           sum_of_ints = sum_of_ints + 1
       time.sleep(1)
   end = time.time()
   end_proc = time.process_time()
   print(f'total time:   {end-start:5.3f}s')
   print(f'process time: {end_proc-start_proc:5.3f}s')

In a run on the same hardware as used before, we find the following result::

   total time:   10.207s
   process time: 0.197s

The difference basically consists of the ten seconds spent while the code was
sleeping.

One should also be aware that enclosing the code in question in a function will
lead to an additional contribution to the execution time. This particularly poses
a problem if the execution of the code itself requires only little time. We compare
the two scripts

.. code-block:: python

   import time

   sum_of_ints = 0
   start_proc = time.process_time()
   for n in range(10000000):
       sum_of_ints = sum_of_ints + 1
   end_proc = time.process_time()
   print(f'process time: {end_proc-start_proc:5.3f}s')

and

.. code-block:: python

   import time

   def increment_by_one(x):
       return x+1

   sum_of_ints = 0
   start_proc = time.process_time()
   for n in range(10000000):
       increment_by_one(sum_of_ints)
   end_proc = time.process_time()
   print(f'process time: {end_proc-start_proc:5.3f}s')


Tht first script takes on average over 10 runs 0.9 seconds while the second script
takes 1.1 seconds and thus runs about 20% slower.

Independently of the methods used and even if one of the methods discussed later is
employed, a run-time analysis will always influence the execution of the code. The
measured run time therefore will be larger than without doing any timing. However,
we should still be able to identify the parts of the code which take most of the time.

A disadvantage of the methods discussed so far consists in the fact that they require
a modification of the code. Usually, it is desirable to avoid such modifications as
much as possible. In the following sections, we will present a few timing techniques
which can be used according to the specific needs.


The ``timeit`` module
=====================

.. [#cupy] For more information, see the `CuPy homepage <https://cupy.chainer.org>`_.
.. [#cython] For more information, see `Cython – C-Extensions for Python
             <https://cython.org/>`_. 
.. [#pypy] For more information, see the `PyPy homepage <https://pypy.org>`_.
.. [#numba] For more information, see the `Numba homepage <https://numpy.pydta.org>`_.
.. [#dek_tex] Donald E. Knuth is well known far beyond the computer science
              community as the author of the typesetting system TeX.
.. [#knuth_quote] D.\ E. Knuth, Computing Surveys **6**, 261 (1974). The quote
              can be found on page 268.
