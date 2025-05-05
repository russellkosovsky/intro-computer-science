#COM110 Graphis
#drawing a line

from graphics import *
	
def main():

    # create window
    myWin = GraphWin('Fun!', 400,400)

    # draw a line from (100, 100) to (200,100)
    myLine = Line(Point(100,100), Point(200,100))
    myLine.draw(myWin)

    # challenge 1: draw a rectangle uing 4 lines
    # upper-left corner (100, 200) lower-right corner (200,300)

    recLine = Line(Point(100,200), Point(200,200))
    recLine.draw(myWin)
    recLine = Line(Point(200,200), Point(200,300))
    recLine.draw(myWin)
    recLine = Line(Point(200,300), Point(100,300))
    recLine.draw(myWin)
    recLine = Line(Point(100,300), Point(100,200))
    recLine.draw(myWin)

    # challenge 2: draw a solid black rectangle
    # upper-left corner (100, 300) lower-right corner (200,400)

    
    
    #wait for mouse click to close window
    myWin.getMouse()
    myWin.close()

main()
