# C13ex09.py
#Turtle and C curve

from graphics import *
from math import cos,sin,sqrt,pi

class Turtle:
    def __init__(self,window,location = Point(0,0),heading = 0.0):
    # default position is (0,0) and direction is 0.0 (east)
        self.position = location
        self.direction = heading
        self.win = window
        
    def turnRight(self,angle):
        self.direction = self.direction - angle

    def turnLeft(self,angle):
        self.direction = self.direction + angle

    def forward(self, n):
        # Draw a segment n units long, in current direction
        # and move to the new end
        deltaX = n*cos(self.direction)
        deltaY = n*sin(self.direction)
        oldPosition = self.position
        self.position = self.position.clone()
        self.position.move(deltaX,deltaY)
        Line(oldPosition,self.position).draw(self.win)
        

def C_Curve(turtle,length,degree):
    # from the text, chapter 13
    if degree <= 0:
        turtle.forward(length)
    else:
        fourtyfive = 45.0*pi/180.0
        length1 = length/sqrt(2.0)
        degree1 = degree-1
        turtle.turnLeft(fourtyfive)
        C_Curve(turtle,length1,degree1)
        turtle.turnRight(2*fourtyfive)
        C_Curve(turtle,length1,degree1)
        turtle.turnLeft(fourtyfive)
                

def main():    
    print()
    print("Let's draw a C-curve")
    print()

    degree = int(input("What degree C-curve do you want? "))

    
    win = GraphWin("C-curve",500,500)
    win.setCoords(0,0,500,500)
    win.setBackground("green")

    myTurtle = Turtle(win,Point(350,125),pi/2.0)
    
    C_Curve(myTurtle,250,degree)
        

    Text(Point(350,250),"Click in window to close").draw(win)
    win.getMouse()
    win.close()

main()
    
        
             
