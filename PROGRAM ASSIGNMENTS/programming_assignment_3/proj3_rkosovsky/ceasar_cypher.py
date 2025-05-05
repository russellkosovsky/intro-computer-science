## file: program_3.py
## This program is a Caesar cipher encoder/decoder with a Graphical User Interface 
## Author: Russell Kosovsky (rkosovsky@conncoll.edu)

from graphics import *
import time

myWin = GraphWin("XXL Freshman Caesar Cypher", 600, 600)
background = Rectangle(Point(0,0),Point(600,600))
background.setFill('sky blue')
background.draw(myWin)

## first function for the beginning screen
def open_screen():

    ## welcome text
    welcome = Text(Point(300, 250), "Welcome to the XXL Freshman Ceaser Cypher")
    welcome.setFace("arial")
    welcome.setSize(25)
    welcome.setTextColor("black")
    welcome.setStyle("bold")
    welcome.draw(myWin)

    ## instructions
    prompt = Text(Point(300, 300), "Instructions: Click the screen to continue")
    prompt.setFace("arial")
    prompt.setSize(20)
    prompt.setTextColor("orange")
    prompt.setStyle("bold")
    prompt.draw(myWin)   
    myWin.getMouse()
    welcome.undraw()
    ## technically the .move is animation
    prompt.move(0,-200)

    ## description about the ceaser cipher is from wikipedia... https://en.wikipedia.org/wiki/Caesar_cipher
    about = Text(Point(300, 250), "In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, \nCaesar's code or Caesar shift, "
                 "is one of the simplest and most widely known encryption \ntechniques. It is a type of substitution cipher in which each letter in the"
                 "plaintext is \nreplaced by a letter some fixed number of positions down the alphabet. For example, \nwith a left shift of 3, D would be"
                 "replaced by A, E would become B, and so on. \nThe method is named after Julius Caesar, who used it in his private correspondence.")
    about.setFace("arial")
    about.setSize(15)
    about.draw(myWin)

    ## get mouse click before moving on to description of program
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

    ## undraw everything and send user to home screen
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

    ## use these coords for the position of the label
    btnLabel = Text( button.getCenter(), label)
    btnLabel.setFill(txtColor)
    btnLabel.setStyle("bold")
    btnLabel.draw(win)

    return button

##  isClicked() function we made in class 
def isClicked(button, point):

    ## find x and y coordinate of the point
    x = point.getX()
    y = point.getY()

    ## get two corner points of the rectangle object
    pt1 = button.getP1()
    pt2 = button.getP2()
    
    ## calc min/max for the range of x and y
    minX = min(pt1.getX(), pt2.getX())
    maxX = max(pt1.getX(), pt2.getX())
    minY = min(pt1.getY(), pt2.getY())
    maxY = max(pt1.getY(), pt2.getY())

    ## range test
    if ( minX <= x <= maxX and minY <= y <= maxY):
        return True
    else:
        return False

