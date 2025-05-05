# file: program_3.py
# This program is a Caesar cipher encoder/decoder with a Graphical User Interface 
# Author: Russell Kosovsky (rkosovsky@conncoll.edu)

from graphics import *
from time import *

myWin = GraphWin("XXL Freshman Caesar Cypher", 600, 600)
background = Rectangle(Point(0,0),Point(600,600))
background.setFill('sky blue')
background.draw(myWin)


def open_screen():

    ##
    welcome = Text(Point(300, 250), "Welcome to the XXL Freshman Ceaser Cypher")
    welcome.setFace("arial")
    welcome.setSize(25)
    welcome.setTextColor("black")
    welcome.setStyle("bold")
    welcome.draw(myWin)

    prompt = Text(Point(300, 300), "Instructions: Click the screen to continue")
    prompt.setFace("arial")
    prompt.setSize(20)
    prompt.setTextColor("orange")
    prompt.setStyle("bold")
    prompt.draw(myWin)
    myWin.getMouse()
    welcome.undraw()
    prompt.move(0,-200)

    ## description about the ceaser cipher is from wikipedia... https://en.wikipedia.org/wiki/Caesar_cipher
    about = Text(Point(300, 250), "In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, \nCaesar's code or Caesar shift, "
                 "is one of the simplest and most widely known encryption \ntechniques. It is a type of substitution cipher in which each letter in the"
                 "plaintext is \nreplaced by a letter some fixed number of positions down the alphabet. For example, \nwith a left shift of 3, D would be"
                 "replaced by A, E would become B, and so on. \nThe method is named after Julius Caesar, who used it in his private correspondence.")
    about.setFace("arial")
    about.setSize(15)
    #prompt.setStyle("bold")
    about.draw(myWin)

    myWin.getMouse()
    description = Text(Point(300, 350), "This program has the capabilities to encode and decode any message with \nany key value, "
                       "and encode or decode any text file with any key value")
    description.setFace("arial")
    description.setSize(15)
    description.setStyle("bold")
    description.setTextColor("blue")
    description.draw(myWin)

    myWin.getMouse()
    prompt.undraw()

    sendoff = Text(Point(300, 440), "Thank you for trying out this program! \nClick the screen one more time to begin.")
    sendoff.setFace("arial")
    sendoff.setSize(22)
    sendoff.setStyle("bold")
    sendoff.setTextColor("orange")

    sendoff.draw(myWin)

    myWin.getMouse()
    sendoff.undraw()
    description.undraw()
    about.undraw()
    prompt.undraw()

    home()

##  drawButton() function we made in class 
def drawButton(win, pt1, pt2, label,color,shape,txtColor):
    button = shape(pt1, pt2)
    button.setFill(color)
    button.draw(win)

    # use these coords for the position of the label
    btnLabel = Text( button.getCenter(), label)
    btnLabel.setFill(txtColor)
    btnLabel.setStyle("bold")
    btnLabel.draw(win)

    return button

##  isClicked() function we made in class 
def isClicked(button, point):

    # find x and y coordinate of the point
    x = point.getX()
    y = point.getY()

    # get two corner points of the rectangle object
    pt1 = button.getP1()
    pt2 = button.getP2()
    
    # calc min/max for the range of x and y
    minX = min(pt1.getX(), pt2.getX())
    maxX = max(pt1.getX(), pt2.getX())
    minY = min(pt1.getY(), pt2.getY())
    maxY = max(pt1.getY(), pt2.getY())

    # range test
    if ( minX <= x <= maxX and minY <= y <= maxY):
        return True
    else:
        return False




