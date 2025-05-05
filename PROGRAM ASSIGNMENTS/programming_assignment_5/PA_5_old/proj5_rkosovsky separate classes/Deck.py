# blackjack.py
# The model portion of a Blackjack playing program
# """An application object that plays Blackjack"""

from Card import *
from random import *
from graphics import *

class Deck:

    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank,suit))

    def shuffle(self):
        cards = self.cards
        n = len(cards)
        for i in range(n-1):
            j = randrange(i,n)
            cards[i], cards[j] = cards[j], cards[i]

    def dealCard(self):
        return self.cards.pop()

    def cardsLeft(self):
        return len(self.cards)

