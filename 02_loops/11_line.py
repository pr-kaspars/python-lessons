from graphics import *
import random

win = GraphWin('Points', 400, 400)

p0 = None
for n in range(0, 10):
    x = random.randrange(400)
    y = random.randrange(400)
    p1 = Point(x, y)

    if p0 is not None:
        line = Line(p0, p1)
        line.draw(win)

    p0 = p1

win.getMouse()
win.close()
