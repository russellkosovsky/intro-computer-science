# file: program_3.py
# This program is a Caesar cipher encoder/decoder with a Graphical User Interface 
# Author: Russell Kosovsky (rkosovsky@conncoll.edu)

from graphics import *


def encoder(message,key):

  # Empty string where the message will be implemented
  encodedMsg = ''

  # For loop that runs through every character in the message
  for ch in message:

    # Deals with uppercase characters
    if ch.isupper():

      shift = ((ord(ch) - 65 + key) % 26) + 65

      encodedMsg = encodedMsg + chr(shift)                              

    # Deals with lowercase charachters
    elif ch.islower():

      shift = ((ord(ch) - 97 + key) % 26) + 97 

      encodedMsg = encodedMsg + chr(shift)

    # Deals with any other characters (that arent letters)
    else:

      encodedMsg = encodedMsg + ch  
 
  print("The encoded message is:", encodedMsg)
 

def decoder(encryptedMsg,key):

  # Empty string where the message will be implemented
  decodedMsg = ''

  # For loop that runs through every character in the message
  for ch in encryptedMsg:

    # Deals with uppercase characters
    if ch.isupper():

        shift = 65 + ((ord(ch) - 65 - key + 26) % 26) 

        decodedMsg = decodedMsg + chr(shift)     

    # Deals with lowercase charachters
    elif ch.islower():

        shift = 97 + ((ord(ch) - 97 - key + 26) % 26) 

        decodedMsg = decodedMsg + chr(shift)     

    # Deals with any other characters (that arent letters)
    else:

        decodedMsg = decodedMsg + ch  
 
  print("The message decoded is:", decodedMsg)

def shelltest():
  
  message = input("Enter your secret message: ")

  key = int(input("Enter the key: "))

  encoder(message,key)

  encryptedMsg = input("Enter the encrypted message: ")

  key = int(input("Enter the key: "))

  decoder(encryptedMsg,key)

shelltest()



