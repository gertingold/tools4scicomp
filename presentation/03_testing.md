---
layout: section
---

# Testing of code

---

# Why should code be tested?

#### **Scenario**: Numerical calculations have produced interesting results. Are they correct?

* Do the results make sense?  
  For new and unexpected results, this might be difficult to judge.
* Is the code producing the results correct?

<br>

<carbon-arrow-right /> Testing code is important

<br>
<br>

* But testing code from time to time in an informal manner is insufficient.
* Much better: comprehensive set of tests
  * code coverage should be large, i.e. most of the code is traversed when executing the set of tests
  * ideally, code satisfies these tests when being committed
  * tests constitute a safety net when refactoring code
  * tests should be executable automatically

---

# How should code be tested?

* Tests should be independent of each other.
* Tests should be independent of the code logic, if possible.
* Watch out for corner cases.
* Tests should cover the parameter ranges relevant for the relevant use case.
* Whenever a bug is found, write a test to exclude that this bug sneaks back in.

* Here, we focus on *unit tests* which test small pieces of code.
  * With the help of unit tests, problems can be easily located.
  * Writing unit tests often help to improve the logical structure of the code because
    only a well-structured code can be tested easily.
* *Integration tests* test the interplay of different parts of the project code.
* No need to test external libraries. They should come with their own tests.

---

# Strategies for unit testing

* Write tests after having written corresponding code and in particular when bugs have
  been identified.
* Alternative: *Test driven development (TDD)*  
  Write tests first according to some specification. Then write code which satisfies the tests.

<br>

#### Different kinds of tests in Python

<div class="grid grid-cols-[30%_1fr] gap-4">
<div>

* Doctests

</div>
<div>

  * integrated in the docstring of a function
  * documents the usage of the function
  * allows to test the function

</div>
<div>

* Testing with `pytest`

</div>
<div>

  * framework for writing comprehensive tests
  * in contrast to `unittest` not part of the Python standard libary
</div>
<div>

* Testing with `hypothesis`

</div>
<div>

  * creates test data according to a specification
  * good at finding corner cases
  * saves problematic parameter values for later retesting

</div>
</div>

---

# Docstrings

* Immediately below the headline of a function definition, a docstring extending over 
  one or more lines can be put.
* Docstrings can also be used to document modules or classes.
* In Python, docstrings are preferred over comments.
* The string is available as `welcome.__doc__`.
* It is also used when calling the `help()`-function.

<br>

<div class="grid grid-cols-[1fr_1fr] gap-4">
<div>
```python
# hello.py

def welcome(name):
    """Print a greeting.

    name: name of the person to greet
    """
    return f'Hello {name}!'
```
</div>
<div>
```python
>>> from hello import welcome
>>> help(welcome)

Help on function welcome in module hello:

welcome(name)
    Print a greeting.
    
    name: name of the person to greet
```
</div>
</div>

---

# Docstring for testing

```console
$ python -m doctest hello.py
```

<br>

* load the `doctest`-module for execution
* the docstring so far does not contain a test
* output is produced in the case of failing tests or when using the option `-v`

<br>

```console
$ python -m doctest -v hello.py
2 items had no tests:
    hello
    hello.welcome
0 tests in 2 items.
0 passed and 0 failed.
Test passed.
```

* So far, the docstring does not contain a test.

---

# Adding a first doctest

<div class="grid grid-cols-[1fr_1fr] gap-4">
<div>
````md magic-move
```python
# hello.py

def welcome(name):
    """Print a greeting.

    name: name of the person to greet
    """
    return f'Hello {name}!'
```
```python
# hello.py

def welcome(name):
    """Print a greeting.

    name: name of the person to greet

    >>> welcome('Alice')
    'Hello Alice!'
    """
    return f'Hello {name}!'
```
````
</div>

<v-click>

<div>
```console
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
```
</div>

</v-click>
</div>

<br>

<v-after>

* The doctest looks like it were entered in a Python interpreter with the `>>>` prompt and followed by the intended outcome.
* Executing the passing doctest results in an output only because we used the option `-v`.

</v-after>

---

# A corner case

