# COM110: vowelCounter.py
# This program count the number of vowel occurrence in the file

def vowelCounter():

    # open file
    inFile = open('test.txt', 'r')

    # read in all contents of the file
    contents = inFile.read()

    
    # variable to store total number of vowels
    numvowel = 0

    # count total occurances of vowel o or O
    # use conditional instead of count function

    for ch in contents:

        if ch == "o" or ch == "O":
            numvowel = numvowel + 1
        elif ch == "a" or ch == "A":
            numvowel = numvowel + 1
        elif ch == "e" or ch == "E":
            numvowel = numvowel + 1
        elif ch == "i" or ch == "I":
            numvowel = numvowel + 1
        elif ch == "u" or ch == "U":
            numvowel = numvowel + 1

    # print result
    print('test.txt has', numvowel,'vowel occurence')

    # figure which vowel occurs the most
    
    
    # close file
    inFile.close()

vowelCounter()
