#the purpose of this module is to take user input (i.e. some sentence)
#then, count all vowels in the entered string
#however, while writing the program many errors were encounted
#plesae fix those errors and explain!


def vowelCounter(text):

    #accumulator
    totalVowels = 0

    #go over each character and see if it is a vowel
    #if so, increment the accumulator by one
    for c in text:
        
        # there was no semicolen
        
        if c in 'aeiou':
            totalVowels = totalVowels + 1

    #print out result
            
    # have to use commas instead of + because its with a str and a variable
    
    print("There are total ", totalVowels,  " vowels.")


def main():

    #print out program intro message
    
    # the ( was not closed
    
    print("This program computes how many vowels in the given string input.")

    #print one blank line
    print()

    #take user input
    userInput = input("Plesae enter some text here: ")
    inputLower = userInput.lower()

    #call vowel counter function
    
    # there was no paremeter for the calling of the function
    # defined text as the users input
    
    vowelCounter(text = inputLower)


main()
