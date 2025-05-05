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
    if ch.isupper() == True:

      shift = ((ord(ch) - 65 + key) % 26) + 65

      encodedMsg = encodedMsg + (chr(shift))

      #print("The encoded message is:" + encodedMsg)

    # Deals with lowercase charachters
    elif ch.islower() == True:

      shift = ((ord(ch) - 97 + key) % 26) + 97 

      encodedMsg = encodedMsg + chr(shift)

      #print("The encoded message is:", encodedMsg)

    # Deals with any other characters (that arent letters)
    else:

      encodedMsg = encodedMsg + ch  
 
      #print("The encoded message is:", encodedMsg)

  return encodeMsg

def decoder(encryptedMsg,key):

  # Empty string where the message will be implemented
  decodedMsg = ''

  # For loop that runs through every character in the message
  for ch in encryptedMsg:

    # Deals with uppercase characters
    if ch.isupper():

        shift = ((ord(ch) - 65 - key + 26) % 26) + 65

        decodedMsg = decodedMsg + chr(shift)     

    # Deals with lowercase charachters
    elif ch.islower():

        shift = ((ord(ch) - 97 - key + 26) % 26) + 97

        decodedMsg = decodedMsg + chr(shift)     

    # Deals with any other characters (that arent letters)
    else:

        decodedMsg = decodedMsg + ch  
 
  print("The message decoded is:", decodedMsg)

### button that closes brogram
def drawexitButton(win, pt1, pt2, label):
    button = Rectangle(pt1, pt2)
    button.setFill("yellow")
    button.draw(win)

    #coords for position of the label
    btnLabel = Text( button.getCenter(), label)
    btnLabel.setFill("black")
    btnLabel.draw(win)

    return button

### isClicked() function 
def exitisClicked(button, point):

    #find x and y coordinate of the point
    x = point.getX()
    y = point.getY()

    #get two corner points of the rectangle object
    pt1 = button.getP1()
    pt2 = button.getP2()
    
    #calc min/max for the range of x and y
    minX = min(pt1.getX(), pt2.getX())
    maxX = max(pt1.getX(), pt2.getX())
    minY = min(pt1.getY(), pt2.getY())
    maxY = max(pt1.getY(), pt2.getY())

    #range test
    if ( minX <= x <= maxX and minY <= y <= maxY):
        return True
    else:
        return False

def drawEncodeButton(win, pt1, pt2, label):
  
  button = Oval(pt1, pt2)
  button.setFill("red3")
  button.draw(win)

  centerX = (pt1.getX() + pt2.getX()) / 2.0
  centerY = (pt1.getY() + pt2.getY()) / 2.0
  center = Point(centerX,centerY)

  buttonLabel = Text(Point(centerX, centerY), label)
  buttonLabel.setFill("white")

  buttonLabel.draw(win)

  return button

def encodeisClicked(button, point):

  x = point.getX()
  y = point.getY()
  pt1 = button.getP1()
  pt2 = button.getP2()

  if (pt1.getX() < x < pt2.getX() and pt1.getY() < y < pt2.getY()):
      return True

##def encodetextbox(win):
##
##  encodebox = Entry(Point(175,200), 20)
##  encodebox.setFace("arial")
##  encodebox.setSize(15)
##  encodebox.setTextColor("blue3")
##  encodebox.setFill("red3")
##  encodebox.setStyle("bold")
##  encode_message = encodebox.getText()
##  encodebox.draw(win)
##
##  return encode_message


def drawDecodeButton(win, pt1, pt2, label):
  
  button = Oval(pt1, pt2)
  button.setFill("blue3")
  button.draw(win)

  centerX = (pt1.getX() + pt2.getX()) / 2.0
  centerY = (pt1.getY() + pt2.getY()) / 2.0
  center = Point(centerX,centerY)

  buttonLabel = Text(Point(centerX, centerY), label)
  buttonLabel.setFill("white")

  buttonLabel.draw(win)

  return button

def decodeisClicked(button, point):

  x = point.getX()
  y = point.getY()
  pt1 = button.getP1()
  pt2 = button.getP2()

  if (pt1.getX() < x < pt2.getX() and pt1.getY() < y < pt2.getY()):
      return True

def main():

  # create window  
  myWin = GraphWin("Caesar Cipher", 600, 600)

  # create button for encoding
  point1 = Point(150,250)
  point2 = Point(250,300)
  encodebtn = drawEncodeButton(myWin,point1,point2,"ENCODE")

  # create button for decoding
  point3 = Point(350,250)
  point4 = Point(450,300)
  decodebtn = drawDecodeButton(myWin,point3,point4,"DECODE")

  # create button for closing program
  quitBtn = drawexitButton(myWin, Point(585,575), Point(530,550), "Quit")
  
  # print instructions for the program
  instructions = Text(Point(myWin.getWidth()/2, 30), "Enter two numbers.\nThen click the mouse.")
  instructions.draw(myWin)

  # text box for encode
  textbox = Entry(Point(300,200), 30)
  textbox.setFace("arial")
  textbox.setSize(15)
  ##textbox.setTextColor("black")
  textbox.setFill("sky blue")
  textbox.setStyle("bold")
  
  textbox.draw(myWin)

  user_message = textbox.getText()

  keyt = user_key.getTet()
  key = int(keyt)

  pt = myWin.getMouse()

##  while exitisClicked(quitBtn, pt) == False :
##
##    if encodeisClicked(encodebtn,pt):
##
##      encoder(user_message,kee)
##
##    if decodeisClicked(decodebtn,pt):
##
##      decoder(user_message,kee)
##        
##  else:
##
##    myWin.close()

  #wait for click to close window
  while not exitisClicked(quitBtn, pt):

    print("button is not clicked")
    pt = myWin.getMouse()

  # close window
  myWin.close()




##  while encodeisClicked(encodebtn,pt):
##    encoder(encode_this_message,kee)

##  while decodeisClicked(decodebtn,pt):
##    decoder(decode_message,key)
    

main()



