from pyx import canvas, color, deco, path, style, text, trafo

def arrow(x, y, col, mirror=False):
    p = path.curve(0, 0, 0.5, 0, 0.5, -0.1, 0.05, -0.2)
    if mirror:
        t = trafo.mirror(0).translated(x, y)
    else:
        t = trafo.translate(x, y)
    c.stroke(p, [deco.earrow, col, t])

text.set(text.LatexEngine)

color_top = color.hsb(0.3, 0.5, 0.7)
color_bottom = color.hsb(0.6, 0.5, 0.7)
color_frame = color.hsb(0.05, 1, 0.5)

w = 5
d = 0.1
c = canvas.canvas()
c.fill(path.rect(0, 0, w+1, w), [color.grey(1)])
c.fill(path.rect(0, 0, w, w), [color.grey(0.8)])
c.fill(path.rect(d, d, w-2*d, w-2*d), [color.grey(1)])
c.writeGSfile('laplace_communication_1.png', device='png16m', resolution=600)

for i in range(4):
    c.text(d+0.1, (i+0.5)*w/4, rf'$\mathsf{3-i}$', [text.valign.middle, color_frame])
for i in range(1, 4):
    y = i*w/4
    c.stroke(path.line(0, y, w, y), [color_frame, style.linewidth.thick])
c.stroke(path.rect(0, 0, w, w), [color_frame, style.linewidth.thick])
c.writeGSfile('laplace_communication_2.png', device='png16m', resolution=600)

for i in range(1, 4):
    y = i*w/4
    c.fill(path.rect(0, y, w, d), [color_top])
    c.fill(path.rect(0, y, w, -d), [color_bottom])
    c.stroke(path.line(0, y, w, y), [color_frame, style.linewidth.thick])
c.stroke(path.rect(0, 0, w, w), [color_frame, style.linewidth.thick])
c.writeGSfile('laplace_communication_3.png', device='png16m', resolution=600)

for i in range(1, 4):
    y = i*w/4
    arrow(w+d, y+0.5*d, color_top)
    arrow(w+d+0.5, y-0.5*d, color_bottom, True)
c.writeGSfile('laplace_communication_4.png', device='png16m', resolution=600)
