# COM110: vowelCounter.py
# This program count the number of vowel occurrence in the file

def vowelCounter():

    # open file
    inFile = open('test_copy.txt', 'r')

    # read in all contents of the file (made it lowercase for ease) 
    contents = inFile.read().lower()

    
    # variable to store total number of vowels
    numvowel = 0

    # count total occurances of vowel o or O
    # use conditional instead of count function

    for ch in contents:

        if ch == "o":
            numvowel = numvowel + 1
        elif ch == "e":
            numvowel = numvowel + 1
        elif ch == "i":
            numvowel = numvowel + 1

    # print result
    print('test_copy.txt has', numvowel,'I, E, and O vowel occurence')

    # figure which vowel occurs the most
    osearch = contents.count("o")
    
    esearch = contents.count("e")

    isearch = contents.count("i")
    
    # Conditional that compares the number of vowel occurences. Probably not the most efficient way but it works.
    if osearch > esearch and osearch > isearch:
        print("The vowel, O, occurs the most")
    elif esearch > osearch and esearch > isearch:
        print("The vowel, E, occurs the most")
    else:
        print("The vowel, I, occurs the most")
    
    # close file
    inFile.close()

vowelCounter()
