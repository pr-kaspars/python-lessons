from graphics import *

win = GraphWin('Triangle', 300, 130)

a = Point(10, 120)
b = Point(200, 10)
c = Point(290, 120)
d = Point(200, 120)
e = Point(150, 120)

ab = Line(a, b)
bc = Line(b, c)
ca = Line(c, a)
bd = Line(b, d)
be = Line(b, e)

ab.draw(win)
bc.draw(win)
ca.draw(win)
bd.draw(win)
be.draw(win)

win.getMouse()
win.close()
