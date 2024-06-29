from concurrent import futures
from itertools import product
from functools import partial
import time
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_iteration(cx, cy, nitermax):
    x = 0
    y = 0
    for n in range(nitermax):
        x2 = x*x
        y2 = y*y
        if x2+y2 > 4:
            return n
        x, y = x2-y2+cx, 2*x*y+cy
    return nitermax

def mandelbrot(nitermax, npts, nx, ny, xmin, xmax, ymin, ymax):
    data = np.empty(shape=(npts, npts), dtype=int)
    dx = (xmax-xmin)/(npts-1)
    dy = (ymax-ymin)/(npts-1)
    for nx_ in range(npts):
        x = xmin+nx_*dx
        for ny_ in range(npts):
            y = ymin+ny_*dy
            data[ny_, nx_] = mandelbrot_iteration(x, y, nitermax)
    return (nx, ny, data)

def mandelbrot_p(xmin, xmax, ymin, ymax, npts, nitermax, ndiv, max_workers=4):
    cy, cx = np.ogrid[ymin:ymax:npts*1j, xmin:xmax:npts*1j]
    nlen = npts//ndiv
    paramlist = [(nx, ny,
                  cx[0, nx*nlen], cx[0, (nx+1)*nlen-1],
                  cy[ny*nlen, 0], cy[(ny+1)*nlen-1, 0])
                 for nx, ny in product(range(ndiv), repeat=2)]
    with futures.ProcessPoolExecutor(max_workers=max_workers) as executors:
        wait_for = [executors.submit(partial(mandelbrot, nitermax, nlen),
                                             nx, ny, xmin, xmax, ymin, ymax)
                    for (nx, ny, xmin, xmax, ymin, ymax) in paramlist]
        results = [f.result() for f in futures.as_completed(wait_for)]
    data = np.zeros((npts, npts), dtype=int)
    for nx, ny, result in results:
        data[ny*nlen:(ny+1)*nlen, nx*nlen:(nx+1)*nlen] = result
    return data

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
data = mandelbrot_p(xmin, xmax, ymin, ymax, npts, nitermax, 1, 1)
ende = time.time()
print(ende-start)
plot(data)
