#COM110: enCoder.py
#this module takse user message and print out encoded msg in the form of digit

def enCoder():	
    msg = input('enCoder. Enter your message: ')
    for ch in msg:
        print( str(ord(ch)), end=' ')

    print()
    
enCoder()	


#This second function encode each character in three digit
#(Check the string formattig material)
#More regular form of output (all letters always three digit!)
def enCoder2():	
    msg = input('enCoder2. Enter your message: ')
    encodedMsg = ''
    for ch in msg:
        encodedMsg = encodedMsg + '{:03} '.format( ord(ch) )

    print(encodedMsg)

enCoder2()	

#Write encoded digit sting to file (secret message code!!!)
#This time encode just digits without space between letters
def enCoder2File():
    outFile = open('encode.txt', 'w')
    msg = input('enCoder2File. Enter your message: ')
    encodedMsg = ''
    for ch in msg:
        encodedMsg = encodedMsg + '{:03}'.format( ord(ch) )

    print(encodedMsg)
    outFile.write(encodedMsg)
    outFile.close()

enCoder2File()

