.. _testing:

***************
Testing of code
***************

Why testing?
============

Scientific code usually aims at producing new insights which implies that
typically the correctness of the result is difficult to assess. Occasionally,
bugs in the code can be identified because the results do not make any sense.
In general the situation may not be that clear. Therefore testing the code is
crucial. However, it is insufficient to test code from time to time in an
informal manner. Instead, one should aim at a comprehensive set of tests which
can be applied to the code at any time. Ideally, all code committed to version
control should successfully run the existing tests. Test can then also serve as
documentation of which kind of functionality is guaranteed to work.
Furthermore, tests constitute an important safety net when refactoring code,
i.e. when rewriting the inner structure of the code without affecting its
external behavior. Tests running correctly for the old code should do so also
for the refactored code.

Whenever a bug has been discovered in the code, it is a good habit to write
one or more tests capable of detecting this bug. While it is barely possible to detect
all imaginable bugs with tests, one should ensure at least that bugs which
appeared once do not have a chance to sneak back into the code. Furthermore,
one should add tests for any new functionality implemented. One indicator for
the quality of a test suite, i.e. a collection of tests, is code coverage which
says which percentage of lines of code are run during the tests. In practice,
one rarely will reach one hundred percent code coverage but one should nevertheless
strive for a good code coverage. At the same time, code coverage is not the
only aspect to look for. One should also make sure that tests are independent
from each other and independent of the logic of the code, if possible. The
meaning of this will become clear in some of the examples presented later.
Corner cases deserve special attention in testing as they are frequently ignored
when setting up the logic of a program.

Tests can be developed in parallel to the code or even after the code has been
written. A typical example for the latter is when the presence of a bug is
noticed. Then, the bug should be fixed and a test should be implemented which
will detect the presence of the fixed bug in the future. Another approach is
the so-called *test-driven development* where the tests are first written. In a
second step, the code is developed until all test run successfully.

Testing a big piece of software is usually difficult to do and as mentioned in the
beginning in the case of scientific software can be almost impossible because one
cannot anticipate the result beforehand. Therefore, one often tests on a much finer
level, an approach called *unit testing*. Here, typically relatively small functions
are tested to make sure that they work as expected. An interesting side effect of
unit testing is often a significant improvement in code structure. Often a function
needs to be rewritten in order to be tested properly. It often needs to be better
isolated from the rest of the code and its interface has to be defined more carefully,
thereby improving the quality of the code.

In this chapter, we will be concerned with unit testing and mainly cover two approaches.
The first one are doctests which are implemented in Python within the doc strings of a 
function or method. The second approach are unit tests based on asserts using ``py.test``.

.. _doctests:

Doctests
========

The standard way to document a function in Python is a so-called docstring as shown
in the following example.

.. code-block:: python

   # hello.py

   def welcome(name):
       """Print a greeting.

       name: name of the person to greet
       """
       return 'Hello {}!'.format(name)

In our example, the docstring is available as ``welcome.__doc__`` and can also be
obtained by means of ``help(welcome)``.

Even though we have not formulated any test, we can run the (non-existing) doctests::

   $ python -m doctest hello.py

No news is good news, i.e. the fact that this command does not yield any output implied
that no error occurred in running the tests. One can ask doctest to be more verbose by
adding the option ``-v``::

   $ python -m doctest -v hello.py
   1 items had no tests:
       hello.py
   0 tests in 1 items.
   0 passed and 0 failed.
   Test passed.

This message states explicitly that no tests have been run and no tests have failed.

We now add our first doctest. Doing so is quite straightforward. One simply
reproduces how a function call together with its output would look in the
Python shell. 

.. code-block:: python

   # hello.py

   def welcome(name):
       """Print a greeting.

       name: name of the person to greet

       >>> welcome('Alice')
       'Hello Alice!'
       """
       return 'Hello {}!'.format(name)

