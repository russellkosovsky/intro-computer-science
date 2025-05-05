# file: program_1_c.py
# A program used to learn the numbers in the Fibonacci sequence.
# Author: Russell Kosovsky (rkosovsky@conncoll.edu)

def main():
    
    # introduce program
    print("This program can be used to learn the numbers in the Fibonacci sequence.")
    print()
    print("The Fibonacci number sequence can describes how things grow, and also how they might decay.It can be used to predict the increase in the population of a colony of rabbits, and even a colony of bacteria. Some people even think Fibonacci numbers can be used to predict the behavior of financial assets, such as stock market indexes.")
    print()
    print("The first two Fibonacci numbers are 0 and 1.")
    print()

    # ask user for input
    n = eval(input("Enter a positive integer greater than 2: "))
    print()

    value_1, value_2 = 0, 1 # assigns variables with the starting values

    print("The first", n, "Fibonacci numbers are: ", end= "") # output the result

    for i in range(n + 1):       # loop to repeat process based on users input
        print(value_1, end= " ") # Prints each number of the sequence
        value_1, value_2 = value_2, value_1 + value_2  # allows python to swap variable so that it can sequencially add them together

    print()
    print()
    print("So the", n,"th Fibonacci number is:", value_2 - value_1)

# run program
main()












