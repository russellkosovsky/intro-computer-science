
from graphics import *

def drawCircle(center, radius, color, win):
    circ = Circle(center,radius)
    circ.setFill(color)
    circ.draw(win)

def drawSquare(pt1, pt2, color, win):
    square = Rectangle(pt1, pt2)
    square.setFill(color)
    square.draw(win)

def drawButton(pt1, pt2, color, label, win):
    # the rectangle outline
    button = Rectangle(pt1,pt2)
    button.setFill(color)
    button.draw(win)

    # the label text
    centerX, centerY = (pt1.getX()+pt2.getX())/2, (pt1.getY()+pt2.getY())/2
    button_label = Text(Point(centerX, centerY), label)
    button_label.setFill("white")
    button_label.draw(win)

    return button

def getDistance(pt1, pt2):
    #Calculates and returns the distance between points pt1 and pt2
    a = (pt2.getX() - pt1.getX())**2
    b = (pt2.getY() - pt1.getY())**2
    distance = sqrt(a + b)
    return round(distance,2)

def main():
    
    win=GraphWin("Button GUI", 800,800)

    win.setCoords(0,0, 100,100)

    #drawButton(Point(5,96), Point(15,90),"red","QUIT",win)
    ##Now, create "button" 25 ticks over and 90 ticks up
    #drawButton(Point(25,96), Point(35,90),"blue3","Circle",win)

    btn = drawButton(Point(5,96), Point(15,90),"red","Lower Case!",win)

    # Here you will add code to see which button is clicked,
    # and perform the appropriate action. Similar to warm-up 7

    userinput = Entry(Point(50,80), 50)

    userinput.draw(win)

    click = win.getMouse()
    x = click.getX()
    y = click.getY()


    #test if (x,y) fits within the rectangle area
    if (btn.getP1().getX() <= x <= btn.getP2().getX() and btn.getP1().getY() <= y <= btn.getP2().getY()):
        text = userinput.getText()

        out = Text(Point(50,90), text)

        out.draw(win)
        
        
    #else:
         

    

    closeMessage = Text(Point(50,5), "Click anywhere to end program.")
    closeMessage.draw(win)

    #Get a mouse click and then check if it is in a button 
    win.getMouse()
    
    win.close()


main()