Running the test with the option ``-v`` to obtain some output, we find::

   $ python -m doctest -v hello.py
   Trying:
       welcome('Alice')
   Expecting:
       'Hello Alice!'
   ok
   1 items had no tests:
       hello
   1 items passed all tests:
       1 tests in hello.welcome
   1 tests in 2 items.
   1 passed and 0 failed.
   Test passed.

Our test passes as expected. It is worth noting that besides providing a
test, the last two lines of the new doc string can also serve as a documentation
of how to call the function ``welcome``.

Now let us add a corner case. A special case occurs if no name is given. Even in
this situation, the function should behave properly. However, an appropriate test
will reveal in a second that we have not sufficiently considered this corner case
when designing our function.

.. code-block:: python
   :linenos:

   # hello.py

   def welcome(name):
       """Print a greeting.

       name: name of the person to greet

       >>> welcome('')
       'Hello!'
       >>> welcome('Alice')
       'Hello Alice!'
       """
       return 'Hello {}!'.format(name)

Running the doctests, we identify our first coding error by means of a test::

   $ python -m doctest hello.py
   **********************************************************************
   File "hello.py", line 8, in hello.welcome
   Failed example:
       welcome('')
   Expected:
       'Hello!'
   Got:
       'Hello !'
   **********************************************************************
   1 items had failures:
      1 of   2 in hello.welcome
   ***Test Failed*** 1 failures.

The call specified in line 8 of our script failed because we implicitly
add a blank which should not be there. So let us modify our script to
make the tests pass.

.. code-block:: python

   # hello.py

   def welcome(name):
       """Print a greeting.

       name: name of the person to greet

       >>> welcome('')
       'Hello!'
       >>> welcome('Alice')
       'Hello Alice!'
       """
       if name:
           return 'Hello {}!'.format(name)
       else:
           return 'Hello!'

Now the tests pass successfully.

If now we decide to change our script, e.g. by giving a default value to the variable
name, we can use the tests as a safety net. They should run for the modified script
as well.

.. code-block:: python

   # hello.py

   def welcome(name=''):
       """Print a greeting.

       name: name of the person to greet

       >>> welcome('')
       'Hello!'
       >>> welcome('Alice')
       'Hello Alice!'
       """
       if name:
           return 'Hello {}!'.format(name)
       else:
           return 'Hello!'

Both tests pass successfully. However, we have not yet tested the new default value
for the variable ``name``. So, let us add another test to make sure that everything
works fine.

.. code-block:: python

   # hello.py

   def welcome(name=''):
       """Print a greeting.

       name: name of the person to greet

       >>> welcome()
       'Hello!'
       >>> welcome('')
       'Hello!'
       >>> welcome('Alice')
       'Hello Alice!'
       """
       if name:
           return 'Hello {}!'.format(name)
       else:
           return 'Hello!'

All three tests pass successfully.

In a next step development step, we make the function ``welcome`` multilingual.

.. code-block:: python

   # hello.py

   def welcome(name='', lang='en'):
       """Print a greeting.

       name: name of the person to greet

       >>> welcome()
       'Hello!'
       >>> welcome('')
       'Hello!'
       >>> welcome('Alice')
       'Hello Alice!'
       >>> welcome('Alice', lang='de')
       'Hallo Alice!'
       """
       hellodict = {'en': 'Hello', 'de': 'Hallo'}
       hellostring = hellodict[lang]
       if name:
           return '{} {}!'.format(hellostring, name)
       else:
           return '{}!'.format(hellostring)

It is interesting to consider the case where the value of ``lang`` is not a valid
key. Calling the function with ``lang`` set to ``fr``, one obtains::

   $ python hello.py
   Traceback (most recent call last):
     File "hello.py", line 25, in <module>
       welcome('Alice', 'fr')
     File "hello.py", line 18, in welcome
       hellostring = hellodict[lang]
   KeyError: 'fr'

