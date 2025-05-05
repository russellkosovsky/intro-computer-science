# use file

from graphics import *

myWin = GraphWin("title", 600, 600)
background = Rectangle(Point(0,0),Point(600,600))
background.setFill('sky blue')
background.draw(myWin)

def try_file():
    
    title = Text(Point(300, 100),'title')
    title.setFace("arial")
    title.setSize(30)
    title.setStyle("bold")
    title.setTextColor("orange")
    title.draw(myWin)

    filename = Entry(Point(300, 220),20)
    filename.setFill("red3")
    filename.setText("ex: beemovie.txt")
    filename.setFace("arial")
    filename.setStyle("bold")
    filename.draw(myWin)

    userkey = Entry(Point(300, 310),7)
    userkey.setFill("red3")
    userkey.setText('')
    userkey.setFace("arial")
    userkey.setStyle("bold")
    userkey.draw(myWin)


    filename_msg = Text(Point(300, 175), "Type your file name below:")
    filename_msg.setFace("arial")
    filename_msg.setSize(15)
    filename_msg.setStyle("bold")
    filename_msg.setTextColor("blue")
    filename_msg.draw(myWin)

    key_msg = Text(Point(300, 265), "Type the number of frequent words you want to find below:")
    key_msg.setFace("arial")
    key_msg.setSize(15)
    key_msg.setStyle("bold")
    key_msg.setTextColor("blue")
    key_msg.draw(myWin)


    instruct = Text(Point(300, 480),"Click this text to :")
    instruct.setFace("arial")
    instruct.setSize(15)
    instruct.setStyle("bold")
    instruct.setTextColor("blue")
    instruct.draw(myWin)

    myWin.getMouse()


    ## key = text but it needs to be an integer
    keytext = userkey.getText()
    key = int(keytext)

    ## filenameText stores the story the user wants to analize using the getText() function
    filenameText = filename.getText()

    with open(filenameText, "r") as text:
    
        # the wholetext is stored as contents "text.read()"
        contents = filenameText.read()

    text.close


try_file()