<div class="grid grid-cols-[1fr_1fr] gap-4">
<div>
````md magic-move
```python
# hello.py

def welcome(name):
    """Print a greeting.

    name: name of the person to greet

    >>> welcome('Alice')
    'Hello Alice!'
    """
    return f'Hello {name}!'
```
```python
# hello.py

def welcome(name):
    """Print a greeting.

    name: name of the person to greet

    >>> welcome('')
    'Hello!'
    >>> welcome('Alice')
    'Hello Alice!'
    """
    return f'Hello {name}!'
```
````
</div>

<v-click>

<div>
```console
$ python -m doctest hello.py
**********************************************************************
File "/home/gli/testing/hello.py", line 9, in hello.welcome
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
```
</div>

</v-click>
</div>

<br>

<v-after>

* We have discovered a corner case. There should not be a blank before the exclamation
  mark if no name is given.

</v-after>

---

# Adding another test

<div class="grid grid-cols-[1fr_1fr] gap-4">
<div>
````md magic-move
```python
# hello.py

def welcome(name):
    """Print a greeting.

    name: name of the person to greet

    >>> welcome('')
    'Hello!'
    >>> welcome('Alice')
    'Hello Alice!'
    """
    return f'Hello {name}!'
```
```python
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
        return f'Hello {name}!'
    else:
        return 'Hello!'
```
```python
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
        return f'Hello {name}!'
    else:
        return 'Hello!'
```
```python
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
        return f'Hello {name}!'
    else:
        return 'Hello!'
```
````
<v-clicks at='1'>

* code corrected to handle blank correctly
* default added for variable `name`
* test for default value added

</v-clicks>
</div>
<div>
<v-click>

```console
$ python -m doctest -v hello.py
Trying:
    welcome()
Expecting:
    'Hello!'
ok
Trying:
    welcome('')
Expecting:
    'Hello!'
ok
Trying:
    welcome('Alice')
Expecting:
    'Hello Alice!'
ok
1 items had no tests:
    hello
1 items passed all tests:
   3 tests in hello.welcome
3 tests in 2 items.
3 passed and 0 failed.
Test passed.
```

</v-click>
</div>
</div>

---

# Doctest and exceptions

<div class="grid grid-cols-[1fr_1fr] gap-4">
<div>

```python {all|20-25|16-18}{maxHeight:'420px'}
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
        errmsg = f'unknown language: {lang}'
        raise ValueError(errmsg)
    if name:
        return f'{hellostring} {name}!'
    else:
        return f'{hellostring}!'

if __name__ == '__main__':
    welcome('Alice', 'fr')
```

</div>
<div>
<v-click>

```console
$ python hello.py
Traceback (most recent call last):
  File "/home/gli/testing/hello.py", line 22, in welcome
    hellostring = hellodict[lang]
                  ~~~~~~~~~^^^^^^
KeyError: 'fr'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/gli/testing/hello.py", line 32, in <module>
    welcome('Alice', 'fr')
  File "/home/gli/testing/hello.py", line 25, in welcome
    raise ValueError(errmsg)
ValueError: unknown language: fr
```

<br>

* The text between the first and last line is not relevant.

</v-click>
</div>
</div>

---

# Doctest directives

* Sometimes, we are not interested in the error message but only that the correct exception type is raised.
* Then, doctest directives can be used.

<br>

#### Example:

```python
"""
>>> welcome('Alice', lang='fr') # doctest: +ELLIPSIS
Traceback (most recent call last):
ValueError: ...
"""
```

