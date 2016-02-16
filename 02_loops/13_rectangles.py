from graphics import *
import random

win = GraphWin('Rectangles', 400, 400)

for n in range(0, 100):
    p1 = Point(random.randrange(400), random.randrange(400))
    p2 = Point(random.randrange(400), random.randrange(400))
    rectangle = Rectangle(p1, p2)
    rectangle.draw(win)

win.getMouse()
win.close()
