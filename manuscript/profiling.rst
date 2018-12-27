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

.. [#cupy] For more information, see the `CuPy homepage <https://cupy.chainer.org>`_.
.. [#cython] For more information, see `Cython – C-Extensions for Python
             <https://cython.org/>`_. 
.. [#pypy] For more information, see the `PyPy homepage <https://pypy.org>`_.
.. [#numba] For more information, see the `Numba homepage <https://numpy.pydta.org>`_.
.. [#dek_tex] Donald E. Knuth is well known far beyond the computer science
              community as the author of the typesetting system TeX.
.. [#knuth_quote] D.\ E. Knuth, Computing Surveys **6**, 261 (1974). The quote
              can be found on page 268.
