from graphics import *

win = GraphWin('Plus', 220, 220)

l1 = Line(Point(10, 110), Point(210, 110))
l2 = Line(Point(110, 10), Point(110, 210))

l1.draw(win)
l2.draw(win)

win.getMouse()
win.close()
