
# file: program_2.py
# This program will calculate the average length of the words in a text 
# Author: Russell Kosovsky (rkosovsky@conncoll.edu)

# Intro to the program
print("This program analizes the two texts, The Call of The Wild, and The Great Gatsby. This tool has several functions such as displaying descriptions of the books, "
      "figuring word count, figuring the number of sentences, the average length of the sentences, and searching for the occurrence and of and analyzing a word.")     

# open text files for the books    
callofwild = open("The_Call_of_the_Wild.txt", "r", encoding="utf-8")
gatsby = open("The_Great_Gatsby.txt", "r", encoding="utf-8")

# define variables for contents, words, and sentences for call of thewild
callofwild_contents = callofwild.read().lower()
callofwild_words = callofwild_contents.split()

ch_count = 0

for ch in callofwild_contents:
        ch_count += 1

#print(ch_count)

callofwild_sentences = 0

# loop to calcxulate the number of sentences
for word in callofwild_words:
    if word[-1] == ".":
        callofwild_sentences = callofwild_sentences + 1
    elif word[-1] == "!":
        callofwild_sentences = callofwild_sentences + 1
    elif word[-1] == "?":
        callofwild_sentences = callofwild_sentences + 1

# define variables for contents, words, and sentences for the great gatsby
gatsby_contents = gatsby.read().lower()
gatsby_words = gatsby_contents.split()

gatsby_sentences = 0

# loop to calcxulate the number of sentences
for word in gatsby_words:
    if word[-1] == ".":
        gatsby_sentences = gatsby_sentences + 1
    elif word[-1] == "!":
        gatsby_sentences = gatsby_sentences + 1
    elif word[-1] == "?":
        gatsby_sentences = gatsby_sentences + 1

# close BOTH files
callofwild.close()
gatsby.close()

# function for the first choice (book descriptions)
def choicea():

    # option menu that the user can choose from
    choice1 = input("Would you like to \n(A) Print a description of The Great Gatsby \n(B) Print a description of The Call of The Wild \n(C) Print a description for both texts\n")

    # source: https://en.wikipedia.org/wiki/The_Great_Gatsby
    # conditional because the user had 3 options
    if choice1 == "a" or choice1 == "A":

        # gatsby description
        print("The Great Gatsby is a 1925 novel by American writer F. Scott Fitzgerald. Set in the Jazz Age on Long Island, near New York City, the novel depicts first-person "
              "narrator Nick Carraway's interactions with mysterious millionaire Jay Gatsby and Gatsby's obsession to reunite with his former lover, Daisy Buchanan.")

        # ask user if they want to use program again
        areturn = input("Would you like to return to the first menu and use another tool? (yes or no) ")

        if areturn == "yes" or areturn == "Yes":
            # goes back to the main() and runs it
            return main()
        else:
            # end messsage
            print("Ok, thanks for using my program!")

    # source: https://en.wikipedia.org/wiki/The_Call_of_the_Wild
    # conditional because the user had 3 options
    elif choice1 == "b" or choice1 == "B":
        # call of the wild description
        print("The Call of the Wild is a short adventure novel by Jack London, published in 1903 and set in Yukon, Canada, during the 1890s Klondike Gold Rush, when strong sled dogs were "
              "in high demand. The central character of the novel is a dog named Buck. The story opens at a ranch in Santa Clara Valley, California, when Buck is stolen from his home and "
              "sold into service as a sled dog in Alaska. He becomes progressively more primitive and wild in the harsh environment, where he is forced to fight to survive and dominate "
              "other dogs. By the end, he sheds the veneer of civilization, and relies on primordial instinct and learned experience to emerge as a leader in the wild.")

        # ask user if they want to use program again
        areturn = input("Would you like to return to the first menu and use another tool? (yes or no) ")

        if areturn == "yes" or areturn == "Yes":
            return main()
        else:
            print("Ok, thanks for using my program!")

    elif choice1 == "c" or choice1 == "C":

        # new line
        print()
        # gatsby description
        print("The Great Gatsby is a 1925 novel by American writer F. Scott Fitzgerald. Set in the Jazz Age on Long Island, near New York City, the novel depicts first-person "
              "narrator Nick Carraway's interactions with mysterious millionaire Jay Gatsby and Gatsby's obsession to reunite with his former lover, Daisy Buchanan.")

        # new line
        print()
        # call of the wild description
        print("The Call of the Wild is a short adventure novel by Jack London, published in 1903 and set in Yukon, Canada, during the 1890s Klondike Gold Rush, when strong sled dogs were "
              "in high demand. The central character of the novel is a dog named Buck. The story opens at a ranch in Santa Clara Valley, California, when Buck is stolen from his home and "
              "sold into service as a sled dog in Alaska. He becomes progressively more primitive and wild in the harsh environment, where he is forced to fight to survive and dominate "
              "other dogs. By the end, he sheds the veneer of civilization, and relies on primordial instinct and learned experience to emerge as a leader in the wild.")

        # ask user if they want to use program again
        areturn = input("Would you like to return to the first menu and use another tool? (yes or no) ")

        if areturn == "yes" or areturn == "Yes":
            return main()
        else:
            print("Ok, thanks for using my program!")

