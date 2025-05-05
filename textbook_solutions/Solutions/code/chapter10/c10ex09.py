# c10ex09.py
#   class to represent a sphere

import math

class Sphere:

    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return 4.0/3.0 * math.pi * self.radius ** 3

def main():
    print("This program computes the volume and surface area of a sphere.\n")
    r = float(input("Please enter the radius of the sphere: "))
    mySphere = Sphere(r)
    print("The surface area is", mySphere.surfaceArea(), "square units.")
    print("The volume is", mySphere.volume(), "cubic units.")

if __name__ == '__main__':
    main()
    input("\nPress <Enter> to quit.")
