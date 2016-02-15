from graphics import *

win = GraphWin('Diogonals', 400, 400)

for i in range(1, 15):
    circle = Circle(Point(i * 10, i * 10), 5)
    circle.draw(win)

for i in range(1, 14):
    circle = Circle(Point((15 - i) * 10 + 130, i * 10), 5)
    circle.draw(win)

win.getMouse()
win.close()
