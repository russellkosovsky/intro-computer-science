# c08ex05.py
#   Primality tester

import math

def isPrime(n):
    if n % 2 == 0:
        return False
    factor = 3
    while factor <= math.sqrt(n):
        if n % factor == 0:
            return False
        factor = factor + 2
    return True

def main():
    print("Prime number tester\n")
    n = int(input("Enter a value to test: "))
    if isPrime(n):
        print(n, "is prime.")
    else:
        print(n, "is not prime.")

if __name__ == '__main__':
    main()
