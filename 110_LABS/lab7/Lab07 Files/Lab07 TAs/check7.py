#COM 110 Graphical User Interfaces (GUIs)
#button.py program
#Draw two buttons and depending which button the user clicks, draw a circle or square.

from graphics import *
import math

def main():
    win=GraphWin("Button GUI", 600,600)

    win.setCoords(0, 0, 100,100)
    

    drawButton(win, Point(25,90), Point(35,96), "Circle")
    drawButton(win, Point(65,90), Point(75,96), "Square")
    drawButton(win, Point(45,90), Point(55,96), "Exit")

    #optional
    closeMessage = Text(Point(50,20), "Click anywhere to end program.")
    closeMessage.draw(win)

    #Get a mouse click and then check if it is in the button 
    pt = win.getMouse()

    #While the Exit button is not clicked
    while not (45 <= pt.getX() <= 55 and 90 <= pt.getY() <= 96):
        #Check the other two buttons
        if (pt.getX()>=25 and pt.getX()<=35 and pt.getY()>=90 and pt.getY()<=96):
            drawCircle(win) #invokes the drawCircle() function defined below
        elif (pt.getX()>=65 and pt.getX()<=75 and pt.getY()>=90 and pt.getY()<=96):
            drawSquare(win)

        #Get another mouse click
        pt = win.getMouse()

    #Exit button is clicked, close win
    win.close()

def drawButton(gwin, pt1, pt2, words):
    button = Rectangle(pt1, pt2)
    button.setFill("blue3")
    button.draw(gwin)
    labelx = (pt1.getX() + pt2.getX())/2
    labely = (pt1.getY() + pt2.getY())/2
    label = Text(Point(labelx,labely),words)
    label.setFill("white")
    label.draw(gwin)
    
def drawCircle(gwin):
    circ=Circle(Point(50,50),20)
    circ.setFill("red")
    circ.draw(gwin)

def drawSquare(gwin):
    sq = Rectangle(Point(25,25),Point(75,75))
    sq.setFill("red")
    sq.draw(gwin)

def distance(p1, p2):
    dist = math.sqrt((p2.getX()-p1.getX())**2+(p2.getY()-p1.getY())**2)
    return dist
                  
main()
