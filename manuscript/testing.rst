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

Testing with py.test
====================

For more complex test cases, the Python standard library provides a framework called
``unittest``. Recently, however, ``py.test`` has become very popular as it requires
less overhead when writing tests. In this section we will focus on ``py.test`` which
is not part of the Python standard library but it included e.g. in the Anaconda
distribution.
