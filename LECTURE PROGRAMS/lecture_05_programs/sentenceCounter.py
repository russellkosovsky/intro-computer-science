#COM110: sentenceCounter.py
#This program count the total number of lines in the file

def sentenceCounter():
    #open file
    inFile = open('shortsentences.txt', 'r')
    
    #read all contents from the file
    contents = inFile.read()

    #split the contents into words
    wordList = contents.split()
    
    #accumulator for number of sentences
    numSentence = 0

    #assume that a sentence is end with a period, '.'
    ###your code here

    for word in wordList:
        if word[-1] == ".":
            numSentence = numSentence + 1
        elif word[-1] == "!":
            numSentence = numSentence + 1
        elif word[-1] == "?":
            numSentence = numSentence + 1



    #print result
    print('shortsentences.txt has', numSentence, 'sentences')
    
    #close file
    inFile.close()

sentenceCounter()
