
from Card import *
from random import *

class Deck:

    # appends each card (52) into the list
    def __init__(self):
        self.cards = []
        # runs through all suits
        for suit in "cdhs":
            # runs through all ranks
            for rank in range(1,14):
                # creates a card for each rank/suit combo
                # appends cards to the list
                self.cards.append(Card(rank,suit))
    
    def shuffle(self):
        # cards variable holds list of cards in the deck
        cards = self.cards
        n = len(cards)
        for i in range(n-1):
            j = randrange(i,n)
            cards[i], cards[j] = cards[j], cards[i]

    def dealCard(self):
        # removes card from list and returns the value
        return self.cards.pop()

    def cardsLeft(self):
        # how many cards are left in the deck (not dealt yet)
        return len(self.cards)

