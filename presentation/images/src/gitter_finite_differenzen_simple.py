from pyx import canvas, color, deco, path, text

d = 1.5
r = 0.3
color_central = color.hsb(0.08, 1, 0.9)
color_neighbor = color.hsb(0.08, 0.4, 0.9)

c = canvas.canvas()

for offset in (-d, 0, d):
    c.stroke(path.line(-1.5*d, offset, 1.5*d, offset))
    c.stroke(path.line(offset, -1.5*d, offset, 1.5*d))

c.stroke(path.circle(-d, d, r), [deco.filled([color.grey(1)])])
c.stroke(path.circle(-d, -d, r), [deco.filled([color.grey(1)])])
c.stroke(path.circle(d, d, r), [deco.filled([color.grey(1)])])
c.stroke(path.circle(d, -d, r), [deco.filled([color.grey(1)])])
c.fill(path.circle(0, 0, r), [color_central])
c.fill(path.circle(0, d, r), [color_neighbor])
c.fill(path.circle(0, -d, r), [color_neighbor])
c.fill(path.circle(d, 0, r), [color_neighbor])
c.fill(path.circle(-d, 0, r), [color_neighbor])

c.writeGSfile(device="png16m", resolution=600)
