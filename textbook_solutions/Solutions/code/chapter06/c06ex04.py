# c06ex04.py

def sumN(n):
    total = 0
    for i in range(1,n+1):
        total = total + i
    return total

def sumNCube(n):
    total = 0
    for i in range(1,n+1):
        total = total + i**3
    return total

def main():
    print("This program computes the sum and sum of cubes of the first")
    print("N natural numbers.\n")

    n = int(input("Please enter a value for N: "))
    print("The sum of the first %d natural numbers is %d" % (n,sumN(n)))
    print("The sum of the cubes of those numbers is %d" % (sumNCube(n)))

main()


    
