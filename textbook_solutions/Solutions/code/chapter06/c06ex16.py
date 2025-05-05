# c06ex16.py
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

def interactiveFace(w):
    center = w.getMouse()
    edge = w.getMouse()
    radius = distance(center, edge)
    drawFace(center, radius, w)

def distance(p1, p2):
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    return (dx*dx + dy*dy)**.5

def createPicWin(picFile):
    img = Image(Point(0,0),picFile)
    width = img.getWidth()
    height = img.getHeight()
    win = GraphWin(picFile, width, height)
    img.move(width//2, height//2)
    img.draw(win)
    return win
    
def main():
    print("Photo Anonymizer: Draw faces over pictures.")
    picFile = input("Enter name of file containing GIF image: ")
    win = createPicWin(picFile)
    numFaces = int(input("How many faces to draw? "))
    for i in range(numFaces):
        print("Click center and edge of a face.")
        interactiveFace(win)
    print("Click again to quit.")
    win.getMouse()
    win.close()
    
main()
