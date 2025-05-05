# c03ex07.py
#    Calculates the distance between two points

import math

def main():
    print("This program calculates the distance between two points.")
    print()

    x1 = float(input("Enter the x for the first point: "))
    y1 = float(input("Enter the y for the first point: "))
    print()
    x2 = float(input("Enter the x for the second point: "))
    y2 = float(input("Enter the y for the second point: "))
    
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    print()
    print("The distance between the points is", distance)

main()
