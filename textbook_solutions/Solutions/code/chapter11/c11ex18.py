# c11ex18.py
#    random walk tracking crossings

from random import random

def main():
    print("This program simulates a 1-dimensional random walk.\n")
    n = int(input("Enter the number of squares in the sidewalk: "))
    counts = [0]*n

    pos = n // 2
    steps = 0
    while 0 <= pos < n:
        counts[pos] = counts[pos] + 1
        if random() < .5:
            pos = pos + 1
        else:
            pos = pos - 1
        steps = steps + 1

    print("Total steps taken:", steps)
    print("Counts:", counts)
    

main()