Typically, error messages related to exception can be quite complex and it is
either cumbersome to reproduce them in a test or depending on the situation it
might even by impossible. One might think that the complexity of an error
message is irrelevant because error messages should not occur in the first place.
However, there are two reasons to consider such a situation. First, it is not
uncommon that an appropriate exception is raised and one should check in a test
whether it is properly raised. Second, more complex outputs appear not only in
the context of exceptions and one should know ways to handle such situations.

Let us assume that we handle the ``KeyError`` by raising a ``ValueError`` together
with an appropriate error message.

.. code-block:: python
   :linenos:

   # hello.py

   def welcome(name='', lang='en'):
       """Print a greeting.

       name: name of the person to greet

       >>> welcome()
       'Hello!'
       >>> welcome('')
       'Hello!'
       >>> welcome('Alice')
       'Hello Alice!'
       >>> welcome('Alice', lang='de')
       'Hallo Alice!'
       >>> welcome('Alice', lang='fr')
       Traceback (most recent call last):
       ValueError: unknown language: fr
       """
       hellodict = {'en': 'Hello', 'de': 'Hallo'}
       try:
           hellostring = hellodict[lang]
       except KeyError:
           errmsg = 'unknown language: {}'.format(lang)
           raise ValueError(errmsg)
       if name:
           return '{} {}!'.format(hellostring, name)
       else:
           return '{}!'.format(hellostring)

   if __name__ == '__main__':
       welcome('Alice', 'fr')

All tests run successfully. Note that in lines 17 and 18 we did not reproduce the full
traceback. It was sufficient to put line 17 which signals that the following traceback
can be ignored. Line 18 is checked again to be consistent with the actual error message.
If one does not need to verify the error message but just the type of exception raised,
one can use a doctest directive. For example, one could replace lines 16 to 18 by the
following code.

.. code-block:: python

   """
   >>> welcome('Alice', lang='fr') # doctest: +ELLIPSIS
   Traceback (most recent call last):
   ValueError: ...
   """

The directive is here specified by the comment "``# doctest: +ELLIPSIS``" and the 
ellipsis "``...``" in the last line will replace any output following the text
"``ValueError:``".

Another useful directive is ``+SKIP`` which tells doctest to skip the test marked
in this way. Sometimes, one has already written a test before the corresponding
functionality has been implemented. Then it may make sense to temporarily deactivate
the test to avoid getting distracted from seriously failing tests by tests which
are known beforehand to fail. A complete list of directives can be found in
the `doctest documentation <https://docs.python.org/3/library/doctest.html>`_. For
example, it is worth to check out the directive ``+NORMALIZE_WHITESPACE`` which
helps avoiding trouble with different kinds of white spaces.

As we have seen, doctests are easy to write and in addition to testing code they
are helpful in documenting the usage of functions or methods. On the other hand,
they are particularly well suited for numerical tests where results have to agree
only to a certain precision. For more complex test cases, it might also be helpful
to choose the approach discussed in the next section instead of using doctests.

Testing with pytest
===================

For more complex test cases, the Python standard library provides a framework
called ``unittest``. Another often used test framework is ``nose``. Recently,
``pytest`` has become very popular which compared ``unittest`` requires less
overhead when writing tests. In this section we will focus on ``pytest`` which
is not part of the Python standard library but is included e.g. in the Anaconda
distribution.

We illustrate the basic usage of ``pytest`` by testing a function generating
a line of Pascal's triangle.

.. code-block:: python

   def pascal(n):
       """create the n-th line of Pascal's triangle

       The line numbers start with n=0 for the line
       containing only the entry 1. The elements of
       a line are generated successively.

       """
       x = 1
       yield x
       for k in range(n):
           x = x*(n-k)//(k+1)
           yield x

   if __name__ == '__main__':
       for n in range(7):
           line = ' '.join('{:2}'.format(x) for x in pascal(n))
           print(str(n)+line.center(25))

Running this script returns the first seven lines of Pascal's triangle::

   $ python pascal.py
   0             1
   1           1  1
   2          1  2  1
   3        1  3  3  1
   4       1  4  6  4  1
   5     1  5 10 10  5  1
   6    1  6 15 20 15  6  1

