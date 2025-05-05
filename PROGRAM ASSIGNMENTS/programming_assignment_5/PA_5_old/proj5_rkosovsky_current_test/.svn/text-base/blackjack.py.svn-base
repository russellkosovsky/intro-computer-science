# blackjack.py
#    The model portion of a Blackjack playing program

from cards import Card, Deck, BJHand

class BlackjackApp:

    """An application object that plays Blackjack"""

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
        while self.money >= 5 and self.interface.wantToPlay():
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
            self.interface.wantToPlay()
            self.interface.message("Shuffling a new deck")

    
    def initialDeal(self):
        # clear the interface and hands use existing deck
        self.interface.clear()
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
        while self.player.score() <= 21 and self.interface.wantCard():
            card = self.deck.dealCard()
            self.interface.playerCard(card)
            self.player.addCard(card)

    def dealerDeal(self):
        while self.dealer.score() < 17:
            card = self.deck.dealCard()
            self.interface.dealerCard(card)
            self.dealer.addCard(card)

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

