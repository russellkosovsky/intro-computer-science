#illustration of looping mouse clicks until close button is clicked

from graphics import *

#in the GraphWin object gwin, this function draws
#a blue rectangular button with corners at Point objects pt1 and pt2
#then labels the button with the string variable words
def drawButton(gwin, pt1, pt2, words):
    button = Rectangle(pt1, pt2)
    button.setFill("blue3")
    button.draw(gwin)
    #find the x and y coords of the middle of the button
    labelx = (pt1.getX() + pt2.getX())/2.0 
    labely = (pt1.getY() + pt2.getY())/2.0
    #use these coords for the position of the label
    label = Text(Point(labelx,labely),words)
    label.setFill("white")
    label.draw(gwin)

def main():
    win = GraphWin("Loop Test",600,600)
    drawButton(win, Point(250,500), Point(350,450),"Exit")
    
    prompt = Text(Point(300,300),"Click \"exit\" to close.")
    prompt.draw(win)
    
    pt = win.getMouse() #Get a mouse click

    #While the Epoint is not in the Exit button ...
    while not (pt.getX() >= 250 and pt.getX() <= 350 and pt.getY() <= 500 and pt.getY() >= 450):

        #Just draw the clicked point
        pt.draw(win)

        #Get another point
        pt = win.getMouse()

    #Exit button is clicked, close win
    win.close()

main()
