#COM110: deCoder.py
#this module takse a number between 65 to 122 and
#print the letter that has ASCII code same as entered number

def deCoder():
    code = int ( input('Enter ASCII code from 65 to 122: ') )
    letter = chr ( code )
    print('a letter for ASCII code {} is \'{}\''.format(code, letter) )

deCoder()


#this decodeFile function open secret file that has some messages encoded
#in ASCII code (three digits), then convert back to the original message
#find out what secret messages in the file!
def decodeFile():

    inFile = open('secretcode.txt', 'r')
    msg = inFile.read()

    print('encoded secret code in secretcode.txt file is:')
    print(msg, '\n')

    decodedMsg = ''

    #as a single letter encoded with three digits (i.e. A is 065)
    #we use increment 3 for range() so that we access each three digits
    #up to the last position (use len() to check the total length of file contents)
    for i in range(0, len(msg), 3):
        #convert three digits to int number, then convert it to letter
        letter = chr ( int(msg[i:i+3]) )
        decodedMsg = decodedMsg + letter

    print('The secret message is \"{}\"'.format(decodedMsg) )

decodeFile()
