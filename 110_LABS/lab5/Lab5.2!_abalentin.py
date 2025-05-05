#Alexia Balentine
#COM 110 Fall 2020 - Lab 5
#October 2 2020
#This will draw a square point by point in purple

from graphics import *

def main():
    
    Lab5=GraphWin("Lab5", 600,600)
    for x in range(250, 351):
        for y in range(200, 301):
            pt = Point(x, y)
            pt.draw(Lab5).setFill(color_rgb(130, 0, 130))

main()