* Here, the ellipsis (`...`) replaces arbitrary text
* For a list of directives see the [`doctest` documentation](https://docs.python.org/3/library/doctest.html#doctest-options)
* Of interest are in particular: `NORMALIZE_WHITESPACE`, `SKIP`, and `IGNORE_EXCEPTION_DETAIL`

---
layout: gli-two-cols-header
---

# Pascal's triangle as an example

::left::

```python
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
        line = ' '.join(f'{x:2}' for x in pascal(n))
        print(str(n)+line.center(25))
```

::right::

```console
$ python pascal.py
0             1
1           1  1
2          1  2  1
3        1  3  3  1
4       1  4  6  4  1
5     1  5 10 10  5  1
6    1  6 15 20 15  6  1
```

---

# Ideas for test cases

1. explicit tests for certain lines
1. sum of elements in line n should be 2<sup>n</sup>
1. alternating sum of elements in a line should be 0
1. line can be obtained from the previous line by appropriate summation

<br>

* These tests are independent of the logic of the program where
  binomial coefficients are calculated sequentially.
* First test is mostly convenient for small line numbers n and testing
  of the corner case n=0
* The other tests work well also for large line numbers.

---

# Testing elements in a line with small line number

<div class="grid grid-cols-[35%_1fr] gap-4">
<div>

```python
# test_pascal.py

from pascal import pascal

def test_n0():
    assert list(pascal(0)) == [1]

def test_n1():
    assert list(pascal(1)) == [1, 1]

def test_n5():
    expected = [1, 4, 6, 4, 1]
    assert list(pascal(5)) == expected
```

<br>

* use `assert` for testing

<br>

* an error was inserted into the last test intentionally

</div>
<div>

```console
$ pytest
============================= test session starts =============================
platform linux -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0
rootdir: /home/ingold/pascal
plugins: anyio-3.5.0
collected 3 items                                                             

test_pascal.py ..F                                                      [100%]

================================== FAILURES ===================================
___________________________________ test_n5 ___________________________________

    def test_n5():
        expected = [1, 4, 6, 4, 1]
>       assert list(pascal(5)) == expected
E       assert [1, 5, 10, 10, 5, 1] == [1, 4, 6, 4, 1]
E         At index 1 diff: 5 != 4
E         Left contains one more item: 1
E         Use -v to get more diff

test_pascal.py:13: AssertionError
=========================== short test summary info ===========================
FAILED test_pascal.py::test_n5 - assert [1, 5, 10, 10, 5, 1] == [1, 4, 6, 4, 1]
========================= 1 failed, 2 passed in 0.05s =========================
```

</div>
</div>

---

# Tests which are expected to fail

<div class="grid grid-cols-[35%_1fr] gap-4">
<div>

````md magic-move
```python
# test_pascal.py

from pascal import pascal

def test_n0():
    assert list(pascal(0)) == [1]

def test_n1():
    assert list(pascal(1)) == [1, 1]

def test_n5():
    expected = [1, 4, 6, 4, 1]
    assert list(pascal(5)) == expected
```
```python {all|12|3}
# test_pascal.py

import pytest
from pascal import pascal

def test_n0():
    assert list(pascal(0)) == [1]

def test_n1():
    assert list(pascal(1)) == [1, 1]

@pytest.mark.xfail
def test_n5():
    expected = [1, 4, 6, 4, 1]
    assert list(pascal(5)) == expected
```
````

</div>
<div>
<v-click>

```console
$ pytest
============================= test session starts =============================
platform linux -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0
rootdir: /home/ingold/pascal
plugins: anyio-3.5.0
collected 3 items                                                             

test_pascal.py ..x                                                      [100%]

======================== 2 passed, 1 xfailed in 0.02s =========================
```

</v-click>
</div>
</div>

<v-click>

<br>

* import `pytest` and decorate test function
* tests expected to fail are marged with an `x`
* if the test would have passed instead, it would be marked with an `X`

</v-click>

---

# Skipping a test

```python
@pytest.mark.skip(reason="just for demonstration")
def test_n5():
    expected = [1, 4, 6, 4, 1]
    assert list(pascal(5)) == expected
```

```console
$ pytest -r s
======================================= test session starts =======================================
platform linux -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0
rootdir: /home/gli/testing
plugins: anyio-3.5.0
collected 3 items                                                                                 

test_pascal.py ..s                                                                          [100%]

===================================== short test summary info =====================================
SKIPPED [1] test_pascal.py:13: just for demonstration
================================== 2 passed, 1 skipped in 0.01s ===================================
```

* `s` indicates a skipped test
* option `-r s` is needed for the reason to be listed

---

# All tests pass

<div class="grid grid-cols-[35%_1fr] gap-4">
<div>

````md magic-move
```python
# test_pascal.py

from pascal import pascal

def test_n0():
    assert list(pascal(0)) == [1]

def test_n1():
    assert list(pascal(1)) == [1, 1]

def test_n5():
    expected = [1, 4, 6, 4, 1]
    assert list(pascal(5)) == expected
```
```python
# test_pascal.py

from pascal import pascal

def test_n0():
    assert list(pascal(0)) == [1]

def test_n1():
    assert list(pascal(1)) == [1, 1]

def test_n5():
    expected = [1, 5, 10, 10, 5, 1]
    assert list(pascal(5)) == expected
```
````

</div>
<div>
<v-click>

```console
============================ test session starts ============================
platform linux -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0
rootdir: /home/ingold/pascal
plugins: anyio-3.5.0
collected 3 items                                                           

test_pascal.py ...                                                    [100%]

============================= 3 passed in 0.01s =============================
```

<br>

* The three dots indicated three passing tests.

</v-click>
</div>
</div>

<br>

<v-click>

* Now we can add more tests according to the ideas listed earlier.

</v-click>

---

# Sum and alternating sum

<div class="grid grid-cols-[40%_1fr] gap-4">
<div>

```python
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
```

</div>
<div>

```console
======================= test session starts ========================
platform linux -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0 -- ↩
/home/ingold/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /home/ingold/pascal
plugins: anyio-3.5.0
collected 5 items                                                        

test_pascal.py::test_n0 PASSED                               [ 20%]
test_pascal.py::test_n1 PASSED                               [ 40%]
test_pascal.py::test_n5 PASSED                               [ 60%]
test_pascal.py::test_sum PASSED                              [ 80%]
test_pascal.py::test_alternate_sum PASSED                    [100%]

======================== 5 passed in 0.07s =========================
```

</div>
</div>

<br>

* There is no problem in going to rather high line numbers.
* The function name `alternate` does not start with `test` because it should not
  be executed as a test.

---

# Completion of the tests

<div class="grid grid-cols-[40%_1fr] gap-4">
<div>

```python
# test_pascal.py

from itertools import chain
from pascal import pascal

def test_n0():
    assert list(pascal(0)) == [1]

def test_n1():
    assert list(pascal(1)) == [1, 1]

def test_n5():
    expected = [1, 5, 10, 10, 5, 1]
    assert list(pascal(5)) == expected

def test_sum():
    for n in (10, 100, 1000, 10000):
        assert sum(pascal(n)) == 2**n
```

</div>
<div>

```python
def test_alternate_sum():
    for n in (10, 100, 1000, 10000):
        assert sum(alternate(pascal(n))) == 0

def alternate(g):
    sign = 1
    for elem in g:
        yield sign*elem
        sign = -sign

def test_generate_next_line():
    for n in (10, 100, 1000, 10000):
        for left, right, new in zip(chain([0], pascal(n)),
                                    chain(pascal(n), [0]),
                                    pascal(n+1)):
            assert left+right == new
```

</div>
</div>

#### Problem:
* The loops do not constitute individual tests.
* Once a test fails within the loop, the test function exits.

---

# Parametrization of tests

<div class="grid grid-cols-[1fr_1fr] gap-4">
<div>

```python
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
```

</div>
<div>

```python
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
```
</div>
</div>

<br>

* This test suite now amounts to a total of 15 individual tests which are all
  executed.

---

# Testing for exceptions

<div class="grid grid-cols-[1fr_1fr] gap-4">
<div>

```python
def pascal(n):
    """create the n-th line of Pascal's triangle

    The line numbers start with n=0 for the line
    containing only the entry 1. The elements of
    a line are generated successively.

    """
    if n < 0:
        raise ValueError(
            f"n should not be negative, got {n}"
                         )
    x = 1
    yield x
    for k in range(n):
        x = x*(n-k)//(k+1)
        yield x
```

</div>
<div>

```python
def test_negative_int():
    with pytest.raises(ValueError):
        next(pascal(-1))
```

```console
$ pytest
======================== test session starts ========================
platform linux -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0
rootdir: /home/ingold/pascal
plugins: anyio-3.5.0
collected 16 items                                                  

test_pascal.py ................                               [100%]

======================== 16 passed in 0.16s =========================
```

</div>
</div>

<br>

* Execute the test under the `pytest.raises` context manager.
* `pascal` returns a generator. We therefore need to explicitly asked for the 
  next element.

---

# Extension to floats

* The entries in Pascal's triangle are binomial coefficients which appear in
  $(1+x)^n$.  
  Example:
  $$(1+x)^4 = x^4+4x^3+6x^2+4x+1$$
* Calculating a row of Pascals's triangle can be extended to float numbers
  if we use float arithmetics instead of integer arithmetics. Then, the
  generated numbers will not terminate.  
  Example:
  $$(1+x)^{1/3} = 1+\frac{1}{3}x-\frac{1}{9}x^2+\frac{5}{81}x^3+\ldots$$

<br>

* Let us rewrite our code for float arithmetics and test the coefficients.

---

# Adapted code for Pascal's triangle

<div class="grid grid-cols-[1fr_1fr] gap-4">
<div>

````md magic-move
```python
# pascal.py

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
```
```python
# pascal_float.py

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
```
```python
# pascal_float.py

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

if __name__ == "__main__":
    for _, x in zip(range(10), taylor_power(1/3)):
        print(x)
```
````

</div>
<div>
<v-click>

```console
$ python taylor_power.py 
1
0.3333333333333333
-0.11111111111111112
0.0617283950617284
-0.0411522633744856
0.03017832647462277
-0.023472031702484377
0.019001168521058785
-0.015834307100882322
0.013488483826677534
```

<br>

* These results correspond to 1, 1/3, -1/9, and 5/81,
  and so on as expected.

</v-click>
</div>
</div>

---

# The problem with `assert` and floats

<div class="grid grid-cols-[35%_1fr] gap-4">
<div>

```python
# test_taylor_power.py

import pytest
from pascal_float import taylor_power

def test_one_third():
    p = taylor_power(1/3)
    result = [next(p) for _ in range(4)]
    expected = [1, 1/3, -1/9, 5/81]
    assert result == expected
```

<br>

* rounding errors can make assertion fail
* similarly it is usually not a good idea to
  test floats for equality with zero

</div>
<div>

```console
$ pytest
============================= test session starts =============================
⋮

test_taylor_power.py F                                                  [100%]

================================== FAILURES ===================================
_______________________________ test_one_third ________________________________

    def test_one_third():
        p = taylor_power(1/3)
        result = [next(p) for _ in range(4)]
        expected = [1, 1/3, -1/9, 5/81]
>       assert result == expected
E       assert [1, 0.3333333...7283950617284] == [1, 0.3333333...2839506172839]
E         At index 2 diff: -0.11111111111111112 != -0.1111111111111111
E         Use -v to get more diff

test_taylor_power.py:7: AssertionError
=========================== short test summary info ===========================
FAILED test_taylor_power.py::test_one_third - assert [1, 0.3333333... ↩
7283950617284] == [1, 0.3333333...2839506172839]
============================== 1 failed in 0.05s ==============================
```

</div>
</div>

---

# Testing floats with `pytest.approx`

```python
import pytest
from pascal_float import taylor_power

def test_one_third():
    p = taylor_power(1/3)
    result = [next(p) for _ in range(4)]
    expected = [1, 1/3, -1/9, 5/81]
    assert result == pytest.approx(expected, abs=0, rel=1e-15)
```

```console
$ pytest
============================= test session starts =============================
platform linux -- Python 3.11.5, pytest-7.4.0, pluggy-1.0.0
rootdir: /home/ingold/pascal
plugins: anyio-3.5.0
collected 1 item                                                              

test_taylor_power.py .                                                  [100%]

============================== 1 passed in 0.01s ==============================
```

* If the threshold `abs` for the absolute error is not given, its default
  value 10<sup>-12</sup> might take precedence over the relative error.

---

# There is more in testing

* More extensive collections of test functions can be grouped in classes.
* Fixtures can provide data to several tests.
* It is possible to provide setup and teardown functions for tests, e.g.
  when working with databases.
* Mocking allows to handle external dependencies, e.g. when connecting to
  an external data source or when use the current time. `unittest.mock`
  is part of the Python standard library.

<br>

* Documentation of pytest: [docs.pytest.org](https://docs.pytest.org/)
