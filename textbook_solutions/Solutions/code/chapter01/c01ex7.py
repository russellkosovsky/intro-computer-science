# File: chaos.py
# Chaos program to print side-by-side values
# Note: This output is UGLY, but uses only things seen in Chapter 1
#       For a more elegant version see c05ex12.py

def main():
    print("This program illustrates a chaotic function")
    x1 = eval(input("Enter the first seed between 0 and 1: "))
    x2 = eval(input("Enter the second seed between 0 and 1: "))
    print()
    print("input     ", x1, " | ", x2)
    print("-------------------------------------------")
    for i in range(10):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        print("      ", x1, " | ", x2)

main()
