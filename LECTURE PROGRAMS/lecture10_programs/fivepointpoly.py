from graphics import *
from time import *

def main():

    #create window with size of 600 x 600
    win = GraphWin("Interactive Drawing", 600, 600, autoflush=False)

    #a text object for onscreen instruction and message
    msgLabel = Text(Point(300, 35), 'Click mouse to add a point (5 points)')
    msgLabel.setSize(15)
    msgLabel.draw(win)

    #point list to store mouse click points
    pointList = []

    # takes 5 mouse click and append it to pointList
    for i in range(5):
        target = win.getMouse()
        pointList.append(target)
        #for reference draw a point on window
        target.draw(win)        

    #all 5 points are collected. let's draw a ploygon
    myPoly = Polygon(pointList)
    myPoly.draw(win)
    myPoly.setFill('red')

    #some message to a user
    msgLabel.setText('Good job. Very interesting shape. Click anywhere to close.')

    #wait for click to close window
    win.getMouse()
    
    # close window
    win.close()  

main()
