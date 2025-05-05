# c06ex05.py
#    Pizza value with functions


import math


def costPer(d, price):
    return float(price) / area(d)

def area(d):
    return math.pi * (0.5*d)**2

def main():
    print("Program to calculate the value of a pizza\n")

    diam = float(input("Enter the diameter of the pizza: "))
    cost = float(input("Enter the price of the pizza: "))

    print("\nThe pizza costs %0.4f per square unit." % (costPer(diam,cost)))

main()
