#input names from classlist.txt
#print out first names only, in alphabetical order

def getlastname(element):
    names = element.split()
    return names[1]

def sortClasslist():

    inFile = open("classlist.txt","r", encoding='utf-8')
    firstnames = []
    names = []
    
    #real each line from file
    for line in inFile:
        name = line.split() 
        ###your code here to add first name to the list\
        firstnames.append(name[0])

        names.append(line)

    print(names)
        
    #sort firstnames
    firstnames.sort()

    names.sort(key = getlastname)

    #print firstnames
    print(names)
    
    #close file
    inFile.close()



sortClasslist()
