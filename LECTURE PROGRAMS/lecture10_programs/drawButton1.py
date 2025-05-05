#illustration of looping mouse clicks until an "exit" button is clicked

from graphics import *

#in the GraphWin object gwin, this function draws
#a blue rectangular button with corners at Point objects pt1 and pt2
#then labels the button with the string variable words
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

    #or, this is anohter implementation
    #btnLabel = Text(button.getCenter(), label)
    #btnLabel.setFill("white")
    #btnLabel.draw(win)

    return button

#function that returns a value
#tests if the point is within the rectangle object or not
def isClicked(button, point):

    #we are going to implement this
    #your code here

    return True


def main():
    
    #create a window
    myWin = GraphWin("loop test", 600, 600)

    #create exit button (call drawButton function)
    #use two point coordinate (250,450) and (350,500)
    #and text 'exit'
    ###your code here
    exitBtn = drawButton(myWin, Point(250,450), Point(350,500), "Exit")

    colorEntry = Entry(Point(100,100), 5)
    colorEntry.setText('red')
    colorEntry.draw(myWin)
    
    #close the window only when user clicks the exit button
    #i.e., keep taking mouse clicks until exit button is clicked
    pt = myWin.getMouse()


    #we are going to write while loop for above purpose in Wed class
    #while not ( 250 <= pt.getX() <= 350 and 450 <= pt.getY() <= 500):
    #    pt = myWin.getMouse()
    while isClicked(exitBtn, pt) == False:
        #get new mouse click
        pt = myWin.getMouse()
        
       
    #exit button has been clicked at this point
    myWin.close()
    

main()
