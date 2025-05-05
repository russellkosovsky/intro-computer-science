# blackjack.py
# The model portion of a Blackjack playing program
# """An application object that plays Blackjack"""

from random import *
from graphics import *

ranks = range(1,14)
rankNames = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

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


class BlackjackApp:

    def __init__(self, interface):
        # interface is an object for user interaction
        # Initializes the instance variables
        self.money = 100    # user starts with $100
        self.deck = Deck()  # start with a shuffled deck
        self.deck.shuffle()
        self.player = None  # player hand (initially None)
        self.dealer = None  # Dealer hand (initially None
        self.interface = interface # for user interaction

    def play(self):
        # runs the Blackjack program
        while self.money >= 5 and self.interface.userDeal():
            win = self.playRound()
        self.interface.close()

    def playRound(self):
        # plays a single round of Blackjack
        self.money = self.money - 5
        self.interface.setMoney(self.money)
        self.initialDeal()
        self.playerDeal()
        if self.player.score() <= 21:
            self.dealerDeal()
        winnings = self.checkResults()
        self.money = self.money + winnings
        self.interface.setMoney(self.money)
        if self.deck.cardsLeft() < 26:
            self.deck = Deck()
            self.deck.shuffle()
            self.interface.userDeal()
            self.interface.message("Shuffling a new deck")

    
    def initialDeal(self):
        # clearCards the interface and hands use existing deck
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

