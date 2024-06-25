import numpy as np
from pyx import color, graph, text

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
    result = []
    for cxvals, cyvals, dvals in zip(cx, cy, data):
        for cxval, cyval, dval in zip(cxvals, cyvals, dvals):
            result.append((cxval, cyval, dval))
    return result

def plot(data, xmin, xmax, ymin, ymax):
    g = graph.graphxy(height=8, width=8,
                  x=graph.axis.linear(min=xmin, max=xmax, title=r"$\mathrm{Re}(c)$"),
                  y=graph.axis.linear(min=ymin, max=ymax, title=r'$\mathrm{Im}(c)$'))
    g.plot(graph.data.points(data, x=1, y=2, color=3),
           [graph.style.density(gradient=color.gradient.ReverseJet,
                                keygraph=None)])
    g.writeGSfile(device="png16m", resolution=300)

text.set(text.LatexRunner)
text.preamble(r'\usepackage{arev}\usepackage[T1]{fontenc}')

nitermax = 1000
npts = 1024
xmin = -0.7488
xmax = -0.7482
ymin = -0.0634
ymax = -0.0628
data = mandelbrot(xmin, xmax, ymin, ymax, npts, nitermax)
plot(data, xmin, xmax, ymin, ymax)
