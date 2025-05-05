# Thought process 4/2


###

# We need the words which will come from a text.

# Your program can start with reading the text file. [done]
# We need a GUI (graphical user interface) with two text-boxes.
#   # One of the text boxes would let you enter the file name
    # The other text box would have the word count.
# Split the text into words [done]
# Get rid of the common words (aka stop words) [done]
# Get rid of the '.!/?!' [done]
# Check how mony times the word occurs in the text. [done]
# Sort them by descending frequency [done]
# ('dream', 40), ('pencil', 20) ...
# In GUI, display these words.

from graphics import *

def byFreq(pair):
    return pair[1]

def main():

    win = GraphWin("Entry", 800, 800)
    win.setBackground("white")
 
    file = Entry(Point(400,300), 30)
    label1 = Text(Point(400,250), "Type file")
    label1.draw(win)
    file.draw(win)


    num = Entry(Point(400,500), 30)
    label2 = Text(Point(400,450), input("Enter the number of words you'd like to display"))
    label2.draw(win)
    num.draw(win)

    

    pt = win.getMouse()
    text_entry = file.getText()

    if text_entry != "dream.txt":
        text_entry = file.getText()
        file.setText("Wrong file, type again")
        pt = win.getMouse()
    else:
        print(text_entry)

    win = GraphWin("wordcloud", 800, 800)
    window.setBackground("white")

    file = open(text_entry, "r")
    dreamText = file.read().lower()
    

    for ch in '!"#$%&0*+,-./:;<=>?<Q[\\]-_':
        dreamText = dreamText.replace(ch, "")

    dreamWords = dreamText.split()

    stopWordsFile = open("stopwords.txt","r")
    stopWords = stopWordsFile.read().lower().split()

   
    counts = {}
    for w in dreamWords:
        if w not in stopWords:
            counts[w] = counts.get(w,0) + 1

    wordFreqs = list(counts.items())
    wordFreqs.sort(key=byFreq, reverse = True)
    
    print(wordFreqs)



    num_words = eval(num.getText())
    
    words_to_show = []
    start = 0
    for i in range(num_words):
        words_to_show.append(wordFreqs[start])
        start = start + 1

    print(words_to_show)

    for word in words_to_show:
        w = word[0]
        print(w)

    wordcloud = []

    
    




main()
