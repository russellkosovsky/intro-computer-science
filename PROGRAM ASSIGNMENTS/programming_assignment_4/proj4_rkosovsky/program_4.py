# Program Assignment 4
# Russell Kosovsky

from graphics import *
from random import *


# create window
myWin = GraphWin('Word Cloud', 700, 700)
background = Rectangle(Point(0, 0), Point(700, 700))
background.setFill('black')
background.draw(myWin)



def print_intro():
# display a nice opening screen with intro and instructions

    # welcome text
    welcome = Text(Point(180, 120), "Welcome to the word cloud")
    welcome.setFace("arial")
    welcome.setSize(25)
    welcome.setTextColor("white")
    welcome.setStyle("bold")
    welcome.draw(myWin)

    # instructions
    prompt = Text(Point(115, 160), "Instructions: Click the screen to continue")
    prompt.setFace("arial")
    prompt.setSize(10)
    prompt.setTextColor("orange")
    prompt.setStyle("bold")
    prompt.draw(myWin)
    myWin.getMouse()
    welcome.undraw()
    prompt.setTextColor("white")
    prompt.setFace("courier")
    prompt.move(235, 180)
    background.setFill("green")

    # description about program
    about = Text(Point(350, 300), "This is a program built to examine a text file in order to determine the most frequently used words. "
                                  "\nThen the words are shown on the screen as s word cloud. You can also choose how many words to display")
    about.setFace("courier")
    about.setSize(10)
    about.setTextColor("white")
    about.setStyle("bold")
    about.draw(myWin)

    # get mouse click before moving on to send off
    myWin.getMouse()
    prompt.undraw()
    about.undraw()
    background.setFill("blue")
    sendoff = Text(Point(350, 120), "Thank you for trying out this program! \nClick the screen one more time to begin.")
    sendoff.setFace("arial")
    sendoff.setSize(22)
    sendoff.setStyle("bold")
    sendoff.setTextColor("orange")
    sendoff.draw(myWin)

    # undraw everything
    myWin.getMouse()
    sendoff.undraw()
    about.undraw()
    prompt.undraw()
    background.setFill("purple")




# determine what file to use based on users input
def use_file():
    title = Text(Point(350, 100), 'Choose a File')
    title.setFace("arial")
    title.setSize(30)
    title.setStyle("bold")
    title.setTextColor("black")
    title.draw(myWin)

    filename = Entry(Point(350, 220), 20)
    filename.setFill("black")
    filename.setText("ex: beemovie.txt")
    filename.setTextColor("white")
    filename.setFace("arial")
    filename.setStyle("bold")
    filename.draw(myWin)

    userkey = Entry(Point(350, 310), 7)
    userkey.setFill("black")
    userkey.setText('')
    userkey.setTextColor("white")
    userkey.setFace("arial")
    userkey.setStyle("bold")
    userkey.draw(myWin)

    filename_msg = Text(Point(350, 175), "Type your file name below:")
    filename_msg.setFace("arial")
    filename_msg.setSize(15)
    filename_msg.setStyle("bold")
    filename_msg.setTextColor("white")
    filename_msg.draw(myWin)

    key_msg = Text(Point(350, 265), "Type the number of frequent words you want to find below:")
    key_msg.setFace("arial")
    key_msg.setSize(15)
    key_msg.setStyle("bold")
    key_msg.setTextColor("white")
    key_msg.draw(myWin)

    instruct = Text(Point(350, 480), "Click this text to analyze")
    instruct.setFace("arial")
    instruct.setSize(15)
    instruct.setStyle("bold")
    instruct.setTextColor("orange")
    instruct.draw(myWin)


    myWin.getMouse()

    title.undraw()
    filename.undraw()
    userkey.undraw()
    filename_msg.undraw()
    key_msg.undraw()
    instruct.undraw()
    background.setFill("grey")

    # key = text but it needs to be an integer
    keytext = userkey.getText()
    key = int(keytext)

    # filenameText stores the story the user wants to analize using the getText() function
    filenametext = filename.getText()

    with open(filenametext, "r") as text:
        # the wholetext is stored as contents by using "text.read()"
        contents = text.read()
        contents = contents.lower()

    return contents, key



# for formatting (from zelle chapter 11.7.3)
def byfreq(pair):
    return pair[1]



