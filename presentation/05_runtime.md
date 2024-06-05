---
layout: section
---

# Run-time analysis

---
layout: quote
---

# Donald E. Knuth on run-time optimization

<br>

<div class="grid grid-cols-[4%_1fr] gap-4">
<div><carbon-quotes class="text-3xl"/></div><div>
  There is no doubt that the grail of efficiency leads to abuse. Programmers
  waste enormous amounts of time thinking about, or worrying about, the speed of
  noncritical parts of their programs, and these attempts at efficiency actually
  have a strong negative impact when debugging and maintenance are considered. We
  should forget about small efficiencies, say about 97 % of the time: premature
  optimization is the root of all evil.

  Yet we should not pass up our opportunities in that critical 3 %. A good
  programmer will not be lulled into complacency by such reasoning, he will be
  wise to look carefully at the critical code; but only after that code has been
  identified.
</div></div>

<br>

<div style="text-align: right">
D. E. Knuth, ACM Comp. Surveys <b>6</b>, 261 (1974) <a href="https://doi.org/10.1145/356635.356640"><carbon-launch /></a>
</div>

---

# Scaling of run-time with problem size 

### Example from [Project Euler](https://projecteuler.net/problem=18)

<br />

<img src="/images/projecteuler_problem18.png" style="width: 63%; margin: auto">

---

# A naive solution

```python {all|25-36|26,36}{maxHeight:'450px'}
from itertools import product
import math
import time
import numpy as np
import matplotlib.pyplot as plt

origdata = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

data = [[int(x) for x in line.split(" ")] for line in origdata.split("\n")]

def partial_sums(maxline):
    start = time.time()
    sums = []
    for path in product((0,1), repeat=maxline):
        path_sum = data[0][0]
        idx = 0
        for lineno, step in enumerate(path):
            idx = idx + step
            path_sum = path_sum + data[lineno+1][idx]
        sums.append(path_sum)
    time_needed = time.time() - start
    return time_needed

nvalues = np.arange(len(data))
logduration = np.empty(len(data))
for n in nvalues:
    logduration[n] = math.log10(partial_sums(n))
plt.plot(nvalues, logduration, 'o')
plt.xlabel('$n$')
plt.ylabel('$log_{10}(T)$')
plt.show()
```

---

# Dependence of run-time on problem size

<img src="/images/t_pe18a.png" style="width: 50%; margin: auto">

<br />

* For the naive solution, the run-time increases *exponentially* with the
  problem size. <carbon-face-dissatisfied class="text-red-800 text-3xl" />

---

# A better solution

```python {all|24-33}{maxHeight:'450px'}
import math
import time
import numpy as np
import matplotlib.pyplot as plt

origdata = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

data = [[int(x) for x in line.split(" ")] for line in origdata.split("\n")]

def partial_sum(maxline):
    start = time.time()
    sums = data[maxline]
    for level in range(maxline-1, -1, -1):
        newsums = []
        for nr, element in enumerate(data[level]):
            newsums.append(max(element+sums[nr], element+sums[nr+1]))
        sums = newsums
    time_needed = time.time() - start
    return time_needed

nvalues = np.arange(len(data))
duration = np.empty(len(data))
for n in nvalues:
    duration[n] = math.sqrt(partial_sum(n))
plt.plot(nvalues, duration, 'o')
plt.xlabel('$n$')
plt.ylabel('$\sqrt{T}$')
plt.show()

```

---

# Dependence of run-time on problem size

<img src="/images/t_pe18b.png" style="width: 50%; margin: auto">

<br />

* A better solution starts at the last line and works its way upwards.
* For this solution, the run-time increases only *quadratically* with the
  problem size. <carbon-face-satisfied class="text-green-800 text-3xl" />
* Polynomial is better than exponential, but for a given problem size, the prefactor may
  also be relevant.

---

# Reduction of run-time with more hardware

