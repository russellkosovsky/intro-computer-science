# c11ex17.py
#  Implementation of graphics group

from graphics import *

class GraphicsGroup:

    def __init__(self, anchor):
        self.anchor = anchor.clone()
        self.parts = []

    def getAnchor(self):
        return self.anchor.clone()

    def addObject(self, gObject):
        self.parts.append(gObject)

    def move(self, dx, dy):
        for part in self.parts:
            part.move(dx,dy)
        self.anchor.move(dx,dy)

    def draw(self, win):
        for part in self.parts:
            part.draw(win)

    def undraw(self):
        for part in self.parts:
            part.undraw()

def test():
    # Create a graphics window
    win = GraphWin()
    win.setCoords(-10,-10,10,10)

    # create a face object
    face = GraphicsGroup(Point(0,0))

    # create and add the head
    head = Circle(Point(0,0), 5)
    head.setFill("peachpuff")
    face.addObject(head)

    # create and add eyes
    leftEye = Circle(Point(-2,2), 1)
    face.addObject(leftEye)
    rightEye = leftEye.clone()
    rightEye.move(4,0)
    face.addObject(rightEye)

    # create mouth
    face.addObject(Line(Point(-2,-3.5),Point(2,-3.5)))

    face.draw(win)
    for i in range(10):
        p = win.getMouse()
        x,y = p.getX(), p.getY()
        anchor = face.getAnchor()
        ax,ay = anchor.getX(), anchor.getY()
        face.move(x-ax, y-ay)

if __name__ == '__main__':
    test()
    
