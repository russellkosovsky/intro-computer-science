# c07ex14.pyw

from graphics import *
import math

def main():
    print("This program computes the intersection of a circle and")
    print("a horizontal line.")
    print()

    radius = float(input("Please enter the radius of the circle: "))
    yinter = float(input("Please enter the y-intercept of the line: "))

    win = GraphWin("Circle Intersection")
    win.setCoords(-10,-10,10,10)

    Circle(Point(0,0), radius).draw(win)
    Line(Point(-10,yinter), Point(10,yinter)).draw(win)

    if abs(yinter) <= radius:
        x = math.sqrt(radius * radius - yinter * yinter)
        print("X values of intersection", -x, x)

        p1 = Circle(Point(x,yinter),0.25)
        p1.setOutline("red")
        p1.setFill("red")
        p1.draw(win)

        p2 = p1.clone()
        p2.move(-2*x, 0)
        p2.draw(win)
    else:
        print("The line does not intersect the circle.")

    print("Click the window to quit")
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
