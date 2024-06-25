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

  $$z_{n+1} = z_n+c$$

  is carried out with initial value $z_0=0$
* If the threshold $|z|=2$ is reached, it is known that the series will not be bounded.
* For a graphical representation, the number of iterations needed to reach this threshold
  is determined and colour-coded.
* The problem is embarrassingly parallel because the iteration can be done for each
  value of $c$ separately.

</div></div>

---

# MPI

https://doc.sagemath.org/html/en/thematic_tutorials/numerical_sage/parallel_laplace_solver.html
