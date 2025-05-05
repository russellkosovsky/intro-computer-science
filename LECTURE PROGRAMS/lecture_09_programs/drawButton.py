#COM110 graphics exercise: button
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
    #recall that point object has method getX() and getY()
    #and you can compute center point by averaging two Xs and two Ys
    #i.e. centerX = (pt1.getX() + pt2.getX()) / 2.0
    ### your code here
    centerX = (pt1.getX() + pt2.getX()) / 2.0
    centerY = (pt1.getY() + pt2.getY()) / 2.0
    center = Point(centerX,centerY)


    #create a button label (text object)
    #use centerX and centerY computed above for the position of the text
    ### your code here
    buttonlabel = Text(Point(centerX, centerY), label)
    buttonLabel.setFill("white")

    buttonlabel.draw(win)

    return button

#function that returns a value
#tests if the point is within the rectangle object or not
def isClicked(button, point):

    #we are going to implement this soon!
    x = point.getX()
    y = point.getY()
    pt1 = button.getP1()
    pt2 = button.getP2()

    if (pt1.getX() < x < pt2.getX() and pt1.getY() < y < pt2.getY()):
        return True



def main():

    #create a window
    myWin = GraphWin("loop test", 600, 600)

    #create exit button (call drawButton function)
    #use two point coordinate (250,450) and (350,500)
    #and text 'exit'
    ###your code here
    point1 = Point(250,450)
    point2 = Point(350,500)
    exitbtn = drawButton(myWin,point1,point2,"EXIT")

    
    #close the window only when user clicks the exit button
    #i.e., keep taking mouse clicks until exit button is clicked
    pt = myWin.getMouse()

    if isClicked(exitbtn,pt):
        print("Clicked")
    else:
        print("not clocked")
    
    #we are going to write while loop for above purpose later class

    pt = myWin.getMouse()
        
    #exit button has been clicked at this point
    myWin.close()
    

main()
