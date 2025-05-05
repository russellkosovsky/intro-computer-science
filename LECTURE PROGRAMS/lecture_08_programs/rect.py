#COM110 Graphis
#drawing a rectangle

from graphics import *

def main():

    # create window
    myWin = GraphWin('Fun!', 400,400)

    # draw a rectangle and fill color with red
    myRect = Rectangle(Point(200,200), Point(300,300))
    myRect.setFill('red')
    myRect.draw(myWin)


    # challenge: interactive rect stamping tool
    # draw 10 rects on mouse click point
    # hint point object has methods, getX() and getY() to return coordinate value


    #wait for mouse click to close window
    myWin.getMouse()
    myWin.close()
    
main()
