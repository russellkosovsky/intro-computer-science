# c10ex10.py
#    Cube class

class Cube:

    def __init__(self, side):
        self.side = side

    def getSide(self):
        return self.side

    def surfaceArea(self):
        return 6 * self.side ** 2

    def volume(self):
        return self.side ** 3

def main():
    print("This program computes the volume and surface area of a cube.\n")
    r = float(input("Please enter the length of the cube's side: "))
    myCube = Cube(r)
    print("The surface area is", myCube.surfaceArea(), "square units.")
    print("The volume is", myCube.volume(), "cubic units.")

if __name__ == '__main__':
    main()
    input("\nPress <Enter> to quit.")
