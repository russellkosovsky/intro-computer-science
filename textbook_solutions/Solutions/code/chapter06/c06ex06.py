# c06ex06.py

import math
from graphics import *

def square(x):
    return x * x

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX())
                     + square(p2.getY() - p1.getY()))
    return dist

def triArea(a, b, c):
    s = (a+b+c)/2.0
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

def main():
    win = GraphWin("Draw a Triangle",500,500)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Calculate the perimeter of the triangle
    d1 = distance(p1,p2)
    d2 = distance(p2,p3)
    d3 = distance(p3,p1)
    message.setText("perimeter: %0.2f  area: %0.2f "
                    % ((d1+d2+d3),triArea(d1,d2,d3)))

    # Wait for another click to exit
    win.getMouse()

main()
