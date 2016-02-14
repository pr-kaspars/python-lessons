# Graphics

## Window

Graphics module isn’t part of python, it must be imported.

```python
from graphics import *
```

A window is required to display graphics. Let’s create and display a small
(200 by 200 pixels) window.

```python
win = GraphWin()
```

Computer screens usually are much bigger. To use that advantage in our favour,
size of the window can be changed.

```python
win = GraphWin("Hello World", 500, 300)
```

The line above will create a window 500 pixels wide, 300 pixels high and give
it a title ‘Hello world’
You probably noticed that window appears only for a split second on the screen.
Because draw window is the last instruction in our program interpreter draws
the window and exits immediately after. That can be easily fixed by making
window close only after a mouse click.

```python
from graphics import *
win = GraphWin("Hello world", 500, 300)
win.getMouse()
win.close()
```

## Drawing in the Window

So far we learned how to display an empty window and make it close after a
mouse click but GraphWin is capable of much more and in this chapter we will
learn how to display basic elements: `Point`, `Line`, `Circle` and `Rectangle`.

```python    
pt = Point(100, 50)
```

This creates a point at the location (100, 50), 100 pixels right from the left
side edge of the window and 50 pixels down from the top. Unlike when GraphWin
is created, nothing is immediately displayed. That is because a single Python
program can create more than one window and we must explicitly say in which
window we want to display the object. Most objects from graphics library have
draw function that display them in the specified window. For the `Point` we
just created it can be done by the following instruction:

```python
pt.draw(win)
```

> Display four points _A_, _B_, _C_ & _D_ on the screen so that
> _AB = BC = CD = DA_. Can you make program that allows to enter distance when
> ran?

To draw a circle on the screen using Python we need to specify only two things:
centre and radius of the circle. A `Point` can be given as the centre of the
circle and any number larger or equal to zero as the radius.

```python
circle1 = Circle(Point(10, 10), 5)
circle1.draw(win)
pt = Point(20, 10)
circle2 = Circle(pt, 5)
circle2.draw(win)
```

The following block draws a straight line between two points a & b:

```python
a = Point(10, 10)
b = Point(30, 10)
line = Line(a, b)
line.draw(win)
```

`Rectangle` will draw a rectangle _ABCD_ if it's two opposite opposite vertices
_A_ & _B_ will be given:

```python
a = Point(10, 10)
c = Point(20, 30)
rectangle = Rectangle(a, c)
rectangle.draw(win)
```

## Exercises

1. Create a program that draws hosizontal line segment
2. Create a program that draws simetrical plus sign
3. Create a program that draws 5 squares using 2 `Recangle` objects
4. Create a program that draws right-angled triangle
5. Create a program that draws a star
6. Create a program that draws a face and colours it
7. Create a program that draws a triangle _ABC_, it's height _BD_ and median
_BE_
8. Create a program that draws 3 triangles with random numbers as they center
coordinates and radius
9. Create a program that draws 3 triangles so that they are touching each other
