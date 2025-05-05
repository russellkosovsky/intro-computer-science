# c11ex15.py
#   Deck class

from random import randrange

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def value(self):
        if self.getRank() < 10:
            return self.rank
        else:
            return 10

    def __str__(self):
        ranks = [None, "Ace", "Two", "Three", "Four", "Five", "Six",
                 "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        rankStr = ranks[self.rank]
        if self.suit == 'c':
            suitStr = "Clubs"
        elif self.suit == 'd':
            suitStr = "Diamonds"
        elif self.suit == 'h':
            suitStr = "Hearts"
        else:
            suitStr = "Spades"
        return "{0} of {1}".format(rankStr, suitStr)

class Deck:

    def __init__(self):
        self.cards = []
        for suit in "cdhs":
            for rank in range(1,14):
                self.cards.append(Card(rank,suit))

    def shuffle(self):
        n = len(self.cards)
        cards = self.cards
        for pos in range(n):
            randpos = randrange(pos,n)
            cards[pos], cards[randpos] = cards[randpos], cards[pos]

    def dealCard(self):
        return self.cards.pop()

    def cardsLeft(self):
        return len(self.cards)

def main():
    n = int(input("Hose many cards should I deal? "))
    d = Deck()
    d.shuffle()
    for i in range(n):
        print(d.dealCard())


if __name__ == '__main__':
    main()


