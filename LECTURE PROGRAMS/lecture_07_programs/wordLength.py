#COM110: wordLength.py
#The program compute the average length of the sentences

def main():

    #open file
    inFile = open('theprogrammer.txt', 'r', encoding='utf-8')

    #read all contents from the file
    allContents = inFile.read()

    #split the contents into sentences: assume a period is good candidate
    #to split sentences
    sentences = allContents.count(".")


    
    #split the contents into words
    ### your code here
    words = allContents.split()
    

    #avg length of sentence: total number of words / total number of sentence
    ### your code here

    avgsen = len(words) / sentences
        
    #also can computer average length of words
    ### your code here

    print("The average length of the sentences is, ", avgsen)
    
    #close file
    inFile.close()
        
main()
