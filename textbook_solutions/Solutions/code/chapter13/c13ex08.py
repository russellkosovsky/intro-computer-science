# c13ex08.py
#Turtle and Koch snowflake
from graphics import *
from math import cos,sin,pi

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
        # draw a segment n units long in the current 
        # direction and move to the new end
        deltaX = n*cos(self.direction)
        deltaY = n*sin(self.direction)
        oldPosition = self.position
        self.position = self.position.clone()
        self.position.move(deltaX,deltaY)
        Line(oldPosition,self.position).draw(self.win)

def Koch(turtle,length,degree):
    #from the text, chapter 13
    if degree <= 0:
        turtle.forward(length)
    else:
        sixty = 60.0*pi/180.0
        length1 = length/3.0
        degree1 = degree-1
        Koch(turtle,length1,degree1)
        turtle.turnLeft(sixty)
        Koch(turtle,length1,degree1)
        turtle.turnRight(2*sixty)
        Koch(turtle,length1,degree1)
        turtle.turnLeft(sixty)
        Koch(turtle,length1,degree1)

def main():
    
    print()
    print("Let's draw a Koch snowflake")
    print()

    degree = int(input("What degree of Koch flake do you want? "))

    
    win = GraphWin("Koch",500,500)
    win.setCoords(0,0,500,500)
    win.setBackground("green")
    win.flush()

    sixty = 60.0*pi/180.0
    myTurtle = Turtle(win,Point(100,150),sixty)

    # The Koch snowflake is based on applying the Koch
    # algorithm to each side of an equilateral triangle
    for i in range(3):
        Koch(myTurtle,300,degree)
        myTurtle.turnRight(sixty*2)

    Text(Point(250,250),"Click in window to close").draw(win)
    win.getMouse()
    win.close()

main()
    
        
             
