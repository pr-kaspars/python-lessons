from graphics import *
import random

win = GraphWin('Points', 400, 400)

for n in range(0, 1000):
    r = random.randrange(256)
    b = random.randrange(256)
    g = random.randrange(256)

    x = random.randrange(400)
    y = random.randrange(400)
    point = Point(x, y)
    point.setOutline(color_rgb(r, g, b))
    point.draw(win)

win.getMouse()
win.close()
