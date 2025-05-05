# c08ex08.py
#    Euclid's algorithm for GCD

def gcd(m,n):
    while m != 0:
        n, m = m, n % m
    return n

def main():
    print("Euclid's GCD algorithm\n")
    x1, x2 = input("Enter two natural numbers (n1, n2): ").split(",")
    
    print("The GCD of", x1, "and", x2, "is", gcd(int(x1),int(x2)))

if __name__ == '__main__':
    main()

