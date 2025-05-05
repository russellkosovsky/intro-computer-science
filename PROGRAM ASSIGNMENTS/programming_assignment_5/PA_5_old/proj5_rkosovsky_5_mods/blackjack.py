# blackjack.py
# The model portion of a Blackjack playing program
# An application object that plays Blackjack

from Deck import *
from button import *

class BJHand:

    def __init__(self):
        # Initilizes variables for total(score) and whether or not an ace is present
        self.total = 0
        self.hasAce = False

    def addCard(self, c):
        # gets rank of the card
        rank = c.getRank()
        # adds the value of the card to the total (score)
        self.total = self.total + c.BJValue()
        if rank == 1:
            self.hasAce = True

    def score(self):
        if self.hasAce and self.total <=11:
            return self.total + 10
        else:
            return self.total


class BlackjackApp:

    def __init__(self, interface):
        # interface is an object for user interaction
        # Initializes the instance variables
        # user starts with $100
        self.money = 100
        # start with a shuffled deck
        self.deck = Deck()
        self.deck.shuffle()
        # player hand (initially None)
        self.player = None
        # Dealer hand (initially None
        self.dealer = None
        # for user interaction
        self.interface = interface 

    def play(self):
        # runs the Blackjack program when there is enough money and sloses otherwise
        while self.money >= 5 and self.interface.userDeal():
            win = self.playRound()
        self.interface.close()

    def playRound(self):
        # plays a single round of Blackjack
        # reference **def initDeal(self):**
        self.initialDeal()
        # reference def dealPlayer(self):
        self.playerDeal()
        # as lomng as you dont go over 21, run dealDealer
        if self.player.score() <= 21:
            self.dealerDeal()
        # check if won lost busted or tied
        winnings = self.checkResults()
        # new deck and shuffle when there are less than 26 left
        if self.deck.cardsLeft() < 26:
            self.deck = Deck()
            self.deck.shuffle()
            self.interface.userDeal()
            self.interface.message("Shuffling a new deck")

    def initialDeal(self):
        # clearCards the interface and hands use existing deck
        # .clearCards for removing all items in list
        self.interface.clearCards()
        deck = self.deck
        self.player = BJHand()
        self.dealer = BJHand()

        # deal two cards for the player
        for i in range(2):
            card = deck.dealCard()
            self.interface.playerCard(card)
            self.player.addCard(card)

        # deal one card for the dealer
        card = deck.dealCard()
        self.interface.dealerCard(card)
        self.dealer.addCard(card)

    def playerDeal(self):
        while self.player.score() <= 21 and self.interface.userHit():
            card = self.deck.dealCard()
            self.interface.playerCard(card)
            self.player.getCard(card)

    def dealerDeal(self):
        while self.dealer.score() < 17:
            card = self.deck.dealCard()
            self.interface.dealerCard(card)
            self.dealer.getCard(card)

    def checkResults(self):
        pScore = self.player.score()
        dScore = self.dealer.score()
        print(dScore)
   
        
        if pScore > 21:
            self.interface.message("You BUSTED")
            win = 0
        elif dScore > 21 or pScore > dScore:
            self.interface.message("You win")
            win = 10
        elif dScore == pScore:
            self.interface.message("It's a push")
            win = 5
        else:
            self.interface.message("You lose")
            win = 0
        return win

class HandView:

    "Widget for displaying a hand of cards"

    def __init__(self, win, anchor, xinc):
        # win is a GraphWin
        # centr is center point for first card
        # xinc x distance between successive cards
        self.win = win
        self.anchor = anchor
        self.xinc = xinc
        self.current = anchor.clone()
        self.images = []

    def addCard(self, c):
        imageFile = "playingcards/%s%s.gif" % (c.getSuit(), c.getRank())
        img = Image(self.current, imageFile)
        img.draw(self.win)
        self.images.append(img)
        self.current.move(self.xinc, 0)

    def clear(self):
        self.current = self.anchor.clone()
        for img in self.images:
            img.undraw()
        self.images = []

class guiInter:

    "graphical interface implementing methods required of a BJApp interface"

    def __init__(self):
        win = self.win = GraphWin("Python Blackjack!", 700, 500)
        self.win.setCoords(0, 0, 70, 50)
        self.win.setBackground("green")
        rectangle = Rectangle(Point(10, 46), Point(60, 34))
        rectangle.setFill('green4')
        rectangle.draw(win)
        rectangle2 = Rectangle(Point(10, 26), Point(60, 14))
        rectangle2.setFill('green4')
        rectangle2.draw(win)
        text = Text(Point(65, 22), "Player\nCount")
        text.setSize(18)
        text.draw(win)
        text = Text(Point(65, 40), "Dealer\nCount")
        text.setSize(18)
        text.draw(win)
        impic = Image(Point(15, 40), "playingcards/" + "b2fv.gif")
        impic.draw(win)

        self.player = HandView(self.win, Point(15, 20), 8)
        self.dealer = HandView(self.win, Point(23, 40), 8)

        impic2 = Image(Point(23, 40), "playingcards/" + "b2fv.gif")
        impic2.draw(win)

        self.buttons = [Button(win, Point(15, 7), 8, 4, "Hit"),
                        Button(win, Point(30, 7), 8, 4, "Stay"),
                        Button(win, Point(45, 7), 8, 4, "Deal"),
                        Button(win, Point(60, 7), 8, 4, "Quit")]

        self.msgBox = Text(Point(35, 30), "Foxwoods Online Casino: Blackjack!")
        self.msgBox.setTextColor("yellow")
        self.msgBox.setSize(20)
        self.msgBox.draw(self.win)

    def playerCard(self, c):
        self.player.addCard(c)

    def dealerCard(self, c):
        self.dealer.addCard(c)

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
        return (self._choose(["Deal", "Quit"]) == "Deal")

    def wantCard(self):
        return (self._choose(["Hit", "Stay"]) == "Hit")

if __name__ == '__main__':
    inter = guiInter()
    app = BlackjackApp(inter)
    app.play()