# function for number of words
def choiceb():
    # option menu for choice b
    choice2 = input("Would you like to \n(A) Find the word count for The Great Gatsby \n(B) Find the word count for The Call of The Wild \n(C) Find the word count for both texts\n")

    # conditional that prints how many words the great gatsby has when the user chooses a
    if choice2 == "a" or choice2 == "A":
        print("The Great Gatsby has",len(gatsby_words),"words.")

        # ask user if they want to use program again
        breturn = input("Would you like to return to the first menu and use another tool? (yes or no) ")

        if breturn == "yes" or breturn == "Yes":
            return main()
        else:
            print("Ok, thanks for using my program!")

    # conditional that prints how many words the call of the wild has when the user chooses b
    elif choice2 == "b" or choice2 == "B":                                   
        print("The Call of The Wild has",len(callofwild_words),"words.")

        # ask user if they want to use program again
        breturn = input("Would you like to return to the first menu and use another tool? ")

        if breturn == "yes" or breturn == "Yes":
            return main()
        else:
            print("Ok, thanks for using my program!")

    # conditional that prints how many words both texts have when the user chooses c
    elif choice2 == "c" or choice2 == "C":                                     
        print("The Great Gatsby has",len(gatsby_words),"words.")
        print("The Call of The Wild has",len(callofwild_words),"words.")

        # ask user if they want to use program again
        breturn = input("Would you like to return to the first menu and use another tool? (yes or no) ")

        if breturn == "yes" or breturn == "Yes":
            return main()
        else:
            print("Ok, thanks for using my program!")

# function for number of sentences
def choicec():    

    # option menu asking user which book to look at when finding number of sentences
    choice3 = input("Would you like to \n(A) Find the number of sentences in The Great Gatsby \n(B) Find the number of sentences in The Call of The Wild \n(C) Find number of sentences in both texts\n")

    # conditional that prints the number of sentences in the great gatsby
    if choice3 == "a" or choice3 == "A":
        print("The Great Gatsby has", (gatsby_sentences), "sentences.")

        # ask user if they want to use program again
        creturn = input("Would you like to return to the first menu and use another tool? (yes or no) ")

        if creturn == "yes" or creturn == "Yes":
            return main()
        else:
            print("Ok, thanks for using my program!")

    # conditional that prints the number of sentences in the call of the wild
    elif choice3 == "b" or choice3 == "B":                                   
        print("The Call of The Wild has", (callofwild_sentences), "sentences.")

        # ask user if they want to use program again
        creturn = input("Would you like to return to the first menu and use another tool? (yes or no) ")

        if creturn == "yes" or creturn == "Yes":
            return main()
        else:
            print("Ok, thanks for using my program!")

    # conditional that prints the number of sentences in both texts
    elif choice3 == "c" or choice3 == "C":                                     
        print("The Great Gatsby has", (gatsby_sentences), "sentences.")
        print("The Call of The Wild has", (callofwild_sentences), "sentences.")

        # ask user if they want to use program again
        creturn = input("Would you like to return to the first menu and use another tool? (yes or no) ")

        if creturn == "yes" or creturn == "Yes":
            return main()
        else:
            print("Ok, thanks for using my program!")

