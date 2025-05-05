# file: button.py (from class)

from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns true if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label, color):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill(color)
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.color = Text(center, color)
        self.deactivate()

    def clicked(self, p):
        """Returns true if button active and p is inside"""
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getLabel(self):
        """Returns the label string of this button."""
        return self.label.getText()

    def getColor(self):
        """Returns the color of this button."""
        return self.color.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('white')
        self.rect.setWidth(2)
        self.active = 1

    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('orange')
        self.rect.setWidth(1)
        self.active = 0

def main():
    
    # create the application window
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    ##testing Button constructor
    rollButton = Button(win, Point(5,4), 6, 1, "Roll Dice", "black")
    quitButton = Button(win, Point(5,1), 2, 1, "Quit", "red")

    ##testing activate method
    rollButton.activate()

    ##testing clicked() method
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        #when roll button is clicked
        if rollButton.clicked(pt):
            #activate the quit button
            quitButton.activate()
        pt = win.getMouse()
    
    #if quit button is clicked, then loop is broken
    #and we reach this line of code
    win.close()
    
if __name__ == "__main__":
    main()


