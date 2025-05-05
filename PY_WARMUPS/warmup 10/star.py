#lab 5 sunset of over house animation

from graphics import *
from time import *
from random import *

def main():

    window = GraphWin("Stars", 600, 600)
    #green lawn
    lawn = Rectangle(Point(0,620),Point(620,300))
    lawn.setFill("green4")
    lawn.draw(window)
    #blue-ish sky
    sky = Rectangle(Point(620,300),Point(0,0))
    sky.setFill(color_rgb(180,180,245))
    sky.draw(window)
    #yellow sun
    sun = Circle(Point(500,100),60)
    sun.setFill("yellow")
    sun.draw(window)
    window.getMouse()
    
    #animate sunset
    for i in range(35):
        sun.move(5,5) #move 5 pixels down and 5 pixels over at at ime
        #start from blue (color_rgb(180, 180, 247)) and fade down to color_rgb(0,0,0)
        sky.setFill(color_rgb(180-5*i,180-5*i,245-7*i))
        sleep(.1) #slow the animation down so it looks good
        
    #after sunset, create stars [this was a lab 4 bonus check]
    for i in range(100): #do the following 100 times (for 100 stars)
        #generate random x and y values for a Point object
        star = Point(randrange(0,600),randrange(0,300))
        star.setFill("white")
        star.draw(window)

    #pause and wait for mouse click before closing window
    window.getMouse()
    window.close()

main()
