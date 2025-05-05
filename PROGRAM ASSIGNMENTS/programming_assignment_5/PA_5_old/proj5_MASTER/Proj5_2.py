from playingcards import *
from random import*
from graphics import *
from time import*
from button import*

win = GraphWin("Image Practice", 600, 600)
rect = Rectangle(Point(0,0),Point(600,600))
rect.draw(win)
rect.setFill('green')

def intro():
    Welcome = Text(Point(300,50),"Fox Woods Casino Online")
    Welcome.setSize(30)
    Welcome.setFill('white')
    Welcome.draw(win)

    dealerRect = Rectangle(Point(175,115),Point(425,240))
    dealerRect.setFill('green4')
    dealerRect.draw(win)

    dealertext = Text(Point(300,100),'Dealer')
    dealertext.setFill('white')
    dealertext.draw(win)

    impic = Image(Point(260,175), "playingcards/" + "b2fv.gif")
    impic.draw(win)
    
    win.getMouse()

    deal()
    
def deal():
    impicuser = Image(Point(280,475), "playingcards/" + "b2fv.gif")
    impicuser.draw(win)
    
    impicuser2= Image(Point(320,475), "playingcards/" + "b2fv.gif")
    impicuser2.draw(win)

    win.getMouse()
    impicuser.undraw()
    impicuser2.undraw()

    shuffle()
    
    
def shuffle():
        rank = ['C','D','H','S']
        cardSpecs = []
        move = 0
        currentval = []

        

        
        for i in range(52):
            move = move+12
            x =randrange(1,13)
            y = rank[i % 4]
            cardSpecs.append((y,x))
            

            im = Image(Point(320+move,175), "playingcards/" +str(y)  + str(x) + ".gif")
            im.draw(win)
                 
            textcard = Text(Point(300,250), str( x) +  ' of '+ str(y))
            textcard.draw(win)

            card1= Image(Point(280,475), "playingcards/" +str(y)  + str(x) + ".gif")
            card1.draw(win)
            card2= Image(Point(320,475), "playingcards/" +str(y)  + str(x) + ".gif")
            card2.draw(win)
          
            textcard.undraw()

            win.getMouse()
            
        
      
        
     
def main():
    intro()
    shuffle()
    

main()


      

        


