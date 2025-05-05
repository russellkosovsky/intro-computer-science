from graphics import *
from time import *

###drawButton() function we made in class 
def drawButton(win, pt1, pt2, label):
    button = Rectangle(pt1, pt2)
    button.setFill("blue3")
    button.draw(win)

    #find the x and y coords of the middle of the button
    centerX = (pt1.getX() + pt2.getX())/2.0 
    centerY = (pt1.getY() + pt2.getY())/2.0

    #use these coords for the position of the label
    btnLabel = Text(Point(centerX,centerY), label)
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

    #test if (x,y) fits within the rectangle area
    if ( pt1.getX() <= x <= pt2.getX() and pt1.getY() <= y <= pt2.getY()):
        return True
    else:
        return False


def drawquitButton(win, pt1, pt2, label):
    button = Rectangle(pt1, pt2)
    button.setFill("yellow")
    button.draw(win)

    #find the x and y coords of the middle of the button
    centerX = (pt1.getX() + pt2.getX())/2.0 
    centerY = (pt1.getY() + pt2.getY())/2.0

    #use these coords for the position of the label
    btnLabel = Text(Point(centerX,centerY), label)
    btnLabel.setFill("black")
    btnLabel.draw(win)

    return button

###isClicked() function we made in class 
def quitisClicked(button, point):

    #find x and y coordinate of the point
    x = point.getX()
    y = point.getY()

    #get two corner points of the rectangle object
    pt1 = button.getP1()
    pt2 = button.getP2()

    #test if (x,y) fits within the rectangle area
    if ( pt1.getX() <= x <= pt2.getX() and pt1.getY() <= y <= pt2.getY()):
        return True
    else:
        return False




def main():

    #create window with size of 600 x 600
    win = GraphWin("Interactive Drawing", 600, 600, autoflush=False)

    #a text object for onscreen instruction and message
    msgLabel = Text(Point(300, 35), 'Click mouse to add a point (5 points)')
    msgLabel.setSize(15)
    msgLabel.draw(win)

    btn = drawButton(win, Point(100,100), Point(200,200), "DRAW")

    btn2 = drawquitButton(win, Point(550,550), Point(590,590), "QUIT")

    userinput = Entry(Point(400,150), 6)

    userinput.draw(win)

    instruction = Text(Point(400,130), "Please enter three integers between 0 and 255 separated by commas")

    instruction.draw(win)

    win.getMouse()

##    rgb = userinput.getText()
##
##    rgb.split(",")
##
##    r = rgb.split(",")[0]
##
##    g = rgb.split(",")[1]
##
##    b = rgb.split(",")[2]
##
##    r = int(r)
##
##    g = int(g)
##
##    b = int(b)

    

        
    #point list to store mouse click points
    pointList = []

    # takes 5 mouse click and append it to pointList
    click = win.getMouse()
    
    while not isClicked(btn2,click):
        
        click = win.getMouse()
        if isClicked(btn,click) == True:
            #all 5 points are collected. let's draw a ploygon
            rgb = userinput.getText()

            rgb.split(",")

            r = rgb.split(",")[0]

            g = rgb.split(",")[1]

            b = rgb.split(",")[2]

            r = int(r)

            g = int(g)

            b = int(b)

            myPoly = Polygon(pointList)
            myPoly.draw(win)
            myPoly.setFill(color_rgb(r,g,b))
            pointList = []
            
        else:
            
            #target = win.getMouse()
            pointList.append(click)
            #for reference draw a point on window
            click.draw(win)

            #some message to a user
            #msgLabel.setText('Good job. Very interesting shapes. Click anywhere to close.')


    #wait for click to close window
    win.getMouse()
    
    # close window
    win.close()  

main()
