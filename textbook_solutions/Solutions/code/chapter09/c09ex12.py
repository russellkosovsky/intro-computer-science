# c09ex12.py

from random import random

def main():
    print("Simulation of random walk in one dimension.\n")

    walks = int(input("How many walks should I do? "))
    steps = int(input("How many steps should I take on each? "))

    totalDist = 0
    for i in range(walks):
        thisDist = randomWalk(steps)
        totalDist = totalDist + thisDist

    print("Average distance from start", totalDist/walks)

def randomWalk(n):
    pos = 0
    for i in range(n):
        if random() <.5:
            pos = pos - 1
        else:
            pos = pos + 1
    return abs(pos)

if __name__ == '__main__':
    main()


    
