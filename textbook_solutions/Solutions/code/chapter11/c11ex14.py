# c11ex14.py
#   Poker hand evaluation

class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def BJValue(self):
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

def isFlush(hand):
    suit = hand[0].getSuit()
    for c in hand:
        if c.getSuit() != suit:
            return False
    return True
    
def isStraight(hand):
    # Check last four for consecutive order
    for i in range(1,len(hand)-1):
        if hand[i].getRank()+1 != hand[i+1].getRank():
            return False
    # Then check first and handle special case of ace going high
    return (hand[0].getRank()+1 == hand[1].getRank()) or \
            (hand[0].getRank()==1 and hand[1].getRank()==10)

def countRanks(hand):
    rankCounts = [0]*14
    for card in hand:
        r = card.getRank()
        rankCounts[r] = rankCounts[r] + 1
    return rankCounts
        

def main():
    fname = input("Enter name of file with hand: ")
    infile = open(fname,"r")

    # read the file to create a hand of cards
    hand = []
    for line in infile:
        rank, suit = line.split()
        theCard = Card(int(rank),suit)
        hand.append(theCard)
    infile.close()

    hand.sort(key=Card.getRank)
    for c in hand:
        print(c)
    print()
        
    if isStraight(hand):
        if isFlush(hand):
            if hand[0].getRank() == 1 and hand[-1].getRank()==13:
                print("Royal Flush")
            else:
                print("Straight Flush")
        else:
            print("Straight")
    elif isFlush(hand):
        print("Flush")
    else:
        counts = countRanks(hand)
        if 4 in counts:
            print("Four of a Kind")
        elif 3 in counts:
            if 2 in counts:
                print("Full House")
            else:
                print("Three of a Kind")
        elif 2 in counts:
            if counts.count(2) == 2:
                print("Two Pair")
            else:
                print("Pair")
        else:
            if hand[0].getRank() == 1:
                print("Ace High")
            else:
                best = hand[-1]
                rankStr = str(best).split()[0]
                print(rankStr, "High")
        

if __name__ == '__main__':
    main()


