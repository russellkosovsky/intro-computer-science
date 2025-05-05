from playingcards import *
from random import*
from graphics import *
from time import*
from button import*

win = GraphWin("Image Practice", 600, 600)
rect = Rectangle(Point(0,0),Point(600,600))
rect.draw(win)
rect.setFill('green')

Welcome = Text(Point(300,50),"Fox Woods Casino Online")
Welcome.setSize(30)
Welcome.setFill('white')
Welcome.draw(win)

dealertext = Text(Point(300,100),'Dealer')
dealertext.draw(win)

class Deck:
 
    def dealCard(self):
        return self.cards
    
    def cardsLeft(self):
        return len(self.cards)


    def __init__(self):
        rank = ['C','D','H','S']
        cardSpecs = []
        move = 0
        currentval = []

        impicuser = Image(Point(280,475), "playingcards/" + "b2fv.gif")
        impicuser.draw(win)        
        impicuser2= Image(Point(320,475), "playingcards/" + "b2fv.gif")
        impicuser2.draw(win)


       
        for i in range(52):
            move = move+12
            x = i % 13 + 1
            y = rank[i % 4]
            cardSpecs.append((y,x))

            impic = Image(Point(260,175), "playingcards/" + "b2fv.gif")
            impic.draw(win)

            im = Image(Point(320+move,175), "playingcards/" +str( y)  + str(x) + ".gif")
            im.draw(win)
                 
            textcard = Text(Point(300,250), str( x) +  ' of '+ str(y))
            textcard.draw(win)
            count(x, currentval)

            win.getMouse()
            textcard.undraw()
           

            impicuser.undraw()
            impicuser2.undraw()
        
            
            card1= Image(Point(280,475), "playingcards/" +str( y)  + str(x) + ".gif")
            card1.draw(win)
            card2= Image(Point(320,475), "playingcards/" +str( y)  + str(x) + ".gif")
            card2.draw(win)
            

        self.cards = []
        
def main():
    deck = Deck()
    deck.shuffle()
    
    for i in range(52):
        print(deck.dealCard())
       
def count(x,currentval):
    currentval.append(x)
    ads = sum(currentval)
    running = Text(Point(300,300),  ads)
    running.draw(win)
    sleep(0.5)
    running.undraw()

main()


      

        


