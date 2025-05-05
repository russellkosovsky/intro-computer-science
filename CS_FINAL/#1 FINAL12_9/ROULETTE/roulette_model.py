
from graphics import *
from button import *

win = GraphWin('buttons', 900,800)
win.setCoords(0,0,40,24)
win.setBackground('green3')

def redButtons():
    
    red_specs = [(27,23,'1'),              (31,23,'3'),
                           (29,21,'5'),
              (27,19,'7'),              (31,19,'9'),
                                        (31,17,'12'),
                           (29,15,'14'),
              (27,13,'16'),             (31,13,'18'),
              (27,11,'19'),             (31,11,'21'),
                           (29,9,'23'),
              (27,7,'25'),              (31,7,'27'),
                                        (31,5,'30'),
                           (29,3,'32'),
              (27,1,'34'),              (31,1,'36'),
                           (33,1,'RED')]
    
    buttons = []
    
    for x,y,label in red_specs:
        buttons.append(Button(win,Point(x,y),2,2,label,'red'))
        for b in buttons:
            b.activate()
            
def blackButtons():
    
    black_specs = [             (29,23,'2'),
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
            
def command():

    cRect = Rectangle(Point(6.5,6.5),Point(17.5,3.5))
    cRect.setFill('green')
    cRect.draw(win)

    impic = Image(Point(12, 15), "img/" + "wheel2.png")
    impic.draw(win)
            
    play_specs = [(8,5,"Confirm"), (12,5,"Quit"), (16,5, "Spin")]
    
    buttons = []
    for x,y,label in play_specs:
        buttons.append(Button(win,Point(x,y),2,2,label,'grey'))
        for b in buttons:
            b.activate()

def tittle():

    mRect = Rectangle(Point(32.05,25),Point(40,4.02))
    mRect.setFill('green')
    mRect.draw(win)
    
    rtext = Text(Point(12,23), 'Online Roullette')
    rtext.setSize(27)
    rtext.setFill('white')
    rtext.draw(win)

    wtext = Text(Point(35.75,23), 'Your Winnings:')
    wtext.setFill('white')
    wtext.setSize(20)
    wtext.draw(win)

    btext = Text(Point(35.5,16), 'Your  Bet:')
    btext.setFill('white')
    btext.setSize(20)
    btext.draw(win)

    stext = Text(Point(35.75,10), 'Your  Seletion:')
    stext.setFill('white')
    stext.setSize(20)
    stext.draw(win)

    bbox = Entry(Point(35.5,15), '10')
    bbox.setText('10')
    bbox.draw(win)
    
redButtons()
blackButtons()
command()
#tittle()

# grid for buttons
y = 26
for i in range(13):
    line1 = Line(Point(26,y),Point(34,y))
    y = y - 2
    line1.setFill('white')
    line1.draw(win)
##y = 16
##for i in range(3):
##    line1 = Line(Point(26,y),Point(32,y))
##    y = y - 8
##    line1.setFill('yellow')
##    line1.draw(win)
x = 26
for i in range(5):
    line1 = Line(Point(x,26),Point(x,0))
    x = x + 2
    line1.setFill('white')
    line1.draw(win)

tittle()




    


    
