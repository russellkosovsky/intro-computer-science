#the purpose of this module is to take user input (i.e. some sentence)
#then, count all vowels in the entered string
#however, while writing the program many errors were encounted
#plesae fix those errors and explain!


#print out program intro message
# The ( was never closed!
print("This program computes how many vowels in the given string input.")

#print one blank line
print()

#take user input
userInput = input("Plesae enter some text here: ")
inputLower = userInput.lower()

def vowelCounter(text):

    #accumulator
    totalVowels = 0

    #go over each character and see if it is a vowel
    #if so, increment the accumulator by one
    for c in text:
        #There was no semicolen (:) after 'aeiou'
        if c in 'aeiou':
            totalVowels = totalVowels + 1

    #print out result
    # cannot use + for a string and a variable so it has to be a comma
    print("There are total ", totalVowels,  " vowels.")


#def main():

    
#call vowel counter function
vowelCounter(text)

#main()



