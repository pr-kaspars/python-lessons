from graphics import *
import math

win = GraphWin('Start', 300, 300)

face = Circle(Point(150, 150), 140)
face.draw(win)

eye1 = Circle(Point(80, 80), 15)
eye1.draw(win)

eye2 = Circle(Point(220, 80), 15)
eye2.draw(win)

nose = Line(Point(150, 80), Point(150, 180))
nose.draw(win)

mouth = Line(Point(80, 210), Point(220, 210))
mouth.draw(win)

win.getMouse()
win.close()
