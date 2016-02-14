from graphics import *
import math

win = GraphWin('Start', 320, 320)

l = 150
p0 = None

for i in range(0, 6):
    a = 144 * i + 180
    a1 = math.sin(a * math.pi / 180)
    b1 = math.cos(a * math.pi / 180)
    p1 = Point(160 + a1 * l, 160 + b1 * l)

    if p0 is not None:
        line = Line(p0, p1)
        line.draw(win)

    p0 = p1

win.getMouse()
win.close()
