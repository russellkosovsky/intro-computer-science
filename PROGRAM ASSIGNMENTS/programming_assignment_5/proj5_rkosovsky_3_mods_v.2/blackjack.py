# blackjack.py
# rkosovsky@conncoll.edu and lmerrill@conncoll.edu colab

# Contains The Card Class, Deck Class, Hand class, blackjack class,
# HANDgraphics class, and the BJgraphics class.


# also uses graphics.py which is imported in button
from button import *
from random import *

class Card:

    '''Class for generating a playing card'''

    # use the rank/suit of card when calling
    def __init__(self, rank, suit):

        '''create a playing card'''
        
        # assigns user given rank as the rank
        self.rank = rank
        # assigns user given suit as the suit
        self.suit = suit

    def getRank(self):
        
        '''returns value of rank'''

        return self.rank

    def getSuit(self):

        '''returns value of suit'''
        
        return self.suit

    def BJValue(self):

        '''return value (score) of card'''
        
        # jack queen king all == 10
        return min(self.rank, 10)

class Deck:

    '''class for creating and manipulating a deck of playing cards'''

    def __init__(self):

        '''appends each card (52) into the list'''

        # list that acts as deck
        self.cards = []
        # runs through all suits
        for suit in "cdhs":
            # runs through all ranks
            for rank in range(1, 14):
                # creates a card for each rank/suit combo
                # appends cards to the list
                self.cards.append(Card(rank, suit))

    def shuffle(self):

        '''Shuffles the deck of cards / puts them in a random order'''
        
        # cards variable holds list of cards in the deck
        cards = self.cards
        n = len(cards)
        for i in range(n - 1):
            j = randrange(i, n)
            cards[i], cards[j] = cards[j], cards[i]

    def dealCard(self):

        '''removes card from list and returns the value'''
        
        return self.cards.pop()

    def cardsLeft(self):
        
        '''returns how many cards are left in the deck (not dealt yet)'''
        
        return len(self.cards)

class Hand:

    '''creates a 'hand' out of the cards that are
    added (HANDgraphics is used to visually represent the hand)'''

    def __init__(self):
        
        '''Initilizes variables for total(score)
        and whether or not an ace is present'''
        
        self.total = 0
        self.hasAce = False

    def addCard(self, c):

        '''adds a card to the 'hand' of cards'''
        
        # gets rank of the card
        rank = c.getRank()
        # adds the value of the card to the total (score)
        self.total = self.total + c.BJValue()
        if rank == 1:
            self.hasAce = True

    def score(self):

        '''returns the total of all the cards in the hand'''

        # makes it so ace can be 11 or 1
        if self.hasAce and self.total <=11:
            return self.total + 10
        else:
            return self.total

class blackjack:

    '''plays blackjack but without graphics (takes interface as parameter for graphics info)'''

    # interface is an parameter for playing/displaying game on the graphwin
    def __init__(self, interface):
        
        '''Initializes the instance variables
        start with a shuffled deck'''

        #create deck and shuffle it 
        self.deck = Deck()
        self.deck.shuffle()
        # player hand (None until deal is clicked)
        self.player = None
        # Dealer hand ( None until deal is clicked)
        self.dealer = None
        # for user interaction
        self.interface = interface 

    def play(self):
        
        '''runs the Blackjack program until the quit
        button is clicked and then the window closes'''

        # while .wantToPlaye() == True (when deal button is clicked)
        while self.interface.userDeal():
            # play 1 round of blackjack
            win = self.playRound()
        # close graphwin when exit button is clicked
        self.interface.close()

    def playRound(self):
        
        '''plays a single round of Blackjack'''
        
        # two cards dealt to player and one to the dealer
        self.initialDeal()
        # deal card to player
        self.playerDeal()
        # as lomng as you dont go over 21(score), run dealDealer
        if self.player.score() <= 21:
            self.dealerDeal()
        # check if won lost busted or pushed(tied)
        winnings = self.checkResults()
        # makes new deck and shuffles it when there are less than 26 cards in the deck
        if self.deck.cardsLeft() < 26:
            self.deck = Deck()
            self.deck.shuffle()
            self.interface.userDeal()
            self.interface.message("Shuffling a new deck")

    def initialDeal(self):
        
        '''first round of blackjack (two cards to
        player and one card to player)'''
        
        # .clearCards for removing all items in list
        self.interface.clearCards()
        # create deck and card hands
        deck = self.deck
        self.player = Hand()
        self.dealer = Hand()

        # deal two cards to hand for the player
        for i in range(2):
            card = deck.dealCard()
            self.interface.playerCard(card)
            self.player.addCard(card)

        # deal one card to hand for the dealer
        card = deck.dealCard()
        self.interface.dealerCard(card)
        self.dealer.addCard(card)

    def playerDeal(self):

        '''Deal card to player while the players score is still
        below 21, AND the hit button is clicked --> (.wantcard()) '''
        
        while self.player.score() <= 21 and self.interface.userHit():
            card = self.deck.dealCard()
            self.interface.playerCard(card)
            self.player.getCard(card)

    def dealerDeal(self):

        '''Deal card to dealer until score reaches 16'''

        # so dealer doesnt go past busting :)
        while self.dealer.score() < 17:
            card = self.deck.dealCard()
            self.interface.dealerCard(card)
            self.dealer.getCard(card)

    def checkResults(self):

        '''Gets score of dealer and player and
        determines the result of the round'''

        # get scores
        pScore = self.player.score()
        dScore = self.dealer.score()

        # bust 
        if pScore > 21:
            self.interface.message("You BUSTED")
        # big dub
        elif dScore > 21 or pScore > dScore:
            self.interface.message("You win")
        # tie game
        elif dScore == pScore:
            self.interface.message("It's a push")
        # take the L
        else:
            self.interface.message("You lose")

