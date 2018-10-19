# Pygame

Pygame module has to be imported before using it.

```python
import pygame
```

A window is required to display graphics. Let’s create window.

```python
pygame.init()
screen = pygame.display.set_mode([600, 600])
```

The lines above will create a 600 by 600 pixels big window. You probably noticed that the window appeared only for a split second on the screen. It happens because our program does not have any instructions after and therefore quits. That can be easily fixed by making window close only when quit button is pressed.

```python
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
```

## Drawing in the Window

So far we learned how to display an empty window and make it close after a
mouse click but Pygame is capable of much more and in this chapter we will
learn how to display basic elements: rectangle, line, circle and arc.

Colours

```python
BLACK = (0, 0, 0)
RED = (234, 67, 54)
PURPLE = (219, 65, 244)
BLUE = (65, 133, 244)
GREEN = (52, 168, 82)
YELLOW = (244, 233, 65)
GREY = (205, 205, 205)
WHITE = (255, 255, 255)
```

0. Update screen

```python
pygame.display.flip()
```

1. Square

```python
pygame.draw.rect(screen, WHITE, (10, 10, 580, 580), 2)
```

2. Circle

```python
pygame.draw.circle(screen, WHITE, (300, 300), 290, 1)
```

3. Line

```python
pygame.draw.line(screen, WHITE, (10, 300), (300, 10), 1)
pygame.draw.line(screen, WHITE, (300, 10), (590, 300), 1)
pygame.draw.line(screen, WHITE, (590, 300), (300, 590), 1)
pygame.draw.line(screen, WHITE, (300, 590), (10, 300), 1)
```

4. Polygon

```python
pygame.draw.polygon(screen, GREEN, [(10, 300), (300, 10), (590, 300), (300, 590)], 0)
```

5. Arc

```python
from math import pi

pygame.draw.arc(screen, RED,    (10, 10, 580, 580), 0         , pi / 2    , 2)
pygame.draw.arc(screen, PURPLE, (10, 10, 580, 580), pi / 2    , pi        , 2)
pygame.draw.arc(screen, BLUE,   (10, 10, 580, 580), pi        , 3 * pi / 2, 2)
pygame.draw.arc(screen, YELLOW, (10, 10, 580, 580), 3 * pi / 2, 2 * pi    , 2)
```

6. Background colour

```python
screen.fill(GREY)
```


Example

```python
from math import pi
import pygame

# Colours
BLACK = (0, 0, 0)
RED = (234, 67, 54)
PURPLE = (219, 65, 244)
BLUE = (65, 133, 244)
GREEN = (52, 168, 82)
YELLOW = (244, 233, 65)
GREY = (205, 205, 205)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode([600, 600])

n = 0
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Background colour
    screen.fill(GREY)

    # Outer circle
    pygame.draw.rect(screen, WHITE, (10, 10, 580, 580), 2)

    # Circle
    pygame.draw.circle(screen, WHITE, (300, 300), 290, 1)

    # Inner square
    pygame.draw.line(screen, WHITE, (10, 300),  (300, 10),  1)
    pygame.draw.line(screen, WHITE, (300, 10),  (590, 300), 1)
    pygame.draw.line(screen, WHITE, (590, 300), (300, 590), 1)
    pygame.draw.line(screen, WHITE, (300, 590), (10, 300),  1)

    # Filled polygon
    pygame.draw.polygon(screen, GREEN, [(10, 300), (300, 10), (590, 300), (300, 590)], 0)

    # Draw arcs
    pygame.draw.arc(screen, RED,    (10, 10, 580, 580), 0         , pi / 2    , 2)
    pygame.draw.arc(screen, PURPLE, (10, 10, 580, 580), pi / 2    , pi        , 2)
    pygame.draw.arc(screen, BLUE,   (10, 10, 580, 580), pi        , 3 * pi / 2, 2)
    pygame.draw.arc(screen, YELLOW, (10, 10, 580, 580), 3 * pi / 2, 2 * pi    , 2)

    # Update display
    pygame.display.flip()
```

## Exercises

1. Create a program that draws horizontal line segment
2. Create a program that draws symmetrical plus sign
3. Create a program that draws 5 squares using 2 rectangles
4. Create a program that draws right-angled triangle
5. Create a program that draws a star
6. Create a program that draws a face and colours it
7. Create a program that draws a triangle _ABC_, it's height _BD_ and median _BE_
8. Create a program that draws 3 triangles with random numbers as they center coordinates and radius
9. Create a program that draws 3 triangles so that they are touching each other
