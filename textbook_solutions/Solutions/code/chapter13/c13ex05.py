# c13ex05.py
# recursive algorithm for base conversion

def baseConversion(num, base):
    # PRE: num and base are integers with num >= 0  and base > 1

    if num < base:
        # base case is left most digit
        print(num, end=' ')
    else:
        #remove last digit, recurse and then print last digit
        lastDigit = num % base
        baseConversion(num//base, base)
        print(lastDigit, end=' ')

def main():
    print()
    print("Let's convert from base ten to another base.")
    print()

    n = int(input("What base ten integer shall we convert? (>=0 please) "))
    b = int(input("To what base? (>=2 please) "))

    print()
    print("The digits of the new representation are:")
    baseConversion(n,b)
    print()
    print()

main()