class HANDgraphics:

    '''for displaying a hand of cards on the graphics window'''

    def __init__(self, win, anchor, space):

        '''win is a graphWin centr is the center point for first card
        space is the distance between each card'''
        self.win = win
        self.anchor = anchor
        self.xinc = space
        self.current = anchor.clone()
        # stores the cards
        self.images = []

    def addCard(self, c):

        '''Draws the card image of the correct card to the 'hand' in the graphwin'''
        
        imageFile = "playingcards/%s%s.gif" %(c.getSuit(), c.getRank())
        img = Image(self.current, imageFile)
        img.draw(self.win)
        # add them to the list
        self.images.append(img)
        # spaces the cards
        self.current.move(self.xinc, 0)

    def clear(self):

        '''Removes all cards from both dealers hand and players hand'''
        
        self.current = self.anchor.clone()
        for img in self.images:
            img.undraw()
        self.images = []

class BJgraphics:

    '''implements the graphic interface for the game of Blackjack'''

    def __init__(self):

        '''Creates blackjack graphwin and draws the needed graphics objects'''

        # Window
        win = self.win = GraphWin("Python Blackjack!", 700, 500)
        self.win.setCoords(0, 0, 70, 50)
        self.win.setBackground("green")

        # for style
        rectangle = Rectangle(Point(10, 46), Point(60, 34))
        rectangle.setFill('green4')
        rectangle.draw(win)
        rectangle2 = Rectangle(Point(10, 26), Point(60, 14))
        rectangle2.setFill('green4')
        rectangle2.draw(win)

        # deck label
        decktext = Text(Point(15,47), "Deck")
        decktext.draw(win)

        # dealer chip / label
        dealercirc = Circle(Point(5,40),3)
        dealercirc.setFill('white')
        dealertext = Text(Point(5,40), "Dealer")
        dealercirc.draw(win)
        dealertext.draw(win)

        # player label
        text = Text(Point(5, 20), "Player\nHand")
        text.draw(win)

        # simulates the look of a full deck
        impic = Image(Point(15, 40), "playingcards/" + "b2fv.gif")
        impic.draw(win)
        impic3 = Image(Point(15.25, 40), "playingcards/" + "b2fv.gif")
        impic3.draw(win)
        impic4 = Image(Point(15.5, 40), "playingcards/" + "b2fv.gif")
        impic4.draw(win)
        impic2 = Image(Point(23, 40), "playingcards/" + "b2fv.gif")
        impic2.draw(win)

        # card hands
        self.player = HANDgraphics(self.win, Point(15, 20), 8)
        self.dealer = HANDgraphics(self.win, Point(23, 40), 8)
        
        # Hit Stay Deal and Quit buttons
        self.buttons = [Button(win, Point(19, 7), 8, 4, "Hit"), Button(win, Point(34, 7), 8, 4, "Stay"),
                        Button(win, Point(49, 7), 8, 4, "Deal"), Button(win, Point(66, 48), 8, 4, "Quit")]

        # Text obj for intro but also where the outro and where the round results will be displayed
        self.msgBox = Text(Point(35, 30), "Foxwoods Online Casino: Blackjack!")
        self.msgBox.setTextColor("yellow")
        self.msgBox.setSize(20)
        self.msgBox.draw(self.win)

    def playerCard(self, c):

        '''Draws a card to the players hand'''
        
        self.player.addCard(c)

    def dealerCard(self, c):

        '''Draws card to dealers hand'''
        
        self.dealer.addCard(c)

    def clear(self):

        '''removes the card hands and the message from the graphwin'''
        
        self.player.clear()
        self.dealer.clear()
        self.msgBox.setText("")

    def close(self):

        '''Closes graphwin'''

        # deactivate all buttons (not required for functionality but looks nice/feels better)
        for b in self.buttons:
            b.deactivate()
        self.message('Thanks for Playing!')
        # so they can see message
        time.sleep(2)
        self.win.close()

    def message(self, txt):

        '''changes text in textbox (for intro, outro, and end of game results)'''
        
        self.msgBox.setText(txt)

    def choose(self, choices):

        '''recognise which button is clicked and determines which
        buttons to activate/deactivate, and when'''

        # run thru all btns
        for b in self.buttons:
            # if label matches the parameter then activate dat shit
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()
        while True:
            # store location of click
            c = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(c):
                    return b.getLabel()

    def wantToPlay(self):

        '''returns true if Deal button is clicked'''
        
        return (self.choose(["Deal", "Quit"]) == "Deal")

    def wantCard(self):

        '''returns true if Hit button is clicked'''
        
        return (self.choose(["Hit", "Stay"]) == "Hit")

def main():

    # runs BJgraphics which creates all the graphic shit
    GUI = BJgraphics()
    # passes the graphics into the blackjack game as a parameter
    app = blackjack(GUI)
    # all set and ready to go so use .play() to run it up
    app.play()

main()

