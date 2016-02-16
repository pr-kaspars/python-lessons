from graphics import *

h = 300
w = 300
win = GraphWin('Concentric', w, h)

r = 5
while r <= min(w, h) / 2:
    circle = Circle(Point(w / 2, h / 2), r)
    circle.draw(win)
    r = r + 5

win.getMouse()
win.close()