def home():

    # begining of choice function introduces both button options:encode and decode with a message at the top for instruction
    MSG= Text(Point(300, 250), 'The first step is to figure out whether \nyou want to encode or decode a message. \nThen select the corresponding button, or click "QUIT" \nif you want to exit the program.')
    MSG.setFace("arial")
    MSG.setSize(20)
    MSG.setStyle("bold")
    MSG.draw(myWin)

    # create button for encoding
    point1 = Point(140,510)
    point2 = Point(260,580)
    encodebtn = drawButton(myWin,point1,point2,"ENCODE","red3", Rectangle,"white")

    # create button for decoding
    point3 = Point(340,510)
    point4 = Point(460,580)
    decodebtn = drawButton(myWin,point3,point4,"DECODE","blue3", Rectangle,"white")

    # create button for closing program
    quitbtn = drawButton(myWin, Point(580,510), Point(510,580), "Quit","yellow", Rectangle,"black")
    

    # both buttons are drawn to (myWin) and wait for user click
    # user click is stored as variable click
    # x and y cordinates in the window are set to (X and Y) 
    click = myWin.getMouse()

    # while loop, when clicked finds if the click is in the range of the red cicle or blue circle
    while not isClicked(quitbtn,click) == True:

        #click = myWin.getMouse()

        while isClicked(encodebtn,click) == True:

            # if user clicks button, the buttons and the text are undrawn
            encodebtn.undraw()
            decodebtn.undraw()
            quitbtn.undraw()
            MSG.undraw()

            background = Rectangle(Point(0,0),Point(600,600))
            background.setFill('white')
            background.draw(myWin)

            # so the quit button stays
            quitbtn.draw(myWin)
            btnLabel = Text(quitbtn.getCenter(), "QUIT")
            btnLabel.setFill("black")
            btnLabel.setStyle("bold")
            btnLabel.draw(myWin)

            # the user is then sent to the encode function
            encoder()
            click = myWin.getMouse()

        while isClicked(decodebtn,click) == True:

            # if user clicks button, the buttons and the text are undrawn
            decodebtn.undraw()
            encodebtn.undraw()
            quitbtn.undraw()
            MSG.undraw()
            background = Rectangle(Point(0,0),Point(600,600))
            background.setFill('white')
            background.draw(myWin)

            # so the quit button stays
            quitbtn.draw(myWin)
            btnLabel = Text(quitbtn.getCenter(), "QUIT")
            btnLabel.setFill("black")
            btnLabel.setStyle("bold")
            btnLabel.draw(myWin)

            # theuser is then sent to the decode function
            decoder()
            click = myWin.getMouse()
    else:
        myWin.close()

def try_file():

    
    #the tittle is changed to file cipher and drawn to the window
    
    title = Text(Point(300, 100),'FILE CIPHER')
    title.draw(myWin)
    #the easiest way to limit bugs was to keep the texts boxes drawn in both the encode and decodee functions

    filename = Entry(Point(300, 200),20)
    filename.setText("ex: tester.txt")
    filename.draw(myWin)
    #the first text box allows the user to type in their story with an example for correct format

    userkey = Entry(Point(300, 250),20)
    userkey.setText('')
    userkey.draw(myWin)
    #the UserEntKey text box grabs the users preffered key for encode;/decoding the file

    choiceBox = Entry(Point(300, 300),20)
    choiceBox.setText('')
    choiceBox.draw(myWin)
    #the final text box allows the user to type if they want to either "Encode" , or "Decodde" the file

    filename_msg = Text(Point(300, 175), 'Type your file name below:')
    filename_msg.setStyle("bold")
    filename_msg.draw(myWin)

    key_msg = Text(Point(300, 225), 'Type the key below:')
    key_msg.draw(myWin)

    choice_msg = Text(Point(300, 275),"Do you want your file encoded decoded? (type: e to encode or d to decoded:")
    choice_msg.draw(myWin)

    instruct = Text(Point(300, 340),"Click this text to run the cipher and save the result as a file on your computer:")
    instruct.draw(myWin)

    myWin.getMouse()
    #user instructed to click mouse and process
    #choice is stored from the gettext function as encode or decode and used in the loop below
    choice1 = choiceBox.getText()

    #like before the key is stored as a tex from the gettext() function and then has to be translated to integer using the int(keyt) which is stored as variable key
    textkey = userkey.getText()
    key = int(textkey)

    #fname is stored as the story the user wants to change using the getText() function
    filenameText = filename.getText()


    with open(filenameText, "r") as MSG:
    
        #the MSG is saved as the entirety of the text file "f.read()"
        contents = MSG.read()

    MSG.close

    encodedfile = open("encodedfile.txt", "w")

    decodedfile = open("decodedfile.txt", "w")
    

    #the Encoded and Decoded MSG variables are first established as nothing

    #if the text from choice1 is Encoded, the program runs the loop from the Encoded function
    #if the text from choice1 is Decoded, the program runs the loop from the Decoded function
    #with in the if and elif function the code from both the encode and decode functions were pasted

    #myWin.getMouse()


    # Empty string where the message will be implemented
    encodedMsg = ''
    decodedMsg = ''

    if choice1 == 'e' or choice1 =='E':


        # For loop that runs through every character in the message
        for ch in contents:

            # Deals with uppercase characters
            if ch.isupper() == True:
                shift = ((ord(ch) - 65 + key) % 26) + 65

                encodedMsg = encodedMsg + (chr(shift))

            # Deals with lowercase charachters
            elif ch.islower() == True:

                shift = ((ord(ch) - 97 + key) % 26) + 97 

                encodedMsg = encodedMsg + chr(shift)

            # Deals with any other characters (that arent letters)
            else:

                encodedMsg = encodedMsg + ch

        ##
        print(encodedMsg, file=encodedfile)
        encodedfile.close()

    
    elif choice1 == 'e' or choice1 =='E':

        #filewrite = open(filenameText, "w")
        #the only change was for each option to include a writting segment stored as fw

        for ch in contents:
        
            # Deals with uppercase characters
            if ch.isupper():

                shift = ((ord(ch) - 65 - key + 26) % 26) + 65

                decodedMsg = decodedMsg + chr(shift)     

            # Deals with lowercase charachters
            elif ch.islower():

                shift = ((ord(ch) - 97 - key + 26) % 26) + 97

                decodedMsg = decodedMsg + chr(shift)     

            # Deals with any other characters (that arent letters)
            else:

                decodedMsg = decodedMsg + ch  
        ##
        print(decodedMsg, file=decodedfile) 
        decodedfile.close()


    ## end of program!!
    
    done = Text(Point(300, 575), 'Click anywhere to close window.')
    done.draw(myWin)


    myWin.getMouse()

    myWin.close()
    

