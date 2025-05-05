
from turtle import *
from graphics import *


# check 2
def spiral(turtle, length, level):
    '''Create a square spiral with given recursion level'''
    if level==0:
        turtle.draw(length)
    else:
        turtle.draw(length)
        turtle.turn(pi / 2)
        spiral(turtle, 14 * length / 15, level - 1)


# check 4
def kcurve(turtle, length, level):
    '''Draws a Koch curve of given recursion level'''
    if level==0:
        turtle.draw(length)
    else:
        kcurve(turtle,length/3,level-1)
        turtle.turn(pi/3)
        kcurve(turtle, length/3, level-1)
        turtle.turn(-2*pi/3)
        kcurve(turtle,length/3,level-1)
        turtle.turn(pi/3)
        kcurve(turtle,length/3,level-1)

def main():
    #creates a graphical window with quit button
    picture = Drawing(300,300)
    #Note: the coordinates are set so that
    # (0,0) is somewhat close to the bottom left corner of the window,
    # (300,300) is in the upper right corner of the window,
    # the x-axis is increasing toward the right, and
    # the y-axis is increasing upward.

    #creates a turtle object in the graphical window
    turtle = Turtle(picture.win)


    turtle.moveTo(Point(200,250))
    turtle.draw(200)
    turtle.turn(-2*pi/3)
    turtle.draw(200)
    turtle.turn(-2*pi/3)
    turtle.draw(200)


    turtle.moveTo(Point(200,250))
    kcurve(turtle,200,0)
    turtle.turn(-2*pi/3)
    kcurve(turtle, 200, 0)
    turtle.turn(-2*pi/3)
    kcurve(turtle, 200, 0)
main()












