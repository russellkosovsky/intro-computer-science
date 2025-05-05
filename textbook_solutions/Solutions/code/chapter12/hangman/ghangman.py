# file: ghangman.py
# Graphical version of hangman
# by: Cassie Frush


from graphics import *
from button import Button
from hangman import HangmanApp
from hangman import TextInterface
from hangman import HangmanWord
from random import randrange

class GHInterface:

    def __init__(self):
        
        #Create the window for the hangman game.
        self.win = GraphWin('Hangman', 500,500)
        self.win.setCoords(0,0, 40,25)
        self.win.setBackground('red3')
        self.buttonhelper()
        
        #Ready to blend deadguy in
        self.background = "red3"
        self.gallows()

        #dead guy
        head = Circle(Point(13,19),2)
        head.setWidth("4")
        body = Line(Point(13,17),Point(13,12))
        body.setWidth("4")
        Rarm = Line(Point(13,15),Point(16,17))
        Rarm.setWidth("4")
        Larm = Line(Point(13,15),Point(10,17))
        Larm.setWidth("4")
        Rleg = Line(Point(13,12),Point(15,10))
        Rleg.setWidth("4")
        Lleg = Line(Point(13,12),Point(11,10))
        Lleg.setWidth("4")

        self.deadguy = [head, body, Rarm, Larm, Rleg, Lleg]

        for limb in self.deadguy:
            limb.setOutline(self.background)
            limb.draw(self.win)

        #Create wordBox
        self.wordBox = Text(Point(20,4),"text here")
        self.wordBox.setFace("courier")
        self.wordBox.setStyle("bold")
        self.wordBox.draw(self.win)

        #Miss Box
        self.miss = Text(Point(10,3), "")
        self.miss.draw(self.win)
        self.miss1=Text(Point(10,2), "")
        self.miss1.draw(self.win)

        #Prompt Box
        self.text1 = Text(Point(10,5),"The secret word is:")
        self.text1.draw(self.win)

        
        #Create 26 buttons that represent the letters of the alphabet
        #bspecs gives the center coordinate and the label
    def buttonhelper(self):
        self.bspecs = [(25,23,'A'),(28,23,'B'),(31,23,'C'),(34,23,'D'),
            (37,23,'E'),(25,20,'F'),(28,20,'G'),
            (31,20,'H'),(34,20,'I'),(37,20,'J'),(25,17,'K'),
            (28,17,'L'),(31,17,'M'),(34,17,'N'),(37,17,'O'),
            (25,14,'P'),(28,14,'Q'),(31,14,'R'),(34,14,'S'),
            (37,14,'T'),(25,11,'U'),(28,11,'V'),(31,11,'W'),
            (34,11,'X'),(37,11,'Y'),(31,8,'Z')]
        self.buttons = []
        for cx,cy,label in self.bspecs:
            self.buttons.append(Button(self.win,Point(cx,cy),2,2,label))
            for b in self.buttons:
                b.activate()
                
    def gallows(self):
        bottom = Line(Point(1,7), Point(15,7))
        bottom.setWidth('2')
        bottom.draw(self.win)
        line_up = Line(Point(3,7), Point(3,24))
        line_up.setWidth('2')
        line_up.draw(self.win)
        top = Line(Point(3,24), Point(13,24))
        top.setWidth('2')
        top.draw(self.win)
        line_dn = Line(Point(13,24), Point(13,21))
        line_dn.setWidth('2')
        line_dn.draw(self.win)

    def askPlayAgain(self):
        self.playagainwin = GraphWin("Play Again", 300, 300)
        playagaintxt = Text(Point(150,250),"Do you want play again?").draw(self.playagainwin)
        Button1 = Button(self.playagainwin, Point(75, 150), 100,30,"Sure")
        Button1.activate()
        Button2 = Button(self.playagainwin, Point(225, 150), 100,30,"Too Scared")
        Button2.activate()
        self.happyface()
        self.sadface()
        while 1:
            q=self.playagainwin.getMouse()
            if Button1.clicked(q):
                self.playagainwin.close()
                return 1
            elif Button2.clicked(q):
                self.playagainwin.close()
                return 0

    def happyface(self):
        happyhead = Circle(Point(75,75),30)
        happyhead.setFill("yellow")
        happyhead.draw(self.playagainwin)
        happylefteye = Circle(Point(65,60),5)
        happyrighteye = Circle(Point(85,60),5)
        smile = Polygon(Point(57,80),Point(67,90),Point(82,90),Point(92,80)).draw(self.playagainwin)
        happylefteye.setFill("black")
        happylefteye.draw(self.playagainwin)
        happyrighteye.setFill("black")
        happyrighteye.draw(self.playagainwin)

    def sadface(self):
        sadhead = Circle(Point(225,75),30)
        sadhead.setFill("yellow")
        sadhead.draw(self.playagainwin)
        sadlefteye = Circle(Point(215,60),5)
        sadrighteye = Circle(Point(235,60),5)
        frown = Polygon(Point(208,90),Point(218,80),Point(233,80),Point(243,90)).draw(self.playagainwin)
        sadlefteye.setFill("black")
        sadlefteye.draw(self.playagainwin)
        sadrighteye.setFill("black")
        sadrighteye.draw(self.playagainwin)
        
    def reset(self):
        for limb in self.deadguy:
            limb.setOutline(self.background)
        for b in self.buttons:
            b.activate()
        self.miss.setText("")
        self.miss1.setText("")
    
    def showWord(self, word):
        display = ''
        for ch in word:
            display = display + ch +' '
            self.wordBox.setText(display)

    def getGuess(self):
        while 1:
            pt = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(pt):
                    b.deactivate()
                    return b.getLabel() #exit method
        
    def showMiss(self, num):
        nums = str(7-num)
        self.miss.setText(("You have ") + (nums))
        self.miss1.setText("chances left.")
        if num == 1:
            self.deadguy[0].setOutline("green3")
        elif num == 2:
            self.deadguy[1].setOutline("green3")
        elif num == 3:
            self.deadguy[2].setOutline("green3")
        elif num == 4:
            self.deadguy[3].setOutline("green3")
        elif num == 5:
            self.deadguy[4].setOutline("green3")
        elif num == 6:
            self.deadguy[5].setOutline("green3")
        else:
            for limb in self.deadguy:
                limb.setOutline("red3")
        

    def showWin(self):
        self.miss.setText("")
        self.miss1.setText("Yeah, You Win!")
        
    def showLoss(self, word):
        self.miss.setText("")
        self.miss1.setText("Bummer, You Lost!")
        for ch in word:
            self.wordBox.setText(word)

    def outOfWords(self):
        outwin = GraphWin("Out of Words", 300, 300)
        outtext = Text(Point(150, 100), "There are no new words for you.").draw(outwin)
        outtext2 = Text(Point(150, 150), "Click the window to close.").draw(outwin)
        outtext3 = Text(Point(150, 200), "Thank you.").draw(outwin)
        outwin.getMouse()
        outwin.close()

    def closing(self):
        self.wordBox.setText("Thank for playing our game.")
        self.text1.setText("")
        self.win.close()

def main():
    interface = GHInterface()
    HangmanApp(interface).run()

if __name__ == '__main__':
    main()

