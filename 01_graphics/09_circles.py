from graphics import *
import math

win = GraphWin('Triangle', 220, 220)

r = 50

a = Point(110, 150 - math.sqrt(3) * r)
b = Point(60, 150)
c = Point(160, 150)

c1 = Circle(a, r)
c2 = Circle(b, r)
c3 = Circle(c, r)

c1.draw(win)
c2.draw(win)
c3.draw(win)

win.getMouse()
win.close()
