# cbutton.py
#    A circular Button widget.

from graphics import *

class CButton:

    """A button is a labeled circle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, radius, label):
        """ Creates a circular button, eg:
        qb = Button(myWin, Point(30,25), 20, 'Quit') """ 

        
        self.cx = center.getX()
        self.cy = center.getY()
        self.rsquare = radius * radius
        self.circle = Circle(center, radius)
        self.circle.setFill('lightgray')
        self.circle.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "RETURNS true if button active and p is inside"
        dx = p.getX() - self.cx
        dy = p.getY() - self.cy
        return self.active and dx*dx + dy*dy <= self.rsquare

    def getLabel(self):
        "RETURNS the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.circle.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.circle.setWidth(1)
        self.active = False


# Roller Code
from random import randrange
from graphics import GraphWin, Point

from dieview import DieView 

def main():

    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    # Draw the interface widgets
    die1 = DieView(win, Point(3,7), 2)
    die2 = DieView(win, Point(7,7), 2)
    rollButton = CButton(win, Point(5,4.5), 1, "Roll")
    rollButton.activate()
    quitButton = CButton(win, Point(5,1), 1, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1,7)
            die1.setValue(value1)
            value2 = randrange(1,7)
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse()

    # close up shop
    win.close()

main()




