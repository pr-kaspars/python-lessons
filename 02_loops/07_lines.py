from graphics import *

h = 100
w = 500

win = GraphWin('Lines', w, h)

x = 0
while x <= w - 10:
    for r in range(0, 5):
        l1 = Line(Point(x, 5 + r * 10), Point(x + 10, 15 + r * 10))
        l2 = Line(Point(x, 15 + r * 10), Point(x + 10, 5 + r * 10))
        l1.draw(win)
        l2.draw(win)

    x = x + 10

win.getMouse()
win.close()
