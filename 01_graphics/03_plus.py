from graphics import *

win = GraphWin('Plus', 170, 170)

r1 = Rectangle(Point(10, 60), Point(160, 110))
r2 = Rectangle(Point(60, 10), Point(110, 160))

r1.draw(win)
r2.draw(win)

win.getMouse()
win.close()
