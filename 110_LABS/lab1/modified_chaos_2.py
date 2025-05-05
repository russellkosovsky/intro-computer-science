# File: chaos.py
# A simple program illustrating chaotic behavior
# Author: Russell Kosovsky (rkosovsky@conncoll.edu)

def main():
    print("This program illustrates a chaotic function.")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):
        x = 3.9 * x * (1 - x)
        print(x)

main()

# this verson of chaos.py switches "for i in range(10):" to
# "for i in range(20):" which makes the program print 20 values
# instead of 10
