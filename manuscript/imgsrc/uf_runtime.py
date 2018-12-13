import math
import matplotlib.pyplot as plt
import numpy as np
import time

def sin_math(nmax):
    xvals = np.linspace(0, 2*np.pi, nmax)
    start = time.time()
    for x in xvals:
        y = math.sin(x)
    return time.time()-start

def sin_numpy(nmax):
    xvals = np.linspace(0, 2*np.pi, nmax)
    start = time.time()
    yvals = np.sin(xvals)
    return time.time()-start

maxpower = 26
nvals = 2**np.arange(0, maxpower+1)
tvals = np.empty_like(nvals)
for nr, nmax in enumerate(nvals):
    tvals[nr] = sin_math(nmax)/sin_numpy(nmax)
plt.rc('text', usetex=True)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('$n_\mathrm{max}$', fontsize=20)
plt.ylabel('$t_\mathrm{math}/t_\mathrm{numpy}$', fontsize=20)
plt.plot(nvals, tvals, 'o')
plt.show()
