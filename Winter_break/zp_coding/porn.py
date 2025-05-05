# this is a program that will br porn.
# shoutout to phil who commishioned this piece of art. this one goes out to you
# enjoy

from graphics import *

def drawStickFigures():

    win = GraphWin("Stick figure", 400,400)

    # head
    Circle(Point(100, 50), 20).draw(win)

    # body
    Line(Point(100, 70), Point(100, 130)).draw(win)

    # arms with options
    arm1 = Line(Point(100, 90), Point(140, 90))
    arm1.draw(win)
    arm2 = Line(Point(100, 90), Point(130, 110))
    arm2.draw(win)
    
    # 2 legs
    Line(Point(100,130), Point(80,160)).draw(win)
    Line(Point(100,130), Point(120,160)).draw(win)

    # balls
    ball1 = Circle(Point(104, 138), 4)
    ball1.setFill('brown')
    ball1.draw(win)

    ball2 = Circle(Point(96, 136), 4)
    ball2.setFill('brown')
    ball2.draw(win)

    # cock
    #cock = Polygon(Point(100, 135), Point(100, 137), Point(120, 122))
    cock = Oval(Point(100, 135), Point(140, 130))
    cock.setFill('brown')
    cock.draw(win)

    # head
    Circle(Point(205, 70), 20).draw(win)

    # body
    Line(Point(200, 90), Point(150, 130)).draw(win)

    # arms with options
    arm1 = Line(Point(187, 100), Point(215, 120))
    arm1.draw(win)
    arm2 = Line(Point(175, 110), Point(200, 130))
    arm2.draw(win)
    
    # 2 legs
    Line(Point(150,130), Point(140,160)).draw(win)
    Line(Point(150,130), Point(170,160)).draw(win)


    # pause for click in window
    win.getMouse()
    


drawStickFigures()

