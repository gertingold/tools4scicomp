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

# Global interpreter lock



---

# Embarassingly parallel

or perfectly parallel or trivially parallelizable

* A task can sometimes be decomposed into subtasks which do not need to communicate with each other.
* Example: Monte Carlo simulations with different seeds or runs for different parameters like temperature.

---

# MPI

https://doc.sagemath.org/html/en/thematic_tutorials/numerical_sage/parallel_laplace_solver.html
