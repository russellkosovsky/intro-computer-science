from graphics import *
from button import *
from csaudio import *

def main():

    #draw keys using buttons
    win = GraphWin("Midi Piano", 600, 300)
    win.setCoords(0, 0, 10, 12)
    keys = []
    for i in range(10):
        key = Button(win, Point(0.7 + i*1.1, 7), 1, 9, "")
        key.activate()
        key.setBackgroundColor('white')
        keys.append(key)

    # # keys
    akey = Rectangle(Point(0.8, 11.55), Point(1.6, 7))
    akey.setFill('black')
    akey.draw(win)
    akey = Rectangle(Point(1.9, 11.55), Point(2.7, 7))
    akey.setFill('black')
    akey.draw(win)
    akey = Rectangle(Point(4.1, 11.55), Point(4.9, 7))
    akey.setFill('black')
    akey.draw(win)
    akey = Rectangle(Point(5.2, 11.55), Point(6.0, 7))
    akey.setFill('black')
    akey.draw(win)
    akey = Rectangle(Point(6.3, 11.55), Point(7.1, 7))
    akey.setFill('black')
    akey.draw(win)
    akey = Rectangle(Point(8.5, 11.55), Point(9.3, 7))
    akey.setFill('black')
    akey.draw(win)
    
    #quit button
    quitButton = Button(win, Point(5,1), 2, 1, "Quit")
    quitButton.activate()
    
    #key sound files from C to D high
    files = ['key_sound/C.wav', 'key_sound/D.wav', 'key_sound/E.wav', \
             'key_sound/F.wav', 'key_sound/G.wav', 'key_sound/A.wav', \
             'key_sound/B.wav', 'key_sound/C_high.wav', 'key_sound/D_high.wav']
    
    #handle interaction: get mouse click first
    pt = win.getMouse()

    #loop until quit button
    while not quitButton.clicked(pt):

        #for each key button in keys list, check any one is clicked
        #if clicked, then play that key wave file for the click key
        #consider using async argument to True for play function from csaudio module
        ###you code here




        #get new mouse click before back to while statement conditions
        pt = win.getMouse()


    #close window as a user clicked quit button
    win.close()
    
if __name__ == "__main__":
    main()
