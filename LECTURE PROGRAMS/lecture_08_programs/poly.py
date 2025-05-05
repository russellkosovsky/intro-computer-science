#COM110 Graphics
#draw a polygon

from graphics import *

def main():

    # create window
    myWin = GraphWin('Fun!', 400,400)

    # create a polygon and draw it
    myPoly = Polygon(Point(200,100), Point(100,300), Point(300,300))
    myPoly.draw(myWin)

    # challenge: draw interactive polygon
    # i.e. take five mouse click point, then draw a hexagon based on those points
    # hint: use list to store five points. list.append() can add item to a list
    # i.e. pointList = []
    #      pointList.append(myWin.getMouse())

    #wait for mouse click to close window
    myWin.getMouse()
    myWin.close()

main()