def encoder():

    MSG = Text(Point(300, 90), 'ENCODER')
    MSG.setFace("arial")
    MSG.setSize(27)
    MSG.setStyle("bold")
    MSG.setTextColor("red3")
    MSG.draw(myWin)

    # text box for encode
    textbox = Entry(Point(300,200), 40)
    textbox.setFace("arial")
    textbox.setSize(15)
    textbox.setFill("sky blue")
    textbox.setStyle("bold")
    textbox.setText('')
    textbox.draw(myWin)

    # message instructions
    instructions = Text(Point(300,150), "Enter the message that you want to encode \nin the text box below.")
    instructions.setFace("arial")
    instructions.setSize(14)
    instructions.setTextColor("sky blue")
    instructions.setStyle("bold")
    instructions.draw(myWin)

    # text box where user inputs the key and it is drawn to myWin

    keybox = Entry(Point(300, 300),6)
    keybox.setFace("arial")
    keybox.setSize(15)
    keybox.setFill("sky blue")
    keybox.setStyle("bold")
    keybox.setText('')
    keybox.draw(myWin)

    # key instructions
    keyinstructions = Text(Point(300,250), "Enter the key that you want to use \nin the text box below.")
    keyinstructions.setFace("arial")
    keyinstructions.setSize(14)
    keyinstructions.setTextColor("sky blue")
    keyinstructions.setStyle("bold")
    keyinstructions.draw(myWin)

    continuee = Text(Point(300, 335),"After entering the information above, click this text to continue.")
    continuee.draw(myWin)

    # wait for click
    myWin.getMouse()

    # stores the users input for the key but its a string
    text_key = keybox.getText()

    # so we make it an integer stored as key
    key = int(text_key)
 
    # store the message from the user
    userMSG = textbox.getText()

    # Empty string where the message will be implemented
    encodedMsg = ''

    # For loop that runs through every character in the message
    for ch in userMSG:

        # Deals with uppercase characters
        if ch.isupper() == True:
            shift = ((ord(ch) - 65 + key) % 26) + 65

            encodedMsg = encodedMsg + (chr(shift))

        # Deals with lowercase charachters
        elif ch.islower() == True:

            shift = ((ord(ch) - 97 + key) % 26) + 97 

            encodedMsg = encodedMsg + chr(shift)

        # Deals with any other characters (that arent letters)
        else:

            encodedMsg = encodedMsg + ch

    continuee.undraw()

    #a new text box is created with the encoded message inside using the set text function.
    #I did this to make is easy, to encode and decode the same text, using (copy/paste)

    Encoded = Entry(Point(300, 370),20)
    Encoded.setText(encodedMsg)
    Encoded.draw(myWin)
    #greeting message is drawn above the text box

    Encodedresult = Text(Point(300, 340),"Your message has been successfully shifted:")
    Encodedresult.draw(myWin)

    #Menu function is called and the title message is undrawn
    MSG.undraw()

    #menus message is first drawn to the top of two new buttons
    MenuMSG = Text(Point(300, 400),"Would you like to:")
    MenuMSG.draw(myWin)

    # create button for trying with a file
    point1 = Point(215,420)
    point2 = Point(385,445)
    try_file_btn = drawButton(myWin,point1,point2,"Run program with a .TXT file","red3", Rectangle,"white")

    # create button for trying running program again
    point3 = Point(215,455)
    point4 = Point(385,480)
    run_btn = drawButton(myWin,point3,point4,"Run the program again","red3", Rectangle,"white")
    
    #getmouse stores the value to click
    click = myWin.getMouse()

    while isClicked(run_btn,click) == True:

        # if user clicks run button, everything is undrawn and it goes back to home()
        MenuMSG.undraw()
        try_file_btn.undraw()
        run_btn.undraw()
        Encodedresult.undraw()
        Encoded.undraw()
        keyinstructions.undraw()
        keybox.undraw()
        instructions.undraw()
        textbox.undraw()
        
        home()

    while isClicked(try_file_btn,click) == True:

        # if user clicks run button, everything is undrawn and it goes back to home()
        MenuMSG.undraw()
        try_file_btn.undraw()
        run_btn.undraw()
        Encodedresult.undraw()
        Encoded.undraw()
        keyinstructions.undraw()
        keybox.undraw()
        instructions.undraw()
        textbox.undraw()

        try_file()


    

