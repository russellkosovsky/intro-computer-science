
from random import random
from graphics import *

def main():
    throws = int(input("How many darts to throw?: "))
    count = 0

    #Adding graphics is part of Bonus A.No graphics for check 3,4
    win = GraphWin("Monte Carlo Visualization",500,500)
    win.setCoords(-1.25,-1.25,1.25,1.25)
    Rectangle(Point(-1,-1) ,Point(1,1)).draw(win)
    Circle(Point(0,0),1).draw(win)
    Line(Point(-1.25,0),Point(1.25,0)).draw(win)
    Line(Point(0,1.25),Point(0,-1.25)).draw(win)
    Text(Point(-1.05,-0.05),"-1").draw(win)
    Text(Point(1.05,-0.05),"1").draw(win)
    Text(Point(0.05,-1.05),"-1").draw(win)
    Text(Point(0.05,1.05),"1").draw(win)
    Text(Point(0.1,-0.1),"(0,0)").draw(win)

    # Check 3 & 4
    for i in range(throws):
        x, y = random()*2-1, random()*2-1
        point = Point(x,y)
        point.setFill("red")
        if (x**2 + y**2) <= 1:
            count += 1
            point.setFill("green")
        point.draw(win)

    out = Text(Point(0,-0.3), str(count) + " / " + str(throws)  + " DARTS LANDED IN CIRCLE.\n APPROX. AREA & Pi = " + str(count*4/throws))
    out.setSize(20)
    out.setOutline('red')
    out.setStyle('bold')
    out.draw(win)
    print(count, "darts landed in the circle")
    print("The approximate area of the circle is:",count*4/throws)


    Text(Point(0.75,-1.13),"Click anywhere to close").draw(win)
    win.getMouse()
    win.close()

main()
