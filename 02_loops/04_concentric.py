from graphics import *
import math

h = 300
w = 300
win = GraphWin('Concentric', w, h)

r = math.floor(min(w, h) / (2 * 5)) * 5
while r >= 5:
    circle = Circle(Point(w / 2, h / 2), r)

    if r % 10 == 0:
        circle.setFill('red')
    else:
        circle.setFill('blue')

    circle.draw(win)
    r = r - 5

win.getMouse()
win.close()
