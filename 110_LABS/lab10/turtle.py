#Create recursive drawings

from graphics import *
from math import cos, sin, pi

class Turtle:
    '''This Turtle class is used for drawing in a Zelle graphical window'''
    def __init__(self, win, x = 0,y = 0,direction = 0):
        '''Constructor for turtle puts position at x,y and direction 0 radians'''
        self.win = win
        self.pt = Point(x,y)
        self.direction = 0.0  #0.0 points toward the positive direction of the x-axis

    def draw(self, length):
        '''Uses current direction and position and draws line of given length'''
        newPt = Point(self.pt.getX() + length * cos(self.direction), self.pt.getY() + length * sin(self.direction))
        line = Line(self.pt, newPt)
        line.draw(self.win)
        self.moveTo(newPt)

    def turn(self, rad):
        '''Turn the turtle by rad radians.
            Recall that radians are given in terms of pi = 180 degrees
            If rad is positive, turtle turns counterclockwise,
            If rad is negative, turtle turns clockwise.'''
        self.direction = self.direction+rad
        
    def moveTo(self, newPt):
        '''Set the turtle position to newPt, where newPt is a Point object'''
        self.pt = newPt


###################################################################################################


class Drawing:
    '''A class that has a graphical window with a quit button and a
        method to test if the quit button is clicked.'''
    def __init__(self, xcoord = 100, ycoord = 100):
        '''Constructor for Drawing class: creates a graphical window,
            set up coordinate range based on xcoord and ycoord params,
            and sets up a quit button'''
        self.win = GraphWin('Recursive Drawings', 500, 500)
        self.win.setBackground("white")
        #sets up coords so that (0,0) is toward bottom left of win
        self.win.setCoords(-xcoord/10.0, -ycoord/10.0, xcoord, ycoord)
        x = xcoord/10.0
        y = ycoord/10.0
        self.quitButton = Rectangle(Point(xcoord-x,-y), Point(xcoord,-y/2.0))
        self.quitButton.setFill("lightblue")
        self.quitButton.draw(self.win)
        Text(self.quitButton.getCenter(),"Quit").draw(self.win)

    def quit(self, pt):
        '''Assumes pt is the point where the user last clicked.
            Returns true if the pt is in the quit button.'''
        p1 = self.quitButton.getP1()
        p2 = self.quitButton.getP2()
        #if quit button was clicked
        if pt.getX() >= p1.getX() and pt.getX() <= p2.getX() and pt.getY() >= p1.getY() and pt.getY() <= p2.getY():
            return True
        else:
            return False


###################################################################################################


###complete this for checkpoint 2
def spiral(turtle, length, level):
    
    '''Create a square spiral with given recursion level'''
    
    if level == 0: #base case, no recursion in this case
        turtle.draw(length)  # just draws a line of length "length"
                             # from current turtle position with current
                             # turtle direction
    
    else: #recursive case, to be completed for checkpoint 2
        turtle.draw(length)
        turtle.turn(pi/2)
        return(spiral(turtle, length/2, level-1))


###complete this for checkpoint 4
def kcurve(turtle, length, level):
    
    '''Draws a Koch curve of given recursion level'''
    
    if level == 0: #base case
        # draws a line in the current direction "length" long 
        turtle.draw(length)
    
    else: # recursive case that you must complete
        kcurve(turtle, length/3, level-1)
        turtle.turn(-pi/3)
        kcurve(turtle, length/3, level-1)
        turtle.turn(2 * pi/3)
        kcurve(turtle, length/3, level-1)
        turtle.turn(-pi/3)
        kcurve(turtle, length/3, level-1)


###################################################################################################


def main():
    # creates a graphical window with quit button
    picture = Drawing(300, 300)
    
    # Note: the coordinates are set so that
    # (0,0) is somewhat close to the bottom left corner of the window,
    # (300,300) is in the upper right corner of the window,
    # the x-axis is increasing toward the right, and
    # the y-axis is increasing upward.

    # creates a turtle object in the graphical window
    turtle = Turtle(picture.win) 
    # moves the turtle to a position toward the left and halfway up 
    turtle.moveTo(Point(0, 150))

    pt = picture.win.getMouse()


    ''' your code for checkpoint 1 goes here '''
    turtle.draw(50)
    turtle.turn(pi/2)
    turtle.draw(50)
    turtle.turn(pi/2)
    turtle.draw(50)
    turtle.turn(pi/2)
    turtle.draw(100)
    turtle.moveTo(Point(0,150))
    turtle.turn(pi/4)
    turtle.draw(70)
    turtle.moveTo(Point(75,150))
    turtle.turn(7*pi/4)
    turtle.draw(50)
    turtle.moveTo(Point(75,150))
    turtle.turn(pi)
    turtle.draw(50)
    turtle.moveTo(Point(75,150))
    turtle.turn(7*pi/4)
    turtle.draw(60)
    turtle.moveTo(Point(75,150))
    turtle.turn(7*pi/4)
    turtle.turn(7*pi/4)
    turtle.draw(60)


###################################################################################################

    ''' your code for checkpoint 2 goes here '''
    ### also need to complete recursive case for spiral() too (see above) ###
    
    pt = picture.win.getMouse()
    spiral(turtle, 75, 75)


    '''your code for checkpoint 3 & 4 goes here'''
    ### also need to complete recursive case for kcurve() too (see above) ###

    kcurve(turtle, 50, 2)
    turtle.turn(2 * pi/3)

    kcurve(turtle, 50, 2)
    turtle.turn(2 * pi/3)

    kcurve(turtle, 50, 2)
    turtle.turn(2 * pi/3)


    # waits for any mouse click
    pt = picture.win.getMouse()
    # keeps waiting for new mouse clicks until quit is clicked
    while not picture.quit(pt):  
        pt = picture.win.getMouse()
    # closes window after loop breaks
    picture.win.close()


if __name__ == "__main__":
    main()