def decoder():

    MSG= Text(Point(300, 90), 'DECODER')
    MSG.setFace("arial")
    MSG.setSize(27)
    MSG.setStyle("bold")
    MSG.setTextColor("blue3")
    MSG.draw(myWin)

    # text box for decode
    textbox = Entry(Point(300,200), 40)
    textbox.setFace("arial")
    textbox.setSize(15)
    textbox.setFill("sky blue")
    textbox.setStyle("bold")
    textbox.setText('')
    textbox.draw(myWin)

    # message instructions
    instructions = Text(Point(300,150), "Enter the message that you want to decode \nin the text box below.")
    instructions.setFace("arial")
    instructions.setSize(14)
    instructions.setTextColor("sky blue")
    instructions.setStyle("bold")
    instructions.draw(myWin)

    # text box where user inputs the key and it is drawn to myWin

    keybox = Entry(Point(300, 300),6)
    keybox.setFace("arial")
    keybox.setSize(15)
    keybox.setFill("sky blue")
    keybox.setStyle("bold")
    keybox.setText('')
    keybox.draw(myWin)

    # key instructions
    keyinstructions = Text(Point(300,250), "Enter the key that you want use \nin the text box below.")
    keyinstructions.setFace("arial")
    keyinstructions.setSize(14)
    keyinstructions.setTextColor("sky blue")
    keyinstructions.setStyle("bold")
    keyinstructions.draw(myWin)

    continuee = Text(Point(300, 335),"After entering the information above, click this text to continue.")
    continuee.draw(myWin)

    # wait for click
    myWin.getMouse()

    # stores the users input for the key but its a string
    text_key = keybox.getText()

    # so we make it an integer stored as key
    key = int(text_key)
 
    # store the message from the user
    userMSG = textbox.getText()

    # Empty string where the message will be implemented
    decodedMsg = ''

    # For loop that runs through every character in the message
    for ch in userMSG:

        # Deals with uppercase characters
        if ch.isupper():

            shift = ((ord(ch) - 65 - key + 26) % 26) + 65

            decodedMsg = decodedMsg + chr(shift)     

        # Deals with lowercase charachters
        elif ch.islower():

            shift = ((ord(ch) - 97 - key + 26) % 26) + 97

            decodedMsg = decodedMsg + chr(shift)     

        # Deals with any other characters (that arent letters)
        else:

            decodedMsg = decodedMsg + ch  

    continuee.undraw()

    #a new text box is created with the encoded message inside using the set text function.
    #I did this to make is easy, to encode and decode the same text, using (copy/paste)

    Decoded = Entry(Point(300, 370),20)
    Decoded.setText(decodedMsg)
    Decoded.draw(myWin)
    #greeting message is drawn above the text box

    Decodedresult = Text(Point(300, 340),"Your message has been successfully:")
    Decodedresult.draw(myWin)

    #Menu function is called and the title message is undrawn
    MSG.undraw()

    #menus message is first drawn to the top of two new buttons

    MenuMSG = Text(Point(300, 400),"Would you like to:")
    MenuMSG.draw(myWin)

    # create button for trying with a file
    point1 = Point(215,420)
    point2 = Point(385,445)
    try_file_btn = drawButton(myWin,point1,point2,"Run program with a .TXT file","red3", Rectangle,"white")

    # create button for trying running program again
    point3 = Point(215,455)
    point4 = Point(385,480)
    run_btn = drawButton(myWin,point3,point4,"Run the program again","red3", Rectangle,"white")
    
    #getmouse stores the value to click
    click = myWin.getMouse()

    while isClicked(run_btn,click) == True:

        # if user clicks run button, everything is undrawn and it goes back to home()
        MenuMSG.undraw()
        try_file_btn.undraw()
        run_btn.undraw()
        Decodedresult.undraw()
        Decoded.undraw()
        keyinstructions.undraw()
        keybox.undraw()
        instructions.undraw()
        textbox.undraw()
        
        home()

    while isClicked(try_file_btn,click) == True:

        # if user clicks run button, everything is undrawn and it goes back to home()
        MenuMSG.undraw()
        try_file_btn.undraw()
        run_btn.undraw()
        Decodedresult.undraw()
        Decoded.undraw()
        keyinstructions.undraw()
        keybox.undraw()
        instructions.undraw()
        textbox.undraw()

        try_file()

        







open_screen()


