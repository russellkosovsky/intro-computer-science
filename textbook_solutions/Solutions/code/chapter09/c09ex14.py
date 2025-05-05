# c09ex14.py
#   Graphical random walk (auto-doodler)

from random import random
from math import sin, cos, pi
from graphics import *


def main():

    print("Graphical Random Walk\n")
    n = int(input("How many steps should I take? "))

    win = GraphWin("Random Walk", 500,500)
    win.setCoords(-50,-50, 50, 50)
    curr = Point(0,0)
    next = Point(0,0)
    for i in range(n):
        angle = random()* 2 * pi
        dx = cos(angle)
        dy = sin(angle)
        next.move(dx,dy)
        Line(curr,next).draw(win)
        curr.move(dx,dy)
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()

