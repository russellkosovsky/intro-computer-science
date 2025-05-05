#compute a frequency of letters in classlist.txt

def getFreq(item):
    return item[1]

def letterFrequency():

    #open file
    infile = open("classlist.txt","r", encoding='utf-8')
    
    #read all contents and convert it to upper
    names = infile.read().upper()

    #create an empty dictionary
    freq = {}

    # iterate all characters and add it to dictionary here
    # hint: use membership test, in, to see if a character is already
    #      in the dictionary or not. If yes, increment count. Otherwise
    #      add the character to the dictionary
    for ch in names:
        #if ch in freq:
            #freq[ch] = freq[ch] + 1
        #else:
            #freq[ch] = 1
        freq[ch] = freq.get(ch, 0) + 1

    #create sequencial data, a list, from dictionary to sort here
    #dictionary has a method, items(), to return all items in it
    freq_list = list(freq.items())
    freq_list.sort(key=getFreq, reverse=True)

    #print out the contents of the list
    for items in freq_list:
        #items.split(",")
        print(items[0] + ' :', items[1])

    #print out the contents of the list nicely as shown in the lab instruction
    freq_list.sort()
    #close file
    infile.close()



letterFrequency()
