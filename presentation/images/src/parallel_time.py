from pyx import canvas, color, deco, graph, style

cpus = ['i7-6700hq',]
data = {}
for cpu in cpus:
    data[cpu] = []
    with open(cpu+'.dat') as fh:
        for line in fh:
            nr, t1, t4 = line.rstrip('\n').split()
            nr = int(nr)
            t1 = float(t1)
            t4 = float(t4)
            data[cpu].append((t1, t4))
    data[cpu] = [(2**nr, t1/t4, 4/3*(1-t4/t1))
                 for nr, (t1, t4) in enumerate(data[cpu])]

print(data)
c = canvas.canvas()
logparter = graph.axis.parter.log(tickpreexps=
                [graph.axis.parter.preexp([graph.axis.tick.rational(1, 1)], 2)])
g1 = graph.graphxy(width=8,
        x=graph.axis.log(min=1, max=512, parter=logparter,
                         title='number of divisions per axis'),
        y=graph.axis.lin(min=0, max=4, title='acceleration'))
for nr, cpu in enumerate(cpus):
    g1.plot(graph.data.points(data[cpu], x=1, y=2),
            [graph.style.line(lineattrs=[style.linestyle.solid]),
             graph.style.symbol(symbol=graph.style.symbol.circle,
    	         size=0.1, symbolattrs=[deco.filled([color.grey(nr)])])
	    ])
g2 = graph.graphxy(width=8, xpos=g1.xpos+g1.width+2,
        x=graph.axis.log(min=1, max=512, parter=logparter,
                         title='number of divisions per axis'),
        y=graph.axis.lin(min=0, max=1, title='fraction of parallel execution'))
for nr, cpu in enumerate(cpus):
    g2.plot(graph.data.points(data[cpu], x=1, y=3),
            [graph.style.line(lineattrs=[style.linestyle.solid]),
             graph.style.symbol(symbol=graph.style.symbol.circle,
    	         size=0.1, symbolattrs=[deco.filled([color.grey(nr)])])
	    ])
c.insert(g1)
c.insert(g2)
c.writeGSfile(device="png16m", resolution=600)