* distribute tasks over a number of compute nodes of a compute cluster
* even a single CPU contains several cores allowing for parallel computation
* GPUs may be useful if the communication overhead does not become too high
  * architecture supports very well the manipulation of matrices
  * for machine learning tasks high numerical precession is not necessarily needed
  * [CuPy](https://cupy.dev) as a drop-in replacement for most of the NumPy and SciPy libraries,
    runs on NVIDIA GPUs
* human ressources often more costly than hardware ressources

<br />

* BUT: computers need energy to run and thus contribute to the climate change

example: [meta-llama/Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B)

<img src="/images/meta-llama-3-8b.png" style="width: 70%; margin: auto">

---

# Energy efficiency

<img src="/images/green500.png" style="width: 80%; margin: auto">

---

# Reduction of run-time with the right software

* use of appropriate libraries like NumPy and SciPy for numerical tasks
* write time-critical parts e.g. in C
  * autogeneration of C code from Python-like code with [Cython](https://cython.org)
* just in time compilation (JIT)
  * [PyPy](https://www.pypy.org)
  * [Numba](https://numba.pydata.org/): often adding a simple decorator to the most
    critical function is sufficient, but sometimes rewriting the code more in C-style
    may be appropriate

<br />

### Main question:

* Which parts of the program are most time critical and need to be accelerated?<br />  
  <carbon-arrow-right /> profiling of code

---

# Simple time measurements

<div class="grid grid-cols-[35%_1fr] gap-4"><div>

```python
>>> import time
>>> time.ctime()
'Mon Jun  3 12:22:17 2024'
```

</div><div>

* Even though we can obtain the current time, the format is not does not allow to 
  simply calculate time differences.

</div></div>
<div class="grid grid-cols-[35%_1fr] gap-4"><div>

```python
>>> time.time()
1717410254.1613576
```

</div><div>

* Here, the currect time is given in seconds since the begin of the epoch. On Unix systems,
  the epoch starts on January 1, 1970 at 00:00:00 UTC.

</div></div>
<div class="grid grid-cols-[35%_1fr] gap-4"><div>

```python
import time

for _ in range(10):
    sum_of_ints = 0
    start = time.time()
    for n in range(1000000):
        sum_of_ints = sum_of_ints + 1
    end = time.time()
    print(f'{end-start:5.3f}s', end='  ')
```

</div><div>

* timing results fluctuate

  first run:
  ```
  0.072s  0.075s  0.078s  0.080s  0.082s  0.085s  0.087s  0.089s 0.090s  0.093s
  ```

  second run:
  ```
  0.069s  0.094s  0.075s  0.076s  0.078s  0.080s  0.081s  0.083s  0.085s  0.086s
  ```

* it makes sense to average over several runs

</div></div>

---

# Time vs. process time

* CPUs are multitasking. Compute time is shared between different processes running
  in parallel and/or sequentially for short time intervals. Other processes may
  influence the time required to run the script

```python
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
```

```bash
total time:   10.065s
process time: 0.064s
```

* time measures the total elapsed time (wall time)
* process time measures the time spent in the specific process running the script

---
layout: gli-two-cols-header
---

# Overhead when calling a function

::left::

```python
import time

sum_of_ints = 0
start_proc = time.process_time()
for n in range(10000000):
    sum_of_ints = sum_of_ints + 1
end_proc = time.process_time()
print(f'process time: {end_proc-start_proc:5.3f}s')
```

* average over 10 runs: 0.9071 s

::right::

```python
import time

def increment_by_one(x):
    return x+1

sum_of_ints = 0
start_proc = time.process_time()
for n in range(10000000):
    increment_by_one(sum_of_ints)
end_proc = time.process_time()
print(f'process time: {end_proc-start_proc:5.3f}s')
```

* average over 10 runs: 0.9843 s

::bottom::

* details matter
* timing can influence the run time
* The approach used so far requires a modification of the code.
  There should be a better way.

---

# `timeit` module

```python
>>> import timeit
>>> timeit.timeit('0.5**2')
0.007943803999978627
```

* The command has been executed one million times. Therefore, the result given in seconds
  should actually be interpreted as microseconds. The evaluation of the square thus requires
  8 nanoseconds.

```python
>>> x = 0.5
>>> timeit.timeit('x**2')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/opt/anaconda3/lib/python3.11/timeit.py", line 237, in timeit
    return Timer(stmt, setup, timer, globals).timeit(number)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/anaconda3/lib/python3.11/timeit.py", line 180, in timeit
    timing = self.inner(it, self.timer)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<timeit-src>", line 6, in inner
NameError: name 'x' is not defined
```

* By default, `timeit` does not have access to the outside scope.

---

# `timeit` module (cont'd)

```python
>>> x = 0.5
>>> timeit.timeit('x**2', globals=globals())
0.04229282000005696
```

* One possibility is to give `timeit` access to the variables known globally.

<br />

```python
>>> timeit.timeit('x**2', 'x = 0.5')
0.039870551000149135
```

* A second possibility is to define the value of `x` in the setup command given in the
  second argument.

<br />

```python
>>> timeit.timeit('math.pow(x, 2)', 'import math; x=0.5')
0.04683635499986849
```

* Comparison with the power function from the `math`-module. The execution time of the
  setup code is not taken into account.

---

# A more complex `timeit` example

<div class="grid grid-cols-[50%_1fr] gap-4"><div>

```python {all}{maxHeight:'450px'}
import math
from timeit iomport timeit
import numpy as np
import matplotlib.pyplot as plt

def f_numpy(nmax):
    x = np.linspace(0, np.pi, nmax)
    result = np.sin(x)

def f_math(nmax):
    dx = math.pi/(nmax-1)
    result = [math.sin(n*dx) for n in range(nmax)]

x = []
y = []
for n in np.logspace(0.31, 6, 300):
    nint = int(n)
    t_numpy = timeit.timeit('f_numpy(nint)',
                            number=10, globals=globals())
    t_math = timeit.timeit('f_math(nint)',
                           number=10, globals=globals())
    x.append(nint)
    y.append(t_math/t_numpy)

plt.rc('text', usetex=True)
plt.plot(x, y, 'o')
plt.xscale('log')
plt.xlabel('vector size', fontsize=20)
plt.ylabel(r'$t_\mathrm{math}/t_\mathrm{numpy}$',
           fontsize=20)
plt.show()
```

</div><div>

* the argument `number` determines the number of repetitions
* a small value for `number` has been chosen to limit the
  overall run-time

<br />

<img src="/images/timeit_numpy.png" style="width: 85%; margin: auto">

</div></div>

---

# Additional remarks on `timeit`

```python
>>> import timeit
>>> timeit.repeat('x**2', 'x = 0.5', repeat=10)
[0.040641365000738006, 0.0370813729996371, 0.036742248000336986, 0.0370534020003106, 0.03691889000037918,↩
 0.03718556300009368, 0.036579982999683125, 0.0371491790001528, 0.03664499499973317, 0.036883825999211695]
```

* `timeit.repeat` repeats the timing run a number of times specified by the `repeat` argument

<br />
<br />

### `timeit` magic in Jupyter notebooks

<br />

<div class="grid grid-cols-[50%_1fr] gap-4"><div>
<img src="/images/timeit_magic.png" style="width: 100%; margin: auto">
</div><div>

* The `%%timeit` magic contains the setup code in the first line followed by an arbitrary number of code lines
  for which the run-time is determined.
* The number of loops is determined such that the overall time required is reasonable.

</div></div>

---

# `cProfile` module

* `timeit` only determines the overall run-time.
* For a more detailed analysis, the `cProfile` module can be used.

<br />

* `cProfile` helps to identify the pieces of code where most of the
  time is spent
* This process is called *profiling*.

<br />

* Profiling induces some overhead so that the overall run-time is larger than without profiling.
* For a run-time analysis and scaling with problem size, it is better to use the `timeit` module.

---

# An example

We will explain profiling by considering the code producing the following figure which shows
the evolution of a Gaussian quantum state in an infinite potential well (see e.g. 
[W. Kinzel, Phys. Bl. **51**, 1190 (1995)](https://doi.org/10.1002/phbl.19950511215);
[I. Marzoli *et al.*, Acta Phys. Slov. **48**, 323 (1998)](http://www.physics.sk/aps/pubs/1998/aps_1998_48_3_323.pdf))

<img src="/images/carpet.png" style="width: 75%; margin: auto">

---

# A first attempt

```python {all}{maxHeight:'450px'}
# carpet.py

from math import cos, exp, pi, sin, sqrt
from cmath import exp as cexp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

class InfiniteWell:
    def __init__(self, psi0, width, nbase, nint):
        self.width = width
        self.nbase = nbase
        self.nint = nint
        self.coeffs = self.get_coeffs(psi0)

    def eigenfunction(self, n, x):
        if n % 2:
            return sqrt(2/self.width)*sin((n+1)*pi*x/self.width)
        return sqrt(2/self.width)*cos((n+1)*pi*x/self.width)

    def get_coeffs(self, psi):
        coeffs = []
        for n in range(self.nbase):
            f = lambda x: psi(x)*self.eigenfunction(n, x)
            c = trapezoidal(f, -0.5*self.width, 0.5*self.width, self.nint)
            coeffs.append(c)
        return coeffs

    def psi(self, x, t):
        psit = 0
        for n, c in enumerate(self.coeffs):
            psit = psit + c*cexp(-1j*(n+1)**2*t)*self.eigenfunction(n, x)
        return psit

def trapezoidal(func, a, b, nint):
    delta = (b-a)/nint
    integral = 0.5*(func(a)+func(b))
    for k in range(1, nint):
        integral = integral+func(a+k*delta)
    return delta*integral

def psi0(x):
    sigma = 0.005
    return exp(-x**2/(2*sigma))/(pi*sigma)**0.25

w = InfiniteWell(psi0=psi0, width=2, nbase=100, nint=1000)
x = np.linspace(-0.5*w.width, 0.5*w.width, 500)
ntmax = 1000
z = np.zeros((500, ntmax))
for n in range(ntmax):
    t = 0.25*pi*n/(ntmax-1)
    y = np.array([abs(w.psi(x, t))**2 for x in x])
    z[:, n] = y
z = z/np.max(z)
plt.rc('text', usetex=True)
plt.imshow(z, cmap=cm.hot)
plt.xlabel('$t$', fontsize=20)
plt.ylabel('$x$', fontsize=20)
plt.show()
```

---

# Profiling the `carpet.py` script

```bash
$ python -m cProfile -o carpet.prof carpet.py
```

* The profiling data are rewritten into a file `carpet.prof` as indicated by the option `-o`.
* The data in `carpet.prof` can then be displayed in various ways with the following columns:

<br />

<div class="grid grid-cols-[30%_1fr] gap-4">
 <div><code>ncalls</code></div>
 <div>number of calls</div>
 <div><code>tottime</code></div>
 <div>total time spent in the given function (and excluding time made in calls to sub-functions)</div>
 <div><code>percall</code></div>
 <div>tottime divided by number of calls</div>
 <div><code>cumtime</code></div>
 <div>Cumulative time spent in this and all subfunctions (from invocation till exit). This figure is accurate even for recursive functions.</div>
 <div><code>percall</code></div>
 <div>cumtime divided by number of primitive calls</div>
 <div><code>filename:lineno(function)</code></div>
 <div>function to which the data refer</div>
</div>

---

# Displaying the profiling data

```python
>>> import pstats
>>> p = pstats.Stats('carpet.prof')
>>> p.sort_stats('time').print_stats(15)
```

<br />

* Here, the usually rather lengthy output is limited to 15 entries.
* The data can be sorted according to different criteria. The most important ones are
  `time` or `tottime` (internal time), `cumtime` (cumulative time) and `calls` (call
  count). For more details, see the [documentation](https://docs.python.org/3/library/profile.html#pstats.Stats.sort_stats).

<br />

* It is a good idea to take a look at the number of calls and to check whether
  the results given make sense. Frequently, one finds that a certain evaluation
  is done unnecessarily often. 
* Parts of the code with a rather short run-time can be time costly if executed
  very often.

---

# Result of the profiling run

```bash
Wed Jun  5 09:16:31 2024    carpet.prof

         202758242 function calls (202739498 primitive calls) in 106.647 seconds

   Ordered by: internal time
   List reduced from 4256 to 15 due to restriction <15>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   500000   39.380    0.000   97.612    0.000 carpet.py:27(psi)
 50100100   37.933    0.000   49.642    0.000 carpet.py:14(eigenfunction)
 50000000    8.640    0.000    8.640    0.000 {built-in method cmath.exp}
        1    7.482    7.482    7.686    7.686 {built-in method exec}
 50100101    4.295    0.000    4.295    0.000 {built-in method math.sqrt}
 25050129    3.825    0.000    3.825    0.000 {built-in method math.cos}
 25050129    3.590    0.000    3.590    0.000 {built-in method math.sin}
     1000    0.393    0.000   98.079    0.098 carpet.py:50(<listcomp>)
        1    0.084    0.084    0.084    0.084 {built-in method show}
   501506    0.075    0.000    0.075    0.000 {built-in method builtins.abs}
       29    0.070    0.002    0.070    0.002 {method 'readline' of '_io.BufferedReader' objects}
     7309    0.050    0.000    0.077    0.000 /opt/anaconda3/lib/python3.11/inspect.py:867(cleandoc)
    54/52    0.037    0.001    0.042    0.001 {built-in method _imp.create_dynamic}
   100100    0.034    0.000    0.120    0.000 carpet.py:22(<lambda>)
     1775    0.032    0.000    0.032    0.000 {built-in method numpy.array}
```

---

# What do we learn from these two lines?

```bash
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   500000   39.380    0.000   97.612    0.000 carpet.py:27(psi)
 50100100   37.933    0.000   49.642    0.000 carpet.py:14(eigenfunction)
```

* The time for each call is small but the total time is significant because the
  number of calls is large.
* Our figure contains 500×1000 points. Therefore, the 500000 calls of `psi` make
  sense.
* `eigenfunction` is called from `get_coeffs` and from `psi`. 
* In order to determine the expansion coefficients, we use 100 basis functions
  at 1001 nodes resulting in 100100 calls. This is small compared to 50100100
  and is not relevant, at least for the moment. 
* Can we reduce the number of the remaining 50000000 calls?
* For each one of the 500000 image points, we evaluate 100 eigenfunctions, resulting
  in 50000000 calls. So the given number makes sense.
* BUT: The eigenfunctions do not depend on time. Therefore, we unnecessarily repeat
  the evaluation of the eigenfunctions 1000 times.  <carbon-arrow-right /> There is clearly room for improvement.

---

# Using a cache

````md magic-move
```python
    def __init__(self, psi0, width, nbase, nint):
        self.width = width
        self.nbase = nbase
        self.nint = nint
        self.coeffs = self.get_coeffs(psi0)

    def psi(self, x, t):
        psit = 0
        for n, c in enumerate(self.coeffs):
            psit = psit + c*cexp(-1j*(n+1)**2*t)*self.eigenfunction(n, x)
        return psit
```
```python
    def __init__(self, psi0, width, nbase, nint):
        self.width = width
        self.nbase = nbase
        self.nint = nint
        self.coeffs = self.get_coeffs(psi0)
        self.eigenfunction_cache = {}


    def psi(self, x, t):
        if not x in self.eigenfunction_cache:
            self.eigenfunction_cache[x] = [self.eigenfunction(n, x)
                                           for n in range(self.nbase)]
        psit = 0
        for n, (c, ef) in enumerate(zip(self.coeffs, self.eigenfunction_cache[x])):
            psit = psit + c*ef*cexp(-1j*(n+1)**2*t)
        return psit
```
````

<v-click>

* The eigenfunctions are stored in a cache realized in form of a dictionary.
* The cache has size of 100×500×8 Bytes ≈ 390 kB.
* The cache reduces the overall run-time by a factor of 2.4. The factor will in
  general depend on the hardware used.

</v-click>

---

```bash
Wed Jun  5 13:32:07 2024    carpet.prof

         52911733 function calls (52892976 primitive calls) in 32.833 seconds

   Ordered by: internal time
   List reduced from 4257 to 15 due to restriction <15>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   500000   22.029    0.000   28.184    0.000 carpet.py:28(psi)
 50000000    6.115    0.000    6.115    0.000 {built-in method cmath.exp}
        1    3.223    3.223    3.430    3.430 {built-in method exec}
     1000    0.313    0.000   28.549    0.029 carpet.py:54(<listcomp>)
       29    0.070    0.002    0.070    0.002 {method 'readline' of '_io.BufferedReader' objects}
        1    0.066    0.066    0.067    0.067 {built-in method show}
   150100    0.063    0.000    0.082    0.000 carpet.py:15(eigenfunction)
   501506    0.051    0.000    0.051    0.000 {built-in method builtins.abs}
     7309    0.049    0.000    0.077    0.000 /opt/anaconda3/lib/python3.11/inspect.py:867(cleandoc)
    54/52    0.037    0.001    0.042    0.001 {built-in method _imp.create_dynamic}
   100100    0.033    0.000    0.118    0.000 carpet.py:23(<lambda>)
      308    0.030    0.000    0.030    0.000 {built-in method marshal.loads}
   100100    0.028    0.000    0.034    0.000 carpet.py:44(psi0)
     1788    0.028    0.000    0.028    0.000 {built-in method numpy.array}
        1    0.023    0.023    0.023    0.023 {built-in method addToolBar}
```

---

# Effect of the cache

### before

```bash
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   500000   39.380    0.000   97.612    0.000 carpet.py:27(psi)
 50100100   37.933    0.000   49.642    0.000 carpet.py:14(eigenfunction)
```

### after

```bash
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   500000   22.029    0.000   28.184    0.000 carpet.py:28(psi)
   150100    0.063    0.000    0.082    0.000 carpet.py:15(eigenfunction)
```

<br />

* The number of calls to `eigenfunction` now fits our expectation.
* By making the cache also available outside of the function `psi, the number
  of calls could be reduced even further.
* The time required by `eigenfunction` is now negligible compared to total
  run-time.
* We could now continue to improve the code, e.g. by caching results for the
  expoential functions. However, it makes more sense to make use of NumPy
  universal functions.

---

# Version with NumPy

```python {all}{maxHeight:'350px'}
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

class InfiniteWell:
    def __init__(self, psi0, width, nbase, nint):
        self.width = width
        self.nbase = nbase
        self.nint = nint
        self.coeffs = trapezoidal(lambda x: psi0(x)*self.eigenfunction(x),
                                  -0.5*self.width, 0.5*self.width, self.nint)

    def eigenfunction(self, x):
        assert x.ndim == 1
        normalization = sqrt(2/self.width)
        args = (np.arange(self.nbase)[:, np.newaxis]+1)*np.pi*x/self.width
        result = np.empty((self.nbase, x.size))
        result[0::2, :] = normalization*np.cos(args[0::2])
        result[1::2, :] = normalization*np.sin(args[1::2])
        return result

    def psi(self, x, t):
        coeffs = self.coeffs[:, np.newaxis]
        eigenvals = np.arange(self.nbase)[:, np.newaxis]
        tvals = t[:, np.newaxis, np.newaxis]
        psit = np.sum(coeffs * self.eigenfunction(x)
                      * np.exp(-1j*(eigenvals+1)**2*tvals), axis= -2)
        return psit

def trapezoidal(func, a, b, nint):
    delta = (b-a)/nint
    x = np.linspace(a, b, nint+1)
    integrand = func(x)
    integrand[..., 0] = 0.5*integrand[..., 0]
    integrand[..., -1] = 0.5*integrand[..., -1]
    return delta*np.sum(integrand, axis=-1)

def psi0(x):
    sigma = 0.005
    return np.exp(-x**2/(2*sigma))/(np.pi*sigma)**0.25

w = InfiniteWell(psi0=psi0, width=2, nbase=100, nint=1000)
x = np.linspace(-0.5*w.width, 0.5*w.width, 500)
t = np.linspace(0, np.pi/4, 1000)
z = np.abs(w.psi(x, t))**2
z = z/np.max(z)
plt.rc('text', usetex=True)
plt.imshow(z.T, cmap=cm.hot)
plt.xlabel('$t$', fontsize=20)
plt.ylabel('$x$', fontsize=20)
plt.show()
```

* a three-dimensional array is used with axes corresponding to time, eigenvalue and position
* runs faster than the first version by a factor of 74
* further improvements are possible

---

# Result of profiling the NumPy version of the script

```bash
Wed Jun  5 14:49:46 2024    carpet.prof

         1074356 function calls (1058130 primitive calls) in 1.350 seconds

   Ordered by: internal time
   List reduced from 3632 to 15 due to restriction <15>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.614    0.614    0.674    0.674 carpet.py:23(psi)
       19    0.060    0.003    0.060    0.003 {method 'reduce' of 'numpy.ufunc' objects}
     7309    0.052    0.000    0.082    0.000 /opt/anaconda3/lib/python3.11/inspect.py:867(cleandoc)
    53/51    0.042    0.001    0.047    0.001 {built-in method _imp.create_dynamic}
      308    0.034    0.000    0.034    0.000 {built-in method marshal.loads}
        1    0.028    0.028    0.028    0.028 {built-in method addToolBar}
        1    0.023    0.023    0.023    0.023 /opt/anaconda3/lib/python3.11/site-packages/matplotlib/backends/backend_qt.py:93(_create_qApp)
    70504    0.021    0.000    0.021    0.000 {built-in method builtins.getattr}
      448    0.013    0.000    0.013    0.000 {built-in method builtins.dir}
1178/1070    0.013    0.000    0.283    0.000 {built-in method builtins.__build_class__}
     9934    0.012    0.000    0.012    0.000 {method 'search' of 're.Pattern' objects}
      223    0.012    0.000    0.035    0.000 /opt/anaconda3/lib/python3.11/site-packages/matplotlib/artist.py:1517(get_setters)
      223    0.010    0.000    0.018    0.000 /opt/anaconda3/lib/python3.11/site-packages/matplotlib/artist.py:1453(<listcomp>)
    95484    0.010    0.000    0.010    0.000 {method 'startswith' of 'str' objects}
     4252    0.010    0.000    0.114    0.000 /opt/anaconda3/lib/python3.11/site-packages/matplotlib/artist.py:1470(get_valid_values)
```

---

# Line profiling

* The `cProfile` module measures the execution time of functions, but does not indicate which
  parts of a function are time critical.
* There exists also a [line profiler](https://github.com/pyutils/line_profiler) developed originally by Robert Kern.
* `line_profiler` is not part of the standard Anaconda distribution and needs to be installed separately. It is
  also available as extension for Jupyter notebooks and as plugin for the Spyder IDE.
* decorate the function(s) of interest with `@line_profiler.profile`
* run the script with
  `LINE_PROFILE=1 python <script name>`
* The output will be written to a text file.

---

```python {all|3|29-37}{maxHeight:'500px'}
from math import cos, exp, pi, sin, sqrt
from cmath import exp as cexp
from line_profiler import profile
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

class InfiniteWell:
    def __init__(self, psi0, width, nbase, nint):
        self.width = width
        self.nbase = nbase
        self.nint = nint
        self.coeffs = self.get_coeffs(psi0)
        self.eigenfunction_cache = {}

    def eigenfunction(self, n, x):
        if n % 2:
            return sqrt(2/self.width)*sin((n+1)*pi*x/self.width)
        return sqrt(2/self.width)*cos((n+1)*pi*x/self.width)

    def get_coeffs(self, psi):
        coeffs = []
        for n in range(self.nbase):
            f = lambda x: psi(x)*self.eigenfunction(n, x)
            c = trapezoidal(f, -0.5*self.width, 0.5*self.width, self.nint)
            coeffs.append(c)
        return coeffs

    @profile
    def psi(self, x, t):
        if not x in self.eigenfunction_cache:
            self.eigenfunction_cache[x] = [self.eigenfunction(n, x)
                                           for n in range(self.nbase)]
        psit = 0
        for n, (c, ef) in enumerate(zip(self.coeffs, self.eigenfunction_cache[x])):
            psit = psit + c*ef*cexp(-1j*(n+1)**2*t)
        return psit

def trapezoidal(func, a, b, nint):
    delta = (b-a)/nint
    integral = 0.5*(func(a)+func(b))
    for k in range(1, nint):
        integral = integral+func(a+k*delta)
    return delta*integral

def psi0(x):
    sigma = 0.005
    return exp(-x**2/(2*sigma))/(pi*sigma)**0.25

w = InfiniteWell(psi0=psi0, width=2, nbase=100, nint=1000)
x = np.linspace(-0.5*w.width, 0.5*w.width, 500)
ntmax = 1000
z = np.zeros((500, ntmax))
for n in range(ntmax):
    t = 0.25*pi*n/(ntmax-1)
    y = np.array([abs(w.psi(x, t))**2 for x in x])
    z[:, n] = y
z = z/np.max(z)
plt.rc('text', usetex=True)
plt.imshow(z, cmap=cm.hot)
plt.xlabel('$t$', fontsize=20)
plt.ylabel('$x$', fontsize=20)
plt.show()
```

---

# Result of line profiling

```bash
$ cat profile_output.txt
Timer unit: 1e-09 s

Total time: 48.3917 s
File: carpet.py
Function: psi at line 29

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    29                                               @profile
    30                                               def psi(self, x, t):
    31    500000  187205463.0    374.4      0.4          if not x in self.eigenfunction_cache:
    32      1000   37770241.0  37770.2      0.1              self.eigenfunction_cache[x] = [self.eigenfunction(n, x)
    33       500     113746.0    227.5      0.0                                             for n in range(self.nbase)]
    34    500000  104480301.0    209.0      0.2          psit = 0
    35  50500000        2e+10    334.6     34.9          for n, (c, ef) in enumerate(zip(self.coeffs, self.eigenfunction_cache[x])):
    36  50000000        3e+10    621.6     64.2              psit = psit + c*ef*cexp(-1j*(n+1)**2*t)
    37    500000   86944437.0    173.9      0.2          return psit

 48.39 seconds - carpet.py:29 - psi

```

* most of the time is spent in lines 35 and 36
* running the line profiling comes with a significant overhead
