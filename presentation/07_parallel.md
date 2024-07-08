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

* Before using more hardware ressources, other ways to speed-up execution should
  be explored.

<br />

* Python is an interpreted language
* compilation can yield significant speed-up by providing optimized machine code
  * [Cython](https://cython.org): script is converted to C as much as possible in order to be compiled
  * [Numba](https://numba.pydata.org): just-in-time (JIT) compilation, the code of a function is compiled
    when needed
    * There is an overhead during the first function call, but the machine code
      can be used in ensuing calls of that function.
    * Numba can also deal with NumPy arrays and can create universal functions
    * code can be vectorized for distribution on several cores

<br />

* We will discuss Numba as it can be used more easily.

---

# Example: evaluation of the Riemann zeta function

* Riemann zeta function will be evaluated in a very naive way by cutting the summation
  $$\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s}$$
* There are ways to approximate the contribution of the neglected terms.
* There exist also other ways to the determine the Riemann zeta function, see 
  [here in section *Miscellaneous*](http://numbers.computation.free.fr/Constants/constants.html)

```python
def zeta(x, nmax):
    zetasum = 0
    for n in range(1, nmax+1):
        zetasum = zetasum+1/(n**x)
    return zetasum

print(zeta(2, 100000000))
```

* The relative error is 5.5·10⁻⁹ with respect to the exact result $\pi^2/6$.
* The run-time on an i7-6700HQ processor is 8.7s.

---

# Numba version

````md magic-move
```python
def zeta(x, nmax):
    zetasum = 0
    for n in range(1, nmax+1):
        zetasum = zetasum+1/(n**x)
    return zetasum

print(zeta(2, 100000000))
```
```python {all|1-3}
import numba

@numba.njit
def zeta(x, nmax):
    zetasum = 0
    for n in range(1, nmax+1):
        zetasum = zetasum+1/(n**x)
    return zetasum

print(zeta(2, 100000000))
```
````

<v-click at="1">

* The run-time is now 0.78 seconds amounting to a 10× speed-up

</v-click>
<v-click at="2">

* It was sufficient to add a decorator `numba.njit` to the function.
* In `njit` the part `jit` refers to the just-in-time compiler and
  `n` refers to the `nopython` mode.
* It can happen that Numba is not able to compile the entire function.
  Then, the decorator `numba.jit` with option `nopython=False` can be
  used and Numba will try to find loops which it can compile. The rest
  will be implying the Python interpreter and thus reduce performance. 

</v-click>

---

# Compilation time

```python
import time
import numba

@numba.njit
def zeta(x, nmax):
    zetasum = 0
    for n in range(1, nmax+1):
        zetasum = zetasum+1/(n**x)
    return zetasum

start = time.time()
result = zeta(2, 100000000)
print(f'time with compilation:    {time.time()-start:4.2f}s')

start = time.time()
result = zeta(2, 100000000)
print(f'time without compilation: {time.time()-start:4.2f}s')
```

```
time with compilation:    0.78s
time without compilation: 0.40s
```

* After the result of the compilation is available, the run-time is
  smaller by another factor of 2.

---

# Signatures

```python
import numba

@numba.njit
def zeta(x, nmax):
    zetasum = 0
    for n in range(1, nmax+1):
        zetasum = zetasum+1/(n**x)
    return zetasum

print(zeta.signatures)
zeta(2, 100000000)
print(zeta.signatures)
```

```
[]
[(int64, int64)]
```

* As long as the function `zeta` was not called, no compilation happens.
* We have called the function `zeta` with two integer arguments. The
  function has been compiled for the corresponding signature.
* The data type is `int64` and therefore potentially subject to overflow
  in contrast to Python integers.

---

# Different signatures

```python
import time
from numba import njit

def zeta(x, nmax):
    zetasum = 0
    for n in range(1, nmax+1):
        zetasum = zetasum+1/(n**x)
    return zetasum

zeta_numba = njit(zeta)

nmax = 100000000
for x in (2, 2.5, 2+1j):
    start = time.time()
    print(f'ζ({x}) = {zeta_numba(x, nmax)}')
    print(f'execution time with compilation:    {time.time()-start:5.2f}s')
    start = time.time()
    zeta_numba(x, nmax)
    print(f'execution time without compilation: {time.time()-start:5.2f}s')
    start = time.time()
    zeta(x, nmax)
    print(f'execution time without Numba:       {time.time()-start:5.2f}s\n')

print(zeta_numba.signatures)
```

---

# Different signatures (cont'd)

```
ζ(2) = 1.644934057834575
execution time with compilation:     0.79s
execution time without compilation:  0.42s
execution time without Numba:        9.67s

ζ(2.5) = 1.341487257103954
execution time with compilation:     2.56s
execution time without compilation:  2.47s
execution time without Numba:       11.83s

ζ((2+1j)) = (1.1503556987382961-0.43753086346605924j)
execution time with compilation:    10.20s
execution time without compilation: 10.65s
execution time without Numba:       24.74s

[(int64, int64), (float64, int64), (complex128, int64)]
```

* compilation for three different signatures
* timing details and speed-up depend on the signatures 

---

# Parallel execution with Numba

<div class="grid grid-cols-[50%_1fr] gap-4">
<div>

```python
# zeta.py

import os
import time
import numpy as np
from numba import vectorize, float64, int64

@vectorize([float64(float64, int64)], target='parallel')
def zeta(x, nmax):
    zetasum = 0.
    for n in range(nmax):
        zetasum = zetasum+1./((n+1)**x)
    return zetasum

x = np.linspace(2, 10, 200, dtype=np.float64)
start = time.time()
y = zeta(x, 10000000)
print(time.time()-start)
```

</div><div>

* The number of threads can be defined by setting the environment
  variable `NUMBA_NUM_THREADS`:
  ```bash
  $ export NUMBA_NUM_THREADS=4; python zeta.py
  ```
* The required data types for input (`float64, int64`) and output (`float64`)
  need to be specified in order to obtain a universal function. 
* It is possible to specify more than one signature.
* By setting `target` to `cuda`, compilation for NVIDIA GPUs can be requested.
  

</div></div>

---

# Mandelbrot set with Numba

<div class="grid grid-cols-[52%_1fr] gap-4">
<div>

```python
from numba import complex128, guvectorize, int64, njit
import numpy as np

@njit
def mandelbrot_iteration(c, maxiter):
    z = 0
    for n in range(maxiter):
        z = z**2+c
        if z.real*z.real+z.imag*z.imag > 4:
            return n
    return maxiter

@guvectorize([(complex128[:], int64[:], int64[:])],
             '(n), () -> (n)', target='parallel')
def mandelbrot(c, itermax, output):
    nitermax = itermax[0]
    for i in range(c.shape[0]):
        output[i] = mandelbrot_iteration(c[i], nitermax)

def mandelbrot_set(xmin, xmax, ymin, ymax, npts, nitermax):
    cy, cx = np.ogrid[ymin:ymax:npts*1j, xmin:xmax:npts*1j]
    c = cx+cy*1j
    return mandelbrot(c, nitermax)
```

</div><div>

* `guvectorize` allows for a universal function with arrays in the inner loop
* arrays in the signature are indicated by `[:]`
* The second argument of `guvectorize` indicates the layout where the returned
  array `output` has the same shape as the input array `c`.
* The `mandelbrot` function is called with two arguments, but possesses three
  arguments. The function is missing a return statement. Instead, the third
  argument refers to the result. 

</div></div>

---

# Timing of the different Mandelbrot set codes

| Type of code          | size        | run-time |
| --------------------- | ----------- | --------:|
| naive implementation  | 1024×1024   | 40.556s  |
| with NumPy            | 1024×1024   | 28.060s  |
| with Numba, 1 thread  | 1024×1024   |  0.940s  |
| with Numba, 8 threads | 1024×1024   |  0.223s  |
| with Numba, 8 threads | 8192×8192   | 13.680s  |
| with Numba, 8 threads | 16384×16384 | 56.756s  |

* measured for an i7-6700HQ processor with 4 cores and hyperthreading

---

# MPI

* MPI = message passing interface
* allows for communication between different processes
* first version of the standard published in 1994

<br />

* in Python: `mpi4py` module (not part of Anaconda distribution)

<br />

#### installation in a [conda](https://docs.conda.io/en/latest/) environment

<div class="grid grid-cols-[50%_1fr] gap-4">
<div>

* configuration file

```yaml
# environment.yml

name: mpi
channels:
  - conda-forge
dependencies:
  - python
  - mpi4py
```

</div><div>

* name can be appropriately chosen
* additional required packages should be listed in dependencies
* installation
  ```bash
  $ conda env create -f environment.yml
  ```
* activation of the environment
  ```bash
  $ conda activate mpi
  ```

</div></div>

---

# Hello world from several workers

```python
# helloworld.py

from mpi4py import MPI
 
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
 
print(f"Hello world from worker {rank} of {size}")
```

* `COMM_WORLD` is the default communicator
* `GetRank()` returns the ID or rank of the current process
* `GetSize()` number of the processes

#### running the script

```bash
$ mpirun -n 4 python helloworld.py
Hello world from worker 2 of 4
Hello world from worker 3 of 4
Hello world from worker 1 of 4
Hello world from worker 0 of 4
```

* if the script is not run with `mpirun`, only one process will be used

---

# Point-to-point communication

<div class="grid grid-cols-[50%_1fr] gap-4">
<div>

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = 2
if rank == 0:
    dest = rank+1
    comm.send(data, dest=dest) 
    print(f'{rank} sends to {dest}: {data}')
elif rank == size-1:
    source = rank-1
    data = comm.recv(source=source)
    print(f'{rank} receives from {source}: {data}')
else:
    source = rank-1
    data = comm.recv(source=source) 
    print(f'{rank} receives from {source}: {data}')
    data = data*2
    dest = rank+1
    comm.send(data, dest=dest)
    print(f'{rank} sends to {dest}: {data}')
```

</div><div>

* data are handed over from one process to the next where data are multiplied
  by two

<br />

* output:
  ```
  0 sends to 1: 2
  1 receives from 0: 2
  1 sends to 2: 4
  2 receives from 1: 4
  2 sends to 3: 8
  3 receives from 2: 8
  ```

<br />

* The script is given to each worker which as a function of its rank executes
  the prescribed code.
* The `recv` function waits until it has received data. The calculation proceeds
  in the intended order.

</div></div>

---

# Blocking communication

<div class="grid grid-cols-[50%_1fr] gap-4">
<div>

* tags can be used to mark messages

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = 'msg'
if rank == 0:
    comm.send(data, dest=1, tag=1)
    print(f'{rank}: data sent')
else:
    data = comm.recv(source=0, tag=1)
    print(f'{rank}: data received')
```

```
0: data sent
1: data received
```

</div><div>

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = 'msg'
if rank == 0:
    comm.send(data, dest=1, tag=1)
    print(f'{rank}: data sent')
else:
    data = comm.recv(source=0, tag=2)
    print(f'{rank}: data received')
```

```
0: data sent
```

<br />

* Here, the communication is blocked, because worker 1 is
  waiting for a message with tag `2` which is never sent.

</div></div>

---

# Non-blocking communication

<div class="grid grid-cols-[50%_1fr] gap-4">
<div>

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = list(range(1, size))
    for i in range(size-1):
        req = comm.isend(data[i], dest=i+1, tag=i+1)
        print(f"expected: {data[i]**2}")
        req.wait()
else:
    req = comm.irecv(source=0, tag=rank)
    mydata = req.wait()
    print(rank, mydata**2)
```

</div><div>

```bash
$ mpirun -n 4 python test.py
expected: 1
expected: 4
expected: 9
1 1
2 4
3 9
```

</div></div>

* some work can be done before communication is completed
* here, process 0 prints the expected results while waiting

---

# Broadcast

* one process sends data to all other processes

<br />

<div class="grid grid-cols-[50%_1fr] gap-4">
<div>

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    data = [1, 2, 3]
else:
    data = None

print(f'{rank}| data before broadcast: {data}')
data = comm.bcast(data, root=0)
print(f'{rank}| data after broadcast: {data}')
```

</div><div>

```
0| data before broadcast: [1, 2, 3]
0| data after broadcast: [1, 2, 3]
1| data before broadcast: None
1| data after broadcast: [1, 2, 3]
2| data before broadcast: None
2| data after broadcast: [1, 2, 3]
3| data before broadcast: None
3| data after broadcast: [1, 2, 3]
```

</div></div>

---

# Reduce

<div class="grid grid-cols-[50%_1fr] gap-4">
<div>

```python
from math import factorial
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

result = comm.reduce(rank+1, op=MPI.PROD, root=0)

if rank == 0:
    print(f'result: {result}')
    print(f'{size}! = {factorial(size)}')
```


```bash
$ mpirun -n 20 python test.py
result: 2432902008176640000
20! = 2432902008176640000
```

* other common functions include `MPI.SUM`,
  `MPI.MAX`, `MPI.MIN`
* It is also possible to define custom functions.

</div><div>

* compare `reduce` function from the `functools` module
  of the Python standard library

```python
from functools import reduce

N = 20
data = range(1, N+1)
result = reduce(lambda x, y: x*y, data)
print(result)
```

* Since Python 3.8, there exists a function `prod` in the
  `math` module

</div></div>

---

# Scatter and gather

<div class="grid grid-cols-[48%_1fr] gap-4">
<div>

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
   data = [x+1 for x in range(size)]
   print(f'to be scattered: {data}', flush=True)
else:
   data = None
   
data = comm.scatter(data, root=0)
print(f'{rank}| obtained: {data}', flush=True)
data = data**2

result = comm.gather(data, root=0)

if rank == 0:
    print(f'gathered result by worker {rank}: {result}',
          flush=True)
```

</div><div>

```
to be scattered: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
0| obtained: 1
1| obtained: 2
2| obtained: 3
3| obtained: 4
4| obtained: 5
5| obtained: 6
6| obtained: 7
7| obtained: 8
8| obtained: 9
9| obtained: 10
gathered result by worker 0: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

<br />

* `flush=True` is used here to obtain the correct sequence of output
</div></div>

---

# Discretization of the Laplace operator

* As an example for commmunication between processes, we consider the
  2d Laplace equation with boundary conditions.

<br />

<div class="grid grid-cols-[50%_1fr] gap-4">
<div>

<img src="/images/gitter-finite-differenzen.png" style="width: 70%; margin: auto">

</div><div>

* Laplace equation

$$\frac{\partial^2\Phi}{\partial x^2}+\frac{\partial^2\Phi}{\partial y^2} = 0$$

* partial derivative on the lattice

$$\frac{\partial\Phi}{\partial x} \approx \frac{\Phi_{n+1,m}-\Phi_{n-1,m}}{2\Delta}$$
$$\frac{\partial^2\Phi}{\partial x^2} \approx \frac{\Phi_{n+1,m}-2\Phi_{n,m}+\Phi_{n-1,m}}{\Delta^2}$$

* correspondingly for $y$

</div></div>

---

# Solution of discretized Laplace equation

<div class="grid grid-cols-[10%_1fr_25%] gap-4">
<div>

<img src="/images/gitter_finite_differenzen_simple.png" style="width: 100%; margin: auto">

</div><div>

$$\Phi_{n,m} = \frac{1}{4}\left(\Phi_{n+1,m}+\Phi_{n-1,m}+\Phi_{n,m+1}+\Phi_{n,m-1}\right)$$

</div></div>
<br />

1. *Solution of an inhomogeneous system of linear equations*  
   inhomogeneity results from boundary conditions
1. *Jacobi method*   
   iterative approach: new function values result from averaging over old nearest neighbor
   values
1. *Gauß-Seidel method*   
   iterative approach: lattice is traversed, thereby mixing old and new values
   $$\Phi_{n,m} = \frac{1}{4}\left(\Phi^\text{(old)}_{n+1,m}+\Phi^\text{(new)}_{n-1,m}
                                   +\Phi^\text{(old)}_{n,m+1}+\Phi^\text{(new)}_{n,m-1}\right)$$
   here: iteration from top left to bottom right   
   typically faster convergence, less memory required, but breaks a potentially present symmetry

---

# Dividing the grid and need for commuication 

<img src="/images/laplace_communication_1.png" style="width: 45%" class="absolute top-100px">
<div v-click>
<img src="/images/laplace_communication_2.png" style="width: 45%" class="absolute top-100px">
</div>
<div v-click>
<img src="/images/laplace_communication_3.png" style="width: 45%" class="absolute top-100px">
</div>
<div v-click>
<img src="/images/laplace_communication_4.png" style="width: 45%" class="absolute top-100px">
</div>

<div class="absolute left-520px top-100px ">

<v-clicks at="0">

* array with boundary conditions
* subdivisions of the grid for 4 processes
* data from other processes are needed for iteration
* for N processes, 2(N-1) send/receive operations are needed

</v-clicks>

</div>

---

# Implementation (part 1)

<div class="grid grid-cols-[50%_1fr] gap-4"><div>

```python
from mpi4py import MPI
import numpy as np
from numpy import r_
import matplotlib.pyplot as plt

def jacobi_step(u):
    u_old = u.copy()
    u[1:-1, 1:-1] = 0.25*(u[0:-2, 1:-1] + u[2:, 1:-1]
                          + u[1:-1,0:-2] + u[1:-1, 2:])
    v = (u-u_old).flat
    return u, np.dot(v,v)

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
root = 0

num_points = 500
rows_per_process = num_points//size
max_iter = 5000
num_iter = 0
total_err = 1
```

</div><div>

* The function `jacobi_step` averages over the nearest neighbors to update a lattice site.
* The comparison of the old and new values yields an error estimate. Alternatively, one
  could check how well the Laplace equation is satisfied.
* `num_points` defines the grid size.
* `rows_per_process` defines the number of matrix rows attributed to each process.

</div></div>

---

# Implementation (part 2)

<div class="grid grid-cols-[55%_1fr] gap-4"><div>

```python
m = None

if rank == root:
    m = np.zeros((num_points, num_points), dtype=float)
    m[0, :] = 1
    m[:, 0] = 1
    m[-1, :] = -1
    m[:, -1] = -1

my_grid = np.empty((rows_per_process, num_points), dtype=float)
comm.Scatterv(m, my_grid, root)
```

* The initial matrix `m` is defined for process 0, where an arrow containing zeros
  is filled with the boundary values.
* The top and the left boundary values are set to 1 while the bottom and the right
  boundary values are set to -1.

</div><div>

* In order to avoid an undefined variable for all other processes, `m` needs to be
  initialized. It is sufficent to set it to `None`.
* `Scatterv` distributes the section of the matrix `M` to the arrays `my_grid` of 
  the different processes.
* `my_grid` needs to exist and be sufficiently large. Therefore, we create an empty
  matrix of the required size.
* MPI methods starting with uppercase letters do not act on Python objects but on
  buffers instead.

</div></div>

---

# Implementation (part 3) – communication

<div class="grid grid-cols-[55%_1fr] gap-4"><div>

```python
while num_iter < max_iter and total_err > 1e-7:
    if rank == 0:
        comm.Send(my_grid[-1, :], 1)

    if rank > 0 and rank < size-1:
        row_above = np.empty((1, num_points), dtype=float)
        comm.Recv(row_above, rank-1)
        comm.Send(my_grid[-1, :], rank+1)

    if rank == size-1:
        row_above = np.empty((1, num_points), dtype=float)
        comm.Recv(row_above, rank-1)
        comm.Send(my_grid[0, :], rank-1)

    if rank > 0 and rank < size-1:
        row_below = np.empty((1, num_points), dtype=float)
        comm.Recv(row_below, rank+1)
        comm.Send(my_grid[0, :], rank-1)

    if rank == 0:
        row_below = np.empty((1, num_points), dtype=float)
        comm.Recv(row_below, 1)
```

</div><div>

<br />
<img src="/images/laplace_communication_4.png" style="width: 100%">

</div></div>

---

# Implementation (part 4) – Jacobi iteration

<div class="grid grid-cols-[54%_1fr] gap-4"><div>

```python
    if rank > 0 and rank < size-1:
        u, err = jacobi_step(r_[row_above, my_grid, row_below])
        my_grid = u[1:-1, :]

    if rank == 0:
        u, err = jacobi_step(r_[my_grid, row_below])
        my_grid = u[0:-1, :]

    if rank == size-1:
        u, err = jacobi_step(r_[row_above, my_grid])
        my_grid = u[1:, :]

    if num_iter % 500 == 0:
        err_list = np.empty(size, dtype=float)
        comm.Gather(err, err_list, root)
        if rank == 0:
            total_err = 0
            for err in err_list:
                total_err = total_err + err
            total_err = np.sqrt(total_err)/num_points**2
            print(f"{total_err = :8.3g}")
        total_err = comm.bcast(total_err, root)

    num_iter=num_iter+1
```

</div><div>

* We are still within the `while` loop.
* `numpy.r_` stacks arrays. Data received from other processes are
  added  to `my_grid`.
* Every 500 iterations, an error estimate is evaluated. It is important
  to broadcast this information to all processes. Otherwise process 0
  might terminate due to the `while` condition while the other processes
  remain in the loop waiting for data from process 0. The program will
  then hang.
* Even though the broadcasting is done by process 0, the corresponding
  line needs to be executed for all processes. Otherwise `total_err`
  would not get a value assigned.

</div></div>

---

# Implementation (part 5)

<div class="grid grid-cols-[54%_1fr] gap-4"><div>

```python
recvbuf = np.empty_like(m)

comm.Gather(my_grid, recvbuf, root)
if rank == 0:
    sol = np.array(recvbuf)
    sol.shape = (num_points,num_points)
    print(f"{num_iter = }")
    plt.imshow(sol)
    plt.show()
               
```

</div><div>

* Gather the results.
* A buffer `recvbuf` is needed to store the results.
* Finally, the data can be further analyzed or represented
  graphically.

</div></div>

<img src="/images/laplace.png" style="width: 40%; margin: auto">
