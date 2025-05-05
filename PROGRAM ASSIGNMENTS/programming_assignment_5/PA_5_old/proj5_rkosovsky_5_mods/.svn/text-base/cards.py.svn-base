# cards.py

from random import randrange
from graphics import Image

ranks = range(1,14)
rankNames = [None, "Ace" , "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

suits = "cdhs"
suitNames = ["Clubs", "Diamonds", "Hearts", "Spades"]

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def BJValue(self):
        return min(self.rank, 10)

    def __str__(self):
        rankName = rankNames[self.rank]
        suitName = suitNames[suits.index(self.suit)]
        return "%s of %s" % (rankName, suitName)

    def createImage(self, center):
        return Image(center, "cardset/%02d%s.gif"%(self.rank,self.suit))

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

class BJHand:

    def __init__(self):
        self.total = 0
        self.hasAce = False

    def addCard(self, c):
        rank = c.getRank()
        self.total = self.total + c.BJValue()
        if rank == 1:
            self.hasAce = True

    def score(self):
        if self.hasAce and self.total <=11:
            return self.total+10
        else:
            return self.total
