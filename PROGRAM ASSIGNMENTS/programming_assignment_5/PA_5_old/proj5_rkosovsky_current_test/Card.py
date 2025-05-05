
class Card:

    # use the rank/suit of card when calling
    def __init__(self, rank, suit):
        # assigns user given rank as the rank
        self.rank = rank
        # assigns user given suit as the suit
        self.suit = suit

    # returns value of rank
    def getRank(self):
        return self.rank

    # returns value of suit
    def getSuit(self):
        return self.suit
    
    def BJValue(self):
        # return value (score) of card
        # jack queen king all == 10
        return min(self.rank, 10)

    def __str__(self):
        rankName = [None, "Ace" , "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]
        suitName = ["Clubs", "Diamonds", "Hearts", "Spades"]
        rankName = rankName[self.rank]
        suitName = suitName[suits.index(self.suit)]
        return "%s of %s"%(rankName, suitName)

    def createImage(self, center):
        # playingcards == folder
        # first "%" is for rank and second "%" is for suite
        # this is because thats how the .gif file names are formatted
        # then use %(self.rank,self.suit) to substitute rank and suite in the right spot
        return Image(center, "playingcards/%s%s.gif"%(self.suit,self.rank))

