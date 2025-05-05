# File: chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    x2 = x
    x3 = x
    for i in range(100):
        x = 3.9 * x * (1 - x)
        x2 = 3.9 * (x2 - x2*x2)
        x3 = 3.9*x3 - 3.9*x3*x3
        print(x,x2,x3)

main()
