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



<br>

