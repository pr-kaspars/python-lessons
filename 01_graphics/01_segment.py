from graphics import *

win = GraphWin('Segment', 220, 220)

line = Line(Point(10, 10), Point(210, 10))

line.draw(win)

win.getMouse()
win.close()
