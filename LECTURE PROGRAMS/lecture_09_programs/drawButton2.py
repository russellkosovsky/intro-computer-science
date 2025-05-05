from graphics import *
from time import *

###drawButton() function we made in class 
def drawButton(win, pt1, pt2, label):
    button = Rectangle(pt1, pt2)
    button.setFill("blue3")
    button.draw(win)

    #use these coords for the position of the label
    btnLabel = Text( button.getCenter(), label)
    btnLabel.setFill("white")
    btnLabel.draw(win)

    return button

###isClicked() function we made in class 
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

    #range test
    if ( minX <= x <= maxX and minY <= y <= maxY):
        return True
    else:
        return False

def main():

    #create window with size of 600 x 600
    win = GraphWin("Interactive Drawing", 600, 600, autoflush=False)

    #quit button
    quitBtn = drawButton(win, Point(200,200), Point(100,100), "Quit")
    
    #wait for click to close window
    pt = win.getMouse()
    while not isClicked(quitBtn, pt):
        print("button is not clicked")
        pt = win.getMouse()
        
    # close window
    win.close()  

main()
