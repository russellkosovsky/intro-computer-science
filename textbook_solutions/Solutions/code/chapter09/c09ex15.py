# c09ex15.py
#    Puzzle problem. Imagine a cube circumscribed about a unit sphere.
#    An "eyeball" at the origin "sees" each wall as 1/6 of the field of
#    view. Suppose the eye is moved to (0.5, 0, 0), what proportion of
#    the total field of view is taken up by the side of the cube at x = 1.

# This program approximates the solution to this problem using Monte Carlo
# techniques. It generates rays in random directions from the point of
# observation and determines the proportion that intersect the side of cube
# at x = 1.

# if x is the x position of the observer and (a,b,c) are the components of a
#   direction vector, the points along the ray from the observer in that
#   direction are given by the parametric equation: p = (x,0,0) + t(a,b,c) for
#   t >= 0. Solving for the time of intersection (when p.x == 1) we have get
#   t == (1-x)/ a. Thus the point of intersection is (1, (1-x)b/a, (1-x)c/a)
#   So the ray "strikes" the side of interest iff:
#    (-1 <= (1-x)b/a <=1) and (-1 <= (1-x)c/a <= 1)

from random import random

def randomDirection():
    # Generate a random direction vector in threespace.
    # Method: generate a random point inside of a unit sphere.
    #    (x,y,z) are chosen in the range -1.0 to 1.0. Any point falling
    #    outside of the unit sphere is discarded.
    while True:
        # Generate points until a suitable one is found.
        x = 2*random()-1
        y = 2*random()-1
        z = 2*random()-1
        if x*x + y*y + z*z < 1 and (x,y,z) != (0,0,0):
            return x,y,z

def main():
    print("Puzzle problem solver.\n")
    x = float(input("Enter x position of the observer (-1 <= x < 1) "))
    n = int(input("Number of samplings: "))
    hits = 0
    for i in range(n):
        a,b,c = randomDirection()
        t = (1-x)/a
        if t> 0 and (-1 <= t*b <= 1) and (-1 <= t*c <= 1):
            hits = hits + 1
    print("Estimated FOV =", hits/n)

if __name__ == '__main__':
    main()
