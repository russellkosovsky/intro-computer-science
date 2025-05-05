# File: chaos.py
# A simple program illustrating chaotic behavior
# Author: Russell Kosovsky (rkosovsky@conncoll.edu)


def main():
    print("This program illustrates a chaotic function.")
    n = eval(input("how many numbers should i print "))
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter another number between 0 and 1: "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print(x,y)

main()
