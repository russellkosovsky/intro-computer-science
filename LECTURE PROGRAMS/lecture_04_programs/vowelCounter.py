#COM110: vowelCounter.py
#This program count the number of vowel occurrence in the file

def vowelCounter():

    # open file
    inFile = open('test.txt', 'r')

    # read in all contents of the file
    contents = inFile.read()

    
    # variable to store total number of vowels
    numvowel = 0

    # convert all content to lowercase so we only need to count for one occurance
    contents = contents.lower()
    
    # count total number of occurrence of vowel o or O.
    # numvowel = numvowel + contents.count('o')
    # count total number of occurrence of vowel e or E.
    # numvowel = numvowel + contents.count('e')
    # count total number of occurrence of vowel i or I.
    # numvowel = numvowel + contents.count('i')
    # count total number of occurrence of vowel a or A.
    # numvowel = numvowel + contents.count('a')
    # count total number of occurrence of vowel u or U.
    # numvowel = numvowel + contents.count('u')
    # use if conditional instead of str.count function

    for vowel in ['a','e','i','o','u']:
        num = contents.count(vowel)
        numvowel = numvowel + num

    

            
    # print result
    print('test.txt has', numvowel, 'vowel occurence')
    
    # close file
    inFile.close()

vowelCounter()