# function for word occurances
def choiced():
    # option menu asking user which option they would like to choose
    choice4 = input("Would you like to \n(A) Find the number of occurences of a word in The Great Gatsby \n(B) Find the number of occurences of a word in The Call of The Wild \n(C) Compare "
                    "the number of occurences of a word in both texts\n")

    # conditional for option a
    if choice4 == "a" or choice4 == "A":

        # ask user for a word
        userword = input("What word would you like to search? ")

        # variable that stores the number (.count) of occurances of the user specified word
        gatsby_search = gatsby_contents.count(userword)

        # print number of word occurances
        print(userword.capitalize(), "appears in The Great Gatsby,", gatsby_search, "times.")

        # ask user if they want to use program again
        dreturn = input("Would you like to return to the first menu and use another tool? (yes or no) ")
        
        if dreturn == "yes" or dreturn == "Yes":
            return main()
        else:
            print("Ok, thanks for using my program!")

    elif choice4 == "b" or choice4 == "B":

        # ask user for a word
        userword = input("What word would you like to search? ")

        # variable that stores the number (.count) of occurances of the user specified word
        callofwild_search = callofwild_contents.count(userword)

        # print number of word occurances
        print(userword.capitalize(), "appears in The Call of The Wild,", callofwild_search, "times.")

        # ask user if they want to use program again
        dreturn = input("Would you like to return to the first menu and use another tool? (yes or no) ")
        
        if dreturn == "yes" or dreturn == "Yes":
            return main()
        else:
            print("Ok, thanks for using my program!")

    elif choice4 == "c" or choice4 == "C":

        # ask user for a word
        userword = input("What word would you like to search? ")

        # variable that stores the number (.count) of occurances of the user specified word in the great gatsby
        gatsby_search = gatsby_contents.count(userword)

        # variable that stores the number (.count) of occurances of the user specified word in callofwild
        callofwild_search = callofwild_contents.count(userword)

        # conditional that figures which book has more occurances of the user specified word
        if gatsby_search > callofwild_search:
            print("The Great Gatsby uses the word:",userword.upper(),"more frequently than The Call of The Wild.")
        elif gatsby_search < callofwild_search:
            print("The Call of The Wild uses the word:",userword.upper(),"more frequently than The Great Gatsby.")
        else:
            print("Both books use the word:", userword,"the same ammount of times.")

        print("The word:",userword.upper(), "appears in The Great Gatsby,", gatsby_search, "times.")

        print("The word:",userword.upper(), "appears in The Call of The Wild,", callofwild_search, "times.")

        # ask user if they want to use program again
        dreturn = input("Would you like to return to the first menu and use another tool? (yes or no) ")
        
        if dreturn == "yes" or dreturn == "Yes":
            return main()
        else:
            print("Ok, thanks for using my program!")

# function for average number of words per sentence
def choicee():

    # option menu for number of words per sentence
    choice5 = input("Would you like to \n(A) Find the average number of words per sentence in The Great Gatsby \n(B) Find the average number of words per sentence in The Call of The Wild \n(C) "
                    "Compare the number of words per sentence in both texts\n")

    if choice5 == "a" or choice5 == "A":

        # average number of words per sentence (# of words / # of sentences)
        gatsby_avrg = len(gatsby_words) / gatsby_sentences

        print("The Great Gatsby has an average of", round(gatsby_avrg), "words per sentence.")

        # ask user if they want to use program again
        ereturn = input("Would you like to return to the first menu and use another tool? (yes or no) ")
        
        if ereturn == "yes" or ereturn == "Yes":
            return main()
        else:
            print("Ok, thanks for using my program!")

    elif choice5 == "b" or choice5 == "B":

        # average number of words per sentence (# of words / # of sentences)
        callofwild_avrg = len(callofwild_words) / callofwild_sentences
        
        print("The Call of The Wild has an average of",round(callofwild_avrg) , "words per sentence.")

        # ask user if they want to use program again
        ereturn = input("Would you like to return to the first menu and use another tool? (yes or no) ")
        
        if ereturn == "yes" or ereturn == "Yes":
            return main()
        else:
            print("Ok, thanks for using my program!")

    elif choice5 == "c" or choice5 == "C":

        # average number of words per sentence (# of words / # of sentences)
        gatsby_avrg = len(gatsby_words) / gatsby_sentences
        callofwild_avrg = len(callofwild_words) / callofwild_sentences

        # results
        print("The Great Gatsby has an average of", round(gatsby_avrg), "words per sentence.")
        print("The Call of The Wild has an average of", round(callofwild_avrg) , "words per sentence.")

        # conditional to fugure which book has a higher average
        if gatsby_avrg > callofwild_avrg:
            print("The Great Gatsby on average has longer sentences than The Call of The Wild.")
            
        elif gatsby_avrg < callofwild_avrg:
            print("The Call of The Wild on average has longer sentences than The Great Gatsby.")
            
        else:
            print("Both books have the same number of words per sentence.")

        # ask user if they want to use program again
        ereturn = input("Would you like to return to the first menu and use another tool? (yes or no) ")
        
        if ereturn == "yes" or ereturn == "Yes":
            return main()
        else:
            print("Ok, thanks for using my program!")

# define main function       
def main():
    
    # option menu
    choice = input("Are you interested in: \n(A) Displaying a book description \n(B) Finding the word count \n(C) Finding the number of sentences \n(D) Searching and analyzing a word "
                   "occurrence \n(E) Find the average number of words per sentence \n")

    # conditional that takes the users choice and figures out which function to run
    if choice == "a" or choice == "A":
        choicea()
    elif choice == "b" or choice == "B":
        choiceb()
    elif choice == "c" or choice == "C":
        choicec()
    elif choice == "d" or choice == "D":
        choiced()
    elif choice == "e" or choice == "E":
        choicee()

# run main function
main()









