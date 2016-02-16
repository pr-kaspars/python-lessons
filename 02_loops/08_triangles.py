from graphics import *

win = GraphWin('Triangles', 500, 400)

for r in range(0, 20):
    for c in range(0, r):
        p1 = Point(c * 20, r * 15)
        p2 = Point(c * 20 + 15, r * 15)
        p3 = Point(c * 20 + 15, r * 15 + 10)
        l1 = Line(p1, p2)
        l2 = Line(p2, p3)
        l3 = Line(p3, p1)
        l1.draw(win)
        l2.draw(win)
        l3.draw(win)

win.getMouse()
win.close()
