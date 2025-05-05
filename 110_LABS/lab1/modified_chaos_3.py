# File: chaos.py
# A simple program illustrating chaotic behavior
# Author: Russell Kosovsky (rkosovsky@conncoll.edu)

n = eval(input("how many numbers should I print? "))

def main():
    print("This program illustrates a chaotic function.")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)

main()

# this modification asks the user for an input then the program uses that value
# that the user chose as the number of values that are outputted. (the loop)
