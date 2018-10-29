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
control should successfully run the existing tests. Such tests also constitute
an important safety net when refactoring code, i.e. when rewriting the inner
structure of the code without affecting its external behavior. Tests running
correctly for the old code should do the same for the refactored code.

Whenever a bug has been discovered in the code, it is a good habit to write
a tests capable of detecting this bug. While it is barely possible to detect
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

In this chapter, we will be concerned with unit testing and covered to main approaches.
The first one are doctests which are implemented in Python within the doc strings of a 
function or method. The second approach are unit tests based on assserts using ``py.test``.