We will now test the function ``pascal(n)`` which returns the elements of the
:math:`n`-th line of Pascal's triangle.  The function is based on the fact that
the elements of Pascal's triangle are binomial coefficients. While the output
of the first seven lines looks fine, it make sense to test the function more
thoroughly.

The first and most obvious test is to automate at least part of the test which we
were just doing visually. It is always a good idea to check boundary cases. In our
case this means that we make sure that ``n=0`` indeed corresponds to the first line.
We also check the following line as well as a typical non-trivial line. We call the
following script ``test_pascal.py`` because ``pytest`` will run scripts with names
of the form ``test_*.py`` or ``*_test.py`` in the present directory or its subdirectories
automatically. Here, the star stands for any other valid part of a filename.
Within the script, the test functions should start with ``test_`` to distinguish
them from other functions which may be present.

.. code-block:: python

   from pascal import pascal

   def test_n0():
       assert list(pascal(0)) == [1]

   def test_n1():
       assert list(pascal(1)) == [1, 1]

   def test_n5():
       expected = [1, 4, 6, 4, 1]
       assert list(pascal(5)) == expected

The tests contain an ``assert`` statement which raises an ``AssertionError`` in
case the test should fail. In fact, this will happen for our test script, even though
the implementation of the function ``pascal`` is not to blame. In this case, we have
inserted a mistake into our test script to show the output of ``pytest`` in the case
of errors. Can you find the mistake in the test script? If not, it suffices to run
the script::

   $ pytest
   ============================= test session starts =============================
   platform linux -- Python 3.6.6, pytest-3.8.0, py-1.6.0, pluggy-0.7.1
   rootdir: /home/gert/pascal, inifile:
   plugins: remotedata-0.3.0, openfiles-0.3.0, doctestplus-0.1.3, arraydiff-0.2
   collected 3 items                                                             

   test_pascal.py ..F                                                      [100%]

   ================================== FAILURES ===================================
   ___________________________________ test_n5 ___________________________________

       def test_n5():
           expected = [1, 4, 6, 4, 1]
   >       assert list(pascal(5)) == expected
   E       assert [1, 5, 10, 10, 5, 1] == [1, 4, 6, 4, 1]
   E         At index 1 diff: 5 != 4
   E         Left contains more items, first extra item: 1
   E         Use -v to get the full diff

   test_pascal.py:11: AssertionError
   ===================== 1 failed, 2 passed in 0.04 seconds ======================
   

The last line in the first part of the output, before the header entitled ``FAILURES``,
``pytest`` gives a summary of the test run. It ran three tests present in the script
``test_pascal.py`` and the result is indicated by ``..F`` . The two dots represent
two successful tests and the ``F`` marks test which failed and for which detailed information
is given in the second part of the output. Clearly, the elements of line 5 in Pascal's
triangle yielded by our function does not coincide with our expectation.

It occasionally happens that a test is known to fail in the present of
development.  One still may want to keep the test in the test suite, but it
should not be flagged as failure. In such a case, the test can be decorated
with ``pytest.mark.xfail``. Even though decorators can be used without knowing
how they work, it can be useful to have an idea of this concept. A brief introduction
to decorators is given in :numref:`appendixdecorators`.

The relevant test then looks as follows

.. code-block:: python

   @pytest.mark.xfail
   def test_n5():
       expected = [1, 4, 6, 4, 1]
       assert list(pascal(5)) == expected

In addition, the ``pytest`` module need to be imported. Now, the test is marked
by an ``x`` for expected failure::

   $ pytest
   ============================= test session starts =============================
   platform linux -- Python 3.6.6, pytest-3.8.0, py-1.6.0, pluggy-0.7.1
   rootdir: /home/gert/pascal, inifile:
   plugins: remotedata-0.3.0, openfiles-0.3.0, doctestplus-0.1.3, arraydiff-0.2
   collected 3 items                                                             

   test_pascal.py ..x                                                      [100%]

   ===================== 2 passed, 1 xfailed in 0.04 seconds =====================

