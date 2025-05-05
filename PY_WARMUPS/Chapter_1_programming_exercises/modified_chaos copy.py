# File: chaos.py
# A simple program illustrating chaotic behavior
# Author: James Lee (james.lee@conncoll.edu)

def main():
    print("This program illustrates a chaotic function.")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print(x)

main()

# In the original code, when any number is used as an input, it listed 10
# numbers that started out somewhat similar to the original number but then
# each time became mopre and more random. With this modified verson that
# replaces 3.9 with 2.o in the equation, it outputs the original input 10 times
# in a row. 
