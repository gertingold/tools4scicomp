from pyx import canvas, color, deco, path, text, style, trafo, unit

def array(shape):
    baseshape = (3, 4)
    bgcolor = color.grey(0.5)
    c = canvas.canvas()
    c.text(baseshape[1]/2, baseshape[0]+0.3, 'shape=%s' % repr(shape),
           [text.halign.center])
    if len(shape) == 1:
        shape = (1, shape[0])
    assert len(shape) == 2
    c.stroke(path.rect(0, 0, baseshape[1], baseshape[0]), [bgcolor])
    for nx in range(1, baseshape[1]):
        c.stroke(path.line(nx, 0, nx, baseshape[0]), [bgcolor])
    for ny in range(1, baseshape[0]):
        c.stroke(path.line(0, ny, baseshape[1], ny), [bgcolor])
    if not(shape == baseshape):
        c.fill(path.rect(0, baseshape[0], shape[1], -shape[0]),
               [color.rgb(1, 0.8, 0.4)])
        if shape[0] in (1, baseshape[0]) and shape[1] in (1, baseshape[1]):
            for nx in range(baseshape[1]):
                for ny in range(baseshape[0]):
                    c.text(nx+0.5, baseshape[0]-ny-0.5,
                           str(baseshape[1]*min(ny, shape[0]-1)+min(nx, shape[1]-1)+1),
                           [text.halign.center, text.valign.middle, bgcolor])
        else:
            alertcolor = color.rgb(0.6, 0, 0)
            c.stroke(path.line(0, 0, baseshape[1], baseshape[0]),
                     [alertcolor, style.linewidth.Thick])
            c.stroke(path.line(0, baseshape[0], baseshape[1], 0),
                     [alertcolor, style.linewidth.Thick])
    else:
        for nx in range(baseshape[1]):
            for ny in range(baseshape[0]):
                c.text(nx+0.5, baseshape[0]-ny-0.5, str(baseshape[1]*ny+nx+1),
                       [text.halign.center, text.valign.middle])
    c.stroke(path.rect(0, baseshape[0], shape[1], -shape[0]))
    for nx in range(1, shape[1]):
        c.stroke(path.line(nx, baseshape[0], nx, baseshape[0]-shape[0]))
    for ny in range(1, shape[0]):
        c.stroke(path.line(0, ny, shape[1], ny))
    if not(shape == baseshape):
        for nx in range(shape[1]):
            for ny in range(shape[0]):
                c.text(nx+0.5, baseshape[0]-ny-0.5, str(baseshape[1]*ny+nx+1),
                       [text.halign.center, text.valign.middle])
    return c

text.set(text.LatexRunner)
text.preamble(r'\usepackage[sfdefault,scaled=.85,lining]{FiraSans}\usepackage{newtxsf}')
unit.set(xscale=1.6, wscale=1.5)

c = canvas.canvas()

c.insert(array((3, 4)))
c.insert(array((1,)), [trafo.translate(5, 0)])
c.insert(array((4,)), [trafo.translate(10, 0)])
c.insert(array((3,)), [trafo.translate(5, -4.5)])
c.insert(array((3, 1)), [trafo.translate(10, -4.5)])

c.writePDFfile()
c.writeGSfile(device="png16m", resolution=600)
