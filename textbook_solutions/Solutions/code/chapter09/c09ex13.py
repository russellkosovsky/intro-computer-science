# c09ex13.py
#    Random block walking

from random import randrange

def main():
    print("Simulation of two dimensional random walk\n")

    walks = int(input("How man walks should I do? "))
    steps = int(input("How many steps should I take on each? "))

    totalDist = 0
    for i in range(walks):
        thisDist = randomWalk2D(steps)
        totalDist = totalDist + thisDist

    print("Average distance from start", totalDist/walks)

def randomWalk2D(n):
    x,y = 0,0   # start at the origin
    for i in range(n):
        dir = randrange(4)
        if dir == 0:  # go left
            x = x  - 1
        elif dir == 1: # go up
            y = y + 1
        elif dir == 2: # go right
            x = x + 1
        else:          # go down
            y = y - 1

    return (x*x + y*y)**.5 # distance to origin

if __name__ == '__main__':
    main()


    
