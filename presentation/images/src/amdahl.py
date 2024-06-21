import numpy as np
from pyx import color, graph, text

text.set(text.LatexEngine)
text.preamble(r'''\usepackage[sfdefault,lining,scaled=.85]{FiraSans}
\usepackage[scaled=0.85]{FiraMono}
\usepackage{newtxsf}''')

g = graph.graphxy(width=6, height=6,
                  x=graph.axis.lin(min=0, max=1, title='parallel fraction $f$'),
                  y=graph.axis.lin(min=0, max=10, title='speed-up $S$'),
                  key=graph.key.key(pos='tl', dist=0.1))
f = np.linspace(0., 0.95, 100)
s = 1/(1-f)
g.plot(graph.data.values(x=f, y=s, title=r'$p\to\infty$'), [graph.style.line()])

pvals = (1, 2, 4, 8, 16)
f = np.linspace(0., 1., 100)
for nr, p in enumerate(pvals[::-1]):
    s = 1/(1-f+f/p)
    g.plot(graph.data.values(x=f, y=s, title=f'${p=}$'),
           [graph.style.line([color.hsb(2/3*nr/len(pvals), 1, 0.7)])])
g.writeGSfile(device="png16m", resolution=600)
