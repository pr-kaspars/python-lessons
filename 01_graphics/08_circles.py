from graphics import *
import random

win = GraphWin('Circles', 400, 400)

x = random.random() * 300 + 50
y = random.random() * 300 + 50
r = random.random() * 50
c1 = Circle(Point(x, y), r)

x = random.random() * 300 + 50
y = random.random() * 300 + 50
r = random.random() * 50
c2 = Circle(Point(x, y), r)

x = random.random() * 300 + 50
y = random.random() * 300 + 50
r = random.random() * 50
c3 = Circle(Point(x, y), r)

c1.draw(win)
c2.draw(win)
c3.draw(win)

win.getMouse()
win.close()