The marker ``x`` is set in lowercase to distinguish it from serious failures like
``F`` for a failed test. If a test expected to fail actually passes, it will be
marked by an uppercase ``X`` to indicate that corresponding test should not pass.

One can also skip tests by means of the decorator ``pytest.mark.skip`` which
takes an optional variable ``reason``.

.. code-block:: python

   @pytest.mark.skip(reason="just for demonstration")
   def test_n5():
       expected = [1, 4, 6, 4, 1]
       assert list(pascal(5)) == expected

However, the reason will only be listed in the output, if the option ``-r s`` is
applied::

   $ pytest -r s
   ============================= test session starts =============================
   platform linux -- Python 3.6.6, pytest-3.8.0, py-1.6.0, pluggy-0.7.1
   rootdir: /home/gert/pascal, inifile:
   plugins: remotedata-0.3.0, openfiles-0.3.0, doctestplus-0.1.3, arraydiff-0.2
   collected 3 items

   test_pascal.py ..s                                                      [100%]
   =========================== short test summary info ===========================
   SKIP [1] test_pascal.py:10: just for demonstration

   ===================== 2 passed, 1 skipped in 0.01 seconds =====================

In our case, it is of course better to correct the expected result in function ``test_n5``.
The we obtain the following output from ``pytest``::

   $ pytest
   ============================= test session starts =============================
   platform linux -- Python 3.6.6, pytest-3.8.0, py-1.6.0, pluggy-0.7.1
   rootdir: /home/gert/pascal, inifile:
   plugins: remotedata-0.3.0, openfiles-0.3.0, doctestplus-0.1.3, arraydiff-0.2
   collected 3 items

   test_pascal.py ...                                                      [100%]

   ========================== 3 passed in 0.01 seconds ===========================

Now, all tests pass just fine.

One might object that the test so far only verify a few special cases and in particular
are limited to very small values of ``n``. How do we test line 10000 of Pascal's triangle
without having to determine the expected result? We can test properties related to the
fact that the elements of Pascal's triangle are binomial coefficients. The sum of the
elements in the :math:`n`-th line amounts to :math:`2^n` and if the sign is changed
from element to element the sum vanishes. This kind of test is quite independent of the
logic of the function ``pascal`` and therefore particularly significant. We can implement
the two tests in the following way.

.. code-block:: python

   def test_sum():
       for n in (10, 100, 1000, 10000):
           assert sum(pascal(n)) == 2**n

   def test_alternate_sum():
       for n in (10, 100, 1000, 10000):
           assert sum(alternate(pascal(n))) == 0

   def alternate(g):
       sign = 1
       for elem in g:
           yield sign*elem
           sign = -sign

Here, the name of the function ``alternate`` does not start with the string ``test`` because
this function is not intended to be executed as a test. Instead, it serves to alternate
the sign of subsequent elements used in the test ``test_alternate_sum``. One can verify that
indeed five tests are run. For a change, we use the option ``-v`` for a verbose output
listing the name of the test functions being executed. ::

   $ pytest -v
   ============================ test session starts ============================
   platform linux -- Python 3.6.6, pytest-3.8.0, py-1.6.0, pluggy-0.7.1 -- /home/gert/anaconda3/bin/python
   cachedir: .pytest_cache
   rootdir: /home/gert/pascal, inifile:
   plugins: remotedata-0.3.0, openfiles-0.3.0, doctestplus-0.1.3, arraydiff-0.2
   collected 5 items
   
   test_pascal.py::test_n0 PASSED                                        [ 20%]
   test_pascal.py::test_n1 PASSED                                        [ 40%]
   test_pascal.py::test_n5 PASSED                                        [ 60%]
   test_pascal.py::test_sum PASSED                                       [ 80%]
   test_pascal.py::test_alternate_sum PASSED                             [100%]
   
   ========================= 5 passed in 0.10 seconds ==========================

