from graphics import *

def main():
    win = GraphWin("Fun!", 400, 400)
    pt1 = Point(50,80)
    pt1.setFill("magenta3")
    pt1.draw(win)    
    pt2= Point(60,80)
    pt2.setFill("green2")
    pt2.draw(win)    
    sendoff = Text(Point(200,200),"Click anywhere to close.")
    sendoff.draw(win)
    win.getMouse() #freezes the program and waits for mouse click
    win.close()  
main()
