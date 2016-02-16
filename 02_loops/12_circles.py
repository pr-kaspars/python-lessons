from graphics import *
import random

win = GraphWin('Points', 400, 400)

for n in range(0, 100):
    r = random.randrange(256)
    b = random.randrange(256)
    g = random.randrange(256)

    x = random.randrange(400 - 80) + 40
    y = random.randrange(400 - 80) + 40
    r = random.randrange(40)
    circle = Circle(Point(x, y), r)
    circle.setOutline(color_rgb(r, g, b))
    circle.draw(win)

win.getMouse()
win.close()
