from graphics import *
import math

win = GraphWin('Diogonals', 320, 170)

for i in range(1, 30):
    circle = Circle(Point(i * 10, math.fabs(15 - i) * 10 + 10), 5)
    circle.draw(win)

win.getMouse()
win.close()
