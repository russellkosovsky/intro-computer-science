# file: roulette.py
# rkosovsky@conncoll.edu and lmerrill@conncoll.edu colab

from graphics import *
from button import *
from turtle import *
from math import *
from random import *
from time import *
from wavemod import *

class GUIroulette:
    
    """ """
    
    def __init__(self):

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
            self.slot = Circle(Point(x,y), 1)
            self.textr = Text(Point(x,y), i)

            if i % 2 == 0:
                self.slot.setFill("black")
                self.textr.setFill("black")
            else:
                self.slot.setFill("red")
                self.textr.setFill("black")
            self.textr.draw(win)

            #circles are drawn 
            self.slot.draw(win)

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
        self.buttons = [Button(win,Point(10,2),2,2,"Quit",'grey'), Button(win,Point(16,2),2,2,"Spin",'grey')]

        # red btns
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
            for b in self.redButtons:
                b.activate()

        # black btns
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
            for b in self.blackButtons:
                b.activate()

        # grid for betting buttons
        y = 26
        for i in range(13):
            line1 = Line(Point(26,y),Point(34,y))
            y = y - 2
            line1.setFill('white')
            line1.draw(win)

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
        self.MSG = Text(Point(14,23), 'Online Roulette')
        self.MSG.setSize(27)
        self.MSG.setFill('white')
        self.MSG.draw(win)

        #Your winnings text
        self.wtext = Text(Point(35.75,23), 'Your Winnings:')
        self.wtext.setFill('white')
        self.wtext.setSize(20)
        self.wtext.draw(win)

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

        # entry box set to 10 at the start
        self.bbox = Entry(Point(35.5,15), '10')
        self.bbox.draw(win)

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
        
        return (self.choose(["Quit", "Spin"]) == "Spin")

    def spin(self):

        self.number = randrange(0,36) ###    wining number is generated
        print(self.number) # prints number for checking

        #this loop redraws all of the small circles with corresponding numbers 
        for i in range(randrange(36,100)):
            
            angle = i * 10
            x = 13 + 7.5 * sin(radians(angle))
            y = 13 - 7.5 * cos(radians(angle))
            slot = Circle(Point(x,y), 1)
            textr = Text(Point(x,y),i)

            if i % 2 == 0:
                slot.setFill("black")
                textr.setFill("white")
            else:
                slot.setFill("red")
                textr.setFill("white")
            slot.draw(self.win)
            textr.draw(self.win)
            slot.undraw()
            textr.undraw()

        for i in range(36):
            
            angle = i * 10
            x = 13 + 7.5 * sin(radians(angle))
            y = 13 - 7.5 * cos(radians(angle))
            self.slot = Circle(Point(x,y), 1)
            self.textr = Text(Point(x,y),i)

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
            print("black")
            text_color = Text(Point(35.25,8),"Black")
            text_color.setFill('white')
            self.color_box.setFill('black')
            text_color.setSize(20)
        else:
            print("red")
            text_color = Text(Point(35.25,8),"Red")
            text_color.setFill('white')
            self.color_box.setFill('red')
            text_color.setSize(20)
        self.color_box.draw(self.win)
        text_color.draw(self.win)

    def reset(self):
        self.slot.undraw()
        self.textr.undraw()

    def play(self):

        while self.money > 0 and self.userSpin():
            
            wm = WavMod('spin.wav')
            wm.test()
            #self.reset()
            self.spin()
            self.reset()
            self.generateOutcome()

        self.quit()

    def generateOutcome(self):
        
        self.number = randrange(0,36)  ###  wining number is generated
        print(self.number) # prints number for checking
        return self.number

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

# runs the game
def main():
    GAME = GUIroulette()
    GAME.play()
main()



        
