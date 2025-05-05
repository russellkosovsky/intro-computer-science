# c13ex11.py
# A jumble solver using binary search and anagram algorithms
# --------------------------------------------------------
# The dictionary is 'words.txt', a text file with one word 
# per line, all lower case, in alphabetical order. 
# --------------------------------------------------------

def binarySearch(key,searchList):
    # from the text, chapter 13
    # Returns the index in the list at which the key
    # was found or -1 if the key is not found

    low = 0
    high = len(searchList)-1
    while low <= high:
        mid = (low+high)//2
        item = searchList[mid]
        if item == key:
            return mid
        elif key < item:
            high = mid - 1
        else:
            low  = mid + 1
    # completing the loop means a failure to
    # to find the key so return -1
    return -1


def readAndSplit(fname):
    #reads a text file and splits it on white space
    infile = open(fname,"r")
    inText = infile.read()
    infile.close()
    return inText.split()

def anagram(word):
    # from the text, chapter 13
    # Returns a list of all the rearrangements
    # of the parameter
    if len(word) ==1:
        # base case, a single letter
        return [word]
    else:
        answer = []
        for w in anagram(word[1:]):
            for pos in range(len(w)+1):
                answer.append(w[:pos]+word[0]+w[pos:])
        return answer

def remove_dups(lst):
    words = {}
    for w in lst:
        words[w] = True
    return list(words.keys())
        

def main():
    print()
    print("A word scrambler to try out binary search")
    print("Enter a word and I'll check the dictionary for all anagrams")
    print()
    # The dictionary is in the file 'words.txt'
    wordList = readAndSplit("words.txt")

    word = input("What word shall I try to anagram? ")
    word = word.lower()

    potential_anagrams = anagram(word)
    potential_anagrams = remove_dups(potential_anagrams)


    print()
    print("Searching for anagrams in words.txt")
    print("------------------------------------------------------")
    count = 0
    for w in potential_anagrams:
        if binarySearch(w,wordList) > -1:
            print(w)
            count = count + 1
    print()
    print()
    print(count,"anagrams of",word,"were found in 'words.txt'.")
    print()


main()
