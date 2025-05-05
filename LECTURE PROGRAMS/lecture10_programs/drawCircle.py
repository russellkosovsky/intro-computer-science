#COM110 graphics exercise: drawCircle


from graphics import *


def drawColorCircle(win, point, color):
    #draw a circle with the given color
    #your code here
    circle = Circle(point, 50)
    circle.setFill(color)
    circle.draw(win)


def drawCircle(win, point):
    #draw a circle at the give position
    #your code here
    circle = Circle(point, 50)
    circle.draw(win)
    
def main():

    #create window
    win = GraphWin("Interactive Drawing", 600, 600, autoflush=False)

    #create text as a label for entry box
    colorLabel = Text(Point(100, 35), 'Color: ')
    colorLabel.setSize(20)
    colorLabel.draw(win)

    #color entry box
    colorEnt = Entry(Point(200, 35), 15)
    colorEnt.setText('yellow')
    colorEnt.draw(win)

    #draw five circles at the mouse click points
    for i in range(5):
        #get mouse click
        target = win.getMouse()

        #draw a circle
        #drawCircle(win, target)
        drawColorCircle(win, target, colorEnt.getText())

    #wait for one more mouse click before closing the window
    win.getMouse()
    
    # close window
    win.close()  

main()
