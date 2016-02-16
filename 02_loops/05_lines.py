from graphics import *

h = 100
w = 500

win = GraphWin('Lines', w, h)

x = 0
while x <= w:
    line = Line(Point(x, 5), Point(x, 15))
    line.draw(win)
    x = x + 10

win.getMouse()
win.close()