We could also check whether a line in Pascal's triangle can be constructed from the previous
line by adding neighboring elements. This test is completely independent of the inner logic
of the function to be tested. Furthermore, we can execute it for arbitrary line numbers, at least
in principle. We add the test

.. code-block:: python

   def test_generate_next_line():
       for n in (10, 100, 1000, 10000):
           for left, right, new in zip(chain([0], pascal(n)),
                                       chain(pascal(n), [0]),
                                       pascal(n+1)):
               assert left+right == new

where we need to add ``from itertools import chain`` in the import section of our test script.

The last three of our tests contain loops, but they do not behave like several tests. As
soon as an exception is raised, the test has failed. In contrast our first three tests for
the lines in Pascal's triangle with numbers 0, 1, and 5 are individual tests which could
be unified. How can we do this while the keeping the individuality of the test? The answer
is the ``parametrize`` decorator which we use in the following new version of our test script.

.. code-block:: python
   :linenos:

   import pytest
   from itertools import chain
   from pascal import pascal

   @pytest.mark.parametrize("lineno, expected", [
       (0, [1]),
       (1, [1, 1]),
       (5, [1, 5, 10, 10, 5, 1])
   ])
   def test_line(lineno, expected):
       assert list(pascal(lineno)) == expected

   powers_of_ten = pytest.mark.parametrize("lineno",
                       [10, 100, 1000, 10000])

   @powers_of_ten
   def test_sum(lineno):
       assert sum(pascal(lineno)) == 2**lineno

   @powers_of_ten
   def test_alternate_sum(lineno):
       assert sum(alternate(pascal(lineno))) == 0

   def alternate(g):
       sign = 1
       for elem in g:
           yield sign*elem
           sign = -sign
   
   @powers_of_ten
   def test_generate_next_line(lineno):
       for left, right, new in zip(chain([0], pascal(lineno)),
                                   chain(pascal(lineno), [0]),
                                   pascal(lineno+1)):
           assert left+right == new

The function ``test_line`` replaces the original first three tests. In order to do
so, it takes two arguments which are provided by the decorator in lines 5 to 9. This
decorator makes sure that the test function is run three times with different values
of the line number in Pascal's triangle and the expected result. In the remaining three
test functions, we have replaced the original loop by a ``parametrize`` decorator. 
In order to avoid repetitive code, we have defined a decorator ``powers_of_ten`` in 
line 13 and 14 which then is used in three tests. Our script now contains 15 tests.

When discussing doctests, we had seen how one can make sure that a certain exception
is raised. Of course, this can also be achieved with ``pytest``. At least in the present
form, it does not make sense to call ``pascal`` with a negative value for the line number.
In such a case, a ``ValueError`` should be raised, a behavior which can be tested with
the following test.

.. code-block:: python

   def test_negative_int():
       with pytest.raises(ValueError):
           next(pascal(-1))

Here, ``next`` explicitly asks the generator to provide us with a value so that the function
``pascal`` gets a chance to check the validity of the line number. Of course, this test will
only pass once we have adapted our function ``pascal`` accordingly.

In order to illustrate a problem frequently occurring when writing tests for scientific
applications, we generalize our function ``pascal`` to floating point number arguments.
As an example, let us choose the argument 1/3. We would then obtain the coefficients in
the Taylor expansion

.. math::

   (1+x)^{1/3} = 1+\frac{1}{3}x-\frac{1}{9}x^2+\frac{5}{81}x^3+\ldots

Be aware that the generator will now provide us with an infinite number of
return values so that we should take care not to let this happen. In the
following script ``pascal_float``, we do so by taking advantage of the fact
that ``zip`` terminates whenever one of the generators is exhausted.

.. code-block:: python

   def taylor_power(power):
       """generate the Taylor coefficients of (1+x)**power

          This function is based on the function pascal().

       """
       coeff = 1
       yield coeff
       k = 0
       while power-k != 0:
           coeff = coeff*(power-k)/(k+1)
           k = k+1
           yield coeff

   if __name__ == '__main__':
       for n, val in zip(range(5), taylor_power(1/3)):
           print(n, val)

