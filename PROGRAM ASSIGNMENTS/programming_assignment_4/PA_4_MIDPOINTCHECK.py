# Program Assignment 4
# Russell Kosovsky

from graphics import *

from random import *

def check():

    myWin = GraphWin("Word Cloud", 700, 700)

    wordlist = ['Hello', 'words', 'banana', 'love', 'bug', 'code', 'star', 'red', 'cow', 'blast']

    for words in wordlist:
        print(words)
        word = Text(Point(randint(0,701), randint(0,701)), words)
        word.setSize(randint(5,56))
        word.setTextColor(color_rgb(randint(0,256),randint(0,256),randint(0,256)))
        word.draw(myWin)

    myWin.getMouse()
    myWin.close()

def byFreq(pair):
    return pair[1]

def main():

    print('This program analyzes wor frequency in a file')
    print('and prints a report on the n most frequent words.\n')

    # get the sequence of words from the file
    fname = input("file to analyze: ")
    text = open(fname,'r').read()
    text = text.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        text = text.replace(ch, '')
    words = text.split()

    # create dictionary of word counts
    counts = {}
    for w in words:
        counts[w] = counts.get(w,0) + 1

    # output analysis of n most frequent words
    n = eval(input('Output analysis of how many words? '))
    items = list(counts.items())
    items.sort()
    items.sort(key=byFreq, reverse=True)
    for i in range(n):
        word, count = items[i]
        print("{0:<15}{1:>5}".format(word,count))

if __name__ == '__main__': main()

check()













