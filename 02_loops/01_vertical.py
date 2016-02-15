from graphics import *

win = GraphWin('Vertical line', 200, 400)

for i in range(1, 20):
    circle = Circle(Point(20, i * 10), 5)
    circle.draw(win)

win.getMouse()
win.close()