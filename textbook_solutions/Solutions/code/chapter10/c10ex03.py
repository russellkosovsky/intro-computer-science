# c10ex03.py
#     Three Button Monte

from random import randrange
from graphics import *
from button import Button

def main():
    
    win = GraphWin("Three Button Monte", 350, 100)
    win.setCoords(.5,0, 3.5, 3)
    b1 = Button(win, Point(1,2), .75, 1, "Door 1")
    b1.activate()
    b2 = Button(win, Point(2,2), .75, 1, "Door 2")
    b2.activate()
    b3 = Button(win, Point(3,2), .75, 1, "Door 3")
    b3.activate()
    mess = Text(Point(2,.75), "Guess a door.")
    mess.setStyle("bold")
    mess.draw(win)

    secret = randrange(1,4)

    choice = None
    while choice == None:
        pt = win.getMouse()
        for button in [b1, b2, b3]:
            if button.clicked(pt):
                choice = button

    choiceNum = int(choice.getLabel()[-1])
    if choiceNum == secret:
        mess.setText("You win!")
    else:
        mess.setText("You lose. The answer was door {0}.".format(secret))

    win.getMouse()
    win.close()    

if __name__ == '__main__':
    main()

    
