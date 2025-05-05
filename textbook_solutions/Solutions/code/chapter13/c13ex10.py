# c13ex10.py
# spell checker using binary search
# ------------------------------------------------
# words.txt is a text file with one word per line,
# all lower case, in alphabetical order. 

def binarySearch(key,searchList):
    # from the text, chapter 13
    # return the index in the list of the key or -1
    # if the key is not found
    low = 0
    high = len(searchList)-1

    while low <=high:
        mid = (low+high)//2
        item = searchList[mid]
        if item == key:
            return mid
        elif key < item:
            high = mid - 1
        else:
            low  = mid + 1

    # completing the loop means a failure to
    # to find the key
    return -1


def readAndSplit(fname):
    # opens a text file and splits it on white space
    infile = open(fname,"r")
    inText = infile.read()
    infile.close()
    return inText.split()

def lettersOnly(word):
    #strips all non-letters from a word
    answer = ""
    for x in word:
        if x.isalpha():
            answer = answer + x
    return answer

def main():
    print()
    print("A spell checcker to try out binary search")
    print()
    
    wordList = readAndSplit("words.txt")

    targetfile = input("What text file shall I spell check? ")
    text = readAndSplit(targetfile)

    print()
    print("The following words were not found in the dictionary:")
    print("------------------------------------------------------")
    
    
    for w in text:
        w2 = lettersOnly(w).lower()
        if w != "" and binarySearch(w2,wordList) == -1:
            print(w2+",", end=' ')
    print()
    print()
    print("Spell Check Complete")
    print()


main()
