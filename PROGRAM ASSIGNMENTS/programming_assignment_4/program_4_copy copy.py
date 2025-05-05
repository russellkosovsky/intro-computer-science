# Program Assignment 4
# Russell Kosovsky

from graphics import *

from random import *

myWin = GraphWin('Word Cloud', 700, 700)
background = Rectangle(Point(0, 0), Point(700, 700))
background.setFill('sky blue')
background.draw(myWin)

def main():
    print_intro()
    use_file()
    process_stopwords()
    remove_junk(stopwords, contents, title, filename, userkey, filename_msg, key_msg, instruct)
    analysis(key, counts)
    end_menu()

# draw myWin and display a nice opening screen with intro and instructions
def print_intro():

    ## welcome text
    welcome = Text(Point(300, 250), "Welcome ")
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
    prompt.move(0,-200)

    ## description about
    about = Text(Point(300, 250), "  ")
    about.setFace("arial")
    about.setSize(15)
    about.draw(myWin)

    ## get mouse click before moving on to description of program
    myWin.getMouse()
    description = Text(Point(300, 350), "This program has the capabilities to... any text file with any key value")
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

    use_file()

# determine what file to use based on users input (on myWin with text/entry objects ect.)
def use_file():
    title = Text(Point(300, 100), 'title')
    title.setFace("arial")
    title.setSize(30)
    title.setStyle("bold")
    title.setTextColor("orange")
    title.draw(myWin)

    filename = Entry(Point(300, 220), 20)
    filename.setFill("red3")
    filename.setText("ex: beemovie.txt")
    filename.setFace("arial")
    filename.setStyle("bold")
    filename.draw(myWin)

    userkey = Entry(Point(300, 310), 7)
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

    instruct = Text(Point(300, 480), "Click this text to :")
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
        # the wholetext is stored as contents by using "text.read()"
        contents = text.read()
    #filenameText.close

    return contents, key, title, filename, userkey, filename_msg, key_msg, instruct

# open stopwords file and use .split so its a list of each stopword
def process_stopwords():

    stopwords = open('stopwords.txt', "r").read()
    stopwords = stopwords.lower()
    stopwords = stopwords.split()

    return stopwords

# remove all the special characters from the file then the split words from users file into a list and loop through it to remove the stopwords
def remove_junk(stopwords, contents, title, filename, userkey, filename_msg, key_msg, instruct):

    # get the sequence of words from the file
    for ch in "!'\"#$%&()*+,-./:;<=>?@[\\]^_{|}~":
        contents = contents.replace(ch, '')
    words = contents.split()

    # create dictionary of word counts
    counts = {}
    for w in words:
        if w not in stopwords:
            counts[w] = counts.get(w, 0) + 1

    title.undraw()
    filename.undraw()
    userkey.undraw()
    filename_msg.undraw()
    key_msg.undraw()
    instruct.undraw()

    return counts

# for formatting (from zelle chapter 11.7.3)
def byFreq(pair):
    return pair[1]

# display formatted analysis of n most frequent words and draw them on myWin randomly
def analysis(key, counts):
    output = Text(Point(300, 400), '')
    output.setFace("arial")
    output.setSize(12)
    output.setStyle("bold")
    output.setTextColor("orange")
    #output.draw(myWin)
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq, reverse=True)
    for i in range(key):
        word, count = items[i]
        print('{0:<15}{1:>5}'.format(word, count))

    output.setText(result)
    output.draw(myWin)

# give option to run program again or exit
#def end_menu():


main()




    





