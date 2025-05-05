# c10ex14.py
#    A moving face

from random import randrange
from graphics import *
from button import Button
import time

class Face:

    def __init__(self, window, center, size):
        eyeSize = 0.15 * size
        eyeOff = size / 3.0
        mouthSize = 0.8 * size
        mouthOff = size / 2.0
        mouth1Size = 0.3 * size
        self.head = Circle(center, size)
        self.head.draw(window)
        self.leftEye = Circle(center, eyeSize)
        self.leftEye.move(-eyeOff, -eyeOff)
        self.rightEye = Circle(center, eyeSize)
        self.rightEye.move(eyeOff, -eyeOff)
        self.leftEye.draw(window)
        self.rightEye.draw(window)
        p1 = center.clone()
        p1.move(-mouthSize/2, mouthOff)
        p2 = center.clone()
        p2.move(mouthSize/2, mouthOff)
        self.mouth = Line(p1,p2)
        self.mouth.draw(window)
        self.center = center.clone()
    
    def move(self, dx,dy):
        for part in [self.head, self.mouth, self.leftEye,
                     self.rightEye, self.center]:
            part.move(dx,dy)

    def getCenter(self):
        return self.center.clone()
   
def main():
    # Create a window
    window = GraphWin("Moving Face")
    face = Face(window, Point(100,50), 40)

    dx = 1
    dy = 1
    while True:
        if window.checkMouse() != None:
            break
        c = face.getCenter()
        faceX, faceY = c.getX(), c.getY()
        if faceX < 40 or faceX > 160:
            dx = -dx
        if faceY < 40 or faceY > 160:
            dy = -dy
        face.move(dx,dy)
        update(100)
        
    window.close()

main()




        

