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
  * there exist other frameworks like `unittest` and `nose`
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

* load the `doctext`-module for execution
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
