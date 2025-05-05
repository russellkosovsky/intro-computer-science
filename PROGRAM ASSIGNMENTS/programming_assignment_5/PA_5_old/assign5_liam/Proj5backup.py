from playingcards import *
from random import*
from graphics import *
from time import*

win = GraphWin("Image Practice", 600, 600)
rect = Rectangle(Point(0,0),Point(600,600))
rect.draw(win)
rect.setFill('green')

dealertext = Text(Point(300,100),'Dealer')
dealertext.draw(win)

class Deck:
 
    def dealCard(self):
        return self.cards
    
    def cardsLeft(self):
        return len(self.cards)


    def __init__(self):
        rank = ['C','D','H','S']
        cardSpecs = []
        move = 0
        currentval = []
        for i in range(52):
            move = move+12
            x =randrange(0,13)
            y = rank[i % 4]
            cardSpecs.append((y,x))
            im = Image(Point(300+move,175), "playingcards/" +str( y)  + str(x) + ".gif")
            im.draw(win)
            textcard = Text(Point(300,250), str( x)+  'of '+ str(y))
            textcard.draw(win)
            count(x, currentval)
            win.getMouse()
            textcard.undraw()
        self.cards = []
        
def main():
    
    deck = Deck()
    deck.shuffle()
    
    for i in range(52):
        print(deck.dealCard())
       
def count(x,currentval):
    currentval.append(x)
    ads = sum(currentval)
    running = Text(Point(300,300),  ads)
    running.draw(win)
    sleep(0.5)
    running.undraw()
main()
