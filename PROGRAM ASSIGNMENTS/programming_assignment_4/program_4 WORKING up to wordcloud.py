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
    contents, key = use_file()
    frequent_words = remove_junk(contents, key)
    wordcloud(frequent_words)
    # end_menu()


def print_intro():
    # draw myWin and display a nice opening screen with intro and instructions

    # welcome text
    welcome = Text(Point(300, 250), "Welcome ")
    welcome.setFace("arial")
    welcome.setSize(25)
    welcome.setTextColor("black")
    welcome.setStyle("bold")
    welcome.draw(myWin)

    # instructions
    prompt = Text(Point(300, 300), "Instructions: Click the screen to continue")
    prompt.setFace("arial")
    prompt.setSize(20)
    prompt.setTextColor("orange")
    prompt.setStyle("bold")
    prompt.draw(myWin)
    myWin.getMouse()
    welcome.undraw()
    prompt.move(0, -200)

    # description about
    about = Text(Point(300, 250), "  ")
    about.setFace("arial")
    about.setSize(15)
    about.draw(myWin)

    # get mouse click before moving on to description of program
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

    # undraw everything and send user to home screen
    myWin.getMouse()
    sendoff.undraw()
    description.undraw()
    about.undraw()
    prompt.undraw()

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

    title.undraw()
    filename.undraw()
    userkey.undraw()
    filename_msg.undraw()
    key_msg.undraw()
    instruct.undraw()

    # key = text but it needs to be an integer
    keytext = userkey.getText()
    key = int(keytext)

    # filenameText stores the story the user wants to analize using the getText() function
    filenametext = filename.getText()

    with open(filenametext, "r") as text:
        # the wholetext is stored as contents by using "text.read()"
        contents = text.read()
    # filenameText.close

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

    with open('stopwords.txt', "r") as stopword_file:
        stopwords = stopword_file.read()
        stopwords = stopwords.split()

    # create dictionary of word counts
    counts = {}
    for w in words:
        if w not in stopwords:
            counts[w] = counts.get(w, 0) + 1

    items = list(counts.items())
    items.sort()
    items.sort(key=byfreq, reverse=True)

    output = Text(Point(350, 400), '')
    output.setFace("arial")
    output.setSize(22)
    output.setStyle("bold")
    output.setTextColor("orange")
    anal = ''
    newline = '\n'
    for i in range(key):
        word, count = items[i]
        result = '{0:<15}{1:>5}'.format(word, count)
        print('{0:<15}{1:>5}'.format(word, count))
        anal = anal + result + newline
    output.setText(anal)
    output.draw(myWin)
    myWin.getMouse()
    output.undraw()
    anal_list = anal.split()
    frequent_words = []
    for words in anal_list:
        frequent_words.append(words)

    print(frequent_words)

    frequent_words.remove(frequent_words[1])
    frequent_words.remove(frequent_words[2])
    frequent_words.remove(frequent_words[3])
    frequent_words.remove(frequent_words[4])
    frequent_words.remove(frequent_words[5])
    frequent_words.remove(frequent_words[6])
    frequent_words.remove(frequent_words[7])
    frequent_words.remove(frequent_words[8])
    frequent_words.remove(frequent_words[9])
    frequent_words.remove(frequent_words[10])
    print(frequent_words)

    return frequent_words

# display formatted analysis of n most frequent words and draw them on myWin randomly
def wordcloud(frequent_words):

    for i in frequent_words:
        print(i)
        word = Text(Point(randint(0,701), randint(0,701)), i)
        word.setSize(randint(5,56))
        word.setTextColor(color_rgb(randint(0,256),randint(0,256),randint(0,256)))
        word.draw(myWin)

    myWin.getMouse()

# give option to run program again or exit
#def end_menu():

main()