We call this script ``pascal_float.py`` and obtain the following output by running it::

   0 1
   1 0.3333333333333333
   2 -0.11111111111111112
   3 0.0617283950617284
   4 -0.0411522633744856

The first four lines match our expectations from the Taylor expansion of :math:`(1+x)^{1/3}`.

We test our new function with the test script ``test_taylor_power.py``.

.. code-block:: python

   import pytest
   from pascal_float import taylor_power

   def test_one_third():
       p = taylor_power(1/3)
       result = [next(p) for _ in range(4)]
       expected = [1, 1/3, -1/9, 5/81]
       assert result == expected

The failures section of the output of ``pytest -v`` shows where the problem lies::

   ______________________________ test_one_third _______________________________
   
       def test_one_third():
           p = taylor_power(1/3)
           result = [next(p) for _ in range(4)]
           expected = [1, 1/3, -1/9, 5/81]
   >       assert result == expected
   E       assert [1, 0.3333333...7283950617284] == [1, 0.33333333...2839506172839]
   E         At index 2 diff: -0.11111111111111112 != -0.1111111111111111
   E         Full diff:
   E         - [1, 0.3333333333333333, -0.11111111111111112, 0.0617283950617284]
   E         ?                                            -                   ^
   E         + [1, 0.3333333333333333, -0.1111111111111111, 0.06172839506172839]
   E         ?                                                               ^^
   
   test_taylor_power.py:8: AssertionError
   ========================= 1 failed in 0.04 seconds ==========================

It looks like rounding errors spoil our test and this problem will get worse if
we want to check further coefficients. We are thus left with two problems.
First, one needs to have an idea of how well the actual and the expected result
should agree.  It is not straightforward to answer this, because the precision
of a result may depend strongly on the numerical methods employed. For a
numerical integration, a relative error of :math:`10^{-8}` might be perfectly
acceptable while for a pure rounding error, this value would be too large. On a
more practical side, how can we test in the presence of numerical errors?

There are actually a number of possibilities. The ``math``-module of the Python
standard library provides a function ``isclose`` which allows to check whether
two numbers agree up to a given absolute or relative tolerance. However, one
would have to compare each pair of numbers individually and then combine the
Boolean results by means of ``all``. When dealing with arrays, the NumPy
library provides a number of useful functions in its ``testing`` module. Several
of these functions can be useful when comparing floats. Finally, ``pytest``
itself provides a function ``approx`` which can test individual values or
values collected in a list, a NumPy array, or even a dictionary. Using
``pytest.approx``, our test could look as follows.

.. code-block:: python

   import math
   import pytest
   from pascal_float import taylor_power

   def test_one_third():
       p = taylor_power(1/3)
       result = [next(p) for _ in range(4)]
       expected = [1, 1/3, -1/9, 5/81]
       assert result == pytest.approx(expected, abs=0, rel=1e-15)

Here we test whether the relative tolerance between two values in a pair is at
most :math:`10^{-15}`. By default, the absolute tolerance is set to
:math:`10^{-12}` and the relative tolerance to :math:`10^{-6}` where in the end
the larger value is taken. If we would not specify ``abs=0``, a very small
relative tolerance would be ignored in favor of the default absolute tolerance.
On the other hand, if no relative tolerance is specified, the absolute
tolerance is taken for the comparison.

``pytest.approx`` and ``math.isclose`` differ when the relative tolerance is
checked. While the first one takes the relative tolerance with respect to the
argument of ``pytest.approx``, the second one checks whether the relative
tolerances are met with respect to both values.

In this section, we have discussed some of the more important aspects of ``pytest``
without being complete. More information can be found in the `corresponding documentation
<https://docs.pytest.org>`_. Of interest, in particular if more extensive tests
are written, could be the possibility to group tests in classes. This can also
be useful if a number of tests requires the same setup which then can be defined
in a dedicated function.
