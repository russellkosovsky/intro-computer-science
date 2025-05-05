# button.py
from graphics import *
import time
import math

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns true if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        
        self.label.setSize(8) ##added this for check 5 to make the label fit
        
        self.active = True
        self.activate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        #print("clicked", p.getX(), p.getY(), self.xmin, self.xmax)
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

        
    ## check 7
    def setColor(self, color):
        self.rect.setFill(color)

        
  
class Grid:
    """A grid of squares/buttons"""

    
    ##check 4:      
    def __init__(self, win, startX, startY, numCols, numRows, squareWidth, squareHeight):
        """initializes a 2D list of blank button objects startX, startY are the coordinates
of the first button location squareWidth and squareHeight are the width and height of each button"""          
        self.buttonMatrix = []
        self.numCols = numCols
        self.numRows = numRows
        
        for y in range(startY,numRows):
            
            buttonList=[]
            for x in range(startX,numCols):

                
                label = str(x)+","+str(y) ##check 5 (before check 5, just set button labels to "")

                buttonList.append(Button(win,Point(x,y),squareWidth,squareHeight,label))

            self.buttonMatrix.append(buttonList)

            #time.sleep(.03) #if they want to slow down the button drawing to see it happen row by row

    ##check 6:
    def getClickPos(self, clickPt):
        """returns the column and row number of the button that was clicked
           assumes the point clickPt is in/on the grid"""
        #method 1
##        x = round(clickPt.getX())
##        y = round(clickPt.getY())
##        return x,y

        #method 2
        for y in range(self.numRows): #loop through each row
            for x in range(self.numCols): #loop through columns
                if self.buttonMatrix[y][x].clicked(clickPt):
                    return y, x


    ##check 7
    def setSquareColor(self, r, c, color):
        self.buttonMatrix[r][c].setColor(color)






    ##check 9
    def setRowColor(self,rowNum, color):  ##check 8
        for c in range(20):
            self.buttonMatrix[rowNum][c].setColor(color)

    \

    ##check 10
    def setColColor(self, colNum, color): ##check 9
        for r in range(20):
            self.buttonMatrix[r][colNum].setColor(color) 








    def setNeighbors(self, midX, midY, color):
        #method 1
##	for x in range(self.numCols):
##            for y in range(self.numRows):
##                if math.fabs(x-midX) <= 1 and math.fabs(y-midY) <= 1:
##                    self.buttonMatrix[x][y].setColor(color)
        #method 2
        for y in range(midY-1, midY+2):
            for x in range(midX-1,midX+2):
                    if 0 <= x < self.numCols and 0 <= y < self.numRows:
                        self.buttonMatrix[y][x].setColor(color)

        
def main():
    
    # create the application window
    win = GraphWin("Fun with 2D lists", 600, 600)
    
    SIZE = 20 #each dimension of the grid will be this many buttons
    
    win.setCoords(-3, -3, SIZE + 2, SIZE + 2)
    #win.setBackground("green2")

    ##check 3: add code that creates a quitButton
    quitButton = Button(win, Point(SIZE,SIZE+1),2,1,"quit")
  
    ##check 4: fill in the constructor for the Grid class and then use it to create a Grid object here
    grid = Grid(win,0,0,SIZE,SIZE,1,1)
 
    pt = win.getMouse()

    ##check 3: add a while loop that will keep taking mouse clicks until the quit button is clicked
    while not quitButton.clicked(pt):
        #optional if statement for check 6, but it's nice to make sure it's a click within the grid first
        #to prevent errors from stray clicks
        if -.5 <= pt.getX() <= SIZE-.5 and -.5 <= pt.getY() < SIZE-.5: 

            print(pt.getX(),pt.getY())          ##check 6
            row, col = grid.getClickPos(pt)         ##check 6 and 8
            print(row,col,"clicked")                ##check 6
            
            grid.setRowColor(row, "blue")           ##check 9
            grid.setColColor(col, "blue")           ##check 10
            #grid.setNeighbors(col, row, "red")      ##bonus
            grid.setSquareColor(row, col, "blue")   ##check 8
            
        
        pt=win.getMouse()  ##check 3
    
    win.close() ##check 3
    
if __name__ == "__main__":
    main()

