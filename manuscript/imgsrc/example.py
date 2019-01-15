from pyx import canvas, color, path

c = canvas.canvas()
c.fill(path.rect(-1.5, -1.5, 3, 3), [color.rgb(1, 1, 0)])
c.fill(path.rect(-1, 0, 1, 1), [color.rgb(0.8, 0, 0)])
c.fill(path.rect(0, -1, 1, 1), [color.rgb(0.8, 0, 0)])
c.fill(path.rect(0, 0, 1, 1), [color.rgb(0, 0, 0.8)])
c.fill(path.rect(-1, -1, 1, 1), [color.rgb(0, 0, 0.8)])
c.writePDFfile()
c.writeGSfile(device="png16m", resolution=600)
