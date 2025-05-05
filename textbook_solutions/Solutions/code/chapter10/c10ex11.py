# c10ex11.py
#    Card class


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

from random import randrange

def main():
    print("Testing card class")
    n = int(input("How many cards would you like to see? "))
    for i in range(n):
        rank = randrange(1,14)
        suit = "dchs"[randrange(4)]
        randCard = Card(rank, suit)
        print(randCard, "counts", randCard.value())

if __name__ == '__main__':
    main()


