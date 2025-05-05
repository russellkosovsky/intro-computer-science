
from graphics import *
from button import *
from turtle import*
from math import*
from random import*
from time import *
from wavemod import*
#_______________________________________________________________________________
win = GraphWin('buttons', 1200,800)
win.setCoords(0,0,40,24)
win.setBackground('green3')
#_______________________________________________________________________________
def redButtons():
    
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
    
    buttons = []
    
    for x,y,label in red_specs:
        buttons.append(Button(win,Point(x,y),2,2,label,'red'))
        for b in buttons:
            b.activate()
#_______________________________________________________________________________            
def blackButtons():
    
    black_specs = [        (29,23,'2'),
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
       
    buttons = []
    
    for x,y,label in black_specs:
        buttons.append(Button(win,Point(x,y),2,2,label,'black'))
        for b in buttons:
            b.activate()
    #_______________________________________________________________________________
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

#_______________________________________________________________________________            
def command():

    cRect = Rectangle(Point(8,3.25),Point(18,.75))
    cRect.setFill('green')
    cRect.draw(win)
    

#_______________________________________________________________________________
def title():
    #green rectangle on right
    mRect = Rectangle(Point(32.05,25),Point(40,4.02))
    mRect.setFill('green')
    mRect.draw(win)
    
    #Top Text
    rtext = Text(Point(14,23), 'Online Roullette')
    rtext.setSize(27)
    rtext.setFill('white')
    rtext.draw(win)

    #Your winnings text
    wtext = Text(Point(35.75,23), 'Your Winnings:')
    wtext.setFill('white')
    wtext.setSize(20)
    wtext.draw(win)

    #Bet amount text box with enrty

    btext = Text(Point(35.5,16), 'Your  Bet:')
    btext.setFill('white')
    btext.setSize(20)
    btext.draw(win)

    #Outcome Text

    stext = Text(Point(35.75,10), 'Outcome:')
    stext.setFill('white')
    stext.setSize(20)
    stext.draw(win)

    #entry box set to 10 at the start

    bbox = Entry(Point(35.5,15), '10')
    bbox.draw(win)
#_______________________________________________________________________________
def table():

    #bottom brown circle
    table = Circle(Point(13,13), 8.75)
    table.setFill('burlywood4')
    table.draw(win)
    
    #for loop which produces each red and black circle
    for i in range(0, 36):
        angle = i * 10
        x = 13+ 7.5 * sin(radians(angle))
        y = 13- 7.5 * cos(radians(angle))
        slot = Circle(Point(x,y), 1)
        textr = Text(Point(x,y),i)

        if i % 2 == 0:
            slot.setFill("black")
            textr.setFill("black")
        else:
            slot.setFill("red")
            textr.setFill("black")
        textr.draw(win)
#circles are drawn 
        slot.draw(win)
#top brown circle
    table2 = Circle(Point(13,13), 7.25)
    table2.setFill('burlywood4')
    table2.draw(win)
#top green circle
    tablei = Circle(Point(13,13), 7.15)
    tablei.setFill('green3')
    tablei.draw(win)
#yellow arrow at the top
    poin = Polygon(Point(13,18),Point(13.5,13.5),Point(18,13),Point(13.5,12.5),Point(13,8),Point(12.5,12.5),Point(8,13),Point(12.5,13.5))
    poin.setFill('yellow')
    poin.draw(win)
#_______________________________________________________________________________
def spin():
    #top brown circle
    table2 = Circle(Point(13,13), 7.25)
    table2.setFill('burlywood4')
    #top green circle
    tablei = Circle(Point(13,13), 7.15)
    tablei.setFill('green3')
    #yellow arrow at the top
    poin = Polygon(Point(13,18),Point(13.5,13.5),Point(18,13),Point(13.5,12.5),Point(13,8),Point(12.5,12.5),Point(8,13),Point(12.5,13.5))
    poin.setFill('yellow')

    # activate the quit button
    quitbtn.activate()
    number = randrange(0,36) ###    wining number is generated
    print(number) # prints number for checking
    # Two Lists black and red, with each corresponding number
    black = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    # draw the number to the outcome section of window
    text_outcome = Entry(Point(36.75,8),2)
    text_outcome.setText(number)
   # text_outcome.setFill('white')
    text_outcome.draw(win)
    # initiate the color box next to the number in the outcome section
    color_box = Rectangle(Point(34.25,8.5),Point(36.25,7.5))

    # this loop checks which list the number is in and draw the color box to the color
    if number in list(black):
        print("black")
        text_color = Text(Point(35.25,8),"Black")
        text_color.setFill('white')
        color_box.setFill('black')
        text_color.setSize(20)
    else:
        print("red")
        text_color = Text(Point(35.25,8),"Red")
        text_color.setFill('white')
        color_box.setFill('red')
        text_color.setSize(20)
    color_box.draw(win)
    text_color.draw(win)
    
    #all top circles are undrawn
    table2.undraw()
    tablei.undraw()
    poin.undraw()

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
        slot.draw(win)
        textr.draw(win)
        slot.undraw()
        textr.undraw()

    for i in range(36):
        angle = i * 10
        x = 13 + 7.5 * sin(radians(angle))
        y = 13 - 7.5 * cos(radians(angle))
        slot = Circle(Point(x,y), 1)
        textr = Text(Point(x,y),i)

        if i == number:
            slot.setFill("white") ###### if the number = the random number, changes the circle to whiute
            textr.setFill("black")
        elif i % 2 == 0:
            slot.setFill("black")
            textr.setFill("white")
        else:
            slot.setFill("red")
            textr.setFill("white")
                
        slot.draw(win)
        textr.draw(win)
    
#top cirlces and arrows are drawn  
    table2.draw(win)
    tablei.draw(win)
    poin.draw(win)
        
#_______________________________________________________________________________
redButtons()
blackButtons()
command()
title()
table()
#wm = WavMod('Open.wav')
#wm.test()


quitbtn = Button(win,Point(10,2),2,2,"Quit",'grey')
spinbtn = Button(win,Point(16,2),2,2,"Spin",'grey')
spinbtn.activate()


pt = win.getMouse()
while not quitbtn.clicked(pt):
    # when spin button is clicked
    if spinbtn.clicked(pt):
        #activate the quit button
        quitbtn.activate()
        wm = WavMod('spin.wav')
        wm.test()
        spin()
    pt = win.getMouse()
#if quit button is clicked, then loop is broken and we reach this line of code
wm = WavMod('quit.wav')
wm.test()
win.close()

#_______________________________________________________________________________






    


    
