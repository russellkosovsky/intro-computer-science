# c06ex03.py
#    Sphere info with functions

import math

def sphereArea(radius):
    return 4 * math.pi * radius * radius

def sphereVolume(radius):
    return 4.0/3.0 * math.pi * radius**3

def main():
    print("This program computes some properties of a sphere\n")

    r = float(input("Please enter the radius of the sphere: "))
    print("\nThe surface area is %0.2f square units." % (sphereArea(r)))
    print("The volume is %0.2f cubic units." % (sphereVolume(r)))

main()

