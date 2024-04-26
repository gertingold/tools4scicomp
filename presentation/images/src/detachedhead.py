from pyx import canvas, color, deco, path, text, unit

class mycanvas(canvas.canvas):
    def draw_commit(self, x, y, nr, r, dx,
                    fillcolor=color.hsb(0.16, 0.2, 1), strokecolor=color.hsb(0.16, 1, 0.9)):
        p = path.circle(x, y, r)
        self.draw(p, [deco.stroked([strokecolor]), deco.filled([fillcolor])])
        self.text(x, y, fr'\textsf{{{nr}}}', [text.halign.center, text.valign.middle])
        return path.circle(x, y, r+dx)

    def draw_label(self, x, y, label, dx, fillcolor, strokecolor):
        t = text.text(x, y, fr'\textsf{{{label}}}', [text.halign.center, text.valign.middle])
        tbox = t.bbox().enlarged(dx).path()
        self.draw(tbox, [deco.stroked([strokecolor]), deco.filled([fillcolor])])
        self.insert(t)
        return t.bbox().enlarged(1.5*dx).path()

    def draw_arrow(self, x1, y1, x2, y2, outline1, outline2):
        p = path.line(x1, y1, x2, y2)
        p1, _ = p.intersect(outline1)
        p2, _ = p.intersect(outline2)
        p = p.split((p1[0], p2[0]))
        self.stroke(p[1], [deco.earrow])


text.set(text.LatexEngine)
commitfillcolor=color.hsb(0.16, 0.2, 1)
commitstrokecolor=color.hsb(0.16, 1, 0.9)
branchfillcolor = color.hsb(0.6, 0.2, 1)
branchstrokecolor = color.hsb(0.6, 1, 0.9)
headfillcolor = color.hsb(0.05, 0.2, 1)
headstrokecolor = color.hsb(0.05, 1, 0.9)

r = 0.7
dx_commit = 0.05
dx_tag = 0.1
elems = (('text', -2.1, 0, '...'),
         ('commit', 0, 0, '4a49a85'),
         ('commit', 2.5, 0, 'f6a49f3'),
         ('commit', 5, 0, '60234ed'),
         ('commit', 7.5, 0, '1a55fb0'),
         ('commit', 3.75, -2, '4e8e665'),
         ('branch', 7.5, 1.5, 'main'),
         ('branch', 3.75, -3.5, 'test'),
         ('head', 7.5, 2.5, 'HEAD'),
         ('head', 2.5, 1.5, 'HEAD'),
         ('head', 3.75, -4.5, 'HEAD'),
         ('head', 3.75, -3.5, 'HEAD'))
outlines = []
canvas_elems = []
for type, x, y, nr in elems:
    c = mycanvas()
    if type == 'commit':
        outline = c.draw_commit(x, y, nr, r, dx_commit, commitfillcolor, commitstrokecolor)
    elif type == 'branch':
        outline = c.draw_label(x, y, nr, dx_tag, branchfillcolor, branchstrokecolor)
    elif type == 'head':
        outline = c.draw_label(x, y, nr, dx_tag, headfillcolor, headstrokecolor)
    else:
        t = text.text(x, y, nr)
        outline = t.bbox().enlarged(dx_tag).path()
        c.insert(t)
    canvas_elems.append(c)
    outlines.append(outline)

params = {1: ((0, 1, 2, 3, 4, 6, 8),
              ((1, 0), (2, 1), (3, 2), (4, 3), (6, 4), (8, 6))),
          2: ((0, 1, 2, 3, 4, 6, 9),
              ((1, 0), (2, 1), (3, 2), (4, 3), (9, 2), (6, 4))),
          3: ((0, 1, 2, 3, 4, 5, 11),
              ((1, 0), (2, 1), (3, 2), (4, 3), (5, 2), (11, 5))),
          4: ((0, 1, 2, 3, 4, 5, 7, 10),
              ((1, 0), (2, 1), (3, 2), (4, 3), (5, 2), (7, 5), (10, 7)))
          }
               
for lfdnr, (nrs, links) in params.items():
    c = mycanvas()
    for nr in nrs:
        c.insert(canvas_elems[nr])
    for n1, n2 in links:
        c.draw_arrow(*elems[n1][1:3], *elems[n2][1:3], outlines[n1], outlines[n2])
    c.writePDFfile(f'detachedhead_{lfdnr}.pdf')
    c.writeGSfile(f'detachedhead_{lfdnr}.png', device="png16m", resolution=600)
