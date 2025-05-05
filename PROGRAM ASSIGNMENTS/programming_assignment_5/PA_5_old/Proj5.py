from deckclass import *
from random import*
from graphics import *
from time import*

win = GraphWin("Image Practice", 600, 600)
rect = Rectangle(Point(0,0),Point(600,600))
rect.draw(win)
rect.setFill('green')

dealertext = Text(Point(300,100),'Dealer')
dealertext.draw(win)


def main():
    
    deck = Deck(win)
    
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


      

        


