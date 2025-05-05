# c07ex17.py
#    Bouncing circle

import time
from graphics import *

def main():
    win = GraphWin("Bounce", 401, 401)
    win.setCoords(-200,-200, 200, 200)
    radius = 20
    c = Circle(Point(0,160), radius)
    c.setFill("red")
    c.draw(win)
    dx = 1
    dy = 1
    for i in range(10000):
        c.move(dx,dy)
        center = c.getCenter()
        cx, cy = center.getX(), center.getY()
        if 200 - abs(cx) == radius:
            dx = -dx
        if 200 - abs(cy) == radius:
            dy = -dy
        update(30)
        # This exit is optional. The break statement is covered in Chapter 8
        if win.checkMouse() != None:
            break
    win.close()

main()