## function where user chooses if they want to encode or decode
def home():

    ## instructions
    MSG= Text(Point(300, 250), 'The first step is to figure out whether \nyou want to encode or decode a message. \nThen select the corresponding button, or click "QUIT" \nif you want to exit the program.')
    MSG.setFace("arial")
    MSG.setSize(20)
    MSG.setStyle("bold")
    MSG.draw(myWin)

    ## create button for encoding
    point1 = Point(140,510)
    point2 = Point(260,580)
    encodebtn = drawButton(myWin,point1,point2,"ENCODE","red3", Rectangle,"white")

    ## create button for decoding
    point3 = Point(340,510)
    point4 = Point(460,580)
    decodebtn = drawButton(myWin,point3,point4,"DECODE","blue3", Rectangle,"white")

    ## create button for closing program
    quitbtn = drawButton(myWin, Point(580,510), Point(510,580), "Quit","yellow", Rectangle,"black")

    ## click is stored as variable so it can be used to determine where the user is clicking and whether or not they click a buttonhttps://quizlet.com/_c8e2fa?x=1qqt&i=4b06bi
    click = myWin.getMouse()

    ## basically means while the quit button is not clicked, do this
    while not isClicked(quitbtn,click) == True:

        ##click = myWin.getMouse()

        ## when encode button is clicked, undraw things and run encoder
        while isClicked(encodebtn,click) == True:

            ## if user clicks button, the buttons and the text are undrawn
            encodebtn.undraw()
            decodebtn.undraw()
            quitbtn.undraw()
            MSG.undraw()

            background = Rectangle(Point(0,0),Point(600,600))
            background.setFill('white')
            background.draw(myWin)

            ## so the quit button stays (maybe a bit redundant idk)
            quitbtn.draw(myWin)
            btnLabel = Text(quitbtn.getCenter(), "QUIT")
            btnLabel.setFill("black")
            btnLabel.setStyle("bold")
            btnLabel.draw(myWin)

            ## user sent to the encode function
            encoder()
            click = myWin.getMouse()

       ## when decode button is clicked, undraw things and run decoder
        while isClicked(decodebtn,click) == True:

            decodebtn.undraw()
            encodebtn.undraw()
            quitbtn.undraw()
            MSG.undraw()
            background = Rectangle(Point(0,0),Point(600,600))
            background.setFill('white')
            background.draw(myWin)

            ## so the quit button stays
            quitbtn.draw(myWin)
            btnLabel = Text(quitbtn.getCenter(), "QUIT")
            btnLabel.setFill("black")
            btnLabel.setStyle("bold")
            btnLabel.draw(myWin)

            ## theuser sent to decode function
            decoder()
            click = myWin.getMouse()
    else:
        
        myWin.close()

