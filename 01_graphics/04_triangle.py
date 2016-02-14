from graphics import *

win = GraphWin('Triangle', 120, 70)

l1 = Line(Point(10, 10), Point(10, 60))
l2 = Line(Point(10, 60), Point(110, 60))
l3 = Line(Point(10, 10), Point(110, 60))

l1.draw(win)
l2.draw(win)
l3.draw(win)

win.getMouse()
win.close()
