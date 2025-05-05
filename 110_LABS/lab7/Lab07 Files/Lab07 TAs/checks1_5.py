
# lab06.py
# 03/01/2018
# This program creates and draws a Rectangle object,
# takes a mouse click, and then closes the window.



from graphics import *
from random import randrange
from time import sleep

def main():

    #CHECK 4
    PASSWORD = "camels"
    #prompt user for password 
    userentry = input("Hello there.  Please enter the password to use this program --> ")
    #and continue prompting until they get it correct
    while (userentry != PASSWORD):
       userentry = input("Sorry, wrong password.  Please try again --> ")

    #ORIGINAL START OF lab06.py
    win = GraphWin("Fun #5", 600, 600)

    square = Rectangle(Point(200,200),Point(400,400))
    square.draw(win)

    #CHECK 1
    #Get a point from mouse click
    pt = win.getMouse()

    #Check if pt is on the rectangle
    if (pt.getY() >= 200 and pt.getY() <= 400) and (pt.getX() >= 200 and pt.getX() <= 400):
        #Fill rectangle with random color
        r = randrange(0,256)
        g = randrange(0,256)
        b = randrange(0,256)
        square.setFill(color_rgb(r,g,b))

    #CHECK 2
    #Get a point from mouse click
    pt = win.getMouse()

    #Check if pt is on the rectangle
    if (pt.getY() >= 200 and pt.getY() <= 400) and (pt.getX() >= 200 and pt.getX() <= 400):

        #Create a for loop, 50 times
        for i in range(5): #Should be 50
            #Fill rectangle with random color
            r = randrange(0,256)
            g = randrange(0,256)
            b = randrange(0,256)
            square.setFill(color_rgb(r,g,b))
            sleep(0.1)

    #CHECK 3
    #Get a point from mouse click
    pt = win.getMouse()

    #While the pt is on the rectangle
    while (pt.getY() >= 200 and pt.getY() <= 400) and (pt.getX() >= 200 and pt.getX() <= 400):
        #Fill rectangle with random color
        r = randrange(0,256)
        g = randrange(0,256)
        b = randrange(0,256)
        square.setFill(color_rgb(r,g,b))

        #Get (wait for) another mouse click
        pt = win.getMouse()
        
    #win.getMouse() #This should be omitted as part of CHECK 3
    win.close()

main()

#CHECK 5 - in a separate module
def average():
    total = 0
    count = 0
    print("Enter numbers to be averaged. (Entering a negative number \nends the input.")

    #Get the first number
    num = float(input("Number: "))

    while (num >= 0):
        total = total + num
        count = count + 1
        #Get another number
        num = float(input("Number: "))
    print("\nThe average of the numbers is", total/count)







    
