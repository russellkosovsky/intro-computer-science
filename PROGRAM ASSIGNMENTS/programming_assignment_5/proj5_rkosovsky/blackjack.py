# file: blackjack.py
# rkosovsky@conncoll.edu and lmerrill@conncoll.edu colab
#   Contains The Card Class, Deck Class, Hand class, blackjack class,
#   HANDgraphics class, and the BJgraphics class.
#       an object-oriented BlackJack program designed using classes

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
        '''Initilizes variables for total(score) and whether or not an ace is present'''
        
        self.total = 0
        self.hasAce = False

    def getCard(self, c):
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

        # create deck and shuffle it
        self.deck = Deck()
        self.deck.shuffle()
        # player hand (None until deal is clicked)
        self.playerHand = None
        # Dealer hand ( None until deal is clicked)
        self.dealerHand = None
        # for user interaction
        self.interface = interface 

    def play(self):
        '''runs the Blackjack program until the quit
        button is clicked and then the window closes'''

        # while .userDeal() == True (when deal button is clicked)
        while self.interface.userDeal():
            # play 1 round of blackjack
            win = self.playRound()
        # quit graphwin when exit button is clicked
        self.interface.quit()

    def playRound(self):
        '''plays a single round of Blackjack'''
        
        # two cards dealt to playerHand and one to the dealerHand
        self.initDeal()
        # deal card to playerHand
        self.dealPlayer()
        # as lomng as you dont go over 21(score), run dealDealer
        if self.playerHand.score() <= 21:
            self.dealDealer()
        # check if won lost busted or pushed(tied)
        result = self.checkScore()
        # makes new deck and shuffles it when there are less than 26 cards in the deck
        if self.deck.cardsLeft() < 26:
            self.deck = Deck()
            self.deck.shuffle()
            self.interface.userDeal()
            self.interface.message("Shuffling a new deck")

    def initDeal(self):
        '''first round of blackjack (two cards to
        players Hand and one card to dealers Hand)'''
        
        # .clearHand for removing all items in list
        self.interface.clearHand()
        # create deck and card hands
        deck = self.deck
        self.playerHand = Hand()
        self.dealerHand = Hand()

        # deal two cards to hand for the player Hand
        for i in range(2):
            initPlayerCard = deck.dealCard()
            self.interface.playerCard(initPlayerCard)
            self.playerHand.getCard(initPlayerCard)

        # deal one card to hand for the dealer Hand
        initDealerCard = deck.dealCard()
        self.interface.dealerCard(initDealerCard)
        self.dealerHand.getCard(initDealerCard)

    def dealPlayer(self):
        '''Deal card to players hand while the players score is still
        below 21, AND the hit button is clicked --> (.wantcard()) '''
        
        while self.playerHand.score() <= 21 and self.interface.userHit():
            playerCard = self.deck.dealCard()
            self.interface.playerCard(playerCard)
            self.playerHand.getCard(playerCard)

    def dealDealer(self):
        '''Deal card to dealers hand until score reaches 16'''

        # so dealerGUIHand doesnt go past busting :)
        while self.dealerHand.score() < 17:
            dealerCard = self.deck.dealCard()
            self.interface.dealerCard(dealerCard)
            self.dealerHand.getCard(dealerCard)

    def checkScore(self):
        '''Gets score of dealers hand and players hand and
        determines the result of the round'''

        # get scores
        playerScore = self.playerHand.score()
        dealerScore = self.dealerHand.score()

        # bust 
        if playerScore > 21:
            self.interface.message("You BUSTED")
        # big dub
        elif dealerScore > 21 or playerScore > dealerScore:
            self.interface.message("You win")
        # tie game
        elif dealerScore == playerScore:
            self.interface.message("It's a push")
        # take the L
        else:
            self.interface.message("You lose")

class HANDgraphics:
    '''for displaying a hand of cards on the graphics window'''
    def __init__(self, win, centr, space):
        '''win is a graphWin centr is the center point for first card
        space is the distance between each card'''

        self.win = win
        self.center = centr
        self.xinc = space
        self.current = centr.clone()
        # stores the cards
        self.cardImages = []

    def drawCard(self, c):
        '''Draws the card image of the correct card to the 'hand' in the graphwin'''
        
        imageFile = "playingcards/%s%s.gif" %(c.getSuit(), c.getRank())
        cardImg = Image(self.current, imageFile)
        cardImg.draw(self.win)
        # add them to the list
        self.cardImages.append(cardImg)
        # spaces the cards
        self.current.move(self.xinc, 0)

    def clearCards(self):
        '''Removes all cards from both dealers hand and players hand'''
        
        self.current = self.center.clone()
        for img in self.cardImages:
            img.undraw()
        self.cardImages = []

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

        # dealerGUIHand chip / label
        dealerChip = Circle(Point(5,40),3)
        dealerChip.setFill('white')
        dealertext = Text(Point(5,40), "Dealer")
        dealerChip.draw(win)
        dealertext.draw(win)

        # playerGUIHand label
        playerText = Text(Point(5, 20), "Player\nHand")
        playerText.draw(win)

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
        self.playerGUIHand = HANDgraphics(self.win, Point(15, 20), 8)
        self.dealerGUIHand = HANDgraphics(self.win, Point(23, 40), 8)
        
        # Hit Stay Deal and Quit buttons
        self.buttons = [Button(win, Point(19, 7), 8, 4, "Hit"), Button(win, Point(34, 7), 8, 4, "Stay"),
                        Button(win, Point(49, 7), 8, 4, "Deal"), Button(win, Point(66, 48), 8, 4, "Quit")]

        # Text obj for intro but also where the outro and where the round results will be displayed
        self.MSG = Text(Point(35, 30), "Foxwoods Online Casino: Blackjack!")
        self.MSG.setTextColor("yellow")
        self.MSG.setSize(20)
        self.MSG.draw(self.win)

    def playerCard(self, c):
        '''Draws a card to the players hand'''
        self.playerGUIHand.drawCard(c)

    def dealerCard(self, c):
        '''Draws card to dealers hand'''
        self.dealerGUIHand.drawCard(c)

    def clearHand(self):
        '''removes the card hands and the message from the graphwin'''
        self.playerGUIHand.clearCards()
        self.dealerGUIHand.clearCards()
        self.MSG.setText("")

    def message(self, txt):
        '''changes text in textbox (for intro, outro, and end of game results)'''
        self.MSG.setText(txt)

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
            click = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(click):
                    return b.getLabel()
    def userHit(self):
        '''returns true if Hit button is clicked'''
        return (self.choose(["Hit", "Stay"]) == "Hit")
    
    def userDeal(self):
        '''returns true if Deal button is clicked'''
        return (self.choose(["Deal", "Quit"]) == "Deal")

    def quit(self):
        '''Closes graphwin'''

        # deactivate all buttons (not required for functionality but looks nice/feels better)
        for b in self.buttons:
            b.deactivate()
        self.message('Thanks for Playing!')
        # so they can see message
        time.sleep(2)
        self.win.close()

def main():  
    GUI = BJgraphics() # runs BJgraphics which creates all the graphic shit
    app = blackjack(GUI) # passes the graphics into the blackjack game as a parameter
    app.play() # all set and ready to go so use .play() to run it up

if __name__ == '__main__':
    main()
