# c10ex13.py
# This is a program that draws a face and provides the user with buttons
# to change the facial expressions.

from random import randrange
from graphics import *
from button import Button

class Face:

    """Simulates drawing a face and changing its expressions."""
    

    def __init__(self, window, center, size):
        eyeSize = 0.15 * size
        eyeOff = size / 3.0
        mouthSize = 0.8 * size
        mouthOff = size / 2.0
        mouth1Size = 0.3 * size
        self.head = Circle(center, size)
        self.head.draw(window)
        self.leftEye0 = Circle(center, eyeSize)
        self.leftEye0.move(-eyeOff, -eyeOff)
        self.leftEye = self.leftEye0
        self.rightEye0 = Circle(center, eyeSize)
        self.rightEye0.move(eyeOff, -eyeOff)
        self.rightEye = self.rightEye0
        self.leftEye.draw(window)
        self.rightEye.draw(window)
        p1 = center.clone()
        p1.move(-mouthSize/2, mouthOff)
        p2 = center.clone()
        p2.move(mouthSize/2, mouthOff)
        p3 = center.clone()
        p3.move(eyeOff, -eyeOff)
        p4 = p3.clone()
        p4.move(eyeOff,0)
        self.mouth0 = Line(p1,p2)
        self.mouth = self.mouth0
        self.mouth.draw(window)
        self.mouth1 = Circle(center, mouth1Size)
        self.mouth1.move(0, mouthOff)
        self.rightEye1 = Line(p3,p4)
        self.leftEye1 = Line(p3,p4)
        self.leftEye1.move(-mouthOff*2, 0)
        self.window = window
    
    def reset(self):
        self.mouth.undraw()
        self.mouth = self.mouth0
        self.mouth.draw(self.window)
        self.leftEye.undraw()
        self.leftEye = self.leftEye0
        self.leftEye.draw(self.window)
        self.rightEye.undraw()
        self.rightEye = self.rightEye0
        self.rightEye.draw(self.window)
        
    def surprise(self):
        self.mouth.undraw()
        self.mouth = self.mouth1
        self.mouth.draw(self.window)
        self.leftEye.undraw()
        self.leftEye = self.leftEye0
        self.leftEye.draw(self.window)
        self.rightEye.undraw()
        self.rightEye = self.rightEye0
        self.rightEye.draw(self.window)
           
    def yawn(self):
        self.mouth.undraw()
        self.mouth = self.mouth1
        self.mouth.draw(self.window)
        self.leftEye.undraw()
        self.leftEye = self.leftEye1
        self.leftEye.draw(self.window)
        self.rightEye.undraw()
        self.rightEye = self.rightEye1
        self.rightEye.draw(self.window)

    def wink(self):
        self.mouth.undraw()
        self.mouth = self.mouth1
        self.mouth.draw(self.window)
        self.leftEye.undraw()
        self.leftEye = self.leftEye0
        self.leftEye.draw(self.window)
        self.rightEye.undraw()
        self.rightEye = self.rightEye1
        self.rightEye.draw(self.window)
   
def main():
    # Create a window
    window = GraphWin("Face",300,300)
    window.setCoords(0,200,200,0)
    face = Face(window, Point(100,100), 40)

    # Create a message
    message1 = Text(Point(100, 20), "Click on a button to change")
    message1.draw(window)
    message2 = Text(Point(100,35), "the face or quit")
    message2.draw(window)

    # Draw the interface widgets
    yawn = Button(window, Point(30,160), 45,20, "Yawn")
    yawn.activate()
    surprise = Button(window, Point(100,160), 60, 20, "Surpise")
    surprise.activate()
    wink = Button(window, Point(170,160), 45, 20, "Wink")
    wink.activate()
    close = Button(window, Point (130, 190), 45, 20, "Quit")
    close.activate()
    reset = Button(window,Point(60, 190), 45, 20, "Reset")
    reset.activate()
   
    # Have user choose a face button and
    # the selected face will appear on the screen
    pt = window.getMouse()
    while not close.clicked(pt):
        if yawn.clicked(pt):
            face.yawn()
        elif surprise.clicked(pt):
            face.surprise()
        elif wink.clicked(pt):
            face.wink()
        else:
            if reset.clicked(pt):
                face.reset()
        pt = window.getMouse()

    # Close the window
    window.close()

main()




        

