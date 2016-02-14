from graphics import *

win = GraphWin('Shapes 01', 220, 220)

outer_rectangle = Rectangle(Point(10, 10), Point(210, 210))
outer_rectangle.draw(win)

outer_circle = Circle(Point(110, 110), 100)
outer_circle.draw(win)

line_1 = Line(Point(10, 110), Point(110, 10))
line_1.draw(win)

line_2 = Line(Point(110, 10), Point(210, 110))
line_2.draw(win)

line_3 = Line(Point(210, 110), Point(110, 210))
line_3.draw(win)

line_4 = Line(Point(110, 210), Point(10, 110))
line_4.draw(win)

inner_rectangle = Rectangle(Point(60, 60), Point(160, 160))
inner_rectangle.draw(win)

inner_circle = Circle(Point(110, 110), 50)
inner_circle.draw(win)

win.getMouse()
win.close()
