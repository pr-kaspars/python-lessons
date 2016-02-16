from graphics import *

l0 = 400
win = GraphWin('Chess', l0, l0)

l = 10

x = 0
while x < 400 - l:
    y = 0
    while y < 400 - l:
        rectangle = Rectangle(Point(x, y), Point(x + l, y + l))
        if (x + y) % 20 == 0:
            rectangle.setFill('black')
        rectangle.draw(win)
        y = y + l
    x = x + l

win.getMouse()
win.close()