def remove_junk(contents, key):
# remove all the special characters from the file then the split words from users file into a list and loop
# through it to remove the stopwords then display an analysis of the most frequent words
# get the sequence of words from the file

    for ch in "!'\"#$%&()*+,-./:;<=>?@[\\]^_{|}~":
        contents = contents.replace(ch, '')
    words = contents.split()
    stopwords = open('stopwords.txt', "r").read()
    stopwords = stopwords.lower()
    stopwords = stopwords.split()

    # create dictionary of word counts
    counts = {}
    for w in words:
        if str(w) not in stopwords:
            counts[w] = counts.get(w, 0) + 1

    items = list(counts.items())
    items.sort()
    items.sort(key=byfreq, reverse=True)

    label = Text(Point(180, 40), 'Most frequent words and the number of their occurrences')
    label.setFace("arial")
    label.setStyle("bold")
    label.setSize(12)
    label.setTextColor("red3")
    label.draw(myWin)

    output = Text(Point(500, 350), '')
    output.setFace("arial")
    output.setSize(19)
    output.setStyle("bold")

    continuemsg = Text(Point(165, 60), "Instructions: Click the screen to display the word cloud\n Then click the screen again when you are ready to continue")
    continuemsg.setFace("arial")
    continuemsg.setSize(11)
    continuemsg.setStyle("bold")
    continuemsg.setTextColor("black")
    continuemsg.draw(myWin)

    anal = ''
    newline = '\n'
    for i in range(key):
        word, count = items[i]
        result = '{0:<15}{1:>5}'.format(word, count)
        anal = anal + result + newline

    output.setText(anal)
    output.setTextColor(color_rgb(randint(0,255),randint(0,255),randint(0,255)))
    output.draw(myWin)
    myWin.getMouse()
    continuemsg.undraw()
    label.undraw()
    output.undraw()
    background.setFill("white")
    anal_list = anal.split()

    frequent_words = []
    for words in anal_list:
        frequent_words.append(words)

    for i in range(key):
        frequent_words.remove(frequent_words[i+1])

    return frequent_words



def wordcloud(frequent_words):
# display formatted analysis of n most frequent words and draw them on myWin randomly

    for i in frequent_words:
        word = Text(Point(randint(50,650), randint(50,650)), i)
        word.setSize(randint(5,56))
        word.setStyle('bold')
        word.setTextColor(color_rgb(randint(0,255),randint(0,255),randint(0,255)))
        word.draw(myWin)

    myWin.getMouse()
    #myWin.close()



def end_menu():
# give option to run program again or exit the progfram

    newWin = GraphWin('Word Cloud', 700, 700)
    background = Rectangle(Point(0, 0), Point(700, 700))
    background.setFill('sky blue')
    background.draw(newWin)

    choice_msg = Text(Point(350, 100),"Do you want to run this program again? \n\nType: Y to jump to the beginning or type N to finish up:")
    choice_msg.setFace("arial")
    choice_msg.setSize(15)
    choice_msg.setStyle("bold")
    choice_msg.setTextColor("red")
    choice_msg.draw(newWin)

    choiceBox = Entry(Point(350, 150), 2)
    choiceBox.setFill("red3")
    choiceBox.setText('')
    choiceBox.setFace("arial")
    choiceBox.setStyle("bold")
    choiceBox.draw(newWin)

    exit_message = Text(Point(350, 350), 'Thank you for trying my program!\n Click the screen to close program.\n Have a wonderful day :)')
    exit_message.setSize(20)
    exit_message.setStyle("bold")
    exit_message.setTextColor("blue3")

    instructions = Text(Point(350, 350),'Click the screen to once you type your response')
    instructions.setSize(12)
    instructions.setStyle("bold")
    instructions.draw(newWin)
    newWin.getMouse()
    instructions.undraw()
    choiceBox.undraw()

    # choice gets the text from entry
    choice = choiceBox.getText()

    if choice == 'y' or choice == 'Y':
        newWin.close()
        background = Rectangle(Point(0, 0), Point(700, 700))
        background.setFill('black')
        background.draw(myWin)
        main()

    elif choice == 'n' or choice =='N':
        choice_msg.undraw()
        exit_message.draw(newWin)
        newWin.getMouse()
        myWin.close()
        newWin.close()



# basically same as main ... used to start program over
def repeat():
    print_intro()
    contents, key = use_file()
    frequent_words = remove_junk(contents, key)
    wordcloud(frequent_words)
    end_menu()



# runs all functions
def main():
    print_intro()
    contents, key = use_file()
    frequent_words = remove_junk(contents, key)
    wordcloud(frequent_words)
    end_menu()



main()






















