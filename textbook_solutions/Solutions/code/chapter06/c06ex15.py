# c06ex15.py
#   face drawing program


from graphics import *

def drawFace(center, size, window):
    eyeSize = 0.15 * size
    eyeOff = size / 3.0
    mouthSize = 0.8 * size
    mouthOff = size / 2.0
    head = Circle(center, size)
    head.setFill("yellow")
    head.draw(window)
    leftEye = Circle(center, eyeSize)
    leftEye.move(-eyeOff, -eyeOff)
    rightEye = Circle(center, eyeSize)
    rightEye.move(eyeOff, -eyeOff)
    leftEye.draw(window)
    rightEye.draw(window)
    p1 = center.clone()
    p1.move(-mouthSize/2, mouthOff)
    p2 = center.clone()
    p2.move(mouthSize/2, mouthOff)
    mouth = Line(p1,p2)
    mouth.draw(window)

def test():
    win = GraphWin("Faces")
    drawFace(Point(50,50), 10, win)
    drawFace(Point(100,100), 20, win)
    drawFace(Point(150,150), 30, win)
    win.getMouse()
    win.close()
    

test()
