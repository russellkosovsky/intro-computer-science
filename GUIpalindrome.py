#GUIpalindrome.py
#
#a GUI-based palindrome-checker
# intermediary tasks like smushing and reversing the text
# are also made available as features of the program

from graphics import *

###################### STRING FUNCTIONS ######################

#lowercases then filters out all non-letters in the string s
#returns the resulting string
def smush(s):
    s = s.lower() #lowercase the entire input string
    smushed = ""
    for char in s: #loop through input string one character at a time
        if char >= "a" and  char <= "z": #only if its a letter...
            smushed = smushed + char #...do we add it to the result string
    return smushed

#reverses the letters in the string s and returns the resulting string
def reverse(s):
    revstring = ""
    for char in s: #loop through input string one character at a time
        revstring = char + revstring #add each character to the front of the result string 
    return revstring

#returns True if the string s is a palindrome
#false otherwise

















def isPalindrome(string):
    
    smushed = smush(string) #first smush out extraneous characters
    
    rev_smushed = reverse(smushed) #then reverse the smushed string
    
    if smushed == rev_smushed: #check if it reads the same forward and backward
        return True #if so, yes, it's a palindrome!
    
    else: #if not,
        return False #it's not a palindrome

    

############################# GUI STUFF ############################
    
#in the GraphWin object gwin, this function draws
#a blue rectangular button with corners at Point objects pt1 and pt2
#then labels the button with the string variable words
def drawButton(gwin, pt1, pt2, words):

    button = Rectangle(pt1, pt2)
    button.setFill("blue3")
    button.draw(gwin)

    #find the x and y coords of the middle of the button
    labelx = (pt1.getX() + pt2.getX())/2.0 
    labely = (pt1.getY() + pt2.getY())/2.0

    #use these coords for the position of the label
    label = Text(Point(labelx,labely),words)
    label.setFill("white")
    label.draw(gwin)
    
def main():
    win = GraphWin("String Manipulation", 600, 600)

    #Entry object for user input
    inputBox = Entry(Point(300,200),50) 
    inputBox.draw(win)

    drawButton(win, Point(100,300), Point(200,350), "Lower Case!")
    drawButton(win, Point(250,300), Point(350,350), "Smush!")
    drawButton(win, Point(400,300), Point(500,350), "Reverse!")
    drawButton(win, Point(200,400), Point(400,450), "Palindrome?")
    
    prompt = Text(Point(300,100),"Enter some text, then click a button.")
    prompt.draw(win)

    #Text object for output
    display = Text(Point(300, 500),"") 
    display.draw(win)
    
    #wait for user to enter something and then click the mouse
    pt = win.getMouse()
    #take the text that the user has (hopefully) inputted
    userPhrase = inputBox.getText()

    #set default output in case user didn't click on a button at all
    output = "You didn't click a button!"
    
    #check if mouse click was on a button
    if pt.getY() >= 300 and pt.getY() <= 350:
        if pt.getX() >= 100 and pt.getX() <= 200:   #Lower Case button was clicked
            output = userPhrase.lower()          
        elif pt.getX() >= 250 and pt.getX() <= 350: #Smush button was clicked
            output = smush(userPhrase)
        elif pt.getX() >= 400 and pt.getX() <= 500: #Reverse button
            output = reverse(userPhrase)
    #if Palindrome button was clicked
    elif pt.getY() >=400 and pt.getY() <=450 and pt.getX() >=200 and pt.getX() <=400:
        if isPalindrome(userPhrase):
            output = "That's a Palindrome!"
        else:
            output = "That's not a Palindrome."

    display.setText(output)
    display.setFill("purple3")
    display.setStyle("bold")

    prompt.setText("Click anywhere to close.  Have a nice day!")
    prompt.setFill("red")

    #take another mouse click
    pt = win.getMouse()
    win.close()

main()
