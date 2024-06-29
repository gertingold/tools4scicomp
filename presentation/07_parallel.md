---
layout: section
---

# Aspects of parallel computing

---

# Multicore CPUs


<div class="grid grid-cols-[40%_1fr] gap-4">
<div><img src="/images/haswell.png" style="width: 100%; margin: auto"></div>
<div>

* [CPU with four cores (Haswell architecture, 2013)](https://cdrdv2-public.intel.com/786255/786255_330119_ia-introduction-basics-paper.pdf)

</div>
</div>

<br />

<img src="/images/monitor.png" style="width: 95%; margin: auto">

* diagonalization of a matrix with NumPy with MKL support on an Intel i5-1135G7 with four cores

---

# Compute cluster

<img src="/images/juwels.jpg" style="width: 95%; margin: auto">

* JUWELS + booster ([FZ Jülich](https://fz-juelich.de))
  * JUWELS: 122.768 cores + 71.680 FP64-CUDA cores
  * JUWELS booster: 44.928 cores + 12.939.264 FP64-CUDA cores

---

# Amdahls's law

<div class="grid grid-cols-[50%_1fr] gap-4"><div>

* compute time with one core: $T_1$
* number of cores: $p$
* fraction of parallel computation: $f$

<br />

* serial time: $T_\text{s} = (1-f)T_1$
* parallel time: $T_\text{p} = \dfrac{fT_1}{p}$

<br />

* speedup: $S_\text{p} = \dfrac{T_1}{T_\text{s}+T_\text{p}} = \dfrac{1}{1-f+\dfrac{f}{p}}$

  Amdahl's law represents a theoretical optimum which is not reached because of 
  overhead for parallel computation.

</div><div>
<img src="/images/amdahl.png" style="width: 100%; margin: auto">
</div></div>

---

# Communication overhead

* suppose that the whole program can be executed in parallel in the time: $T_\text{p}=\dfrac{T_1}{p}$
* time spent for communication between different processes: $T_\text{c}$

<br />

* speedup $S_\text{p} = \dfrac{T_1}{\dfrac{T_1}{p}+T_\text{c}} < p$

<br />

* In the limit $p\to\infty$, the time is dominated by the communication time $T_\text{c}$.
* For the communication time to be irrelevant, we need
  $$p\ll\dfrac{T_1}{T_\text{c}}\,.$$

<br />

* More cores lead to more need for communication.

---

# Race condition

<img src="/images/race.png" style="width: 100%; margin: auto">

<br />

* If processes are not properly synchronized and use shared memory, results may be incorrect.
* One process might have to wait for another one to complete its computation.
* One process needs to signal to the other one that it has completed its computation.
* Waiting times reduce the speed-up.

---

# Threads

* Threads share a common range of memory.
* Therefore, they can access the same data and easily exchange data with other threads.
* Threads result in little overhead.
* However, if data are not accessed and modified in the right order, mistakes may occur.
* Such mistakes can be very difficult to identify, because there occurrence may depend 
  on the details of the timing.

<br />

* For CPython, the global interpreter lock (GIL) presently does not allow to execute 
  several threads in parallel.
* Multithreading in Python therefore is only useful for *I/O-bound* problems.
* For *runtime-bound* problems, multiple threads will lead to a performance reduction
  because of the overhead involved in switching between threads.

---

# Global interpreter lock (GIL)

* Memory management in CPython is done by reference counting.

``` python
>>> import sys
>>> a = [1, 2]
>>> sys.getrefcount(a)
2
>>> b = a
>>> sys.getrefcount(a)
3
>>> b = []
>>> sys.getrefcount(a)
2
```

* When the number of references to an object becomes zero, the memory occupied by
  that object will be released.
* Threads running in parallel can lead to an incorrect reference count causing
  either memory leakage or freeing memory which is still needed. This is prevented
  by the GIL.
* Side note: Because of the possibility of reference cycles, additional garbage
  collection is done.

---

# Processes

* The `multiprocessing` module allows to start several Python interpreters which
  can run independently, each with its own GIL.
* The interpreter processes can run on different cores and thus lead to a speed-up
  of runtime-bound tasks.
* However, starting new processes implies more overhead than starting new threads.
* Furthermore, data are not shared so that communication between processes is more
  complicated.

<br />

### Embarrassingly parallel problems

* A task can sometimes be decomposed into subtasks which do not need to communicate with each other.
* Example: Monte Carlo simulations with different seeds or runs for different parameters like temperature.
* For embarrassingly parallel problems, the `multiprocessing` module helps to easily organize
  the distribution of the problem over several processes and to collect the results.

---

# [PEP 703](https://peps.python.org/pep-0703/)

* PEP = Python Enhancement Proposal
* PEP 703: Making the Global Interpreter Lock Optional in CPython
* proposal for implementation of a thread-safe memory management

<br />

* plans to abandon the GIL in steps over the next five years
* The process will be monitored and adjusted when necessary.
* For the moment, the CPython with GIL will remain the standard,
  but the possibility for a no-GIL build might appear in Python 3.13
  or Python 3.14.

---

# Example: Mandelbrot set

<div class="grid grid-cols-[50%_1fr] gap-4">
<div>
<img src="/images/mandelbrot_detail.png" style="width: 100%; margin: auto">
</div><div>

* For a complex number $c$, the recursion

  $$z_{n+1} = z_n^2+c$$

  is carried out with initial value $z_0=0$
* If the threshold $|z|=2$ is reached, it is known that the series will not be bounded.
* For a graphical representation, the number of iterations needed to reach this threshold
  is determined and colour-coded.
* The problem is embarrassingly parallel because the iteration can be done for each
  value of $c$ separately.

</div></div>

---

# A first implementation

<div class="grid grid-cols-[50%_1fr] gap-4">
<div>

```python
import time
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_iteration(cx, cy, nitermax):
    x = 0
    y = 0
    for n in range(nitermax):
        x2 = x*x
        y2 = y*y
        if x2+y2 > 4: return n
        x, y = x2-y2+cx, 2*x*y+cy
    return nitermax

def mandelbrot(xmin, xmax, ymin, ymax, npts, nitermax):
    data = np.empty(shape=(npts, npts), dtype=int)
    dx = (xmax-xmin)/(npts-1)
    dy = (ymax-ymin)/(npts-1)
    for nx in range(npts):
        x = xmin+nx*dx
        for ny in range(npts):
            y = ymin+ny*dy
            data[ny, nx] = mandelbrot_iteration(
                                x, y, nitermax)
    return data
```

</div><div>

```python
def plot(data):
    plt.imshow(data, extent=(xmin, xmax, ymin, ymax),
               cmap='jet', origin='lower', interpolation='none')
    plt.show()

nitermax = 2000
npts = 1024
xmin = -2
xmax = 1
ymin = -1.5
ymax = 1.5
start = time.time()
data = mandelbrot(xmin, xmax, ymin, ymax, npts, nitermax)
ende = time.time()
print(ende-start)
plot(data)
```

* run-time measured on an i5-1135G7 processor: 44.9s

</div></div>

---

# Implementation with NumPy

````md magic-move
```python
def mandelbrot_iteration(cx, cy, nitermax):
    x = 0
    y = 0
    for n in range(nitermax):
        x2 = x*x
        y2 = y*y
        if x2+y2 > 4: return n
        x, y = x2-y2+cx, 2*x*y+cy
    return nitermax

def mandelbrot(xmin, xmax, ymin, ymax, npts, nitermax):
    data = np.empty(shape=(npts, npts), dtype=int)
    dx = (xmax-xmin)/(npts-1)
    dy = (ymax-ymin)/(npts-1)
    for nx in range(npts):
        x = xmin+nx*dx
        for ny in range(npts):
            y = ymin+ny*dy
            data[ny, nx] = mandelbrot_iteration(
                                x, y, nitermax)
    return data
```
```python
def mandelbrot(xmin, xmax, ymin, ymax, npts, nitermax):
    cy, cx = np.mgrid[ymin:ymax:npts*1j, xmin:xmax:npts*1j]
    x = np.zeros_like(cx)
    y = np.zeros_like(cx)
    data = np.zeros(cx.shape, dtype=int)
    for n in range(nitermax):
        x2 = x*x
        y2 = y*y
        notdone = x2+y2 < 4
        data[notdone] = n
        x[notdone], y[notdone] = (x2[notdone]-y2[notdone]+cx[notdone],
                                  2*x[notdone]*y[notdone]+cy[notdone])
    return data
```
````

<v-after>

* The calculation is restricted by means of fancy indexing to matrix elements
  for which the threshold of 2 is not yet exceeded.
* run-time measured on an i5-1135G7 processor: 17.0s
+ speed up by a factor of about 2.6

</v-after>

---

# The `concurrent` module

* With the help of the `concurrent.futures` module, parallel execution of code
  in threads or processes can be organized.
* We will consider the evaluation of a Mandelbrot set as example of an embarrassingly
  parallel problem which will be handled in parallel processes.

<br />

* import the module

```python
from concurrent import futures
```

* create a parameter list from which parameter sets will be taken and distributed
  to the different processes or workers
* use a `with` context to distribute the tasks and collect the results

```python
with futures.ProcessPoolExecutor(max_workers=max_workers) as executors:
    ...
```

* create a list scheduling function calls and collect the results in a list

---

# Parallel evaluation of Mandelbrot set

* Split region in the complex plane into subregions which will be handled
  by processes running in parallel.
* `import` statements

```python
from concurrent import futures
from itertools import product
from functools import partial
import numpy as np
```

* evaluation of the Mandelbrot set in a subregion
```python
def mandelbrot_tile(nitermax, nx, ny, cx, cy):
    x = np.zeros_like(cx)
    y = np.zeros_like(cx)
    data = np.zeros(cx.shape, dtype=int)
    for n in range(nitermax):
        x2 = x*x
        y2 = y*y
        notdone = x2+y2 < 4
        data[notdone] = n
        x[notdone], y[notdone] = (x2[notdone]-y2[notdone]+cx[notdone],
                                  2*x[notdone]*y[notdone]+cy[notdone])
    return (nx, ny, data)
```

---

# Parallel evaluation of Mandelbrot set (cont'd)

```python {all|4-7|8-12|14-15}
def mandelbrot(xmin, xmax, ymin, ymax, npts, nitermax, ndiv, max_workers=4):
    cy, cx = np.mgrid[ymin:ymax:npts*1j, xmin:xmax:npts*1j]
    nlen = npts//ndiv
    paramlist = [(nx, ny,
                  cx[nx*nlen:(nx+1)*nlen, ny*nlen:(ny+1)*nlen],
                  cy[nx*nlen:(nx+1)*nlen, ny*nlen:(ny+1)*nlen])
                 for nx, ny in product(range(ndiv), repeat=2)]
    with futures.ProcessPoolExecutor(max_workers=max_workers) as executors:
        wait_for = [executors.submit(partial(mandelbrot_tile, nitermax), nx, ny, cx, cy)
                    for (nx, ny, cx, cy) in paramlist]
        results = [f.result() for f in futures.as_completed(wait_for)]
    data = np.zeros(cx.shape, dtype=int)
    for nx, ny, result in results:
        data[nx*nlen:(nx+1)*nlen, ny*nlen:(ny+1)*nlen] = result
    return data
```

<v-click at="1">

* create a list of parameters for the different tasks

</v-click>
<v-click at="2">

* submit the tasks to a number of workers (parallel processes)
* we use `partial` to specify a fixed parameter not specified in the parameter list
* wait for results and collect them in a list

</v-click>
<v-click at="3">

* gather the results in an array for later plotting

</v-click>

---

# Distribution of subregions over four processes

<div class="grid grid-cols-[50%_1fr] gap-4">
<div>

<img src="/images/mandelbrot_tiles.png" style="width: 100%; margin: auto">
</div><div>

* not all subregions need the same compute time
* the number of subregions handled by one process ranges from 15 to 17

</div></div>

---

# Run-time as a function of the number of tasks

<br />

<img src="/images/mandelbrot_parallel.png" style="width: 100%; margin: auto">

<br />

* 4 parallel processes, NumPy version of the program
* If only four tasks are distributed to four processes, the longest-running process
  determines the run-time.
* If a large number of tasks is defined, the overhead in starting the tasks and collecting
  the results becomes relevant.
* In the present example, 64 tasks are optimal.

---

# Speed-up

<img src="/images/parallel_time.png" style="width: 100%; margin: auto">

<br />

* 4 processes, treatment of individual points in the complex plane
* A maximum speed-up by a factor of 3.3 corresponding a fraction of 93% of 
  parallel execution according to Amdahl's law

---

# Compilation

* Python is an interpreted language
* compilation can yield significant speed-up by providing optimized machine code
  * [Cython](https://cython.org): script is converted to C as much as possible in order to be compiled
  * [Numba](https://numba.pydata.org): just-in-time compilation, the code of a function is compiled
    when needed. Therefore, there is an overhead during the first function call, but the machine code
    can be used in ensuing calls of that function.

<br />

* We will discuss Numba as it can be used more easily.



---

# MPI

https://doc.sagemath.org/html/en/thematic_tutorials/numerical_sage/parallel_laplace_solver.html
