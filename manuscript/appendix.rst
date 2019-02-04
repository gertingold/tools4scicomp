========
Appendix
========

.. _appendixdecorators:

Decorators
==========

In this appendix, we give a short introduction to decorators so that we have an idea
of what they are about when making use of them. Decorators are a way to modify the
behavior of functions, methods, or classes. We will restrict our discussion to functions.
The effect of a decorator is then to replace the function by a modified version of
the original function. Some examples will demonstrate how this works.

For the first example we assume that our script defines a couple of functions which we
would like to register. To keep things simple, registering a function shall simply mean
that an appropriate message is printed.

.. code-block:: python
   :linenos:

   def register(func):
       print(f'{func.__name__} registered')
       return func

   @register
   def myfunc():
       print('executing myfunc')

   @register
   def myotherfunc():
       print('executing myotherfunc')

   print('-'*40)
   myfunc()
   myotherfunc()

In lines 1-3 we define a decorator called ``register`` which is then applied in lines
5 and 9 to two functions ``myfunc`` and ``myotherfunc``. Running the script produces
the following output::

   myfunc registered
   myotherfunc registered
   ----------------------------------------
   executing myfunc
   executing myotherfunc

What has happened? Before running the code in lines 13-15, Python has defined the functions
in the lines 1-11. When getting to ``myfunc``, the decorator ``register`` will come into
action. Its argument ``func`` will be the function ``myfunc``, i.e. the argument of a decorator
is implicitly given by the function following the decorator statement. Then, ``register``
is executed, first printing a message which contains the name of the decorated function.
Then it returns the function ``myfunc`` unmodified. The effect of the decorator thus is
simply to print a message that the function ``myfunc`` has been registered. As the output
reproduced above shows, this is only done once, namely when Python processes the function
code. Later, the function is executed which was returned by the decorator. In our case, this
is simply the original function.

The decorator can also be used to modify the function so that a desired effect
occurs each time the function is executed. In the following example, we define
a somewhat more complex decorator named ``logging`` which prints a message when
the function is starting execution and another message indicating the time of
execution just before the function finishes execution. The interest of using
the ``logging`` decorator is to analyse how the execution of a recursive function
works.

.. code-block:: python
   :linenos:

   import time
   from itertools import chain

   def logging(func):
       def func_with_log(*args, **kwargs):
           arguments = ', '.join(map(repr, chain(args, kwargs.items())))
           print(f'calling {func.__name__}({arguments})')
           start = time.time()
           result = func(*args, **kwargs)
           elapsed = time.time()-start
           print(f'got {func.__name__}({arguments}) = {result} '
                 f'in {elapsed*1000:5.3f} ms')
           return result
       return func_with_log
   
   @logging
   def factorial(n):
       if n == 1:
           return 1
       else:
           return n*factorial(n-1)
   
   factorial(5)

The main difference to our first example consists in the fact that the
decorator in lines 5-14 defines a new function. As a consequence, the
modifications apply whenever the decorated function is run. Then new function
``func_with_log`` is written in a rather general way to allow its use for
arbitrary functions. In particular, the decorated function can take an
arbitrary number of arguments including keyword arguments. Whenever the
decorated function is executed, it will print a message including the arguments
with which the function was called. In addition, the starting time is stored.
Then, the original function, in our case ``factorial``, is run and when it
returns, the elapsed time is determined. Before quitting, the result 
together with the elapsed time are printed.

Running the script, we obtain the following output::

   calling factorial(5)
   calling factorial(4)
   calling factorial(3)
   calling factorial(2)
   calling factorial(1)
   got factorial(1) = 1 in 0.001 ms
   got factorial(2) = 2 in 0.042 ms
   got factorial(3) = 6 in 0.069 ms
   got factorial(4) = 24 in 0.094 ms
   got factorial(5) = 120 in 0.127 ms
   
It nicely demonstrates how the function ``factorial`` is called recursively
until the recursion comes to an end when the argument equals 1.

A decorator could even go as far as not running the decorated function at all
and possibly returning a result nevertheless. A situation where such a decorator
could make sense is during testing. Suppose that we want to test a program which
relies on obtaining data from a measuring device. If we are not interested in
testing the connection to the device but only how received data are handled, an
appropriate decorator would allows us to test the program even without connection
to the measuring device as long as the decorator provides us with appropriate
data.
