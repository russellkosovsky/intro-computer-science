#COM110: movingSquare.py
#This program shows how to animation a square

from graphics import *
	
def main():
    #create window
    win = GraphWin('Moving Square',400,600)

    #create a rectangle and draw it
    square = Rectangle(Point(100,100), Point(300,300))
    square.draw(win)

    #wait for mouse click
    win.getMouse()

    #loop to move the square
    for i in range(100):
        square.move(1,0)
        #sleep(0.02)     #for PC, slow down speed

    #create/draw message
    sendoff = Text(Point(200, 400), 'Click anywhere to close window.')
    sendoff.draw(win)

    #wait for mouse click to close window
    win.getMouse()
    win.close()
    
main()
