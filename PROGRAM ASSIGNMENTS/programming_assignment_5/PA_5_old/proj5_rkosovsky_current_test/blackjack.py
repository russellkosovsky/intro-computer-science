# blackjack.py
# The model portion of a Blackjack playing program
# An application object that plays Blackjack

from Deck import *
from graphics import *


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
        # subtract 5 dollars
        self.money = self.money - 5
        # set money to new value in the window
        self.interface.setMoney(self.money)
        # reference **def initDeal(self):**
        self.initialDeal()
        # reference def dealPlayer(self):
        self.playerDeal()
        # as lomng as you dont go over 21, run dealDealer
        if self.player.score() <= 21:
            self.dealerDeal()
        # check if won lost busted or tied
        winnings = self.checkResults()
        # add winnings to total money
        self.money = self.money + winnings
        # draw new money total in window
        self.interface.setMoney(self.money)
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

    
        

