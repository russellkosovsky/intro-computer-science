# bjgui.pyw
#    Blackjack with a graphical interface.

import time

from graphics import *
from button import Button
from blackjack import BlackjackApp

class HandView:

    "Widget for displaying a hand of cards"

    def __init__(self, win, anchor, xinc):
        # win is a GraphWin
        # anchor is center point for first card
        # xinc x distance between successive cards 
        self.win = win
        self.anchor = anchor
        self.xinc = xinc
        self.current = anchor.clone()
        self.images = []

    def addCard(self, c):
        imageFile = "cardset/%02d%s.gif" %(c.getRank(),c.getSuit())
        img = Image(self.current, imageFile)
        img.draw(self.win)
        self.images.append(img)
        self.current.move(self.xinc,0)

    def clear(self):
        self.current = self.anchor.clone()
        for img in self.images:
            img.undraw()
        self.images = []
        

class guiInter:

    "graphical interface implementing methods required of a BJApp interface"

    def __init__(self):
        win=self.win = GraphWin("Python Blackjack!", 700,500)
        self.win.setCoords(0, 0, 70, 50)
        self.win.setBackground("green3")
        text = Text(Point(5,22),"Player")
        text.setSize(18)
        text.draw(win)
        text = Text(Point(5,40),"Dealer")
        text.setSize(18)
        text.draw(win)
        self.player = HandView(self.win, Point(15,20), 8)
        self.dealer = HandView(self.win, Point(15,40), 8)
        self.buttons = [Button(win,Point(15,7),8,4,"Hit"),
                        Button(win,Point(30,7), 8,4,"Stay"),
                        Button(win,Point(45,7), 8,4,"Deal"),
                        Button(win,Point(60,7),8,4,"Quit")]
        self.msgBox = Text(Point(35,30), "Welcome to Blackjack!")
        self.msgBox.setSize(20)
        self.msgBox.setFace('arial')
        self.msgBox.setStyle('bold')
        self.msgBox.draw(self.win)
        self.moneyBox = Text(Point(5,18),"$100")
        self.moneyBox.setSize(20)
        self.moneyBox.draw(win)

    def playerCard(self,c):
        self.player.addCard(c)

    def dealerCard(self, c):
        self.dealer.addCard(c)

    def setMoney(self, amt):
        self.moneyBox.setText("$%d" % amt)

    def pause(self):
        self.win.getMouse()

    def clear(self):
        self.player.clear()
        self.dealer.clear()
        self.msgBox.setText("")

    def close(self):
        for b in self.buttons:
            b.deactivate()
        self.msgBox.setText("Thanks for Playing!")
        time.sleep(3)
        self.win.close()

    def message(self, txt):
        self.msgBox.setText(txt)

    def _choose(self, choices):
        for b in self.buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()
        while True:
            c = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(c):
                    return b.getLabel()

    def wantToPlay(self):
        return (self._choose(["Deal","Quit"]) == "Deal")

    def wantCard(self):
        return (self._choose(["Hit", "Stay"]) == "Hit")
    
if __name__ == '__main__':
    inter = guiInter()
    app = BlackjackApp(inter)
    app.play()
