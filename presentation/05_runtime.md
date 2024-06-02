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

# A naive solution

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
