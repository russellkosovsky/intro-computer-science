#lab 5 sunset of over house animation
#house part is removed
from graphics import *
from time import *
from random import *
def main():

    window = GraphWin("Twinkling Stars", 600, 600)
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
        #start from the initial blue-ish (color_rgb(180, 180, 247)) color (set above)
        sky.setFill(color_rgb(180-5*i,180-5*i,245-7*i)) #and fade down to color_rgb(0,0,0)
        sleep(.1) #slow the animation down so it looks good
    
    #after sunset, create stars
    star = [] #start with an empty list of stars
    for i in range(100):
        #generate random x and y values for a Point object
        #and add it to the list of stars
        star.append(Point(randrange(0,600),randrange(0,300)))

    xValues = []
    yValues = []
    for point in star:
        x = point.getX()
        xValues.append(x)
        y = point.getY()
        yValues.append(y)

    xValues.sort()
    starsInOrder = []
    for i in range(100):
        newcords = Point(xValues[i],yValues[i])
        starsInOrder.append(newcords)
        starsInOrder[i].setFill('white')
        starsInOrder[i].draw(window)
        
    #make the stars "twinkle"
    for i in range(10):
        for j in range(100):
            star[j].undraw()
            sleep(.02)
            star[j].draw(window)
    #pause and wait for mouse click before closing window
    window.getMouse()
    window.close()
main()
