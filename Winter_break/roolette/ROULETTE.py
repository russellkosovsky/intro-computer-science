# file: ROULETTE.py
# a functioning game of roulette, a casino game, where a ball spins around a wheel and players pick where they think the ball will land.
# rkosovsky@conncoll.edu and lmerrill@conncoll.edu colab
# turned in 12/15/22
# due 12/19/22

from graphics import *
from button import *
from math import *
from random import *
from time import *
from wavemod import *

class GUIroulette:
    
    """Plays a graphical version of Roulette"""
    
    def __init__(self):

        """Initializes the graphics"""

        # window
        win = self.win = GraphWin('ROULETTE', 1200,800)
        self.win.setCoords(0,0,40,24)
        self.win.setBackground('green3')
        self.money = 1000

        #bottom brown circle
        table = Circle(Point(13,13), 8.75)
        table.setFill('burlywood4')
        table.draw(win)

        #for loop which produces each red and black circle
        for i in range(0, 36):
            self.angle = i * 10
            x = 13 + 7.5 * sin(radians(self.angle))
            y = 13 - 7.5 * cos(radians(self.angle))
            self.slotOG = Circle(Point(x,y), 1)
            self.textrOG = Text(Point(x,y), i)

            if i % 2 == 0:
                self.slotOG.setFill("black")
                self.textrOG.setFill("black")
            else:
                self.slotOG.setFill("red")
                self.textrOG.setFill("black")
            self.textrOG.draw(win)

            #circles are drawn 
            self.slotOG.draw(win)

        #top brown circle
        self.table2 = Circle(Point(13,13), 7.25)
        self.table2.setFill('burlywood4')
        self.table2.draw(win)

        #top green circle
        self.tablei = Circle(Point(13,13), 7.15)
        self.tablei.setFill('green3')
        self.tablei.draw(win)

        #yellow arrow at the top
        self.poin = Polygon(Point(13,18),Point(13.5,13.5),Point(18,13),Point(13.5,12.5),Point(13,8),Point(12.5,12.5),Point(8,13),Point(12.5,13.5))
        self.poin.setFill('yellow')
        self.poin.draw(win)

        # box around btns for style
        cRect = Rectangle(Point(8,3.25),Point(18,.75))
        cRect.setFill('green')
        cRect.draw(win)

        # quit/spin btns
        self.buttons = [Button(win,Point(10,2),2,2,"Quit",'grey'),Button(win,Point(16,2),2,2,"Spin",'grey'),Button(win,Point(13,2),2,2,"Play Again",'grey')]

        # red btns arranged  in order to line up cordinates
        red_specs = [(27,23,'1'),             (31,23,'3'),
                                 (29,21,'5'),
                     (27,19,'7'),             (31,19,'9'),
                                              (31,17,'12'),
                                 (29,15,'14'),
                     (27,13,'16'),            (31,13,'18'),
                     (27,11,'19'),            (31,11,'21'),
                                 (29,9,'23'),
                     (27,7,'25'),             (31,7,'27'),
                                              (31,5,'30'),
                                 (29,3,'32'),
                     (27,1,'34'),             (31,1,'36'),
                                 (33,1,'RED')]
    
        self.redButtons = []
        
        for x,y,label in red_specs:
            self.redButtons.append(Button(win,Point(x,y),2,2,label,'red'))

        # black btns arranged in order to line up cordinates
        black_specs = [            (29,23,'2'),
                      (27,21,'4'),               (31,21,'6'),
                                   (29,19,'8'),
                      (27,17,'10'),(29,17,'11'),
                      (27,15,'13'),              (31,15,'15'),
                                   (29,13,'17'),
                                   (29,11,'20'),
                      (27,9,'22'),               (31,9,'24'),
                                   (29,7,'26'),
                      (27,5,'28'), (29,5,'29'),
                      (27,3,'31'),               (31,3,'33'),
                                   (29,1,'35'),
                                   (33,3,'BLACK')]
       
        self.blackButtons = []
        
        for x,y,label in black_specs:
            self.blackButtons.append(Button(win,Point(x,y),2,2,label,'black'))

        self.bettingBTNS = self.redButtons + self.blackButtons
        self.bettingBTNlabels = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19'
                                 ,'20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','RED','BLACK','Quit']
        
        # grid for betting buttons horizontal
        y = 26
        for i in range(13):
            line1 = Line(Point(26,y),Point(34,y))
            y = y - 2
            line1.setFill('white')
            line1.draw(win)
        #grid for betting buttons vertical
        x = 26
        for i in range(5):
            line1 = Line(Point(x,26),Point(x,0))
            x = x + 2
            line1.setFill('white')
            line1.draw(win)

        #green rectangle on right
        mRect = Rectangle(Point(32.05,25),Point(40,4.02))
        mRect.setFill('green')
        mRect.draw(win)
        
        #Top Text
        self.MSG = Text(Point(13,23), 'Online Roulette')
        self.MSG.setSize(27)
        self.MSG.setFill('white')
        self.MSG.draw(win)

        #Your winnings text
        self.wtext = Text(Point(35.75,23), 'Your Winnings:')
        self.wtext.setFill('white')
        self.wtext.setSize(20)
        self.wtext.draw(win)

        #winnings box
        winni = 0
        self.wbox = Entry(Point(35.75,22), '10')
        self.wbox.setText(winni)
        self.wbox.draw(win)

        #wallet text
        self.watext = Text(Point(35.75,20), 'Your Wallet:')
        self.watext.setFill('white')
        self.watext.setSize(20)
        self.watext.draw(win)

        #wallet box

        walletamount = 1000
        self.wabox = Entry(Point(35.75,19), '10')
        self.wabox.setText(walletamount)
        self.wabox.draw(win)

        #Bet amount text box with enrty
        self.btext = Text(Point(35.5,16), 'Your  Bet:')
        self.btext.setFill('white')
        self.btext.setSize(20)
        self.btext.draw(win)

        #Outcome Text
        self.stext = Text(Point(35.75,10), 'Outcome:')
        self.stext.setFill('white')
        self.stext.setSize(20)
        self.stext.draw(win)

        # bet text 10 at the start
        self.bbtext = Text(Point(35.5,15), '$10')
        self.bbtext.setFill('white')
        self.bbtext.setSize(20)
        self.bbtext.draw(win)

    def message(self, txt):

        '''changes text in textbox (for intro, outro, and end of game results)'''
        
        self.MSG.setText(txt)

    def choose(self, choices):

        '''recognise which button is clicked and determines which
        buttons to activate/deactivate'''

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
                                                
    def userSpin(self):

        '''returns true if spin button is clicked'''
        
        return (self.choose("Spin") == "Spin")
    
    def userCollect(self):
        
        '''returns true if collect button is clicked'''
        
        return (self.choose(["Play Again", "Quit"]) == "Play Again")
    
    def getBetSpecs(self, choices):

        '''returns value and color of bet'''

        # run thru all betting btns
        for b in self.bettingBTNS:
            # if label matches the parameter then activate dat shit
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()
        while 1:
            pt = self.win.getMouse()
            for b in self.bettingBTNS:
                if b.clicked(pt):
                    wm = WavMod('button.wav')
                    wm.test()
                    b.deactivate()
                    return b.getLabel(), b.getColor()

    def spin(self):

        '''spins the wheel'''

        wm = WavMod('spin.wav')
        wm.test()

        self.generateOutcome()

        #this loop redraws all of the small circles with corresponding numbers 
        self.circl = []
        for i in range(randrange(37,100)):
            
            angle = i * 10
            x = 13 + 7.5 * sin(radians(angle))
            y = 13 - 7.5 * cos(radians(angle))
            self.slot = Circle(Point(x,y), 1)
            self.textr = Text(Point(x,y),i)

            self.circl.append(self.slot)
            self.circl.append(self.textr)

            if i % 2 == 0:
                self.slot.setFill("black")
                self.textr.setFill("white")
            else:
                self.slot.setFill("red")
                self.textr.setFill("white")
            self.slot.draw(self.win)
            self.textr.draw(self.win)
            self.slot.undraw()
            self.textr.undraw()

        # redraws circles with the winning number displaying white.
        self.circl2 = []
        for i in range(1,37):
            
            angle = i * 10
            x = 13 + 7.5 * sin(radians(angle))
            y = 13 - 7.5 * cos(radians(angle))
            self.slot = Circle(Point(x,y), 1)
            self.textr = Text(Point(x,y),i)

            self.circl2.append(self.slot)
            self.circl2.append(self.textr)
            
            if i == self.number:
                self.slot.setFill("white") ###### if the number = the random number, changes the circle to whiute
                self.textr.setFill("black")
            elif i % 2 == 0:
                self.slot.setFill("black")
                self.textr.setFill("white")
            else:
                self.slot.setFill("red")
                self.textr.setFill("white")
                    
            self.slot.draw(self.win)
            self.textr.draw(self.win)
        
        #all top circles are undrawn
        self.table2.undraw()
        self.tablei.undraw()
        self.poin.undraw()
        #all top cirlces and arrows are drawn  
        self.table2.draw(self.win)
        self.tablei.draw(self.win)
        self.poin.draw(self.win)

        # Two Lists black and red, with each corresponding number
        black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
        red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        # draw the number to the outcome section of window
        self.text_outcome = Entry(Point(36.75,8),2)
        self.text_outcome.setText(self.number)
        # text_outcome.setFill('white')
        self.text_outcome.draw(self.win)
        # initiate the color box next to the number in the outcome section
        self.color_box = Rectangle(Point(34.25,8.5),Point(36.25,7.5))

        # this loop checks which list the number is in and draw the color box to the color
        if self.number in list(black):
            self.text_color = Text(Point(35.25,8),"Black")
            self.text_color.setFill('white')
            self.color_box.setFill('black')
            self.text_color.setSize(20)
        else:
            self.text_color = Text(Point(35.25,8),"Red")
            self.text_color.setFill('white')
            self.color_box.setFill('red')
            self.text_color.setSize(20)
        self.color_box.draw(self.win)
        self.text_color.draw(self.win)

        #if the winning number is in the black list
        if self.number in list(self.black):
            #checks and sees if the bet tile is the same number
            if self.betColor == 'black' and self.betValue == self.number:
                self.winni = 360
                #if the user correctly guessed the number tile $360 is awareded
                self.money = self.money+360
                #$360 is added to the wallet
                wm = WavMod('win.wav')
                #win sound played
                wm.test()
                    
            elif self.betValue == 'BLACK':
                self.winni = 20
                #checks if the user clicked the right color tile
                self.money = self.money+20
                #20 is awrded to the user
                wm = WavMod('win.wav')
                wm.test()
        #if the winning number is in the red list (SAME AS BLACK conditional above)
        elif self.number in list(self.red):
            if self.betColor == 'red' and self.betValue == self.number:
                self.winni = 360
                self.money = self.money+360
                wm = WavMod('win.wav')
                wm.test()
            elif self.betValue == 'RED':
                self.winni = 20
                self.money = self.money+20
                wm = WavMod('win.wav')
                wm.test()
            #if the users pick is wrong, lose sound plays and no money is awarded
        else:
            self.winni = 0
        if self.winni == 0:
            wm = WavMod('lose.wav')
            wm.test()
            
        #winnings box sets the value to the total win amount for the round
        self.wbox.setText(self.winni)
        #wallet box shows the winnings and subtracts the bet amount
        self.wabox.setText(self.money)

    def reset(self):
        
        '''clears the wheel'''
        
        wm = WavMod('confrim.wav')
        wm.test()
        self.buttons[0].deactivate()
        for i in self.circl:
            i.undraw()
            i.undraw()
        for i in self.circl2:
            i.undraw()
            i.undraw()
        self.text_outcome.setText('')
        self.color_box.undraw()
        self.text_color.undraw()

    def makeBet(self):

        '''collects data for the users bet'''
        
        spex = self.getBetSpecs(self.bettingBTNlabels)
        self.betValue = spex[0]
        self.betColor = spex[1]
        #print('color:', self.betColor, 'value:', self.betValue)  #used to check if input is correct

    def play(self):

        '''runs the game'''

        while self.money > 0:
            self.makeBet()
            if self.userSpin() == True:
                self.spin()
                if self.userCollect() == True:
                    self.reset()
                else:
                    self.quit()
            else:
                self.quit()
        self.quit()

    def generateOutcome(self):

        '''creates the winning number randomly'''
        
        #winning number is generated 
        self.number = randrange(0,36)  ###  wining number 

        #two lists are then created contating all values on the table except for the color tiles
        self.black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
        self.red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
        #winni is the amount won after each spin and is always zero at the start of each round
        self.winni = 0
        #each time the user spins, self.money is called subtracting the bet amount of 10
        self.money = self.money - 10
    
    def quit(self):

        '''Closes graphwin'''
        # deactivate all buttons (not required for functionality but looks nice/feels better)
        for b in self.buttons:
            b.deactivate()
        self.message('Thanks for Playing!')
        # sound
        wm = WavMod('quit.wav')
        wm.test()
        self.win.close()

# runs everything
def main():
    
    GAME = GUIroulette()
    wm = WavMod('intro.wav')
    wm.test()
    GAME.play()
main()



        
