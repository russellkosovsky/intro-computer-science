#compute a frequency of letters in classlist.txt


def letterFrequency():

    #open file
    infile = open("classlist.txt","r")
    
    #read all contents and convert it to upper
    names = infile.read().upper()

    #create an empty dictionary
    freq = {}

    #iterate all character and add it to dictionary here
    #hint: use membership test, in, to see if a character is already
    #      in the dictionary or not. If yes, increment count. Otherwise
    #      add the character to the dictionary

    #create sequencial data, a list, from dictionary to sort here
    #dictionary has a method, items(), to return all items in it

    
    #close file
    infile.close()



letterFrequency()
