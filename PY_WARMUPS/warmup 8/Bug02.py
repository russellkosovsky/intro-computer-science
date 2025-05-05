#Bug02.py
#
#the purpose of this module is to take five mouse clicks from a user
#at each mouse click, program shows coordinate of the click point
#however, while writing the program many errors were encounted
#plesae fix those errors and explain!
#remeber that you need to copy graphics.py file in the same directory
#as this module to run the program

from graphics import *


def drawCoord(win, pt):

    #first draw the click point
    pt.draw(win)

    #create string to show coordinate information: i.e. (x, y)
    xCoord = int( pt.getX())
                  # () was never closed
    yCoord = int(pt.getY())
    text = "(" + str(xCoord) + ", " + str(yCoord) + ")"

    #create and draw a text object with the coordinate information
    Text(pt, text).draw(win)
    # needed to add (win) after .draw so it shows in myWin

def main():

    #create a window
    myWin = GraphWin("Print Coordinate", 400, 400);

    #print out program intro message
    introMsg = "This program shows the coordinate for your mouse click point\nPlease click anywhere five times."
    Text(Point(200, 40), introMsg).draw(myWin)

    #take five clicks
    for i in range(5):
        
        #wait for a click
        click = myWin.getMouse()

        #call draw coordinate function
        drawCoord(myWin, click)
        # you need to use myWin as a paremeter so that it assigns myWin to win in the drawCoord function
        # you also need to use click is the paremeter because it assigns the value of the mouse click to the pt paremeter in the defCoord function

    #wait for one more click to close the window
    myWin.getMouse()
    myWin.close()



main()
