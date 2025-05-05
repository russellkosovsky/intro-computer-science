# c06ex17.py
#    Moving a shape with a function

from graphics import *

def moveTo(shape, newCenter):
    center = shape.getCenter()
    dx = newCenter.getX() - center.getX()
    dy = newCenter.getY() - center.getY()
    shape.move(dx,dy)

def main():
    win = GraphWin("Circle Mover", 400, 400)
    item = Circle(Point(200,200), 40)
    item.setFill("red")
    item.draw(win)
    for i in range(10):
        p = win.getMouse()
        moveTo(item, p)
    win.getMouse()
    win.close()

main()
