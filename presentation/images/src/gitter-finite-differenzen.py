from pyx import canvas, color, deco, path, text

d = 2.27
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

c.text(r-d, r-d, '$\Phi_{n-1, m-1}$')
c.text(r, r-d, '$\Phi_{n, m-1}$')
c.text(r+d, r-d, '$\Phi_{n+1, m-1}$')
c.text(r-d, r, '$\Phi_{n-1, m}$')
c.text(r, r, '$\Phi_{n, m}$')
c.text(r+d, r, '$\Phi_{n+1, m}$')
c.text(r-d, r+d, '$\Phi_{n-1, m+1}$')
c.text(r, r+d, '$\Phi_{n, m+1}$')
c.text(r+d, r+d, '$\Phi_{n+1, m+1}$')

c.text(-d-0.2, d/2, '$\Delta$', [text.halign.right, text.valign.middle])
c.text(-d-0.2, -d/2, '$\Delta$', [text.halign.right, text.valign.middle])
c.text(-d/2, -d-0.3, '$\Delta$', [text.halign.center, text.valign.top])
c.text(d/2, -d-0.3, '$\Delta$', [text.halign.center, text.valign.top])

c.writeGSfile(device="png16m", resolution=600)
