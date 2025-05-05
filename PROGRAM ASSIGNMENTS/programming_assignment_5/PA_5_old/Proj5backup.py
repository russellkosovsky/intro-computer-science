from playingcards import *
from random import*
from graphics import *

class Deck:
    def __init__(self):
        rank = ['C','D','H','S']
        cardSpecs = []
        for i in range(52):
            x = i % 13 + 1
            y = rank[i % 4]
            cardSpecs.append((x,y))
        self.cards = []
        for (x, y) in cardSpecs:
            self.cards.append(PlayingCard(x, y))
    
    def __shuffle(self):
        newList = []
        for i in range (len(self.cards)):
            x = int(random() * len(self.cards)) - 1
            newList.append(self.cards[x])
            self.cards.remove(self.cards[x])
        return newList

    def shuffle(self):
        self.cards = self.__shuffle()
    
    def dealCard(self):
        return self.cards.pop(0)

    def cardsLeft(self):
        return len(self.cards)

def main():
    
    deck = Deck()
    deck.shuffle()
    for i in range(52):
        print(deck.dealCard())
main()

def main():
    
    win = GraphWin("Image Practice", 600, 600)
    rect = Rectangle(Point(0,0),Point(600,600))
    rect.draw(win)
    rect.setFill('green')
    
    n = eval(input("how many cards"))

    for i in range (n):

        x = int(randrange(0,14))
        y = int(randrange(0,4))
        suit = ['d', 's', 'h', 'c']
    
        card = x, suit[y]
        im = Image(Point(randrange(0,600),randrange(0,600)), "playingcards/" + suit[y] + str(x) + ".gif")
        im.draw(win)
        
        print(card)
        
        time.sleep(0.15)
        

main()
