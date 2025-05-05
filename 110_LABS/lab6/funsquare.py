#COM110 Lab6 sample program

from graphics import *
from random import *
from time import *

###you may copy & paste isClicked() function we made in class here
#tests if the point is within the rectangle object or not
def isClicked(button, point):

    #find x and y coordinate of the point
    x = point.getX()
    y = point.getY()

    #get two corner points of the rectangle object
    pt1 = button.getP1()
    pt2 = button.getP2()


    #calc min/max for the range of x and y
    minX = min(pt1.getX(), pt2.getX())
    maxX = max(pt1.getX(), pt2.getX())
    minY = min(pt1.getY(), pt2.getY())
    maxY = max(pt1.getY(), pt2.getY())

    #test if (x,y) fits within the rectangle area
    if ( pt1.getX() <= x <= pt2.getX() and pt1.getY() <= y <= pt2.getY()):
        return True
    else:
        return False

def randColor(shape):

    for i in range(50):
        shape.setFill(color_rgb(randrange(0,255),randrange(0,255),randrange(0,255)))
        sleep(.2)
        
def main():

    #create window    
    win = GraphWin("Fun #5", 600, 600)

    #create & draw a rectangle
    square = Rectangle(Point(200,200),Point(400,400))
    square.draw(win)

    ###your code to check user's mouse click on the rectangle
    ###recall isClicked function we implemented in class
    ###recall indefinite while loop and randrange function

    click = win.getMouse()

    while isClicked(square, click):
        randColor(square)
        click = win.getMouse()
    
    #wait for mouse click and then close window
    win.getMouse()
    win.close()



main()



