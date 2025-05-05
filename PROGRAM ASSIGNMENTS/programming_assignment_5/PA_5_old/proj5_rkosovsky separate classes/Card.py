
from random import *
from graphics import *

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
        return Image(center, "playingcards/%02d%s.gif"%(self.rank,self.suit))

