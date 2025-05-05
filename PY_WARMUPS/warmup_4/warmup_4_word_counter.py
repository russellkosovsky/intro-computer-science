# This program will count the total number of words (separated by space) in a file

def wordCounter():

    # describe program
    print("This program will count the total number of words (separated by space) in a file (test.txt) ")

    # print new line
    print()

    # open file
    inFile = open('test_copy.txt', 'r')

    # read in all contents of the file
    contents = inFile.read()

    # get the length (number of words) of the file
    numwords = len(contents.split())

    # print result
    print('test.txt has a total of', numwords, 'words')
    
    # close file
    inFile.close()

wordCounter()

