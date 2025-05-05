#COM110 Graphis
#drawing a point

# import everything from graphics.py
from graphics import *
	
def main():
    # create window
    myWin = GraphWin('Fun!', 400,400)
    # create point
    myPt = Point(100, 100)
    # draw point
    myPt.draw(myWin)

    # challenge 1: draw 10 points on mouse click point
    for i in range(10):
        # variable that stores location of mouse click
        click = myWin.getMouse()
        # draw a point in the location of the mouse click
        click.draw(myWin)

    # challenge 2: draw a line from (100,200) to (300,200)
    myLine = Line(Point(100,200), Point(300,200))
    myLine.draw(myWin)

    # close window
    myWin.getMouse()
    myWin.close()
    
main()
