
# lab06.py
# 03/01/2018
# This program creates and draws a Rectangle object,
# takes a mouse click, and then closes the window.



from graphics import *

def main():
    
    win = GraphWin("Fun #5", 600, 600)

    square = Rectangle(Point(200,200),Point(400,400))
    square.draw(win)
    
    win.getMouse()
    win.close()

main()