def try_file():
    
    title = Text(Point(300, 100),'ENCODE/DECODE A FILE')
    title.setFace("arial")
    title.setSize(30)
    title.setStyle("bold")
    title.setTextColor("orange")
    title.draw(myWin)

    filename = Entry(Point(300, 220),20)
    filename.setFill("red3")
    filename.setText("ex: test.txt")
    filename.setFace("arial")
    filename.setStyle("bold")
    filename.draw(myWin)

    userkey = Entry(Point(300, 310),7)
    userkey.setFill("red3")
    userkey.setText('')
    userkey.setFace("arial")
    userkey.setStyle("bold")
    userkey.draw(myWin)

    choiceBox = Entry(Point(440, 399),2)
    choiceBox.setFill("red3")
    choiceBox.setText('')
    choiceBox.setFace("arial")
    choiceBox.setStyle("bold")
    choiceBox.draw(myWin)

    filename_msg = Text(Point(300, 175), "Type your file name below:")
    filename_msg.setFace("arial")
    filename_msg.setSize(15)
    filename_msg.setStyle("bold")
    filename_msg.setTextColor("blue")
    filename_msg.draw(myWin)

    key_msg = Text(Point(300, 265), "Type the key below:")
    key_msg.setFace("arial")
    key_msg.setSize(15)
    key_msg.setStyle("bold")
    key_msg.setTextColor("blue")
    key_msg.draw(myWin)

    choice_msg = Text(Point(300, 380),"Do you want your file to be encoded decoded? \n\ntype: E to encode or D to decoded:")
    choice_msg.setFace("arial")
    choice_msg.setSize(15)
    choice_msg.setStyle("bold")
    choice_msg.setTextColor("blue")
    choice_msg.draw(myWin)

    instruct = Text(Point(300, 480),"Click this text to run the cipher and save the result as a file on your computer:")
    instruct.setFace("arial")
    instruct.setSize(15)
    instruct.setStyle("bold")
    instruct.setTextColor("blue")
    instruct.draw(myWin)

    myWin.getMouse()

    ## choice gets the text from entry ans is used to determine whether to decode or encode
    choice1 = choiceBox.getText()

    ## key = text but it needs to be an integer
    textkey = userkey.getText()
    key = int(textkey)

    ## fname is stored as the story the user wants to change using the getText() function
    filenameText = filename.getText()

    with open(filenameText, "r") as MSG:
    
        #the MSG is saved as the entirety of the text file "f.read()"
        contents = MSG.read()

    MSG.close

    #the Encoded and Decoded MSG variables are first established as nothing
    encodedfile = open("encodedfile.txt", "w")

    decodedfile = open("decodedfile.txt", "w")

    ## this was the cause of an issue i had while making this
    #myWin.getMouse()

    ## Empty string that will hold result
    encodedMsg = ''
    decodedMsg = ''

    ## ENCODE
    if choice1 == 'e' or choice1 =='E':

        ## for loop for every character in the text file
        for ch in contents:

            ## Deals with uppercase characters
            if ch.isupper() == True:
                shift = ((ord(ch) - 65 + key) % 26) + 65

                encodedMsg = encodedMsg + (chr(shift))

            ## Deals with lowercase charachters
            elif ch.islower() == True:

                shift = ((ord(ch) - 97 + key) % 26) + 97 

                encodedMsg = encodedMsg + chr(shift)

            ## Deals with any other characters (that arent letters)
            else:

                encodedMsg = encodedMsg + ch

        ## prints the result into the empty file that is submitted with the project
        print(encodedMsg, file=encodedfile)
        encodedfile.close()

    ## DECODE
    elif choice1 == 'e' or choice1 =='E':

        for ch in contents:
        
            ## Deals with uppercase characters
            if ch.isupper():

                shift = ((ord(ch) - 65 - key + 26) % 26) + 65

                decodedMsg = decodedMsg + chr(shift)     

            ## Deals with lowercase charachters
            elif ch.islower():

                shift = ((ord(ch) - 97 - key + 26) % 26) + 97

                decodedMsg = decodedMsg + chr(shift)     

            ## Deals with any other characters (that arent letters)
            else:

                decodedMsg = decodedMsg + ch  

        ## prints the result into the empty file that is submitted with the project
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

    ## text box for encode
    textbox = Entry(Point(300,200), 40)
    textbox.setFace("arial")
    textbox.setSize(15)
    textbox.setFill("sky blue")
    textbox.setStyle("bold")
    textbox.setText('')
    textbox.draw(myWin)

    ## instructions
    instructions = Text(Point(300,150), "Enter the message that you want to encode \nin the text box below.")
    instructions.setFace("arial")
    instructions.setSize(14)
    instructions.setTextColor("sky blue")
    instructions.setStyle("bold")
    instructions.draw(myWin)

    ## entry box that holds key 
    keybox = Entry(Point(300, 300),6)
    keybox.setFace("arial")
    keybox.setSize(15)
    keybox.setFill("sky blue")
    keybox.setStyle("bold")
    keybox.setText('')
    keybox.draw(myWin)

    ## key instructions
    keyinstructions = Text(Point(300,250), "Enter the key that you want to use \nin the text box below.")
    keyinstructions.setFace("arial")
    keyinstructions.setSize(14)
    keyinstructions.setTextColor("sky blue")
    keyinstructions.setStyle("bold")
    keyinstructions.draw(myWin)

    continuee = Text(Point(300, 335),"After entering the information above, click this text to continue.")
    continuee.draw(myWin)

    ## waits for click
    myWin.getMouse()

    ## string with the text that the user inputted for the key
    text_key = keybox.getText()

    ## the key needs to be an integer
    key = int(text_key)
 
    ## grabs text of the message from user
    userMSG = textbox.getText()

    ## empty string that will hold result
    encodedMsg = ''

    ## For loop - runs through characters in message
    for ch in userMSG:

        ## Deals with uppercase characters
        if ch.isupper() == True:
            shift = ((ord(ch) - 65 + key) % 26) + 65

            encodedMsg = encodedMsg + (chr(shift))

        ## Deals with lowercase charachters
        elif ch.islower() == True:

            shift = ((ord(ch) - 97 + key) % 26) + 97 

            encodedMsg = encodedMsg + chr(shift)

        ## Deals with any other characters (that arent letters)
        else:

            encodedMsg = encodedMsg + ch

    continuee.undraw()

    ## entry box that hold the encrypted messgae
    Encoded = Entry(Point(300, 370),20)
    Encoded.setText(encodedMsg)
    Encoded.draw(myWin)
    Encodedresult = Text(Point(300, 340),"Your message has been successfully shifted:")
    Encodedresult.draw(myWin)

    MSG.undraw()

    ## message that prompts user with question
    MenuMSG = Text(Point(300, 400),"Would you like to:")
    MenuMSG.draw(myWin)

    ## create try file button
    point1 = Point(215,420)
    point2 = Point(385,445)
    try_file_btn = drawButton(myWin,point1,point2,"Run program with a .TXT file","red3", Rectangle,"white")

    ## create button for running program again
    point3 = Point(215,455)
    point4 = Point(385,480)
    run_btn = drawButton(myWin,point3,point4,"Run the program again","red3", Rectangle,"white")
    
    click = myWin.getMouse()

    while isClicked(run_btn,click) == True:

        ## if user clicks run button, everything is undrawn and it goes back to home()
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

        ## if user clicks try file button, everything is undrawn and it goes to try_file()
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

    ## title
    MSG= Text(Point(300, 90), 'DECODER')
    MSG.setFace("arial")
    MSG.setSize(27)
    MSG.setStyle("bold")
    MSG.setTextColor("blue3")
    MSG.draw(myWin)

    ## text box for decode
    textbox = Entry(Point(300,200), 40)
    textbox.setFace("arial")
    textbox.setSize(15)
    textbox.setFill("sky blue")
    textbox.setStyle("bold")
    textbox.setText('')
    textbox.draw(myWin)

    ## instructions
    instructions = Text(Point(300,150), "Enter the message that you want to decode \nin the text box below.")
    instructions.setFace("arial")
    instructions.setSize(14)
    instructions.setTextColor("sky blue")
    instructions.setStyle("bold")
    instructions.draw(myWin)

    ## entry box that holds key
    keybox = Entry(Point(300, 300),6)
    keybox.setFace("arial")
    keybox.setSize(15)
    keybox.setFill("sky blue")
    keybox.setStyle("bold")
    keybox.setText('')
    keybox.draw(myWin)

    ## key instructions
    keyinstructions = Text(Point(300,250), "Enter the key that you want use \nin the text box below.")
    keyinstructions.setFace("arial")
    keyinstructions.setSize(14)
    keyinstructions.setTextColor("sky blue")
    keyinstructions.setStyle("bold")
    keyinstructions.draw(myWin)

    continuee = Text(Point(300, 335),"After entering the information above, click this text to continue.")
    continuee.draw(myWin)

    myWin.getMouse()

    ## string with the text that the user inputted for the key
    text_key = keybox.getText()

    ## the key needs to be an integer
    key = int(text_key)
 
    ## grabs text of the message from user
    userMSG = textbox.getText()

    ## empty string that will hold result
    decodedMsg = ''

    ## For loop - runs through characters in message
    for ch in userMSG:

        ## Deals with uppercase characters
        if ch.isupper():

            shift = ((ord(ch) - 65 - key + 26) % 26) + 65

            decodedMsg = decodedMsg + chr(shift)     

        ## Deals with lowercase charachters
        elif ch.islower():

            shift = ((ord(ch) - 97 - key + 26) % 26) + 97

            decodedMsg = decodedMsg + chr(shift)     

        ## Deals with any other characters (that arent letters)
        else:

            decodedMsg = decodedMsg + ch  

    continuee.undraw()

    ## entry box that hold the decrypted messgae
    Decoded = Entry(Point(300, 370),20)
    Decoded.setText(decodedMsg)
    Decoded.draw(myWin)

    Decodedresult = Text(Point(300, 340),"Your message has been successfully:")
    Decodedresult.draw(myWin)

    MSG.undraw()

    ## gives user an option
    MenuMSG = Text(Point(300, 400),"Would you like to:")
    MenuMSG.draw(myWin)

    ## button for trying program with a file
    point1 = Point(215,420)
    point2 = Point(385,445)
    try_file_btn = drawButton(myWin,point1,point2,"Run program with a .TXT file","red3", Rectangle,"white")

    ## create button for running program again
    point3 = Point(215,455)
    point4 = Point(385,480)
    run_btn = drawButton(myWin,point3,point4,"Run the program again","red3", Rectangle,"white")
    
    click = myWin.getMouse()

    while isClicked(run_btn,click) == True:

        ## if user clicks run button, everything is undrawn and it goes back to home()
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

        ## if user clicks try file button, everything is undrawn and it goes to try_file()
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

## Runs program from the beginning
open_screen()
