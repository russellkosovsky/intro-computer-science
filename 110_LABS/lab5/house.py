
from graphics import *

myWin = GraphWin('House', 600,600)

def drawcoral(win, point):
    coral = Polygon(Point(500,500),Point(490,450),Point(505,475),Point(520,430),Point(530,485),Point(560,450),Point(540,500))
    xval = point.getX() - 500
    yval = point.getY() - 500
    coral.move(xval,yval)
    coral.draw(win)
    coral.setFill("purple")

def main():

    myWin.setBackground("deep sky blue")

    moon = Circle(Point(100,400), 50)
    moon.setFill("white")
    moon.draw(myWin)


    roof = Polygon(Point(290,200), Point(310,200), Point(360,100), Point(320,125), Point(300,60), Point(280,125), Point(240,100))
    roof.draw(myWin)
    roof.setFill("forest green")


    houseBase = Oval(Point(225,150), Point(375,400))
    houseBase.draw(myWin)
    houseBase.setFill("gold")


    door = Oval(Point(275,300), Point(325,400))
    door.draw(myWin)
    door.setFill("sienna")


    sun = Circle(Point(500,100), 60)
    sun.draw(myWin)
    sun.setFill("yellow")


    grass = Rectangle(Point(0,350), Point(600,600))
    grass.draw(myWin)
    grass.setFill("green")


    path = Polygon(Point(275,350),Point(325,350),Point(430,600),Point(150,600))
    path.setFill("light grey")
    path.draw(myWin)


    window1 = Circle(Point(275,230), 15)
    window1.draw(myWin)
    window1.setFill("dodger blue")
    windowpart = Circle(Point(275,230), 10)
    windowpart.draw(myWin)
    windowpart.setFill("sky blue")


    window2 = Circle(Point(340, 280), 12)
    window2.draw(myWin)
    window2.setFill("dodger blue")
    windowpart2 = Circle(Point(340, 280), 8)
    windowpart2.draw(myWin)
    windowpart2.setFill("sky blue")


    # Animation 1
    text = Text(Point(100,60), "Click anywhere to start animation")
    text.draw(myWin)
    myWin.getMouse()
    text.undraw()
    for i in range(150):
        sun.move(1,2)
        moon.move(0,-2)
        #time.sleep(.12)
    myWin.setBackground("midnight blue")


    # Animation 2
    grasstext = Text(Point(100,20), "Click on yard to plant grass")
    grasstext.setTextColor("white")
    grasstext.draw(myWin)
    myWin.getMouse()
    grasstext.undraw()
    for i in range(10):
        target = myWin.getMouse()
        drawcoral(myWin,target)

    # Close Program
    myWin.getMouse()
    myWin.close()
main()












